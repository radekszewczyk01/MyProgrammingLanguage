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


    # Enter a parse tree produced by MiniLangParser#ifStmt.
    def enterIfStmt(self, ctx:MiniLangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#ifStmt.
    def exitIfStmt(self, ctx:MiniLangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#whileStmt.
    def enterWhileStmt(self, ctx:MiniLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#whileStmt.
    def exitWhileStmt(self, ctx:MiniLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#forStmt.
    def enterForStmt(self, ctx:MiniLangParser.ForStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#forStmt.
    def exitForStmt(self, ctx:MiniLangParser.ForStmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#forControl.
    def enterForControl(self, ctx:MiniLangParser.ForControlContext):
        pass

    # Exit a parse tree produced by MiniLangParser#forControl.
    def exitForControl(self, ctx:MiniLangParser.ForControlContext):
        pass


    # Enter a parse tree produced by MiniLangParser#forInit.
    def enterForInit(self, ctx:MiniLangParser.ForInitContext):
        pass

    # Exit a parse tree produced by MiniLangParser#forInit.
    def exitForInit(self, ctx:MiniLangParser.ForInitContext):
        pass


    # Enter a parse tree produced by MiniLangParser#forUpdate.
    def enterForUpdate(self, ctx:MiniLangParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by MiniLangParser#forUpdate.
    def exitForUpdate(self, ctx:MiniLangParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by MiniLangParser#breakStmt.
    def enterBreakStmt(self, ctx:MiniLangParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#breakStmt.
    def exitBreakStmt(self, ctx:MiniLangParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by MiniLangParser#block.
    def enterBlock(self, ctx:MiniLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniLangParser#block.
    def exitBlock(self, ctx:MiniLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniLangParser#structDecl.
    def enterStructDecl(self, ctx:MiniLangParser.StructDeclContext):
        pass

    # Exit a parse tree produced by MiniLangParser#structDecl.
    def exitStructDecl(self, ctx:MiniLangParser.StructDeclContext):
        pass


    # Enter a parse tree produced by MiniLangParser#memberDecl.
    def enterMemberDecl(self, ctx:MiniLangParser.MemberDeclContext):
        pass

    # Exit a parse tree produced by MiniLangParser#memberDecl.
    def exitMemberDecl(self, ctx:MiniLangParser.MemberDeclContext):
        pass


    # Enter a parse tree produced by MiniLangParser#classDecl.
    def enterClassDecl(self, ctx:MiniLangParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by MiniLangParser#classDecl.
    def exitClassDecl(self, ctx:MiniLangParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by MiniLangParser#MethodDeclaration.
    def enterMethodDeclaration(self, ctx:MiniLangParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by MiniLangParser#MethodDeclaration.
    def exitMethodDeclaration(self, ctx:MiniLangParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by MiniLangParser#ConstructorDeclaration.
    def enterConstructorDeclaration(self, ctx:MiniLangParser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by MiniLangParser#ConstructorDeclaration.
    def exitConstructorDeclaration(self, ctx:MiniLangParser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by MiniLangParser#functionDecl.
    def enterFunctionDecl(self, ctx:MiniLangParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by MiniLangParser#functionDecl.
    def exitFunctionDecl(self, ctx:MiniLangParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by MiniLangParser#params.
    def enterParams(self, ctx:MiniLangParser.ParamsContext):
        pass

    # Exit a parse tree produced by MiniLangParser#params.
    def exitParams(self, ctx:MiniLangParser.ParamsContext):
        pass


    # Enter a parse tree produced by MiniLangParser#param.
    def enterParam(self, ctx:MiniLangParser.ParamContext):
        pass

    # Exit a parse tree produced by MiniLangParser#param.
    def exitParam(self, ctx:MiniLangParser.ParamContext):
        pass


    # Enter a parse tree produced by MiniLangParser#functionCall.
    def enterFunctionCall(self, ctx:MiniLangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MiniLangParser#functionCall.
    def exitFunctionCall(self, ctx:MiniLangParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MiniLangParser#memberAccess.
    def enterMemberAccess(self, ctx:MiniLangParser.MemberAccessContext):
        pass

    # Exit a parse tree produced by MiniLangParser#memberAccess.
    def exitMemberAccess(self, ctx:MiniLangParser.MemberAccessContext):
        pass


    # Enter a parse tree produced by MiniLangParser#args.
    def enterArgs(self, ctx:MiniLangParser.ArgsContext):
        pass

    # Exit a parse tree produced by MiniLangParser#args.
    def exitArgs(self, ctx:MiniLangParser.ArgsContext):
        pass


    # Enter a parse tree produced by MiniLangParser#returnStmt.
    def enterReturnStmt(self, ctx:MiniLangParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by MiniLangParser#returnStmt.
    def exitReturnStmt(self, ctx:MiniLangParser.ReturnStmtContext):
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


    # Enter a parse tree produced by MiniLangParser#FunctionCallExpr.
    def enterFunctionCallExpr(self, ctx:MiniLangParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#FunctionCallExpr.
    def exitFunctionCallExpr(self, ctx:MiniLangParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:MiniLangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:MiniLangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#CompareExpr.
    def enterCompareExpr(self, ctx:MiniLangParser.CompareExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#CompareExpr.
    def exitCompareExpr(self, ctx:MiniLangParser.CompareExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#NewExpr.
    def enterNewExpr(self, ctx:MiniLangParser.NewExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#NewExpr.
    def exitNewExpr(self, ctx:MiniLangParser.NewExprContext):
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


    # Enter a parse tree produced by MiniLangParser#MemberAccessExpr.
    def enterMemberAccessExpr(self, ctx:MiniLangParser.MemberAccessExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#MemberAccessExpr.
    def exitMemberAccessExpr(self, ctx:MiniLangParser.MemberAccessExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:MiniLangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:MiniLangParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#MethodCallExpr.
    def enterMethodCallExpr(self, ctx:MiniLangParser.MethodCallExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#MethodCallExpr.
    def exitMethodCallExpr(self, ctx:MiniLangParser.MethodCallExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#type.
    def enterType(self, ctx:MiniLangParser.TypeContext):
        pass

    # Exit a parse tree produced by MiniLangParser#type.
    def exitType(self, ctx:MiniLangParser.TypeContext):
        pass



del MiniLangParser