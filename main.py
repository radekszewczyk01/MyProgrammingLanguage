from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from MiniLangVisitor import MiniLangVisitor

# Kod źródłowy w języku MiniLang
code = """
int x;
float32 pi;
float64 big;
string name;
int arr[5];
int mat[2][3];

read x;
read pi;
read big;
read name;

arr[0] = x * 2;
mat[1][2] = arr[0] + 10;

pi = pi * pi;
big = big * big;

print x;
print pi;
print big;
print name;
print arr[0];
print mat[1][2];

int a;
int b;
a = 1;
b = 0;
print a && !b;
"""

input_stream = InputStream(code)
lexer = MiniLangLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = MiniLangParser(tokens)
tree = parser.program()

variables = {}
types = {}

class MyVisitor(MiniLangVisitor):

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitDecl(self, ctx):
        var_type = ctx.type_().getText()
        var_name = ctx.ID().getText()

        dims = len(ctx.INT())
        if dims == 2:  # macierz
            rows = int(ctx.INT(0).getText())
            cols = int(ctx.INT(1).getText())
            variables[var_name] = [[None for _ in range(cols)] for _ in range(rows)]
            types[var_name] = {"type": var_type, "dims": 2}
            print(f"Zadeklarowano macierz: {var_name}[{rows}][{cols}] typu {var_type}")
        elif dims == 1:  # tablica
            size = int(ctx.INT(0).getText())
            variables[var_name] = [None] * size
            types[var_name] = {"type": var_type, "dims": 1}
            print(f"Zadeklarowano tablicę: {var_name}[{size}] typu {var_type}")
        else:  # zmienna
            variables[var_name] = None
            types[var_name] = {"type": var_type, "dims": 0}
            print(f"Zadeklarowano zmienną: {var_name} typu {var_type}")

    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in variables:
            print(f"Błąd: zmienna {var_name} nie została zadeklarowana.")
            return

        dims = len(ctx.expr()) - 1
        value = self.visit(ctx.expr()[-1])

        if dims == 2:  # przypisanie do macierzy
            row = self.visit(ctx.expr(0))
            col = self.visit(ctx.expr(1))
            try:
                variables[var_name][row][col] = value
                print(f"Przypisano: {var_name}[{row}][{col}] = {value}")
            except:
                print(f"Błąd: niepoprawny indeks macierzy dla {var_name}")
        elif dims == 1:  # przypisanie do tablicy
            index = self.visit(ctx.expr(0))
            try:
                variables[var_name][index] = value
                print(f"Przypisano: {var_name}[{index}] = {value}")
            except:
                print(f"Błąd: niepoprawny indeks tablicy dla {var_name}")
        else:  # przypisanie do zmiennej
            variables[var_name] = value
            print(f"Przypisano: {var_name} = {value}")

    def visitReadStmt(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in variables:
            print(f"Błąd: zmienna {var_name} nie została zadeklarowana.")
            return

        var_type = types[var_name]["type"]
        value = input(f"Podaj wartość dla {var_name} ({var_type}): ")
        try:
            if var_type == "int":
                value = int(value)
            elif var_type in ("float32", "float64"):
                value = float(value)
            elif var_type == "string":
                value = str(value)
            else:
                raise ValueError()
            variables[var_name] = value
        except:
            print(f"Błąd: nieprawidłowy format danych dla typu {var_type}")

    def visitPrintStmt(self, ctx):
        try:
            value = self.visit(ctx.expr())
            print(f"{value}")
        except Exception as e:
            print(f"Błąd przy wypisywaniu: {e}")



    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left + right if ctx.op.text == '+' else left - right

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left * right if ctx.op.text == '*' else left / right

    def visitLogicExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '&&':
            return bool(left) and bool(right)
        elif ctx.op.text == '||':
            return bool(left) or bool(right)
        elif ctx.op.text == '^^':
            return bool(left) != bool(right)
        
    def visitNegExpr(self, ctx):
        return not self.visit(ctx.expr())

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
            if dims == 2:
                row = self.visit(ctx.expr(0))
                col = self.visit(ctx.expr(1))
                return variables[var_name][row][col]
            elif dims == 1:
                index = self.visit(ctx.expr(0))
                return variables[var_name][index]
            else:
                return variables.get(var_name)
        except:
            print(f"Błąd: nie można odczytać {var_name}")
            return None

    def visitParensExpr(self, ctx):
        return self.visit(ctx.expr())

# === Uruchomienie programu ===
visitor = MyVisitor()
visitor.visit(tree)
