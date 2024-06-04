import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_101(self):
        """test BKEL"""
        ip = 'abc'
        op = 'abc,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 101))

    def test_102(self):
        """test BKEL"""
        ip = '1234567'
        op = '1234567,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 102))

    def test_103(self):
        """test BKEL"""
        ip = '1234.567'
        op = '1234.567,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 103))

    def test_104(self):
        """test BKEL"""
        ip = '"He asked me: \'"Where is John?\'""'
        op = 'He asked me: \'\"Where is John?\'\",<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 104))

    def test_105(self):
        """test comment inline"""
        ip = 'abc ##123'
        op = 'abc,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 105))

    def test_106(self):
        """test comment inline"""
        ip = """ abc ##,.&*#[]~ """
        op = 'abc,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 106))

    def test_107(self):
        """test comment in newline"""
        ip = """
##123 ##,.&*#[]~ qwer
abc
"""
        op = """
,
,abc,
,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 107))

    def test_108(self):
        """test comment in newline"""
        ip = """
##123 ##,.&*#[]~ qwer
abc
##123 ##,.&*#[]~ qwer
"""
        op = """
,
,abc,
,
,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 108))

    def test_109(self):
        """test comment in newline and inline"""
        ip = """
##123
abc ##123 ##### qwer
"""
        op = """
,
,abc,
,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 109))

    def test_110(self):
        """test comment in newline and inline"""
        ip = """
##123 ##
abc ##123 ##### qwer
##123 ##,.&*#[]~ qwer
"""
        op = """
,
,abc,
,
,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 110))

    def test_111(self):
        """test KEYWORDS"""
        ip = "true false number bool string return var dynamic func for until by break continue if else elif begin end not and or"
        op = "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,<EOF>"
        self.assertTrue(TestLexer.test(ip, op, 111))

    def test_112(self):
        """test OPERATORS"""
        ip = '+-*/%= <- != < <= > >= ... =='
        op = '+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 112))

    def test_113(self):
        """test SEPERATORS"""
        ip = "[](),"
        op = "[,],(,),,,<EOF>"
        self.assertTrue(TestLexer.test(ip, op, 113))

    def test_114(self):
        """test IDENTIFIER"""
        ip = "A a az AZ aZ a1 A1"
        op = "A,a,az,AZ,aZ,a1,A1,<EOF>"
        self.assertTrue(TestLexer.test(ip, op, 114))

    def test_115(self):
        """test IDENTIFIER """
        ip = "_ _a a_ _1"
        op = "_,_a,a_,_1,<EOF>"
        self.assertTrue(TestLexer.test(ip, op, 115))

    def test_116(self):
        """test NOT 1 IDENTIFIER """
        ip = "1abc"
        op = "1,abc,<EOF>"
        self.assertTrue(TestLexer.test(ip, op, 116))

    def test_117(self):
        """test NOT 1 IDENTIFIER """
        ip = "1abc1"
        op = "1,abc1,<EOF>"
        self.assertTrue(TestLexer.test(ip, op, 117))

    def test_118(self):
        """test NUMBERLIT: int number"""
        ip = '0 199 000001 023'
        op = '0,199,000001,023,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 118))

    def test_119(self):
        """test NUMBERLIT: negative number will give another token"""
        ip = "-0 -199 -0001"
        op = "-,0,-,199,-,0001,<EOF>"
        self.assertTrue(TestLexer.test(ip, op, 119))

    def test_120(self):
        """test NUMBERLIT: int decimal number"""
        ip = '012. 12. 0. 12.3'
        op = '012.,12.,0.,12.3,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 120))

    def test_121(self):
        """test NUMBERLIT: int exponent number"""
        ip = '1e+4 1e-3 012e+3 023e-3'
        op = '1e+4,1e-3,012e+3,023e-3,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 121))

    def test_122(self):
        """test NUMBERLIT: int decimal exponent number"""
        ip = '1.2e3 1.2e-3 1.e2 0.e-199'
        op = '1.2e3,1.2e-3,1.e2,0.e-199,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 122))

    def test_123(self):
        """test NUMBERLIT: error token"""
        ip = ".12e-3"
        op = "Error Token ."
        self.assertTrue(TestLexer.test(ip, op, 123))

    def test_124(self):
        """test NUMBERLIT: error give another token"""
        ip = "12.2h-3"
        op = "12.2,h,-,3,<EOF>"
        self.assertTrue(TestLexer.test(ip, op, 124))

    def test_125(self):
        """test STRINGLIT: normal case"""
        ip = """ "hello world" """
        op = 'hello world,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 125))

    def test_126(self):
        """test STRINGLIT: normal case"""
        ip = """ " He said: '"Hello world!#?~'"  " """
        op = """ He said: '"Hello world!#?~'"  ,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 126))

    def test_127(self):
        """test STRINGLIT: normal case"""
        ip = """ "He said: '"Hello world! \\' \\\\ \\b \\f \\r \\n \\t Yeah!'"" """
        op = """He said: '"Hello world! \\' \\\\ \\b \\f \\r \\n \\t Yeah!'",<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 127))

    def test_128(self):
        """test STRINGLIT: normal case"""
        ip = """ "" """
        op = ",<EOF>"
        self.assertTrue(TestLexer.test(ip, op, 128))

    def test_129(self):
        """test STRINGLIT: unclosed string"""
        ip = """ "abc"""
        op = "Unclosed String: abc"
        self.assertTrue(TestLexer.test(ip, op, 129))

    def test_130(self):
        """test STRINGLIT: unclosed string"""
        ip = """ "abc'" """
        op = """Unclosed String: abc'" """
        self.assertTrue(TestLexer.test(ip, op, 130))

    def test_131(self):
        """test STRINGLIT: unclosed string"""
        ip = """ "abc
"""
        op = """Unclosed String: abc"""
        self.assertTrue(TestLexer.test(ip, op, 131))

    def test_132(self):
        """test STRINGLIT: unclosed string"""
        ip = """ "abc \t abc \n" """
        op = """Unclosed String: abc 	 abc """
        self.assertTrue(TestLexer.test(ip, op, 132))

    def test_133(self):
        """test STRINGLIT: unclosed string"""
        ip = """ "abc \\n \n" """
        op = """Unclosed String: abc \\n """
        self.assertTrue(TestLexer.test(ip, op, 133))

    def test_134(self):
        """test STRINGLIT: unclosed string"""
        ip = """ "abc \\n """
        op = 'Unclosed String: abc \\n '
        self.assertTrue(TestLexer.test(ip, op, 134))

    def test_135(self):
        """test STRINGLIT: unclosed string"""
        ip = """ "abc ##abc """
        op = 'Unclosed String: abc ##abc '
        self.assertTrue(TestLexer.test(ip, op, 135))

    def test_136(self):
        """test STRINGLIT: unclosed string"""
        ip = """ "abc ' " " """
        op = "abc ' ,Unclosed String:  "
        self.assertTrue(TestLexer.test(ip, op, 136))

    def test_137(self):
        """test STRINGLIT: illegal escape"""
        ip = """ "abc \m " """
        op = 'Illegal Escape In String: abc \m'
        self.assertTrue(TestLexer.test(ip, op, 137))

    def test_138(self):
        """test STRINGLIT: illegal escape"""
        ip = """ "abc \\m" """
        op = 'Illegal Escape In String: abc \m'
        self.assertTrue(TestLexer.test(ip, op, 138))

    def test_139(self):
        """test STRINGLIT: illegal escape"""
        ip = """ "abc \\m abc" """
        op = 'Illegal Escape In String: abc \m'
        self.assertTrue(TestLexer.test(ip, op, 139))

    def test_140(self):
        """test STRINGLIT: illegal escape"""
        ip = """ "abc \\"1 " """
        op = "Illegal Escape In String: abc \\\""
        self.assertTrue(TestLexer.test(ip, op, 140))

    def test_141(self):
        """test STRINGLIT: illegal escape"""
        ip = """ "abc \\## abc" """
        op = 'Illegal Escape In String: abc \#'
        self.assertTrue(TestLexer.test(ip, op, 141))

    def test_142(self):
        """test STRINGLIT: illegal escape"""
        ip = """  """
        op = '<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 142))

    def test_143(self):
        """test STRINGLIT: illegal escape and unclose string"""
        ip = """ "abc \\m """
        op = 'Illegal Escape In String: abc \m'
        self.assertTrue(TestLexer.test(ip, op, 143))

    def test_144(self):
        """test STRINGLIT: illegal escape and unclose string"""
        ip = """ "abc \n \\m """
        op = """Unclosed String: abc """
        self.assertTrue(TestLexer.test(ip, op, 144))

    def test_145(self):
        """test STRINGLIT: illegal escape and unclose string"""
        ip = """ "\n """
        op = """Unclosed String: """
        self.assertTrue(TestLexer.test(ip, op, 145))

    def test_146(self):
        """test ERROR TOKEN"""
        ip = '#'
        op = 'Error Token #'
        self.assertTrue(TestLexer.test(ip, op, 146))

    def test_147(self):
        """test ERROR TOKEN"""
        ip = '&'
        op = 'Error Token &'
        self.assertTrue(TestLexer.test(ip, op, 147))

    def test_148(self):
        """test ERROR TOKEN"""
        ip = '|'
        op = 'Error Token |'
        self.assertTrue(TestLexer.test(ip, op, 148))

    def test_149(self):
        """test ERROR TOKEN"""
        ip = '~ |'
        op = 'Error Token ~'
        self.assertTrue(TestLexer.test(ip, op, 149))

    def test_150(self):
        """test normal statement"""
        ip = 'var a <- x+y*z - (1+2)'
        op = 'var,a,<-,x,+,y,*,z,-,(,1,+,2,),<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 150))

    def test_151(self):
        """test normal statement"""
        ip = 'if (i + 1 = 10) return true'
        op = 'if,(,i,+,1,=,10,),return,true,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 151))

    def test_152(self):
        """test normal statement"""
        ip = 'func isEven(number x) return x % 2 = 0'
        op = 'func,isEven,(,number,x,),return,x,%,2,=,0,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 152))

    def test_153(self):
        """test normal statement"""
        ip = """number x <- 2
bool a <- true
print(x)
"""
        op = """number,x,<-,2,
,bool,a,<-,true,
,print,(,x,),
,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 153))

    def test_154(self):
        """test normal statement"""
        ip = 'a[3 + foo(2)] <- a[b[2, 3]] + 4'
        op = 'a,[,3,+,foo,(,2,),],<-,a,[,b,[,2,,,3,],],+,4,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 154))

    def test_155(self):
        """test normal statement"""
        ip = 'print("abc")'
        op = 'print,(,abc,),<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 155))

    def test_156(self):
        """test normal statement"""
        ip = """func main()
begin
number x <- readNumber()
if (isPrime(x)) writeString("Yes")
else writeString("No")
end
"""
        op = """func,main,(,),
,begin,
,number,x,<-,readNumber,(,),
,if,(,isPrime,(,x,),),writeString,(,Yes,),
,else,writeString,(,No,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 156))

    def test_157(self):
        """test normal statement"""
        ip = 'var a <- [1,2,3][1]'
        op = 'var,a,<-,[,1,,,2,,,3,],[,1,],<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 157))

    def test_158(self):
        """test normal statement"""
        ip = 'var a <- a[1][1]'
        op = 'var,a,<-,a,[,1,],[,1,],<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 158))

    def test_159(self):
        """test normal statement"""
        ip = """
        func a()
            return if (x <= 1) return false"""
        op = """
,func,a,(,),
,return,if,(,x,<=,1,),return,false,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 159))

    def test_160(self):
        """test normal statement"""
        ip = """
        func a()
            if (x <= 1) return false
"""
        op = """
,func,a,(,),
,if,(,x,<=,1,),return,false,
,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 160))

    def test_161(self):
        """test normal statement"""
        ip = """func main(number x, number y)
        func f(bool x, bool y)
"""
        op = """func,main,(,number,x,,,number,y,),
,func,f,(,bool,x,,,bool,y,),
,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 161))

    def test_162(self):
        """test normal statement"""
        ip = 'var a[3] <- <- <- [1,2,3]'
        op = 'var,a,[,3,],<-,<-,<-,[,1,,,2,,,3,],<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 162))

    def test_163(self):
        """test normal statement"""
        ip = 'func func func main()'
        op = 'func,func,func,main,(,),<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 163))

    def test_164(self):
        """test normal statement"""
        ip = """## ./././,.||||"::":"
abc ##
123.33333 ##abc
fff ##
"""
        op = """
,abc,
,123.33333,
,fff,
,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 164))

    def test_165(self):
        """test random lexer"""
        ip = '[a+b)'
        op = '[,a,+,b,),<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 165))

    def test_166(self):
        """test random lexer"""
        ip = '*****'
        op = '*,*,*,*,*,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 166))

    def test_167(self):
        """test random lexer"""
        ip = 'abc[]]... ...'
        op = 'abc,[,],],...,...,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 167))

    def test_168(self):
        """test random lexer"""
        ip = '[(_+.'
        op = '[,(,_,+,Error Token .'
        self.assertTrue(TestLexer.test(ip, op, 168))

    def test_169(self):
        """test random lexer"""
        ip = '___12.3'
        op = '___12,Error Token .'
        self.assertTrue(TestLexer.test(ip, op, 169))

    def test_170(self):
        """test random lexer"""
        ip = '_++_+__+_+_+_'
        op = '_,+,+,_,+,__,+,_,+,_,+,_,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 170))

    def test_171(self):
        """test some expression"""
        ip = '12.e-30-30.e-10'
        op = '12.e-30,-,30.e-10,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 171))

    def test_172(self):
        """test some expression"""
        ip = '12.e-30 ^ 10'
        op = '12.e-30,Error Token ^'
        self.assertTrue(TestLexer.test(ip, op, 172))

    def test_173(self):
        """test some expression"""
        ip = 'a() + (12.e+30+30)[1]'
        op = 'a,(,),+,(,12.e+30,+,30,),[,1,],<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 173))

    def test_174(self):
        """test some expression"""
        ip = '1>2+3**3'
        op = '1,>,2,+,3,*,*,3,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 174))

    def test_175(self):
        """test some expression"""
        ip = 'true + false = false'
        op = 'true,+,false,=,false,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 175))

    def test_176(self):
        """test some expression"""
        ip = 'abc + abc()'
        op = 'abc,+,abc,(,),<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 176))

    def test_177(self):
        """test some expression"""
        ip = '"abc"..."def"'
        op = 'abc,...,def,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 177))

    def test_178(self):
        """test some expression"""
        ip = '"abc"..."def"..."def"'
        op = 'abc,...,def,...,def,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 178))

    def test_179(self):
        """test some expression"""
        ip = '|1| + |-2|'
        op = 'Error Token |'
        self.assertTrue(TestLexer.test(ip, op, 179))

    def test_180(self):
        """test some expression"""
        ip = 'abc ^ 78'
        op = 'abc,Error Token ^'
        self.assertTrue(TestLexer.test(ip, op, 180))

    def test_181(self):
        """test random"""
        ip = """
string a <- "abc \\n \t" \n string a <- "abc\t"
"""
        op = """
,string,a,<-,abc \\n 	,
,string,a,<-,abc	,
,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 181))

    def test_182(self):
        """test random"""
        ip = 'var a[3] <- ["abc", abc, "123", 123]'
        op = 'var,a,[,3,],<-,[,abc,,,abc,,,123,,,123,],<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 182))

    def test_183(self):
        """test random"""
        ip = 'var a <- "abc'
        op = 'var,a,<-,Unclosed String: abc'
        self.assertTrue(TestLexer.test(ip, op, 183))

    def test_184(self):
        """test random"""
        ip = 'var a <- "\m"'
        op = 'var,a,<-,Illegal Escape In String: \m'
        self.assertTrue(TestLexer.test(ip, op, 184))

    def test_185(self):
        """test random"""
        ip = 'func "main"()'
        op = 'func,main,(,),<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 185))

    def test_186(self):
        """test random"""
        ip = """ "abc,.,.,.,.,." funcmain() """
        op = 'abc,.,.,.,.,.,funcmain,(,),<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 186))

    def test_187(self):
        """test random"""
        ip = """1 + 1 = 2 is true
1 + 1 = 3 is false"""
        op = """1,+,1,=,2,is,true,
,1,+,1,=,3,is,false,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 187))

    def test_188(self):
        """test random"""
        ip = """#######
        ##
        ## abc
        begin end"""
        op = """
,
,
,begin,end,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 188))

    def test_189(self):
        """test random"""
        ip = 'my_name_is_abc abcd abcde'
        op = 'my_name_is_abc,abcd,abcde,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 189))

    def test_190(self):
        """test random"""
        ip = '__________123.'
        op = '__________123,Error Token .'
        self.assertTrue(TestLexer.test(ip, op, 190))

    def test_191(self):
        """test random"""
        ip = """a\n\n\n#"""
        op = """a,
,
,
,Error Token #"""
        self.assertTrue(TestLexer.test(ip, op, 191))

    def test_192(self):
        """test random"""
        ip = """a\\n\\n\\n"""
        op = """a,Error Token \\"""
        self.assertTrue(TestLexer.test(ip, op, 192))

    def test_193(self):
        """test random"""
        ip = """ "a\\n\\n\\n" """
        op = 'a\\n\\n\\n,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 193))

    def test_194(self):
        """test random"""
        ip = '__ .012e-20.e-20.e-20'
        op = '__,Error Token .'
        self.assertTrue(TestLexer.test(ip, op, 194))

    def test_195(self):
        """test random"""
        ip = '__ .012e-2 0.e-2 0.e-20'
        op = '__,Error Token .'
        self.assertTrue(TestLexer.test(ip, op, 195))

    def test_196(self):
        """test random"""
        ip = '__ 1.012e-2 0.e-2 0.e-20'
        op = '__,1.012e-2,0.e-2,0.e-20,<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 196))

    def test_197(self):
        """test random"""
        ip = 'a[12,12.0e-10]'
        op = 'a,[,12,,,12.0e-10,],<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 197))

    def test_198(self):
        """test random"""
        ip = 'dynamic dyna c [(123.e)]'
        op = 'dynamic,dyna,c,[,(,123.,e,),],<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 198))

    def test_199(self):
        """test random"""
        ip = 'a\n##1\nb'
        op = """a,
,
,b,<EOF>"""
        self.assertTrue(TestLexer.test(ip, op, 199))

    def test_200(self):
        """test random"""
        ip = 'a <- var dynamic c()[a12]'
        op = 'a,<-,var,dynamic,c,(,),[,a12,],<EOF>'
        self.assertTrue(TestLexer.test(ip, op, 200))


