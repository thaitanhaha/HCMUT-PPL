import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_301(self):
        ### Test BKEL
        input = """number a
"""
        expect = """Program([VarDecl(Id(a), NumberType, None, None)])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        ### Test BKEL
        input = """var str <- "Hello world!"
"""
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_303(self):
        ### Test BKEL
        input = """func main() return 1
"""
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        ### Test 2 decls
        input = """number a
number b
"""
        expect = """Program([VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        ### Test BKEL
        input = """func inc(number a) return a + 1
func main() begin
var a <- 1
inc(a)
writeNumber(a)
end
"""
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        ###
        input = """func areDivisors(number num1, number num2)
return ((num1 % num2 = 0) or (num2 % num1 = 0))
"""
        expect = """Program([FuncDecl(Id(areDivisors), [VarDecl(Id(num1), NumberType, None, None), VarDecl(Id(num2), NumberType, None, None)], Return(BinaryOp(or, BinaryOp(=, BinaryOp(%, Id(num1), Id(num2)), NumLit(0.0)), BinaryOp(=, BinaryOp(%, Id(num2), Id(num1)), NumLit(0.0)))))])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        ###
        input = """func main()
begin
var num1 <- readNumber()
var num2 <- readNumber(a,b,1,2,3)
write("YES")
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(num1), None, var, CallExpr(Id(readNumber), [])), VarDecl(Id(num2), None, var, CallExpr(Id(readNumber), [Id(a), Id(b), NumLit(1.0), NumLit(2.0), NumLit(3.0)])), CallStmt(Id(write), [StringLit(YES)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        ###
        input = """func main()
begin
if (1) writeString("Yes")
elif (2) writeString("YES")
else writeString("No")
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(Yes)])), [(NumLit(2.0), CallStmt(Id(writeString), [StringLit(YES)]))], CallStmt(Id(writeString), [StringLit(No)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        ###
        input = """func main()
begin
if (areDivisors(num1, num2)) writeString("Yes")
else writeString("No")
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([If((CallExpr(Id(areDivisors), [Id(num1), Id(num2)]), CallStmt(Id(writeString), [StringLit(Yes)])), [], CallStmt(Id(writeString), [StringLit(No)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        ###
        input = """func isPrime(number x)
begin
if (x <= 1) return false
var i <- 2
for i until i > x / 2 by 1
begin
if (x % i = 0) return false
end
return true
end
"""
        expect = """Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], \
Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), \
VarDecl(Id(i), None, var, NumLit(2.0)), \
For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), \
Block([If((BinaryOp(=, BinaryOp(%, Id(x), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None)])), \
Return(BooleanLit(True))]))])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_311(self):
        ### test assign stmt
        input = """
func main()
begin
    number a
    number b <- 1
    a <- 1 + 1e-30 + b
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), \
VarDecl(Id(b), NumberType, None, NumLit(1.0)), \
AssignStmt(Id(a), BinaryOp(+, BinaryOp(+, NumLit(1.0), NumLit(1e-30)), Id(b)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        ### test array decl
        input = """
number a[5] <- [1, 2, 3, 4, 5]
number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
"""
        expect = """Program([VarDecl(Id(a), ArrayType([5.0], NumberType), None, \
ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0))), \
VarDecl(Id(b), ArrayType([2.0, 3.0], NumberType), None, \
ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), \
ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0))))])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        ### test assign with lhs is a[]
        input = """
func main()
begin
a[1] <- 1
end
"""
        expect = """Program([FuncDecl(Id(main), [], \
Block([AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        ### test
        input = """
func main(number a[100])
"""
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None)], None)])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        ### test vardecl with array cell
        input = """
func main(number a[100])
begin
    var abc <- a[0]
end
"""
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(a), ArrayType([100.0], NumberType), None, None)], Block([VarDecl(Id(abc), None, var, ArrayCell(Id(a), [NumLit(0.0)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        ### test declaration
        input = """
            string abc
            bool abc
            string abc <- 1
            bool abc <- 1
        """
        expect = str(Program([
                VarDecl(Id("abc"), StringType()),
                VarDecl(Id("abc"), BoolType()),
                VarDecl(Id("abc"), StringType(), None, NumberLiteral(1.0)),
                VarDecl(Id("abc"), BoolType(), None, NumberLiteral(1.0))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        ### test declaration
        input = """
            number abc[100] <- 1
            string abc[100]
        """
        expect = str(Program([
                VarDecl(Id("abc"), ArrayType([100.0], NumberType()), None, NumberLiteral(1.0)),
                VarDecl(Id("abc"), ArrayType([100.0], StringType()))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        ### test declaration
        input = """
            dynamic abc
            dynamic abc <- 1
        """
        expect = str(Program([
                    VarDecl(Id("abc"), None, "dynamic"),
                    VarDecl(Id("abc"), None, "dynamic", NumberLiteral(1.0))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        ### test declaration
        input = """
            func main()
                begin
                    break
                    continue
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Break(), Continue()]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        ### test declaration
        input = """
            func foo(number a)
            func foo(number a, string a, bool a[100])
            func foo(number abc[1,2])
                return
        """
        expect = str(Program([
                    FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([100.0], BoolType()))], None),
                    FuncDecl(Id("foo"), [VarDecl(Id("abc"), ArrayType([1.0, 2.0], NumberType()))], Return(None))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 320))
        
    def test_321(self):
        ### test expression
        input = """
            var a <- 1
            var a <- "123"
            var a <- true
            var a <- false
        """
        expect = str(Program([
                    VarDecl(Id("a"), None, "var",  NumberLiteral(1.0)),
                    VarDecl(Id("a"), None, "var",  StringLiteral("123")),
                    VarDecl(Id("a"), None, "var",  BooleanLiteral(True)),
                    VarDecl(Id("a"), None, "var",  BooleanLiteral(False))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 321))
        
    def test_322(self):
        ### test expression
        input = """
            var a <- [1, "a", false]
        """
        expect = str(Program([
                    VarDecl(Id("a"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(False)]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 322))   
        
    def test_323(self):
        input = """
            var a <- [[1], [1]]
            var a <- [[1]]
        """
        expect = str(Program([
                    VarDecl(Id("a"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)]), ArrayLiteral([NumberLiteral(1.0)])])),
                    VarDecl(Id("a"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 323))  
        
    def test_324(self):
        input = """
            var a <- 1 ... "2"
            var a <- 1 <= "2"
            var a <- 1 and 2 or 3
            var a <- 1 + 2 - 3
            var a <- 1 * 2 / 3 % 4
            var a <- ---1
            var a <- not not 1
            var a <- a 
            var a <- a[1,2,3]
        """
        expect = str(Program([
                    VarDecl(Id("a"), None, "var",  BinaryOp("...", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("a"), None, "var",  BinaryOp("<=", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("a"), None, "var",  BinaryOp("or", BinaryOp("and", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("a"), None, "var",  BinaryOp("-", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("a"), None, "var",  BinaryOp("%", BinaryOp("/", BinaryOp("*", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0))),
                    VarDecl(Id("a"), None, "var",  UnaryOp("-", UnaryOp("-", UnaryOp("-", NumberLiteral(1.0))))),
                    VarDecl(Id("a"), None, "var",  UnaryOp("not", UnaryOp("not", NumberLiteral(1.0)))),
                    VarDecl(Id("a"), None, "var",  Id("a")),
                    VarDecl(Id("a"), None, "var",  ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 324))  
        
    def test_325(self):
        input = """
            dynamic a <- 1 or 2 and 3 <= 4 ... 5 <= 6 + abc * 7 + def - -8 + not - 9
        """
        expect = str(Program([
                VarDecl(Id("a"), None, "dynamic",  
                        BinaryOp("...", 
                                BinaryOp("<=", BinaryOp("and", BinaryOp("or", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0)), 
                                BinaryOp("<=", NumberLiteral(5.0), BinaryOp("+", BinaryOp("-", BinaryOp("+", BinaryOp("+", NumberLiteral(6.0), BinaryOp("*", Id("abc"), NumberLiteral(7.0))), Id("def")), UnaryOp("-", NumberLiteral(8.0))), UnaryOp("not", UnaryOp("-", NumberLiteral(9.0)))))
                            ))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 325))  

    def test_326(self):
        input = """
            number a <- -abc[1+2] ... 2
        """
        expect = str(Program([
                    VarDecl(Id("a"), NumberType(), None,  
                            BinaryOp("...", UnaryOp("-", ArrayCell(Id("abc"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0))])), NumberLiteral(2.0)))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 326))  
        
    def test_327(self):
        input = """
            dynamic abc <- foo()
        """
        expect = str(Program([
                    VarDecl(Id("abc"), None, "dynamic",  CallExpr(Id("foo"), []))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 327)) 
        
    def test_328(self):
        input = """
            var abc <- foo(1+1, "a")
        """
        expect = str(Program([
                    VarDecl(Id("abc"), None, "var",  CallExpr(Id("foo"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), StringLiteral("a")]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 328)) 
        
    def test_329(self):
        input = """
            string a <- foo(foo(foo(1)))
        """
        expect = str(Program([
            VarDecl(Id("a"), StringType(), None, CallExpr(Id("foo"), [CallExpr(Id("foo"), [CallExpr(Id("foo"), [NumberLiteral(1.0)])])]))])
        )
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 329)) 
        
    def test_330(self):
        input = """
            var abc <- (1 ... 2) ... 0
        """
        expect = str(Program([
                    VarDecl(Id("abc"), None, "var",  BinaryOp("...", BinaryOp("...", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(0.0)))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 330)) 

    def test_331(self):
        # Test statements BKEL
        input = """
number a <- 100

func sum(number n)
begin
    if (n = 0) return 0
    return n + sum(n - 1)
end

func main()
begin
    writeNumber(sum(a))
end
        """
        expect = "Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 331)) 

    def test_332(self):
        # Test statements
        input = """
func main()
    begin
        continue
        continue
        break
        begin
            continue
            continue
            break                    
        end
    end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue(), Continue(), Break(),
                        Block([Continue(), Continue(), Break()])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
        # Test statements
        input = """
func main()
    begin
        return n + 1
    end
func main()
    return 1
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Return(BinaryOp("+", Id("n"), NumberLiteral(1.0)))])),
                    FuncDecl(Id("main"), [], Return(NumberLiteral(1.0)))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        # Test statements
        input = """
func main()
    begin
        foo(a)
        foo(a,1)
    end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], 
                    Block([
                        CallStmt(Id("foo"), [Id("a")]),
                        CallStmt(Id("foo"), [Id("a"), NumberLiteral(1.0)])
                    ]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_335(self):
        # Test statements
        input = """
func foo1()
    begin
        a <- 1
        a[1] <- 1
        a[1,1] <- 2+3
    end
func foo2()
    begin
        a[1+1, 2] <- 1
    end
        """
        expect = str(Program([
                    FuncDecl(Id("foo1"), [], Block([
                    Assign(Id("a"), NumberLiteral(1.0)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(1.0)]), NumberLiteral(1.0)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(1.0)]), BinaryOp("+", NumberLiteral(2.0), NumberLiteral(3.0)))])),
                    FuncDecl(Id("foo2"), [], Block([
                    Assign(ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), NumberLiteral(2.0)]), NumberLiteral(1.0))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_336(self):
        # Test statements
        input = """
            var a <- abc[1,2]
            var a <- foo()[1,2]
            dynamic a <- foo(1,2)[1,3]
        """
        expect = str(Program([
            VarDecl(Id("a"), None, "var", ArrayCell(Id("abc"), [NumberLiteral(1.0), NumberLiteral(2.0)])),
            VarDecl(Id("a"), None, "var", ArrayCell(CallExpr(Id("foo"), []), [NumberLiteral(1.0), NumberLiteral(2.0)])),
            VarDecl(Id("a"), None, "dynamic", ArrayCell(CallExpr(Id("foo"), [NumberLiteral(1.0), NumberLiteral(2.0)]), [NumberLiteral(1.0), NumberLiteral(3.0)]))
        ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
        # Test statements
        input = """
func main()
begin
    var a <- 1e2
    dynamic b <- 3.14
    bool c
    number d[1e1, 2] <- 3.14
    string e[3.14] <- "Hello"
end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block(
                [VarDecl(Id("a"), None, "var", NumberLiteral(100.0)), 
                 VarDecl(Id("b"), None, "dynamic", NumberLiteral(3.14)), 
                 VarDecl(Id("c"), BoolType(), None, None),
                 VarDecl(Id("d"), ArrayType([10.0, 2.0], NumberType()), None, NumberLiteral(3.14)),
                 VarDecl(Id("e"), ArrayType([3.14], StringType()), None, StringLiteral("Hello"))
            ]))]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 337))    

    def test_338(self):
        # Test statements
        input = """
func foo1()
    begin
        for i until i < 10 by 1 + 1
            print(i)
    end
func foo2()
    begin
        for i until i != 10 by a[1]
        begin
            print(i+1)
        end
    end
        """
        expect = str(Program([
                    FuncDecl(Id("foo1"), [], Block([
                    For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), CallStmt(Id("print"), [Id("i")]))])),
                    FuncDecl(Id("foo2"), [], Block([
                    For(Id("i"), BinaryOp("!=", Id("i"), NumberLiteral(10.0)), ArrayCell(Id("a"), [NumberLiteral(1.0)]), Block([
                    CallStmt(Id("print"), [BinaryOp("+", Id("i"), NumberLiteral(1.0))])]))]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_339(self):
        # Test statements
        input = """
func foo1()
    begin
        if (true) return true
    end
func foo2()
    begin
        if (true) return true
        else return false
    end
        """
        expect = str(Program([
                    FuncDecl(Id("foo1"), [], Block([
                    If(BooleanLiteral(True), Return(BooleanLiteral(True)), [], None)])),
                    FuncDecl(Id("foo2"), [], Block([
                    If(BooleanLiteral(True), Return(BooleanLiteral(True)), [], Return(BooleanLiteral(False)))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
        # Test statements
        input = """
            func main()
                begin
                    if (true) return 1
                    elif (true) return 1
                    elif (true) return 1
                    else return 1
                end

        """
        expect =str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(1.0)), 
                       [(BooleanLiteral(True), Return(NumberLiteral(1.0))),
                        (BooleanLiteral(True), Return(NumberLiteral(1.0)))], 
                        Return(NumberLiteral(1.0)))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
        # Test statements
        input = """
func main()
    begin
        if (true)
            if(true) return 1
            else return 1
    end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(1.0))), [], None)
            ]))]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 341))     

    def test_342(self):
        # Test statements
        input = """
func main()
    begin
        if (true)
            if(true) return 1
            else return 1
        else return 1
    end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(1.0))), 
               [], Return(NumberLiteral(1.0)))
            ]))]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 342))   

    def test_343(self):
        # Test statements
        input = """
func main()
    begin
        if (true)
            if (true) return 1
            elif (true) return 1
            else return 1
    end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0))), 
               [], None)
            ]))]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 343))   

    def test_344(self):
        # Test statements
        input = """
func main()
    begin
        if (true)
            if (true) return 1
            elif (true) return 1
            elif (true) return 1
    end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))]), [], None)
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_345(self):
        # Test statements
        input = """
func main()
    begin
        if (true)
            if(true) return 1
            elif (true) return 1
            elif (true) return 1
            else return 1
        elif (true) return 1
        elif (true) return 1                        
        else return 1
    end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0)))
            , [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0)))
            ]))]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 345))   
        
    def test_346(self):
        # Test some complex expression
        input = """
var a <- b...c==d or e + f / g + not - arr[4]
        """
        expect = str(Program([
            VarDecl(Id("a"), None, "var", 
                BinaryOp("...", Id("b"), 
                    BinaryOp("==", Id("c"), 
                        BinaryOp("or", Id("d"), 
                            BinaryOp("+", 
                                BinaryOp("+", Id("e"), BinaryOp("/", Id("f"), Id("g"))), 
                                UnaryOp("not", UnaryOp("-", ArrayCell(Id("arr"), [NumberLiteral(4.0)])))
                            )
                        )
                    )
                ))
        ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
        # Test some complex expression
        input = """
number a[2,3] <- [a,b+1,"abc",foo(4),true,-----1]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([2.0, 3.0], NumberType()), None, 
            ArrayLiteral([
                Id("a"), 
                BinaryOp("+", Id("b"), NumberLiteral(1.0)), 
                StringLiteral("abc"), 
                CallExpr(Id("foo"), [NumberLiteral(4.0)]), 
                BooleanLiteral(True), 
                UnaryOp("-", UnaryOp("-", UnaryOp("-", UnaryOp("-", UnaryOp("-", NumberLiteral(1.0))))))]
            ))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_348(self):
        # Test some complex expression
        input = """
bool a <- (((foo1((n1*-2))))) > foo2(a(n+1, n+2))
        """
        expect = str(Program([VarDecl(Id("a"), BoolType(), None, 
            BinaryOp(">", 
                CallExpr(Id("foo1"), [BinaryOp("*", Id("n1"), UnaryOp("-", NumberLiteral(2.0)))]), 
                CallExpr(Id("foo2"), [CallExpr(Id("a"), [BinaryOp("+", Id("n"), NumberLiteral(1.0)), BinaryOp("+", Id("n"), NumberLiteral(2.0))])])
            ))
        ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
        # Test some complex expression
        input = """
dynamic a <- int("..." ... "...") + foo(a + b * not c - d % e)
        """
        expect = str(Program([VarDecl(Id("a"), None, "dynamic", 
                    BinaryOp("+", 
                        CallExpr(Id("int"), [BinaryOp("...", StringLiteral("..."), StringLiteral("..."))]), 
                        CallExpr(Id("foo"), [BinaryOp("-", BinaryOp("+", Id("a"), BinaryOp("*", Id("b"), UnaryOp("not", Id("c")))), BinaryOp("%", Id("d"), Id("e")))])
                    ))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_350(self):
        # Test some complex expression
        input = """
string a <- (abc[(1)] * (not-1)) % "abc"
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, 
                    BinaryOp("%", 
                        BinaryOp("*", ArrayCell(Id("abc"), [NumberLiteral(1.0)]), UnaryOp("not", UnaryOp("-", NumberLiteral(1.0)))), 
                        StringLiteral("abc"))
                    )]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_351(self):
        input = """
func isPrime(number x)
begin
    if (x <= 1) return false
    var i <- 2
    for i until i > x / 2 by 1
        begin
            if (x % i = 0) return false
        end
    return true
end
        """
        expect = str(Program([FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType(), None, None)], 
            Block([
                If(BinaryOp("<=", Id("x"), NumberLiteral(1.0)), Return(BooleanLiteral(False)), [], None), 
                VarDecl(Id("i"), None, "var", NumberLiteral(2.0)),
                For(Id("i"), BinaryOp(">", Id("i"), BinaryOp("/", Id("x"), NumberLiteral(2.0))), NumberLiteral(1.0), 
                    Block([If(BinaryOp("=", BinaryOp("%", Id("x"), Id("i")), NumberLiteral(0.0)), Return(BooleanLiteral(False)), [], None)])), 
                Return(BooleanLiteral(True))
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_352(self):
        input = """
func main()
    begin
        number a <- a[1,2,3] * (1 > 2)
        for a until a > "YES" by 1
            begin
                if (x == "YES") continue
                elif (x == "NO") return
            end
    end
"""
        expect = str(Program([FuncDecl(Id("main"), [], 
                Block([VarDecl(Id("a"), NumberType(), None, BinaryOp("*", ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), BinaryOp(">", NumberLiteral(1.0), NumberLiteral(2.0)))), 
                For(Id("a"), BinaryOp(">", Id("a"), StringLiteral("YES")), NumberLiteral(1.0), 
                    Block([If(BinaryOp("==", Id("x"), StringLiteral("YES")), Continue(), 
                            [(BinaryOp("==", Id("x"), StringLiteral("NO")), Return())], None)]))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_353(self):
        input = """
func main()
    begin
        return c() ... "YES" == "YESS"
        return c() ... "YES" == "YESS"
        return c() ... "YES" == "YESS"
    end
"""
        expect = str(Program([FuncDecl(Id("main"), [], 
                Block([
                    Return(BinaryOp("...", CallExpr(Id("c"), []), BinaryOp("==", StringLiteral("YES"), StringLiteral("YESS")))), 
                    Return(BinaryOp("...", CallExpr(Id("c"), []), BinaryOp("==", StringLiteral("YES"), StringLiteral("YESS")))), 
                    Return(BinaryOp("...", CallExpr(Id("c"), []), BinaryOp("==", StringLiteral("YES"), StringLiteral("YESS"))))]
                ))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_354(self):
        input = """
func main()
    begin
        a[1] <- f()[1]
    end
"""
        expect = str(Program([FuncDecl(Id("main"), [], 
                Block([Assign(ArrayCell(Id("a"), [NumberLiteral(1.0)]), ArrayCell(CallExpr(Id("f"), []), [NumberLiteral(1.0)]))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 354))


    def test_355(self):
        input = """
var a <- -[a,b,c]
"""
        expect = str(Program([VarDecl(Id("a"), None, "var", UnaryOp("-", ArrayLiteral([Id("a"), Id("b"), Id("c")])))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 355))


    def test_356(self):
        input = """
func main() 
begin 
    if (1) ####
        number a[01.9] <- [0,0,0]
end
"""
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            If(NumberLiteral(1.0), 
               VarDecl(Id("a"), ArrayType([1.9], NumberType()), None, ArrayLiteral([NumberLiteral(0.0), NumberLiteral(0.0), NumberLiteral(0.0)])), 
                [], None)]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 356))


    def test_357(self):
        input = """
func main() 
begin 
    for i until i != 10 by b ##dynamic i
        var a <- 10
end
"""
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            For(Id("i"), BinaryOp("!=", Id("i"), NumberLiteral(10.0)), Id("b"), 
                VarDecl(Id("a"), None, "var", NumberLiteral(10.0)))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 357))


    def test_358(self):
        input = """
func main()
begin 
if (1) return 
elif (2) 
    if (3) return 
    elif (4) return 
    elif (5) return 
    else return
end
"""
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            If(NumberLiteral(1.0), Return(), 
               [(NumberLiteral(2.0), 
                 If(NumberLiteral(3.0), Return(), 
                    [(NumberLiteral(4.0), Return()), (NumberLiteral(5.0), Return())], Return())), ], 
                    None
                )]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 358))


    def test_359(self):
        # test in BKEL forum
        input = """
func main() begin
if (1)
	if (2)
		b()
	elif (3)
		if (4)
			c()
		elif (5)
			d()
		else e()
	elif (6)
		f()
	else g()
elif (7) 
    h()
end
"""
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            If(NumberLiteral(1.0), 
                If(NumberLiteral(2.0), CallStmt(Id("b"), []), 
                [(NumberLiteral(3.0), If(NumberLiteral(4.0), CallStmt(Id("c"), []), [(NumberLiteral(5.0), CallStmt(Id("d"), []))], CallStmt(Id("e"), []))), 
                (NumberLiteral(6.0), CallStmt(Id("f"), []))], CallStmt(Id("g"), [])), 
            [(NumberLiteral(7.0), CallStmt(Id("h"), []))], None)]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 359))


    def test_360(self):
        input = """
var a <- [a()[1,2] + [1,2]]
"""
        expect = str(Program([VarDecl(Id("a"), None, "var", 
            ArrayLiteral([BinaryOp("+", 
                    ArrayCell(CallExpr(Id("a"), []), [NumberLiteral(1.0), NumberLiteral(2.0)]), 
                    ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 360))


    def test_361(self):
        input = """
var a <- foo()[a()[1,2] + [1,2]]
"""
        expect = str(Program([VarDecl(Id("a"), None, "var", 
                ArrayCell(
                    CallExpr(Id("foo"), []), 
                    [BinaryOp("+", 
                        ArrayCell(CallExpr(Id("a"), []), [NumberLiteral(1.0), NumberLiteral(2.0)]), 
                        ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]))])
                )]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 361))


    def test_362(self):
        ## testcase in specification file
        input = """
func main() begin
number r
number s
r <- 2.0
number a[5]
number b[5]
s <- r * r * 3.14
a[0] <- s
end
"""
        expect = str(Program([FuncDecl(Id("main"), [], Block([
                    VarDecl(Id("r"), NumberType(), None, None), 
                    VarDecl(Id("s"), NumberType(), None, None), 
                    Assign(Id("r"), NumberLiteral(2.0)), 
                    VarDecl(Id("a"), ArrayType([5.0], NumberType()), None, None), 
                    VarDecl(Id("b"), ArrayType([5.0], NumberType()), None, None), 
                    Assign(Id("s"), BinaryOp("*", BinaryOp("*", Id("r"), Id("r")), NumberLiteral(3.14))), 
                    Assign(ArrayCell(Id("a"), [NumberLiteral(0.0)]), Id("s"))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 362))


    def test_363(self):
        input = """
func foo()
begin
    for i until i < 100 by 1
        for j until j < i by 1
            if (a > b) write("YES")
            else write("NO")
end
"""
        expect = str(Program([FuncDecl(Id("foo"), [], Block([
            For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(100.0)), NumberLiteral(1.0), 
                For(Id("j"), BinaryOp("<", Id("j"), Id("i")), NumberLiteral(1.0), 
                    If(BinaryOp(">", Id("a"), Id("b")), CallStmt(Id("write"), [StringLiteral("YES")]), [], 
                       CallStmt(Id("write"), [StringLiteral("NO")]))))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 363))


    def test_364(self):
        input = """number a <- arr[foo(1), foo(1)%1]
"""
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, 
                    ArrayCell(Id("arr"), [CallExpr(Id("foo"), [NumberLiteral(1.0)]), BinaryOp("%", CallExpr(Id("foo"), [NumberLiteral(1.0)]), NumberLiteral(1.0))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 364))


    def test_365(self):
        input = """number a <- (not [1,2,3] - [1,2,3]) * -(-b * [1,2])
"""
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, 
                    BinaryOp("*", 
                        BinaryOp("-", UnaryOp("not", ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])), ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)])), 
                        UnaryOp("-", BinaryOp("*", UnaryOp("-", Id("b")), ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)])))))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 365))


    def test_366(self):
        input = """
func foo()
begin
    begin
        begin
            begin
            end
        end
    end
end
"""
        expect = str(Program([FuncDecl(Id("foo"), [], Block([Block([Block([Block([])])])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 366))


    def test_367(self):
        input = """
func foo()
begin 
    return continue_ + 1
end
"""
        expect = str(Program([FuncDecl(Id("foo"), [], Block([Return(BinaryOp("+", Id("continue_"), NumberLiteral(1.0)))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 367))


    def test_368(self):
        input = """
func foo(number n)
begin
    if (n = 0) return
    write(n)
    foo(n-1)
end
"""
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("n"), NumberType(), None, None)], Block([
            If(BinaryOp("=", Id("n"), NumberLiteral(0.0)), Return(), [], None), 
            CallStmt(Id("write"), [Id("n")]), 
            CallStmt(Id("foo"), [BinaryOp("-", Id("n"), NumberLiteral(1.0))])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 368))


    def test_369(self):
        input = """
func foo(number n)
begin
    if (n = 0) return
    begin
        continue
    end
end
"""
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("n"), NumberType(), None, None)], Block([
            If(BinaryOp("=", Id("n"), NumberLiteral(0.0)), Return(), [], None), 
            Block([Continue()])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 369))


    def test_370(self):
        input = """
func sum(number a[100], number n)
begin
    number i <- 0
    number sum <- 0
    for i until i > n by 1
        sum <- sum + a[i]
    return sum
end
"""
        expect = str(Program([FuncDecl(Id("sum"), [VarDecl(Id("a"), ArrayType([100.0], NumberType()), None, None), VarDecl(Id("n"), NumberType(), None, None)], 
                Block([VarDecl(Id("i"), NumberType(), None, NumberLiteral(0.0)), 
                       VarDecl(Id("sum"), NumberType(), None, NumberLiteral(0.0)), 
                       For(Id("i"), BinaryOp(">", Id("i"), Id("n")), NumberLiteral(1.0), Assign(Id("sum"), BinaryOp("+", Id("sum"), ArrayCell(Id("a"), [Id("i")])))), Return(Id("sum"))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 370))


    def test_371(self):
        input = """
func foo() return true
func main()
begin
    return foo()
end
"""
        expect = str(Program([FuncDecl(Id("foo"), [], Return(BooleanLiteral(True))), 
                              FuncDecl(Id("main"), [], Block([Return(CallExpr(Id("foo"), []))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 371))


    def test_372(self):
        input = """
func isEven(number x)
begin ## abc
    return x % 2 = 0 ## abc
end
##


func main()


begin
    a <- 10
    if (isEven(a)) print(a)
    ## a
end
"""
        expect = str(Program([FuncDecl(Id("isEven"), [VarDecl(Id("x"), NumberType(), None, None)], 
                Block([Return(BinaryOp("=", BinaryOp("%", Id("x"), NumberLiteral(2.0)), NumberLiteral(0.0)))])), 
                FuncDecl(Id("main"), [], Block([
                    Assign(Id("a"), NumberLiteral(10.0)), 
                    If(CallExpr(Id("isEven"), [Id("a")]), CallStmt(Id("print"), [Id("a")]), [], None)]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 372))


    def test_373(self):
        input = """
var a <- []
"""
        expect = str(Program([VarDecl(Id("a"), None, "var", ArrayLiteral([]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 373))


    def test_374(self):
        input = """
dynamic a <- [[[[]]]]
"""
        expect = str(Program([VarDecl(Id("a"), None, "dynamic", ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([])])])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 374))


    def test_375(self):
        input = """
var a <- [1,[1,2,[1,2]]]
"""
        expect = str(Program([VarDecl(Id("a"), None, "var", 
                ArrayLiteral([NumberLiteral(1.0), 
                            ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), 
                                         ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)])])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 375))


    def test_376(self):
        input = """
func fib(number x) begin 
    if ((x = 0) or (x = 1)) return x + 1
    return fib(x-1) + fib(x-2)
end
"""
        expect = str(Program([FuncDecl(Id("fib"), [VarDecl(Id("x"), NumberType(), None, None)], Block([
            If(BinaryOp("or", BinaryOp("=", Id("x"), NumberLiteral(0.0)), BinaryOp("=", Id("x"), NumberLiteral(1.0))), Return(BinaryOp("+", Id("x"), NumberLiteral(1.0))), [], None), 
            Return(BinaryOp("+", CallExpr(Id("fib"), [BinaryOp("-", Id("x"), NumberLiteral(1.0))]), CallExpr(Id("fib"), [BinaryOp("-", Id("x"), NumberLiteral(2.0))])))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 376))


    def test_377(self):
        input = """
bool a <- x< -1
"""
        expect = str(Program([VarDecl(Id("a"), BoolType(), None, BinaryOp("<", Id("x"), UnaryOp("-", NumberLiteral(1.0))))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 377))


    def test_378(self):
        input = """
bool a <- b > (c > (d > (e > 1)))
"""
        expect = str(Program([VarDecl(Id("a"), BoolType(), None, 
                BinaryOp(">", Id("b"), 
                    BinaryOp(">", Id("c"), 
                        BinaryOp(">", Id("d"), 
                            BinaryOp(">", Id("e"), NumberLiteral(1.0))))))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 378))


    def test_379(self):
        input = """
bool a <- (((b > c) > d) > e) > 1
"""
        expect = str(Program([VarDecl(Id("a"), BoolType(), None, 
                BinaryOp(">", 
                    BinaryOp(">", 
                        BinaryOp(">", 
                            BinaryOp(">", Id("b"), Id("c")), Id("d")), Id("e")), NumberLiteral(1.0)))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 379))


    def test_380(self):
        input = """
number a <- foo([1,2], a[1,2])
"""
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, 
                CallExpr(Id("foo"), [
                    ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]), 
                    ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0)])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 380))


    def test_381(self):
        input = """
number a <- foo([1,2] + a[1,2] + f(a()[1]))
"""
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, 
                CallExpr(Id("foo"), [
                    BinaryOp("+", BinaryOp("+", 
                        ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]), 
                        ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0)])), 
                        CallExpr(Id("f"), [ArrayCell(CallExpr(Id("a"), []), [NumberLiteral(1.0)])]))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 381))


    def test_382(self):
        input = """
bool a <- (1>2) <= (3>4)
"""
        expect = str(Program([VarDecl(Id("a"), BoolType(), None, 
                BinaryOp("<=", 
                    BinaryOp(">", NumberLiteral(1.0), NumberLiteral(2.0)), 
                    BinaryOp(">", NumberLiteral(3.0), NumberLiteral(4.0))))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 382))


    def test_383(self):
        input = """
dynamic a <- x and y and z and 1 and 2 and 3 or 4
"""
        expect = str(Program([VarDecl(Id("a"), None, "dynamic", 
                BinaryOp("or", BinaryOp("and", BinaryOp("and", BinaryOp("and", BinaryOp("and", BinaryOp("and", Id("x"), Id("y")), Id("z")), NumberLiteral(1.0)), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0)))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 383))


    def test_384(self):
        input = """
dynamic a <- -x and y and z and 1 and 2 and 3 or 4
"""
        expect = str(Program([VarDecl(Id("a"), None, "dynamic", 
                BinaryOp("or", BinaryOp("and", BinaryOp("and", BinaryOp("and", BinaryOp("and", BinaryOp("and", UnaryOp("-", Id("x")), Id("y")), Id("z")), NumberLiteral(1.0)), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0)))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 384))


    def test_385(self):
        input = """
string x <- "     "
"""
        expect = str(Program([VarDecl(Id("x"), StringType(), None, StringLiteral("     "))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 385))


    def test_386(self):
        input = """
func foo(string x) 
begin
    write(toUpper(x + "!"))
end
"""
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("x"), StringType(), None, None)], Block([
                CallStmt(Id("write"), [CallExpr(Id("toUpper"), [BinaryOp("+", Id("x"), StringLiteral("!"))])])])
            )]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 386))


    def test_387(self):
        input = """
string x <- "## is this comment? ##"
"""
        expect = str(Program([VarDecl(Id("x"), StringType(), None, StringLiteral("## is this comment? ##"))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 387))


    def test_388(self):
        input = """
func main()
begin 
    dynamic _var
    var dynamic_  <- _var 
    if (var_) if_<--_var
end
"""
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("_var"), None, "dynamic", None), 
            VarDecl(Id("dynamic_"), None, "var", Id("_var")), 
            If(Id("var_"), Assign(Id("if_"), UnaryOp("-", Id("_var"))), [], None)]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 388))


    def test_389(self):
        input = """
func printAll(string x[100])
begin
    var i<-0
    for i until i = size(x) by 1
        print(x[i])
end
"""
        expect = str(Program([FuncDecl(Id("printAll"), [VarDecl(Id("x"), ArrayType([100.0], StringType()), None, None)], 
                    Block([VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), 
                           For(Id("i"), BinaryOp("=", Id("i"), CallExpr(Id("size"), [Id("x")])), NumberLiteral(1.0), CallStmt(Id("print"), [ArrayCell(Id("x"), [Id("i")])]))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 389))


    def test_390(self):
        ## testcase in specification file
        input = """
func foo(number a[5], string b)
begin
    var i <- 0
        for i until i >= 5 by 1
        begin
            a[i] <- i * i + 5
        end
    return -1
end
"""
        expect = str(Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), ArrayType([5.0], NumberType()), None, None), VarDecl(Id("b"), StringType(), None, None)], 
                    Block([
                        VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), 
                        For(Id("i"), BinaryOp(">=", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([
                            Assign(ArrayCell(Id("a"), [Id("i")]), BinaryOp("+", BinaryOp("*", Id("i"), Id("i")), NumberLiteral(5.0)))])), 
                            Return(UnaryOp("-", NumberLiteral(1.0)))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 390))


    def test_391(self):
        input = """
func gcd(number a, number b)
begin
    if (b = 0) return a
    return gcd(b, a % b)
end
"""
        expect = str(Program([FuncDecl(Id("gcd"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], 
                            Block([
                                If(BinaryOp("=", Id("b"), NumberLiteral(0.0)), Return(Id("a")), [], None), 
                                Return(CallExpr(Id("gcd"), [Id("b"), BinaryOp("%", Id("a"), Id("b"))]))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 391))


    def test_392(self):
        input = """
func main()
begin
    for i until i = a*-2 by -2
        if (i)
            continue
        elif (i-1)
            break
        for j until j = i by _+_
            if (j) return
end
"""
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            For(Id("i"), BinaryOp("=", Id("i"), BinaryOp("*", Id("a"), UnaryOp("-", NumberLiteral(2.0)))), UnaryOp("-", NumberLiteral(2.0)), 
                If(Id("i"), Continue(), [(BinaryOp("-", Id("i"), NumberLiteral(1.0)), Break())], None)), 
                For(Id("j"), BinaryOp("=", Id("j"), Id("i")), BinaryOp("+", Id("_"), Id("_")), If(Id("j"), Return(), [], None))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 392))


    def test_393(self):
        input = """
func main() begin 
    if (a < 50) a <- 50
    elif (a < 100) a <- 100
    else a <- 1000
end
"""
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            If(BinaryOp("<", Id("a"), NumberLiteral(50.0)), Assign(Id("a"), NumberLiteral(50.0)), 
               [(BinaryOp("<", Id("a"), NumberLiteral(100.0)), Assign(Id("a"), NumberLiteral(100.0)))], 
               Assign(Id("a"), NumberLiteral(1000.0)))]
        ))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 393))


    def test_394(self):
        input = """
func main() begin 
    var a <- foo()
    if (a < 0) 
        begin
        end
    else if (a < 50) a <- 50
        elif (a < 100) a <- 100
        else a <- 1000
end
"""
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("a"), None, "var", CallExpr(Id("foo"), [])), 
            If(BinaryOp("<", Id("a"), NumberLiteral(0.0)), Block([]), [], 
               If(BinaryOp("<", Id("a"), NumberLiteral(50.0)), Assign(Id("a"), NumberLiteral(50.0)), 
                  [(BinaryOp("<", Id("a"), NumberLiteral(100.0)), Assign(Id("a"), NumberLiteral(100.0)))], 
                  Assign(Id("a"), NumberLiteral(1000.0))))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 394))


    def test_395(self):
        input = """
func main() begin 
    if (true)
        if (true)
            if (true)
                if (true)
                    if (true)
                        return
                    else break
end
"""
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
                If(BooleanLiteral(True), 
                    If(BooleanLiteral(True), 
                        If(BooleanLiteral(True), 
                            If(BooleanLiteral(True), Return(), [], Break()), 
                        [], None), 
                    [], None), 
                [], None), 
            [], None)]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 395))


    def test_396(self):
        input = """
func main() 
begin 
    for i until i = 10 by 1 number a <- 10
end
"""
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            For(Id("i"), BinaryOp("=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), 
                VarDecl(Id("a"), NumberType(), None, NumberLiteral(10.0)))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 396))


    def test_397(self):
        input = """
func main() begin 
if (false) 
	for i until i=10 by x
		if (true) continue
		elif (x) continue
		else continue
end
"""
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(False), 
               For(Id("i"), BinaryOp("=", Id("i"), NumberLiteral(10.0)), Id("x"), 
                   If(BooleanLiteral(True), Continue(), [(Id("x"), Continue())], Continue())), 
            [], None)]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 397))


    def test_398(self):
        input = """bool a <- foo(("" ... "") == "")[x,y]
"""
        expect = str(Program([VarDecl(Id("a"), BoolType(), None, 
                    ArrayCell(
                        CallExpr(Id("foo"), [BinaryOp("==", BinaryOp("...", StringLiteral(""), StringLiteral("")), StringLiteral(""))]), 
                        [Id("x"), Id("y")]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 398))


    def test_399(self):
        input = """bool a <- foo("" ... "" == "")[x,y]
"""
        expect = str(Program([VarDecl(Id("a"), BoolType(), None, 
                    ArrayCell(
                        CallExpr(Id("foo"), [BinaryOp("...", StringLiteral(""), BinaryOp("==", StringLiteral(""), StringLiteral("")))]), 
                        [Id("x"), Id("y")]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 399))


    def test_400(self):
        input = """
func isPalindrome(string s[100], number left, number right)
begin
    if (left > right + 1) return false
    elif ((left = right) or (left = right + 1)) return true
    else 
        return (s[left] == s[right]) and isPalindrome(s, left + 1, right - 1)
end
"""
        expect = str(Program([FuncDecl(Id("isPalindrome"), [VarDecl(Id("s"), ArrayType([100.0], StringType()), None, None), VarDecl(Id(("left")), NumberType(), None, None), VarDecl(Id(("right")), NumberType(), None, None)], 
                    Block([
                        If(BinaryOp(">", Id("left"), BinaryOp("+", Id("right"), NumberLiteral(1.0))), Return(BooleanLiteral(False)), 
                           [(BinaryOp("or", BinaryOp("=", Id("left"), Id("right")), BinaryOp("=", Id("left"), BinaryOp("+", Id("right"), NumberLiteral(1.0)))), Return(BooleanLiteral(True)))], 
                           Return(BinaryOp("and", BinaryOp("==", ArrayCell(Id("s"), [Id("left")]), ArrayCell(Id("s"), [Id("right")])), CallExpr(Id("isPalindrome"), [Id("s"), BinaryOp("+", Id("left"), NumberLiteral(1.0)), BinaryOp("-", Id("right"), NumberLiteral(1.0))])))
                        )
                    ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 400))
