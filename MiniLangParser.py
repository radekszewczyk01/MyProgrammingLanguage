# Generated from MiniLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,1,1,1,1,1,1,1,3,1,26,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,36,8,2,3,2,38,8,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,50,8,3,3,3,52,8,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,77,8,6,3,6,79,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,3,6,88,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,99,8,6,10,6,
        12,6,102,9,6,1,7,1,7,1,7,0,1,12,8,0,2,4,6,8,10,12,14,0,4,1,0,7,8,
        1,0,9,10,1,0,11,13,1,0,17,20,115,0,17,1,0,0,0,2,25,1,0,0,0,4,27,
        1,0,0,0,6,41,1,0,0,0,8,57,1,0,0,0,10,61,1,0,0,0,12,87,1,0,0,0,14,
        103,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,
        0,0,19,20,1,0,0,0,20,1,1,0,0,0,21,26,3,4,2,0,22,26,3,6,3,0,23,26,
        3,8,4,0,24,26,3,10,5,0,25,21,1,0,0,0,25,22,1,0,0,0,25,23,1,0,0,0,
        25,24,1,0,0,0,26,3,1,0,0,0,27,28,3,14,7,0,28,37,5,21,0,0,29,30,5,
        1,0,0,30,31,5,22,0,0,31,35,5,2,0,0,32,33,5,1,0,0,33,34,5,22,0,0,
        34,36,5,2,0,0,35,32,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,29,1,
        0,0,0,37,38,1,0,0,0,38,39,1,0,0,0,39,40,5,3,0,0,40,5,1,0,0,0,41,
        51,5,21,0,0,42,43,5,1,0,0,43,44,3,12,6,0,44,49,5,2,0,0,45,46,5,1,
        0,0,46,47,3,12,6,0,47,48,5,2,0,0,48,50,1,0,0,0,49,45,1,0,0,0,49,
        50,1,0,0,0,50,52,1,0,0,0,51,42,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,
        0,53,54,5,4,0,0,54,55,3,12,6,0,55,56,5,3,0,0,56,7,1,0,0,0,57,58,
        5,5,0,0,58,59,5,21,0,0,59,60,5,3,0,0,60,9,1,0,0,0,61,62,5,6,0,0,
        62,63,3,12,6,0,63,64,5,3,0,0,64,11,1,0,0,0,65,66,6,6,-1,0,66,67,
        5,14,0,0,67,88,3,12,6,6,68,78,5,21,0,0,69,70,5,1,0,0,70,71,3,12,
        6,0,71,76,5,2,0,0,72,73,5,1,0,0,73,74,3,12,6,0,74,75,5,2,0,0,75,
        77,1,0,0,0,76,72,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,69,1,0,0,
        0,78,79,1,0,0,0,79,88,1,0,0,0,80,88,5,23,0,0,81,88,5,22,0,0,82,88,
        5,24,0,0,83,84,5,15,0,0,84,85,3,12,6,0,85,86,5,16,0,0,86,88,1,0,
        0,0,87,65,1,0,0,0,87,68,1,0,0,0,87,80,1,0,0,0,87,81,1,0,0,0,87,82,
        1,0,0,0,87,83,1,0,0,0,88,100,1,0,0,0,89,90,10,9,0,0,90,91,7,0,0,
        0,91,99,3,12,6,10,92,93,10,8,0,0,93,94,7,1,0,0,94,99,3,12,6,9,95,
        96,10,7,0,0,96,97,7,2,0,0,97,99,3,12,6,8,98,89,1,0,0,0,98,92,1,0,
        0,0,98,95,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,
        101,13,1,0,0,0,102,100,1,0,0,0,103,104,7,3,0,0,104,15,1,0,0,0,11,
        19,25,35,37,49,51,76,78,87,98,100
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "';'", "'='", "'read'", 
                     "'print'", "'*'", "'/'", "'+'", "'-'", "'&&'", "'||'", 
                     "'^^'", "'!'", "'('", "')'", "'int'", "'float32'", 
                     "'float64'", "'string'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "FLOAT", "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_decl = 2
    RULE_assign = 3
    RULE_readStmt = 4
    RULE_printStmt = 5
    RULE_expr = 6
    RULE_type = 7

    ruleNames =  [ "program", "statement", "decl", "assign", "readStmt", 
                   "printStmt", "expr", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    ID=21
    INT=22
    FLOAT=23
    STRING=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.statement()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4063328) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniLangParser.DeclContext,0)


        def assign(self):
            return self.getTypedRuleContext(MiniLangParser.AssignContext,0)


        def readStmt(self):
            return self.getTypedRuleContext(MiniLangParser.ReadStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(MiniLangParser.PrintStmtContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 19, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.decl()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.assign()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.readStmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.printStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.INT)
            else:
                return self.getToken(MiniLangParser.INT, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniLangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.type_()
            self.state = 28
            self.match(MiniLangParser.ID)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 29
                self.match(MiniLangParser.T__0)
                self.state = 30
                self.match(MiniLangParser.INT)
                self.state = 31
                self.match(MiniLangParser.T__1)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 32
                    self.match(MiniLangParser.T__0)
                    self.state = 33
                    self.match(MiniLangParser.INT)
                    self.state = 34
                    self.match(MiniLangParser.T__1)




            self.state = 39
            self.match(MiniLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MiniLangParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(MiniLangParser.ID)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 42
                self.match(MiniLangParser.T__0)
                self.state = 43
                self.expr(0)
                self.state = 44
                self.match(MiniLangParser.T__1)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 45
                    self.match(MiniLangParser.T__0)
                    self.state = 46
                    self.expr(0)
                    self.state = 47
                    self.match(MiniLangParser.T__1)




            self.state = 53
            self.match(MiniLangParser.T__3)
            self.state = 54
            self.expr(0)
            self.state = 55
            self.match(MiniLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_readStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStmt" ):
                return visitor.visitReadStmt(self)
            else:
                return visitor.visitChildren(self)




    def readStmt(self):

        localctx = MiniLangParser.ReadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_readStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MiniLangParser.T__4)
            self.state = 58
            self.match(MiniLangParser.ID)
            self.state = 59
            self.match(MiniLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = MiniLangParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(MiniLangParser.T__5)
            self.state = 62
            self.expr(0)
            self.state = 63
            self.match(MiniLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(MiniLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class FloatExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(MiniLangParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatExpr" ):
                listener.enterFloatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatExpr" ):
                listener.exitFloatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class LogicExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicExpr" ):
                listener.enterLogicExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicExpr" ):
                listener.exitLogicExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpr" ):
                return visitor.visitLogicExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegExpr" ):
                listener.enterNegExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegExpr" ):
                listener.exitNegExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegExpr" ):
                return visitor.visitNegExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiniLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                localctx = MiniLangParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 66
                self.match(MiniLangParser.T__13)
                self.state = 67
                self.expr(6)
                pass
            elif token in [21]:
                localctx = MiniLangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.match(MiniLangParser.ID)
                self.state = 78
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 69
                    self.match(MiniLangParser.T__0)
                    self.state = 70
                    self.expr(0)
                    self.state = 71
                    self.match(MiniLangParser.T__1)
                    self.state = 76
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        self.state = 72
                        self.match(MiniLangParser.T__0)
                        self.state = 73
                        self.expr(0)
                        self.state = 74
                        self.match(MiniLangParser.T__1)




                pass
            elif token in [23]:
                localctx = MiniLangParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                self.match(MiniLangParser.FLOAT)
                pass
            elif token in [22]:
                localctx = MiniLangParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.match(MiniLangParser.INT)
                pass
            elif token in [24]:
                localctx = MiniLangParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 82
                self.match(MiniLangParser.STRING)
                pass
            elif token in [15]:
                localctx = MiniLangParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 83
                self.match(MiniLangParser.T__14)
                self.state = 84
                self.expr(0)
                self.state = 85
                self.match(MiniLangParser.T__15)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 100
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 98
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MulDivExprContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 90
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 91
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.AddSubExprContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 92
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 93
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 94
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.LogicExprContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 95
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 96
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 97
                        self.expr(8)
                        pass

             
                self.state = 102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1966080) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         




