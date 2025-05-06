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
        4,1,42,264,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,4,0,47,8,0,11,0,12,0,48,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,64,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,74,8,2,3,2,76,8,2,1,2,1,2,3,2,80,8,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,92,8,3,3,3,94,8,3,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,
        6,115,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,
        9,3,9,131,8,9,1,9,1,9,1,9,3,9,136,8,9,1,9,1,9,1,9,3,9,141,8,9,1,
        10,1,10,1,10,1,10,5,10,147,8,10,10,10,12,10,150,9,10,3,10,152,8,
        10,1,11,1,11,1,11,5,11,157,8,11,10,11,12,11,160,9,11,1,12,1,12,1,
        12,1,13,1,13,5,13,167,8,13,10,13,12,13,170,9,13,1,13,1,13,1,14,1,
        14,1,14,1,14,3,14,178,8,14,1,14,1,14,1,14,1,15,1,15,1,15,5,15,186,
        8,15,10,15,12,15,189,9,15,1,16,1,16,1,16,1,17,1,17,1,17,3,17,197,
        8,17,1,17,1,17,1,18,1,18,1,18,5,18,204,8,18,10,18,12,18,207,9,18,
        1,19,1,19,3,19,211,8,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,
        3,20,221,8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,
        232,8,20,3,20,234,8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,243,
        8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        5,20,257,8,20,10,20,12,20,260,9,20,1,21,1,21,1,21,0,1,40,22,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,5,1,0,
        16,18,1,0,19,20,1,0,21,23,1,0,24,29,1,0,31,35,284,0,46,1,0,0,0,2,
        63,1,0,0,0,4,65,1,0,0,0,6,83,1,0,0,0,8,99,1,0,0,0,10,103,1,0,0,0,
        12,107,1,0,0,0,14,116,1,0,0,0,16,122,1,0,0,0,18,130,1,0,0,0,20,151,
        1,0,0,0,22,153,1,0,0,0,24,161,1,0,0,0,26,164,1,0,0,0,28,173,1,0,
        0,0,30,182,1,0,0,0,32,190,1,0,0,0,34,193,1,0,0,0,36,200,1,0,0,0,
        38,208,1,0,0,0,40,242,1,0,0,0,42,261,1,0,0,0,44,47,3,28,14,0,45,
        47,3,2,1,0,46,44,1,0,0,0,46,45,1,0,0,0,47,48,1,0,0,0,48,46,1,0,0,
        0,48,49,1,0,0,0,49,1,1,0,0,0,50,64,3,4,2,0,51,64,3,6,3,0,52,64,3,
        8,4,0,53,64,3,10,5,0,54,64,3,12,6,0,55,64,3,14,7,0,56,64,3,16,8,
        0,57,64,3,24,12,0,58,64,3,26,13,0,59,64,3,38,19,0,60,61,3,34,17,
        0,61,62,5,42,0,0,62,64,1,0,0,0,63,50,1,0,0,0,63,51,1,0,0,0,63,52,
        1,0,0,0,63,53,1,0,0,0,63,54,1,0,0,0,63,55,1,0,0,0,63,56,1,0,0,0,
        63,57,1,0,0,0,63,58,1,0,0,0,63,59,1,0,0,0,63,60,1,0,0,0,64,3,1,0,
        0,0,65,66,3,42,21,0,66,75,5,36,0,0,67,68,5,1,0,0,68,69,5,37,0,0,
        69,73,5,2,0,0,70,71,5,1,0,0,71,72,5,37,0,0,72,74,5,2,0,0,73,70,1,
        0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,67,1,0,0,0,75,76,1,0,0,0,76,
        79,1,0,0,0,77,78,5,3,0,0,78,80,3,40,20,0,79,77,1,0,0,0,79,80,1,0,
        0,0,80,81,1,0,0,0,81,82,5,42,0,0,82,5,1,0,0,0,83,93,5,36,0,0,84,
        85,5,1,0,0,85,86,3,40,20,0,86,91,5,2,0,0,87,88,5,1,0,0,88,89,3,40,
        20,0,89,90,5,2,0,0,90,92,1,0,0,0,91,87,1,0,0,0,91,92,1,0,0,0,92,
        94,1,0,0,0,93,84,1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,96,5,3,0,
        0,96,97,3,40,20,0,97,98,5,42,0,0,98,7,1,0,0,0,99,100,5,4,0,0,100,
        101,5,36,0,0,101,102,5,42,0,0,102,9,1,0,0,0,103,104,5,5,0,0,104,
        105,3,40,20,0,105,106,5,42,0,0,106,11,1,0,0,0,107,108,5,6,0,0,108,
        109,5,7,0,0,109,110,3,40,20,0,110,111,5,8,0,0,111,114,3,2,1,0,112,
        113,5,9,0,0,113,115,3,2,1,0,114,112,1,0,0,0,114,115,1,0,0,0,115,
        13,1,0,0,0,116,117,5,10,0,0,117,118,5,7,0,0,118,119,3,40,20,0,119,
        120,5,8,0,0,120,121,3,2,1,0,121,15,1,0,0,0,122,123,5,11,0,0,123,
        124,5,7,0,0,124,125,3,18,9,0,125,126,5,8,0,0,126,127,3,2,1,0,127,
        17,1,0,0,0,128,131,3,20,10,0,129,131,1,0,0,0,130,128,1,0,0,0,130,
        129,1,0,0,0,131,132,1,0,0,0,132,135,5,42,0,0,133,136,3,40,20,0,134,
        136,1,0,0,0,135,133,1,0,0,0,135,134,1,0,0,0,136,137,1,0,0,0,137,
        140,5,42,0,0,138,141,3,22,11,0,139,141,1,0,0,0,140,138,1,0,0,0,140,
        139,1,0,0,0,141,19,1,0,0,0,142,152,3,4,2,0,143,148,3,6,3,0,144,145,
        5,41,0,0,145,147,3,6,3,0,146,144,1,0,0,0,147,150,1,0,0,0,148,146,
        1,0,0,0,148,149,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,151,142,
        1,0,0,0,151,143,1,0,0,0,152,21,1,0,0,0,153,158,3,6,3,0,154,155,5,
        41,0,0,155,157,3,6,3,0,156,154,1,0,0,0,157,160,1,0,0,0,158,156,1,
        0,0,0,158,159,1,0,0,0,159,23,1,0,0,0,160,158,1,0,0,0,161,162,5,12,
        0,0,162,163,5,42,0,0,163,25,1,0,0,0,164,168,5,13,0,0,165,167,3,2,
        1,0,166,165,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,
        0,0,169,171,1,0,0,0,170,168,1,0,0,0,171,172,5,14,0,0,172,27,1,0,
        0,0,173,174,3,42,21,0,174,175,5,36,0,0,175,177,5,7,0,0,176,178,3,
        30,15,0,177,176,1,0,0,0,177,178,1,0,0,0,178,179,1,0,0,0,179,180,
        5,8,0,0,180,181,3,26,13,0,181,29,1,0,0,0,182,187,3,32,16,0,183,184,
        5,41,0,0,184,186,3,32,16,0,185,183,1,0,0,0,186,189,1,0,0,0,187,185,
        1,0,0,0,187,188,1,0,0,0,188,31,1,0,0,0,189,187,1,0,0,0,190,191,3,
        42,21,0,191,192,5,36,0,0,192,33,1,0,0,0,193,194,5,36,0,0,194,196,
        5,7,0,0,195,197,3,36,18,0,196,195,1,0,0,0,196,197,1,0,0,0,197,198,
        1,0,0,0,198,199,5,8,0,0,199,35,1,0,0,0,200,205,3,40,20,0,201,202,
        5,41,0,0,202,204,3,40,20,0,203,201,1,0,0,0,204,207,1,0,0,0,205,203,
        1,0,0,0,205,206,1,0,0,0,206,37,1,0,0,0,207,205,1,0,0,0,208,210,5,
        15,0,0,209,211,3,40,20,0,210,209,1,0,0,0,210,211,1,0,0,0,211,212,
        1,0,0,0,212,213,5,42,0,0,213,39,1,0,0,0,214,215,6,20,-1,0,215,216,
        5,30,0,0,216,243,3,40,20,7,217,218,5,36,0,0,218,220,5,7,0,0,219,
        221,3,36,18,0,220,219,1,0,0,0,220,221,1,0,0,0,221,222,1,0,0,0,222,
        243,5,8,0,0,223,233,5,36,0,0,224,225,5,1,0,0,225,226,3,40,20,0,226,
        231,5,2,0,0,227,228,5,1,0,0,228,229,3,40,20,0,229,230,5,2,0,0,230,
        232,1,0,0,0,231,227,1,0,0,0,231,232,1,0,0,0,232,234,1,0,0,0,233,
        224,1,0,0,0,233,234,1,0,0,0,234,243,1,0,0,0,235,243,5,38,0,0,236,
        243,5,37,0,0,237,243,5,39,0,0,238,239,5,7,0,0,239,240,3,40,20,0,
        240,241,5,8,0,0,241,243,1,0,0,0,242,214,1,0,0,0,242,217,1,0,0,0,
        242,223,1,0,0,0,242,235,1,0,0,0,242,236,1,0,0,0,242,237,1,0,0,0,
        242,238,1,0,0,0,243,258,1,0,0,0,244,245,10,11,0,0,245,246,7,0,0,
        0,246,257,3,40,20,12,247,248,10,10,0,0,248,249,7,1,0,0,249,257,3,
        40,20,11,250,251,10,9,0,0,251,252,7,2,0,0,252,257,3,40,20,10,253,
        254,10,8,0,0,254,255,7,3,0,0,255,257,3,40,20,9,256,244,1,0,0,0,256,
        247,1,0,0,0,256,250,1,0,0,0,256,253,1,0,0,0,257,260,1,0,0,0,258,
        256,1,0,0,0,258,259,1,0,0,0,259,41,1,0,0,0,260,258,1,0,0,0,261,262,
        7,4,0,0,262,43,1,0,0,0,27,46,48,63,73,75,79,91,93,114,130,135,140,
        148,151,158,168,177,187,196,205,210,220,231,233,242,256,258
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'='", "'read'", "'print'", 
                     "'if'", "'('", "')'", "'else'", "'while'", "'for'", 
                     "'break'", "'{'", "'}'", "'return'", "'*'", "'/'", 
                     "'%'", "'+'", "'-'", "'&&'", "'||'", "'^^'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'!'", "'int'", 
                     "'float32'", "'float64'", "'string'", "'void'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "FLOAT", "STRING", "WS", "COMMA", "SEMI" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_decl = 2
    RULE_assign = 3
    RULE_readStmt = 4
    RULE_printStmt = 5
    RULE_ifStmt = 6
    RULE_whileStmt = 7
    RULE_forStmt = 8
    RULE_forControl = 9
    RULE_forInit = 10
    RULE_forUpdate = 11
    RULE_breakStmt = 12
    RULE_block = 13
    RULE_functionDecl = 14
    RULE_params = 15
    RULE_param = 16
    RULE_functionCall = 17
    RULE_args = 18
    RULE_returnStmt = 19
    RULE_expr = 20
    RULE_type = 21

    ruleNames =  [ "program", "statement", "decl", "assign", "readStmt", 
                   "printStmt", "ifStmt", "whileStmt", "forStmt", "forControl", 
                   "forInit", "forUpdate", "breakStmt", "block", "functionDecl", 
                   "params", "param", "functionCall", "args", "returnStmt", 
                   "expr", "type" ]

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
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    ID=36
    INT=37
    FLOAT=38
    STRING=39
    WS=40
    COMMA=41
    SEMI=42

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

        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.FunctionDeclContext,i)


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
            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 44
                    self.functionDecl()
                    pass

                elif la_ == 2:
                    self.state = 45
                    self.statement()
                    pass


                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 135291518064) != 0)):
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


        def ifStmt(self):
            return self.getTypedRuleContext(MiniLangParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(MiniLangParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(MiniLangParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(MiniLangParser.BreakStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniLangParser.BlockContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(MiniLangParser.ReturnStmtContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(MiniLangParser.FunctionCallContext,0)


        def SEMI(self):
            return self.getToken(MiniLangParser.SEMI, 0)

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
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.readStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.printStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.ifStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.whileStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 56
                self.forStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 57
                self.breakStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 58
                self.block()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 59
                self.returnStmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 60
                self.functionCall()
                self.state = 61
                self.match(MiniLangParser.SEMI)
                pass


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

        def SEMI(self):
            return self.getToken(MiniLangParser.SEMI, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.INT)
            else:
                return self.getToken(MiniLangParser.INT, i)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


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
            self.state = 65
            self.type_()
            self.state = 66
            self.match(MiniLangParser.ID)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 67
                self.match(MiniLangParser.T__0)
                self.state = 68
                self.match(MiniLangParser.INT)
                self.state = 69
                self.match(MiniLangParser.T__1)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 70
                    self.match(MiniLangParser.T__0)
                    self.state = 71
                    self.match(MiniLangParser.INT)
                    self.state = 72
                    self.match(MiniLangParser.T__1)




            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 77
                self.match(MiniLangParser.T__2)
                self.state = 78
                self.expr(0)


            self.state = 81
            self.match(MiniLangParser.SEMI)
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


        def SEMI(self):
            return self.getToken(MiniLangParser.SEMI, 0)

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
            self.state = 83
            self.match(MiniLangParser.ID)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 84
                self.match(MiniLangParser.T__0)
                self.state = 85
                self.expr(0)
                self.state = 86
                self.match(MiniLangParser.T__1)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 87
                    self.match(MiniLangParser.T__0)
                    self.state = 88
                    self.expr(0)
                    self.state = 89
                    self.match(MiniLangParser.T__1)




            self.state = 95
            self.match(MiniLangParser.T__2)
            self.state = 96
            self.expr(0)
            self.state = 97
            self.match(MiniLangParser.SEMI)
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

        def SEMI(self):
            return self.getToken(MiniLangParser.SEMI, 0)

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
            self.state = 99
            self.match(MiniLangParser.T__3)
            self.state = 100
            self.match(MiniLangParser.ID)
            self.state = 101
            self.match(MiniLangParser.SEMI)
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


        def SEMI(self):
            return self.getToken(MiniLangParser.SEMI, 0)

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
            self.state = 103
            self.match(MiniLangParser.T__4)
            self.state = 104
            self.expr(0)
            self.state = 105
            self.match(MiniLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = MiniLangParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(MiniLangParser.T__5)
            self.state = 108
            self.match(MiniLangParser.T__6)
            self.state = 109
            self.expr(0)
            self.state = 110
            self.match(MiniLangParser.T__7)
            self.state = 111
            self.statement()
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 112
                self.match(MiniLangParser.T__8)
                self.state = 113
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(MiniLangParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = MiniLangParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(MiniLangParser.T__9)
            self.state = 117
            self.match(MiniLangParser.T__6)
            self.state = 118
            self.expr(0)
            self.state = 119
            self.match(MiniLangParser.T__7)
            self.state = 120
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forControl(self):
            return self.getTypedRuleContext(MiniLangParser.ForControlContext,0)


        def statement(self):
            return self.getTypedRuleContext(MiniLangParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = MiniLangParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(MiniLangParser.T__10)
            self.state = 123
            self.match(MiniLangParser.T__6)
            self.state = 124
            self.forControl()
            self.state = 125
            self.match(MiniLangParser.T__7)
            self.state = 126
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.SEMI)
            else:
                return self.getToken(MiniLangParser.SEMI, i)

        def forInit(self):
            return self.getTypedRuleContext(MiniLangParser.ForInitContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(MiniLangParser.ForUpdateContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_forControl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForControl" ):
                listener.enterForControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForControl" ):
                listener.exitForControl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForControl" ):
                return visitor.visitForControl(self)
            else:
                return visitor.visitChildren(self)




    def forControl(self):

        localctx = MiniLangParser.ForControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forControl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31, 32, 33, 34, 35, 36]:
                self.state = 128
                self.forInit()
                pass
            elif token in [42]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 132
            self.match(MiniLangParser.SEMI)
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 30, 36, 37, 38, 39]:
                self.state = 133
                self.expr(0)
                pass
            elif token in [42]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 137
            self.match(MiniLangParser.SEMI)
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.state = 138
                self.forUpdate()
                pass
            elif token in [8]:
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


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniLangParser.DeclContext,0)


        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.AssignContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.AssignContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.COMMA)
            else:
                return self.getToken(MiniLangParser.COMMA, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = MiniLangParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forInit)
        self._la = 0 # Token type
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31, 32, 33, 34, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.decl()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.assign()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==41:
                    self.state = 144
                    self.match(MiniLangParser.COMMA)
                    self.state = 145
                    self.assign()
                    self.state = 150
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.AssignContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.AssignContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.COMMA)
            else:
                return self.getToken(MiniLangParser.COMMA, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_forUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdate" ):
                listener.enterForUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdate" ):
                listener.exitForUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = MiniLangParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forUpdate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.assign()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 154
                self.match(MiniLangParser.COMMA)
                self.state = 155
                self.assign()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = MiniLangParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MiniLangParser.T__11)
            self.state = 162
            self.match(MiniLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
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
            return MiniLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(MiniLangParser.T__12)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 135291518064) != 0):
                self.state = 165
                self.statement()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 171
            self.match(MiniLangParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(MiniLangParser.BlockContext,0)


        def params(self):
            return self.getTypedRuleContext(MiniLangParser.ParamsContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = MiniLangParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.type_()
            self.state = 174
            self.match(MiniLangParser.ID)
            self.state = 175
            self.match(MiniLangParser.T__6)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66571993088) != 0):
                self.state = 176
                self.params()


            self.state = 179
            self.match(MiniLangParser.T__7)
            self.state = 180
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.COMMA)
            else:
                return self.getToken(MiniLangParser.COMMA, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = MiniLangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.param()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 183
                self.match(MiniLangParser.COMMA)
                self.state = 184
                self.param()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.type_()
            self.state = 191
            self.match(MiniLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(MiniLangParser.ArgsContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = MiniLangParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MiniLangParser.ID)
            self.state = 194
            self.match(MiniLangParser.T__6)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1031865892992) != 0):
                self.state = 195
                self.args()


            self.state = 198
            self.match(MiniLangParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.COMMA)
            else:
                return self.getToken(MiniLangParser.COMMA, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = MiniLangParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.expr(0)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 201
                self.match(MiniLangParser.COMMA)
                self.state = 202
                self.expr(0)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniLangParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = MiniLangParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(MiniLangParser.T__14)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1031865892992) != 0):
                self.state = 209
                self.expr(0)


            self.state = 212
            self.match(MiniLangParser.SEMI)
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


    class FunctionCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)
        def args(self):
            return self.getTypedRuleContext(MiniLangParser.ArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpr" ):
                listener.enterFunctionCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpr" ):
                listener.exitFunctionCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpr" ):
                return visitor.visitFunctionCallExpr(self)
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


    class CompareExprContext(ExprContext):

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
            if hasattr( listener, "enterCompareExpr" ):
                listener.enterCompareExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareExpr" ):
                listener.exitCompareExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareExpr" ):
                return visitor.visitCompareExpr(self)
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.NegExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 215
                self.match(MiniLangParser.T__29)
                self.state = 216
                self.expr(7)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 217
                self.match(MiniLangParser.ID)
                self.state = 218
                self.match(MiniLangParser.T__6)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1031865892992) != 0):
                    self.state = 219
                    self.args()


                self.state = 222
                self.match(MiniLangParser.T__7)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 223
                self.match(MiniLangParser.ID)
                self.state = 233
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 224
                    self.match(MiniLangParser.T__0)
                    self.state = 225
                    self.expr(0)
                    self.state = 226
                    self.match(MiniLangParser.T__1)
                    self.state = 231
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        self.state = 227
                        self.match(MiniLangParser.T__0)
                        self.state = 228
                        self.expr(0)
                        self.state = 229
                        self.match(MiniLangParser.T__1)




                pass

            elif la_ == 4:
                localctx = MiniLangParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 235
                self.match(MiniLangParser.FLOAT)
                pass

            elif la_ == 5:
                localctx = MiniLangParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 236
                self.match(MiniLangParser.INT)
                pass

            elif la_ == 6:
                localctx = MiniLangParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 237
                self.match(MiniLangParser.STRING)
                pass

            elif la_ == 7:
                localctx = MiniLangParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 238
                self.match(MiniLangParser.T__6)
                self.state = 239
                self.expr(0)
                self.state = 240
                self.match(MiniLangParser.T__7)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 256
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MulDivExprContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 244
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 245
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 246
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.AddSubExprContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 247
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 248
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 249
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.LogicExprContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 250
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 251
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 252
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = MiniLangParser.CompareExprContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 253
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 254
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 255
                        self.expr(9)
                        pass

             
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66571993088) != 0)):
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
        self._predicates[20] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         




