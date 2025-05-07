from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from MiniLangVisitor import MiniLangVisitor
import numpy as np
import sys
from test.tests import code_1, code_2, code_3, code_struct_test

class FunctionReturn(Exception):
    def __init__(self, value):
        self.value = value


class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.variables = {}
        self.types = {}
        self.structs = {}
        self.classes = {}

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.get_variable(name)
        else:
            raise NameError(f"Variable '{name}' not defined")

    def get_type(self, name):
        if name in self.types:
            return self.types[name]
        elif self.parent:
            return self.parent.get_type(name)
        else:
            raise NameError(f"Type for variable '{name}' not defined")

    def set_variable(self, name, value):
        if name in self.variables:
            self.variables[name] = value
        elif self.parent and self.parent.has_variable(name):
            self.parent.set_variable(name, value)
        else:
            self.variables[name] = value

    def has_variable(self, name):
        if name in self.variables:
            return True
        elif self.parent:
            return self.parent.has_variable(name)
        else:
            return False

    def declare_variable(self, name, var_type, dims=0):
        if name in self.variables:
            raise NameError(f"Variable '{name}' already defined")
        self.types[name] = {"type": var_type, "dims": dims}
        if dims == 2:
            self.variables[name] = None  # Will be initialized later
        elif dims == 1:
            self.variables[name] = None
        else:
            self.variables[name] = None

    def add_struct(self, name, members):
        self.structs[name] = members

    def get_struct(self, name):
        if name in self.structs:
            return self.structs[name]
        elif self.parent:
            return self.parent.get_struct(name)
        else:
            raise NameError(f"Struct '{name}' not defined")

    def add_class(self, name, class_def):
        self.classes[name] = class_def

    def get_class(self, name):
        if name in self.classes:
            return self.classes[name]
        elif self.parent:
            return self.parent.get_class(name)
        else:
            raise NameError(f"Class '{name}' not defined")



class Function:
    def __init__(self, return_type, params, body):
        self.return_type = return_type
        self.params = params
        self.body = body


class StructInstance:
    def __init__(self, struct_type, members, scope):
        self.type = struct_type
        self.scope = scope
        self.members = {}
        # Initialize all members with proper default values
        for member_name, member_type in members.items():
            if member_type == 'int':
                self.members[member_name] = 0
            elif member_type == 'float32':
                self.members[member_name] = np.float32(0.0)
            elif member_type == 'float64':
                self.members[member_name] = 0.0
            elif member_type == 'string':
                self.members[member_name] = ""
            else:
                self.members[member_name] = None


class ClassInstance:
    def __init__(self, class_type, members, methods, scope):
        self.type = class_type
        self.members = {}
        self.methods = methods.copy()
        self.scope = scope

        for member_name, member_type in members.items():
            try:
                # Check if the member is a struct
                struct_def = self.scope.get_struct(member_type)
                self.members[member_name] = StructInstance(member_type, struct_def, self.scope)
                print(f"Initialized class member {member_name} as {member_type}")
            except NameError:
                # Handle primitive types
                if member_type == 'float32':
                    self.members[member_name] = np.float32(0.0)
                elif member_type == 'int':
                    self.members[member_name] = 0
                elif member_type == 'float64':
                    self.members[member_name] = 0.0
                else:
                    self.members[member_name] = None
                print(f"Initialized class member {member_name} with default {member_type}")


class BreakException(Exception):
    pass

class MyVisitor(MiniLangVisitor):
    def __init__(self, scope=None):
        self.scope = scope if scope else Scope()
        self.current_function = None
        self.current_class = None

    def visitProgram(self, ctx):
        # First pass - collect all declarations
        for child in ctx.children:
            if isinstance(child, MiniLangParser.StructDeclContext):
                self.visitStructDecl(child)
            elif isinstance(child, MiniLangParser.ClassDeclContext):
                # Process class declaration immediately
                class_name = child.ID(0).getText()
                parent_class = child.ID(1).getText() if child.ID(1) else None

                members = {}
                methods = {}
                constructors = []

                # Process members
                for member in child.memberDecl():
                    member_type = member.type_().getText()
                    member_name = member.ID().getText()
                    members[member_name] = member_type

                # Process methods
                for method in child.methodDecl():
                    if isinstance(method, MiniLangParser.ConstructorDeclarationContext):
                        params = []
                        if method.params():
                            for param in method.params().param():
                                param_type = param.type_().getText()
                                param_name = param.ID().getText()
                                params.append((param_type, param_name))
                        constructors.append((params, method.block()))
                    else:
                        method_name = method.ID().getText()
                        return_type = method.type_().getText()
                        params = []
                        if method.params():
                            for param in method.params().param():
                                param_type = param.type_().getText()
                                param_name = param.ID().getText()
                                params.append((param_type, param_name))
                        methods[method_name] = Function(return_type, params, method.block())

                # Handle inheritance
                if parent_class:
                    parent = self.scope.get_class(parent_class)
                    members.update(parent.members)
                    methods.update(parent.methods)
                    constructors.extend(parent.constructors)

                class_def = {
                    'members': members,
                    'methods': methods,
                    'constructors': constructors,
                    'parent': parent_class
                }
                self.scope.add_class(class_name, class_def)
                print(f"Class '{class_name}' declared")

            elif isinstance(child, MiniLangParser.FunctionDeclContext):
                self.visitFunctionDecl(child)

        # Second pass - execute statements
        for child in ctx.children:
            if not isinstance(child, (MiniLangParser.FunctionDeclContext,
                                      MiniLangParser.StructDeclContext,
                                      MiniLangParser.ClassDeclContext)):
                self.visit(child)

    def visitClassDecl(self, ctx):
        class_name = ctx.ID(0).getText()
        parent_class = ctx.ID(1).getText() if ctx.ID(1) else None

        members = {}
        methods = {}
        constructors = []

        # Process member declarations
        for member in ctx.memberDecl():
            member_type = member.type_().getText()
            member_name = member.ID().getText()
            members[member_name] = member_type

        # Process methods and constructors
        for method in ctx.methodDecl():
            # Check which alternative we're dealing with
            if isinstance(method, MiniLangParser.ConstructorDeclarationContext):
                # Handle constructor
                params = []
                if method.params():
                    for param in method.params().param():
                        param_type = param.type_().getText()
                        param_name = param.ID().getText()
                        params.append((param_type, param_name))
                constructors.append((params, method.block()))
            else:
                # Handle regular method
                method_name = method.ID().getText()
                return_type = method.type_().getText()
                params = []
                if method.params():
                    for param in method.params().param():
                        param_type = param.type_().getText()
                        param_name = param.ID().getText()
                        params.append((param_type, param_name))
                methods[method_name] = Function(return_type, params, method.block())

        # Handle inheritance
        if parent_class:
            parent = self.scope.get_class(parent_class)
            members.update(parent.members)
            methods.update(parent.methods)
            constructors.extend(parent.constructors)

        class_def = {
            'members': members,
            'methods': methods,
            'constructors': constructors,
            'parent': parent_class
        }
        self.scope.add_class(class_name, class_def)
        print(f"Class '{class_name}' declared")

    def visitNewExpr(self, ctx):
        class_name = ctx.ID().getText()
        try:
            class_def = self.scope.get_class(class_name)
        except NameError:
            raise NameError(f"Class '{class_name}' not defined")

        # Create instance with current scope

        args = []
        if ctx.args():
            args = [self.visit(arg) for arg in ctx.args().expr()]

        # Create new instance
        instance = ClassInstance(class_name, class_def['members'],
                                 class_def['methods'], self.scope)

        # Find matching constructor
        constructor = None
        for constr_params, constr_body in class_def['constructors']:
            if len(constr_params) == len(args):
                constructor = (constr_params, constr_body)
                break

        if constructor:
            constr_params, constr_body = constructor
            constr_scope = Scope(self.scope)

            # Ensure 'this' is properly registered
            constr_scope.declare_variable("this", class_name)
            constr_scope.set_variable("this", instance)

            # Add parameters
            for (param_type, param_name), arg_value in zip(constr_params, args):
                constr_scope.declare_variable(param_name, param_type)
                constr_scope.set_variable(param_name, arg_value)

            # Execute constructor with proper scope
            visitor = MyVisitor(constr_scope)
            visitor.current_class = class_name
            visitor.visit(constr_body)

        return instance

    def visitStructDecl(self, ctx):
        struct_name = ctx.ID().getText()
        members = {}
        for member in ctx.memberDecl():
            member_type = member.type_().getText()
            member_name = member.ID().getText()
            members[member_name] = member_type
        self.scope.add_struct(struct_name, members)
        print(f"Struct '{struct_name}' declared with members: {list(members.keys())}")

    def visitMemberAccessExpr(self, ctx):
        parts = [ctx.memberAccess().ID(i).getText() for i in range(len(ctx.memberAccess().ID()))]

        # Check if we're in a class context and first part is a class member
        if self.current_class and len(parts) > 1:
            try:
                class_def = self.scope.get_class(self.current_class)
                if parts[0] in class_def['members']:
                    # Prepend 'this' to access class members
                    parts = ['this'] + parts
                    print(f"Resolved class member access to: {'.'.join(parts)}")
            except NameError:
                pass

        try:
            current = self.scope.get_variable(parts[0])
            for part in parts[1:]:
                if isinstance(current, (StructInstance, ClassInstance)):
                    current = current.members.get(part)
                    if current is None:
                        raise ValueError(
                            f"Member '{part}' not found in {current.type if hasattr(current, 'type') else 'object'}")
                else:
                    raise ValueError(f"'{'.'.join(parts[:parts.index(part) + 1])}' is not a structure or class")
            return current
        except NameError as e:
            print(f"Member access error: {e}")
            raise

    def visitMethodCallExpr(self, ctx):
        member_access = ctx.memberAccess()
        ids = [id_node.getText() for id_node in member_access.ID()]
        obj_name = ids[0]
        method_name = ids[-1]

        obj = self.scope.get_variable(obj_name)
        if not isinstance(obj, ClassInstance):
            raise ValueError(f"'{obj_name}' is not a class instance")

        if method_name not in obj.methods:
            raise NameError(f"Method '{method_name}' not found in class '{obj.type}'")

        method = obj.methods[method_name]
        args = [self.visit(arg) for arg in ctx.args().expr()] if ctx.args() else []

        # Create method scope with 'this' reference
        method_scope = Scope(self.scope)
        method_scope.declare_variable("this", obj.type)
        method_scope.set_variable("this", obj)

        # Add parameters to scope
        for (param_type, param_name), arg_value in zip(method.params, args):
            method_scope.declare_variable(param_name, param_type)
            method_scope.set_variable(param_name, arg_value)

        # Execute method with proper context
        visitor = MyVisitor(method_scope)
        visitor.current_function = method_name
        visitor.current_class = obj.type  # Set class context

        try:
            visitor.visit(method.body)
            if method.return_type != 'void':
                raise TypeError(f"Method '{method_name}' should return a value")
            return None
        except FunctionReturn as ret:
            return ret.value

    def visitFunctionDecl(self, ctx):
        func_name = ctx.ID().getText()
        return_type = ctx.type_().getText()
        params = []

        if ctx.params():
            for param in ctx.params().param():
                param_type = param.type_().getText()
                param_name = param.ID().getText()
                params.append((param_type, param_name))

        # Store the function in the global functions dictionary
        functions[func_name] = Function(return_type, params, ctx.block())
        print(f"Function '{func_name}' declared")

    def visitFunctionCall(self, ctx):
        func_name = ctx.ID().getText() if ctx.ID() else ctx.memberAccess().getText()

        if func_name not in functions:
            raise NameError(f"Function '{func_name}' not defined")

        func = functions[func_name]
        args = []
        if ctx.args():
            args = [self.visit(arg) for arg in ctx.args().expr()]

        # Create new scope for function execution
        function_scope = Scope(self.scope)

        # Add parameters to the scope
        for (param_type, param_name), arg_value in zip(func.params, args):
            function_scope.declare_variable(param_name, param_type)
            function_scope.set_variable(param_name, arg_value)

        # Execute function body
        visitor = MyVisitor(function_scope)
        visitor.current_function = func_name

        try:
            visitor.visit(func.body)
            if func.return_type != 'void':
                raise TypeError(f"Function '{func_name}' should return a value")
            return None
        except FunctionReturn as ret:
            return ret.value

    def visitReturnStmt(self, ctx):
        if not self.current_function:
            raise SyntaxError("return statement outside function")

        # Check if we're in a class method
        if self.current_class:
            # Get class definition
            class_def = self.scope.get_class(self.current_class)
            # Get method from class methods
            method = class_def['methods'].get(self.current_function)
            if not method:
                raise NameError(f"Method '{self.current_function}' not found in class '{self.current_class}'")
        else:
            # Regular function
            if self.current_function not in functions:
                raise NameError(f"Function '{self.current_function}' not defined")
            method = functions[self.current_function]

        if ctx.expr():
            value = self.visit(ctx.expr())
            if method.return_type == 'void':
                raise TypeError(
                    f"{'Method' if self.current_class else 'Function'} '{self.current_function}' should not return a value")
            raise FunctionReturn(value)
        else:
            if method.return_type != 'void':
                raise TypeError(
                    f"{'Method' if self.current_class else 'Function'} '{self.current_function}' should return a value")
            raise FunctionReturn(None)

    def visitDecl(self, ctx):
        var_type = ctx.type_().getText()
        var_name = ctx.ID().getText()
        dims = len(ctx.INT())

        self.scope.declare_variable(var_name, var_type, dims)

        # Check if the type is a struct by attempting to get it from any scope
        try:
            struct_members = self.scope.get_struct(var_type)
            # It's a struct type, initialize the struct instance
            struct_instance = StructInstance(var_type, struct_members, self.scope)
            self.scope.set_variable(var_name, struct_instance)
            print(f"Initialized struct '{var_name}' of type '{var_type}' with members: {list(struct_members.keys())}")
        except NameError:
            # Not a struct type, proceed with normal initialization
            pass

        # Handle array initializations
        if dims == 2:
            rows = int(ctx.INT(0).getText())
            cols = int(ctx.INT(1).getText())
            self.scope.set_variable(var_name, [[0] * cols for _ in range(rows)])
            print(f"Initialized 2D array '{var_name}' with dimensions {rows}x{cols}")
        elif dims == 1:
            size = int(ctx.INT(0).getText())
            self.scope.set_variable(var_name, [0] * size)
            print(f"Initialized 1D array '{var_name}' with size {size}")

        # Handle explicit initialization
        if ctx.expr():
            value = self.visit(ctx.expr())
            # Add struct copy handling
            if isinstance(value, StructInstance):
                # Create deep copy for structs
                new_struct = StructInstance(value.type, value.scope.get_struct(value.type), value.scope)
                new_struct.members = value.members.copy()
                self.scope.set_variable(var_name, new_struct)
            else:
                self.scope.set_variable(var_name, value)
            print(f"Initialized variable '{var_name}' with value {value}")

    def visitAssign(self, ctx):
        if ctx.memberAccess():
            parts = [ctx.memberAccess().ID(i).getText() for i in range(len(ctx.memberAccess().ID()))]
            # Prepend 'this' if accessing a class member
            if self.current_class:
                try:
                    class_def = self.scope.get_class(self.current_class)
                    if parts[0] in class_def['members']:
                        parts = ['this'] + parts
                        print(f"Resolved member access to: {'.'.join(parts)}")
                except NameError as e:
                    print(f"Error resolving class member: {e}")
                    raise

            try:
                current = self.scope.get_variable(parts[0])
                for part in parts[1:-1]:
                    if isinstance(current, (StructInstance, ClassInstance)):
                        current = current.members.get(part)
                        if current is None:
                            raise ValueError(f"Member '{part}' not found")
                    else:
                        raise ValueError(f"Invalid member access on {current}")
                member_name = parts[-1]
                value = self.visit(ctx.expr()[-1])
                # Type conversion based on member type
                if isinstance(current, StructInstance):
                    member_type = current.scope.get_struct(current.type).get(member_name)
                elif isinstance(current, ClassInstance):
                    class_def = current.scope.get_class(current.type)
                    member_type = class_def['members'].get(member_name)
                else:
                    member_type = None
                if member_type == 'float32':
                    value = np.float32(value)
                elif member_type == 'int':
                    value = int(value)
                current.members[member_name] = value
                print(f"Assigned {'.'.join(parts)} = {value}")
            except NameError as e:
                print(f"Assignment error: {e}")
                raise
        else:
            # Handle regular variable assignment
            var_name = ctx.ID().getText()
            if self.current_class:
                try:
                    class_def = self.scope.get_class(self.current_class)
                    if var_name in class_def['members']:
                        # Get the LAST expression which is the actual value
                        value_expr = ctx.expr()[-1]  # ← THIS IS THE CRUCIAL FIX
                        value = self.visit(value_expr)

                        # Type conversion and assignment
                        member_type = class_def['members'][var_name]
                        if member_type == 'float32':
                            value = np.float32(value)
                        elif member_type == 'int':
                            value = int(value)

                        instance = self.scope.get_variable('this')
                        instance.members[var_name] = value
                        print(f"Assigned class member {var_name} = {value}")
                        return
                except Exception as e:
                    print(f"Class member assignment error: {e}")
                    raise


            dims = len(ctx.expr()) - 1
            value = self.visit(ctx.expr()[-1])

            # Type conversion based on declared type
            var_info = self.scope.get_type(var_name)
            var_type = var_info["type"]
            if var_type == "float32":
                value = np.float32(value)
            elif var_type == "float64":
                value = float(value)
            elif var_type == "int":
                value = int(value)

            # Handle array assignments
            if dims == 2:
                row = self.visit(ctx.expr(0))
                col = self.visit(ctx.expr(1))
                arr = self.scope.get_variable(var_name)
                arr[row][col] = value
            elif dims == 1:
                index = self.visit(ctx.expr(0))
                arr = self.scope.get_variable(var_name)
                arr[index] = value
            else:
                self.scope.set_variable(var_name, value)
                print(f"Assigned {var_name} = {value}")

    def visitPrintStmt(self, ctx):
        try:
            value = self.visit(ctx.expr())
            if isinstance(value, (StructInstance, ClassInstance)):
                print(f"<{value.type} instance>")
            elif isinstance(value, np.float32):
                print(f"{value:.8f}")
            elif isinstance(value, float):
                print(f"{value:.15f}")
            else:
                print(value)
        except Exception as e:
            print(f"Print error: {e}")

    def visitIfStmt(self, ctx):
        condition = self.visit(ctx.expr())
        if condition:
            self.visit(ctx.statement(0))
        elif ctx.getChildCount() > 5:  # Check if there's an else clause
            self.visit(ctx.statement(1))

    def visitWhileStmt(self, ctx):
        while self.visit(ctx.expr()):
            self.visit(ctx.statement())

    def visitForStmt(self, ctx):
        # Create new scope for the loop
        loop_scope = Scope(self.scope)
        visitor = MyVisitor(loop_scope)
        visitor.current_function = self.current_function

        # Handle initialization
        if ctx.forControl().forInit():
            visitor.visit(ctx.forControl().forInit())

        while True:
            # Check condition
            if ctx.forControl().expr():
                condition = visitor.visit(ctx.forControl().expr())
                if not condition:
                    break

            # Execute loop body
            try:
                visitor.visit(ctx.statement())
            except BreakException:
                break
            except FunctionReturn as e:
                raise e

            # Handle update
            if ctx.forControl().forUpdate():
                visitor.visit(ctx.forControl().forUpdate())

    def visitForControl(self, ctx):
        pass

    def visitForInit(self, ctx):
        if ctx.decl():
            self.visit(ctx.decl())
        else:
            for assign in ctx.assign():
                self.visit(assign)

    def visitForUpdate(self, ctx):
        for assign in ctx.assign():
            self.visit(assign)

    def visitBreakStmt(self, ctx):
        raise BreakException()

    def visitBlock(self, ctx):
        new_scope = Scope(self.scope)
        visitor = MyVisitor(new_scope)
        visitor.current_function = self.current_function
        visitor.current_class = self.current_class
        for stmt in ctx.statement():
            visitor.visit(stmt)

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        result = left + right if ctx.op.text == '+' else left - right
        if isinstance(left, np.float32) or isinstance(right, np.float32):
            return np.float32(result)
        return result


    def visitLogicExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '&&':
            return bool(left) and bool(right)
        elif ctx.op.text == '||':
            return bool(left) or bool(right)
        elif ctx.op.text == '^^':
            return bool(left) != bool(right)

    def visitCompareExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '==':
            return left == right
        elif op == '!=':
            return left != right
        elif op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right

    def visitNegExpr(self, ctx):
        return not self.visit(ctx.expr())

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '*':
            result = left * right
        elif op == '/':
            result = left / right
        elif op == '%':
            result = left % right

        if isinstance(left, np.float32) or isinstance(right, np.float32):
            return np.float32(result)
        return result

    def visitFunctionCallExpr(self, ctx):
        return self.visitFunctionCall(ctx)

    def visitIntExpr(self, ctx):
        return int(ctx.getText())

    def visitFloatExpr(self, ctx):
        return float(ctx.getText())

    def visitStringExpr(self, ctx):
        return ctx.getText().strip('"')

    def visitIdExpr(self, ctx):
        var_name = ctx.ID().getText()
        dims = len(ctx.expr())

        try:
            # Try normal variable lookup first
            var_value = self.scope.get_variable(var_name)
            if dims == 2:
                row = self.visit(ctx.expr(0))
                col = self.visit(ctx.expr(1))
                return var_value[row][col]
            elif dims == 1:
                index = self.visit(ctx.expr(0))
                return var_value[index]
            return var_value
        except NameError:
            # If variable not found, check if it's a class member
            if self.current_class:
                try:
                    # Get 'this' reference
                    this_instance = self.scope.get_variable('this')
                    # Access the member directly
                    return this_instance.members.get(var_name)
                except NameError:
                    pass

            print(f"Error: cannot read {var_name}")
            return None

    def visitParensExpr(self, ctx):
        return self.visit(ctx.expr())


input_stream = InputStream(code_3)
lexer = MiniLangLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = MiniLangParser(tokens)
tree = parser.program()

global_scope = Scope()
functions = {}

visitor = MyVisitor(global_scope)
visitor.visit(tree)