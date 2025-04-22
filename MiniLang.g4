grammar MiniLang;

program : statement+ ;

statement
    : decl
    | assign
    | readStmt
    | printStmt
    ;

decl
    : type ID ('[' INT ']' ('[' INT ']')?)? ';'
    ; // zmienna, tablica, macierz

assign
    : ID ('[' expr ']' ('[' expr ']')?)? '=' expr ';'
    ;

readStmt
    : 'read' ID ';'
    ;

printStmt: 'print' expr ';';


expr
    : expr op=('*'|'/') expr           # MulDivExpr
    | expr op=('+'|'-') expr           # AddSubExpr
    | expr op=('&&' | '||' | '^^') expr # LogicExpr
    | '!' expr                         # NegExpr
    | ID ('[' expr ']' ('[' expr ']')?)?  # IdExpr
    | FLOAT                            # FloatExpr
    | INT                              # IntExpr
    | STRING                           # StringExpr
    | '(' expr ')'                     # ParensExpr
    ;

type
    : 'int'
    | 'float32'
    | 'float64'
    | 'string'
    ;

ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
INT    : [0-9]+ ;
FLOAT  : [0-9]+ '.' [0-9]+ ;
STRING : '"' (~["\r\n])* '"' ;

WS : [ \t\r\n]+ -> skip ;
