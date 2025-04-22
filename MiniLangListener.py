# Generated from MiniLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete listener for a parse tree produced by MiniLangParser.
class MiniLangListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLangParser#program.
    def enterProgram(self, ctx:MiniLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniLangParser#program.
    def exitProgram(self, ctx:MiniLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniLangParser#statement.
    def enterStatement(self, ctx:MiniLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniLangParser#statement.
    def exitStatement(self, ctx:MiniLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniLangParser#decl.
    def enterDecl(self, ctx:MiniLangParser.DeclContext):
        pass

    # Exit a parse tree produced by MiniLangParser#decl.
    def exitDecl(self, ctx:MiniLangParser.DeclContext):
        pass


    # Enter a parse tree produced by MiniLangParser#assign.
    def enterAssign(self, ctx:MiniLangParser.AssignContext):
        pass

    # Exit a parse tree produced by MiniLangParser#assign.
    def exitAssign(self, ctx:MiniLangParser.AssignContext):
        pass


    # Enter a parse tree produced by MiniLangParser#readStmt.
    def enterReadStmt(self, ctx:MiniLangParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#readStmt.
    def exitReadStmt(self, ctx:MiniLangParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#printStmt.
    def enterPrintStmt(self, ctx:MiniLangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#printStmt.
    def exitPrintStmt(self, ctx:MiniLangParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#StringExpr.
    def enterStringExpr(self, ctx:MiniLangParser.StringExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#StringExpr.
    def exitStringExpr(self, ctx:MiniLangParser.StringExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#FloatExpr.
    def enterFloatExpr(self, ctx:MiniLangParser.FloatExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#FloatExpr.
    def exitFloatExpr(self, ctx:MiniLangParser.FloatExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:MiniLangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:MiniLangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#IdExpr.
    def enterIdExpr(self, ctx:MiniLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#IdExpr.
    def exitIdExpr(self, ctx:MiniLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#LogicExpr.
    def enterLogicExpr(self, ctx:MiniLangParser.LogicExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#LogicExpr.
    def exitLogicExpr(self, ctx:MiniLangParser.LogicExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#NegExpr.
    def enterNegExpr(self, ctx:MiniLangParser.NegExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#NegExpr.
    def exitNegExpr(self, ctx:MiniLangParser.NegExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#ParensExpr.
    def enterParensExpr(self, ctx:MiniLangParser.ParensExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#ParensExpr.
    def exitParensExpr(self, ctx:MiniLangParser.ParensExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#IntExpr.
    def enterIntExpr(self, ctx:MiniLangParser.IntExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#IntExpr.
    def exitIntExpr(self, ctx:MiniLangParser.IntExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:MiniLangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:MiniLangParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#type.
    def enterType(self, ctx:MiniLangParser.TypeContext):
        pass

    # Exit a parse tree produced by MiniLangParser#type.
    def exitType(self, ctx:MiniLangParser.TypeContext):
        pass



del MiniLangParser