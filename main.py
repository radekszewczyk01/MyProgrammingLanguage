from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from MiniLangVisitor import MiniLangVisitor
import numpy as np
import sys


class FunctionReturn(Exception):
    def __init__(self, value):
        self.value = value


class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.variables = {}
        self.types = {}

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


class Function:
    def __init__(self, return_type, params, body):
        self.return_type = return_type
        self.params = params
        self.body = body


class BreakException(Exception):
    pass

class MyVisitor(MiniLangVisitor):
    def __init__(self, scope=None):
        self.scope = scope if scope else Scope()
        self.current_function = None

    def visitProgram(self, ctx):
        # First pass - collect function declarations
        for child in ctx.children:
            if isinstance(child, MiniLangParser.FunctionDeclContext):
                func_name = child.ID().getText()
                return_type = child.type_().getText()
                params = []
                if child.params():
                    for param in child.params().param():
                        param_type = param.type_().getText()
                        param_name = param.ID().getText()
                        params.append((param_type, param_name))

                functions[func_name] = Function(return_type, params, child.block())

        # Second pass - execute statements
        for child in ctx.children:
            if not isinstance(child, MiniLangParser.FunctionDeclContext):
                self.visit(child)

    def visitFunctionDecl(self, ctx):
        pass  # Handled in visitProgram

    def visitFunctionCall(self, ctx):
        func_name = ctx.ID().getText()
        if func_name not in functions:
            raise NameError(f"Function '{func_name}' not defined")

        func = functions[func_name]
        args = []
        if ctx.args():
            args = [self.visit(arg) for arg in ctx.args().expr()]

        if len(args) != len(func.params):
            raise TypeError(f"Function '{func_name}' expects {len(func.params)} arguments but got {len(args)}")

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

        func = functions[self.current_function]
        if ctx.expr():
            value = self.visit(ctx.expr())
            if func.return_type == 'void':
                raise TypeError(f"Function '{self.current_function}' should not return a value")
            raise FunctionReturn(value)
        else:
            if func.return_type != 'void':
                raise TypeError(f"Function '{self.current_function}' should return a value")
            raise FunctionReturn(None)

    def visitDecl(self, ctx):
        var_type = ctx.type_().getText()
        var_name = ctx.ID().getText()

        dims = len(ctx.INT())
        self.scope.declare_variable(var_name, var_type, dims)

        if dims == 2:
            rows = int(ctx.INT(0).getText())
            cols = int(ctx.INT(1).getText())
            self.scope.set_variable(var_name, [[None for _ in range(cols)] for _ in range(rows)])
            print(f"Zadeklarowano macierz: {var_name}[{rows}][{cols}] typu {var_type}")
        elif dims == 1:
            size = int(ctx.INT(0).getText())
            self.scope.set_variable(var_name, [None] * size)
            print(f"Zadeklarowano tablicę: {var_name}[{size}] typu {var_type}")
        else:
            print(f"Zadeklarowano zmienną: {var_name} typu {var_type}")

        if ctx.expr():
            value = self.visit(ctx.expr())
            self.scope.set_variable(var_name, value)

    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()
        if not self.scope.has_variable(var_name):
            print(f"Błąd: zmienna {var_name} nie została zadeklarowana.")
            return

        dims = len(ctx.expr()) - 1
        value = self.visit(ctx.expr()[-1])

        var_info = self.scope.get_type(var_name)
        var_type = var_info["type"]

        if var_type == "float32":
            value = np.float32(value)
        elif var_type == "float64":
            value = float(value)
        elif var_type == "int":
            value = int(value)

        if dims == 2:
            row = self.visit(ctx.expr(0))
            col = self.visit(ctx.expr(1))
            try:
                var_value = self.scope.get_variable(var_name)
                var_value[row][col] = value
                self.scope.set_variable(var_name, var_value)
                print(f"Przypisano: {var_name}[{row}][{col}] = {value}")
            except:
                print(f"Błąd: niepoprawny indeks macierzy dla {var_name}")
        elif dims == 1:
            index = self.visit(ctx.expr(0))
            try:
                var_value = self.scope.get_variable(var_name)
                var_value[index] = value
                self.scope.set_variable(var_name, var_value)
                print(f"Przypisano: {var_name}[{index}] = {value}")
            except:
                print(f"Błąd: niepoprawny indeks tablicy dla {var_name}")
        else:
            self.scope.set_variable(var_name, value)
            print(f"Przypisano: {var_name} = {value}")

    def visitReadStmt(self, ctx):
        var_name = ctx.ID().getText()
        if not self.scope.has_variable(var_name):
            print(f"Błąd: zmienna {var_name} nie została zadeklarowana.")
            return

        var_type = self.scope.get_type(var_name)["type"]
        value = input(f"Podaj wartość dla {var_name} ({var_type}): ")
        try:
            if var_type == "int":
                value = int(value)
            elif var_type == "float32":
                value = np.float32(value)
            elif var_type == "float64":
                value = float(value)
            elif var_type == "string":
                value = str(value)
            else:
                raise ValueError()
            self.scope.set_variable(var_name, value)
        except:
            print(f"Błąd: nieprawidłowy format danych dla typu {var_type}")

    def visitPrintStmt(self, ctx):
        try:
            value = self.visit(ctx.expr())
            if isinstance(value, np.float32):
                print(f"{value:.8f}")
            elif isinstance(value, float):
                print(f"{value:.15f}")
            else:
                print(value)
        except Exception as e:
            print(f"Błąd przy wypisywaniu: {e}")

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
            var_value = self.scope.get_variable(var_name)
            if dims == 2:
                row = self.visit(ctx.expr(0))
                col = self.visit(ctx.expr(1))
                return var_value[row][col]
            elif dims == 1:
                index = self.visit(ctx.expr(0))
                return var_value[index]
            else:
                return var_value
        except:
            print(f"Błąd: nie można odczytać {var_name}")
            return None

    def visitParensExpr(self, ctx):
        return self.visit(ctx.expr())

code_1 = """
int globalVar = 10;

float32 power(float32 base, int exponent) {
    float32 result = 1.0;
    int i = 0;
    while (i < exponent) {
        result = result * base;
        i = i + 1;
    }
    return result;
}

void printNumbers(int count) {
    int i = 1;
    while (i <= count) {
        print i;
        if ((i / 2 * 2) == i) {  
            print "even";
        } else {
            print "odd";
        }
        i = i + 1;
    }
}

int factorial(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

void main() {
    int localVar = 5;
    print "Global variable:";
    print globalVar;
    print "Local variable:";
    print localVar;
    print "";
    print "-------------------------------------------------------";
    print "";
    print "Testing power function:";
    float32 p = power(2.5, 3);
    print p;
    
    print "";
    print "-------------------------------------------------------";
    print "";
    print "Testing printNumbers:";
    printNumbers(4);

    print "";
    print "-------------------------------------------------------";
    print "";
    print "Testing factorial:";
    int fact = factorial(5);
    print fact;
    
    print "";
    print "-------------------------------------------------------";
    print "";
    print "Testing if statement:";
    if (globalVar > localVar) {
        print "Global is greater";
    } else {
        print "Local is greater";
    }
    
    print "";
    print "-------------------------------------------------------";
    print "";
    print "Testing while loop:";
    int counter = 3;
    while (counter > 0) {
        print counter;
        counter = counter - 1;
    }

    print "Testing comparison:";
    print (5 > 3);
    print (5 == 3);
}

main();
"""


code_2 = """
void testStandardFor() {
    int i;
    for (i = 0; i < 5; i = i + 1) {
        print i;
    }
}

void testExternalVar() {
    int j = 0;
    for (; j < 3; ) {
        print j;
        j = j + 1;
    }
}

void testInfiniteWithBreak() {
    int k = 0;
    for (; ; ) {
        print k;
        k = k + 1;
        if (k >= 2) {
            break;
        }
    }
}

void testMultipleInits() {
    int a = 0;
    int b = 10;
    for (; a < b; ) {
        print a;
        print b;
        a = a + 1;
        b = b - 1;
    }
}

void main() {
    testStandardFor();
    testExternalVar();
    testInfiniteWithBreak();
    testMultipleInits();
}

main();
"""


input_stream = InputStream(code_1)
lexer = MiniLangLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = MiniLangParser(tokens)
tree = parser.program()

global_scope = Scope()
functions = {}


visitor = MyVisitor(global_scope)
visitor.visit(tree)