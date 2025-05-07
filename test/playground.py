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
        # Check if variable is a class member and prepend 'this'
        if self.current_class:
            try:
                class_def = self.scope.get_class(self.current_class)
                if var_name in class_def['members']:
                    var_name = 'this.' + var_name
                    print(f"Resolved variable {var_name} as class member")
            except NameError:
                pass
        # Existing logic for variable assignment
        # ... [rest of the code]