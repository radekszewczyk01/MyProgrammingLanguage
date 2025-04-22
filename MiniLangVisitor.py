# Generated from MiniLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLangParser#program.
    def visitProgram(self, ctx:MiniLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#statement.
    def visitStatement(self, ctx:MiniLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#decl.
    def visitDecl(self, ctx:MiniLangParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#assign.
    def visitAssign(self, ctx:MiniLangParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#readStmt.
    def visitReadStmt(self, ctx:MiniLangParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#printStmt.
    def visitPrintStmt(self, ctx:MiniLangParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#StringExpr.
    def visitStringExpr(self, ctx:MiniLangParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#FloatExpr.
    def visitFloatExpr(self, ctx:MiniLangParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:MiniLangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#IdExpr.
    def visitIdExpr(self, ctx:MiniLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#LogicExpr.
    def visitLogicExpr(self, ctx:MiniLangParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#NegExpr.
    def visitNegExpr(self, ctx:MiniLangParser.NegExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#ParensExpr.
    def visitParensExpr(self, ctx:MiniLangParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#IntExpr.
    def visitIntExpr(self, ctx:MiniLangParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:MiniLangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#type.
    def visitType(self, ctx:MiniLangParser.TypeContext):
        return self.visitChildren(ctx)



del MiniLangParser