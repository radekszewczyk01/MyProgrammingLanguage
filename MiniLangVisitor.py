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


    # Visit a parse tree produced by MiniLangParser#ifStmt.
    def visitIfStmt(self, ctx:MiniLangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#whileStmt.
    def visitWhileStmt(self, ctx:MiniLangParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#forStmt.
    def visitForStmt(self, ctx:MiniLangParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#forControl.
    def visitForControl(self, ctx:MiniLangParser.ForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#forInit.
    def visitForInit(self, ctx:MiniLangParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#forUpdate.
    def visitForUpdate(self, ctx:MiniLangParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#breakStmt.
    def visitBreakStmt(self, ctx:MiniLangParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#block.
    def visitBlock(self, ctx:MiniLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#structDecl.
    def visitStructDecl(self, ctx:MiniLangParser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#memberDecl.
    def visitMemberDecl(self, ctx:MiniLangParser.MemberDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#classDecl.
    def visitClassDecl(self, ctx:MiniLangParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#MethodDeclaration.
    def visitMethodDeclaration(self, ctx:MiniLangParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#ConstructorDeclaration.
    def visitConstructorDeclaration(self, ctx:MiniLangParser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#functionDecl.
    def visitFunctionDecl(self, ctx:MiniLangParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#params.
    def visitParams(self, ctx:MiniLangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#param.
    def visitParam(self, ctx:MiniLangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#functionCall.
    def visitFunctionCall(self, ctx:MiniLangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#memberAccess.
    def visitMemberAccess(self, ctx:MiniLangParser.MemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#args.
    def visitArgs(self, ctx:MiniLangParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#returnStmt.
    def visitReturnStmt(self, ctx:MiniLangParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#StringExpr.
    def visitStringExpr(self, ctx:MiniLangParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#FloatExpr.
    def visitFloatExpr(self, ctx:MiniLangParser.FloatExprContext):
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


    # Visit a parse tree produced by MiniLangParser#FunctionCallExpr.
    def visitFunctionCallExpr(self, ctx:MiniLangParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:MiniLangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#CompareExpr.
    def visitCompareExpr(self, ctx:MiniLangParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#NewExpr.
    def visitNewExpr(self, ctx:MiniLangParser.NewExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#ParensExpr.
    def visitParensExpr(self, ctx:MiniLangParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#IntExpr.
    def visitIntExpr(self, ctx:MiniLangParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#MemberAccessExpr.
    def visitMemberAccessExpr(self, ctx:MiniLangParser.MemberAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:MiniLangParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#MethodCallExpr.
    def visitMethodCallExpr(self, ctx:MiniLangParser.MethodCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#type.
    def visitType(self, ctx:MiniLangParser.TypeContext):
        return self.visitChildren(ctx)



del MiniLangParser