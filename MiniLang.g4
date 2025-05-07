grammar MiniLang;

program : (functionDecl | structDecl | classDecl | statement)+ ;

statement
    : decl
    | assign
    | readStmt
    | printStmt
    | ifStmt
    | whileStmt
    | forStmt
    | breakStmt
    | block
    | returnStmt
    | functionCall ';'
    ;

decl
    : type ID ('[' INT ']' ('[' INT ']')?)? ('=' expr)? ';'
    ;

assign
    : (ID | memberAccess) ('[' expr ']' ('[' expr ']')?)? '=' expr ';'
    ;

readStmt
    : 'read' (ID | memberAccess) ';'
    ;

printStmt: 'print' expr ';';

ifStmt
    : 'if' '(' expr ')' statement ('else' statement)?
    ;

whileStmt
    : 'while' '(' expr ')' statement
    ;

forStmt
    : 'for' '(' forControl ')' statement
    ;

forControl
    : (forInit | ) ';' (expr | ) ';' (forUpdate | )
    ;

forInit
    : decl
    | assign (',' assign)*
    ;

forUpdate
    : assign (',' assign)*
    ;

breakStmt
    : 'break' ';'
    ;

block
    : '{' statement* '}'
    ;

structDecl
    : 'struct' ID '{' (memberDecl ';')+ '}' ';'
    ;

memberDecl
    : type ID
    ;

classDecl
    : 'class' ID ('extends' ID)? '{'
      (memberDecl ';' | methodDecl)*
      '}' ';'
    ;

methodDecl
    : type ID '(' params? ')' block  # MethodDeclaration
    | 'constructor' '(' params? ')' block  # ConstructorDeclaration
    ;

functionDecl
    : type ID '(' params? ')' block
    ;

params
    : param (',' param)*
    ;

param
    : type ID
    ;

functionCall
    : (ID | memberAccess) '(' args? ')'
    ;

memberAccess
    : ID '.' ID ('.' ID)*
    ;

args
    : expr (',' expr)*
    ;

returnStmt
    : 'return' expr? ';'
    ;

expr
    : expr op=('*'|'/'|'%') expr           # MulDivExpr
    | expr op=('+'|'-') expr               # AddSubExpr
    | expr op=('&&' | '||' | '^^') expr    # LogicExpr
    | expr op=('==' | '!=' | '<' | '>' | '<=' | '>=') expr # CompareExpr
    | '!' expr                             # NegExpr
    | memberAccess '(' args? ')'           # MethodCallExpr
    | ID '(' args? ')'                     # FunctionCallExpr
    | memberAccess                         # MemberAccessExpr
    | ID ('[' expr ']' ('[' expr ']')?)?   # IdExpr
    | FLOAT                                # FloatExpr
    | INT                                  # IntExpr
    | STRING                               # StringExpr
    | 'new' ID '(' args? ')'               # NewExpr
    | '(' expr ')'                         # ParensExpr
    ;

type
    : 'int'
    | 'float32'
    | 'float64'
    | 'string'
    | 'void'
    | ID
    ;

ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
INT    : [0-9]+ ;
FLOAT  : [0-9]+ '.' [0-9]+ ;
STRING : '"' (~["\r\n])* '"' ;

WS : [ \t\r\n]+ -> skip ;

COMMA : ',' ;
SEMI : ';' ;