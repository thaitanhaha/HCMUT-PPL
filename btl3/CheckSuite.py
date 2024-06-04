import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_401(self):
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_402(self):
        input = """
        func main()
        begin
            number a <- 2
            number a 
        end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_403(self):
        input = """
        number a <- 2
        func main()
        begin
            number a 
            number b 
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404(self):
        input = Program([VarDecl(Id("str"), None, "var", None)])
        expect = "Type Cannot Be Inferred: VarDecl(Id(str), None, var, None)"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_405(self):
        input = Program([FuncDecl(Id("main"), [], Block([
            VarDecl(Id("a"), None, "var", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)))
        ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406(self):
        input = Program([VarDecl(Id("a"), None, "var", BinaryOp("+", NumberLiteral(1.0), StringLiteral("A")))])
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), StringLit(A))"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_407(self):
        input = """
        func main()
        begin
            number a
            a <- "abc" 
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_408(self):
        input = """
        func b(number x) return 1
        func main()
        begin
            number a
            number b
            number c
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_409(self):
        input = """
        func b(number x, number y) return 1
        func main()
        begin
            number a <- b(1, 2)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_410(self):
        input = """
        func b(number x, number y) return 1
        func main()
        begin
            var a <- b(1, 2) + "2"
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, CallExpr(Id(b), [NumLit(1.0), NumLit(2.0)]), StringLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_411(self):
        input = """
        func b()
        func main()
        begin
            number a <- b()
        end
        func b() return 1
        func b() return 1
        """
        expect = "Redeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_412(self):
        input = """
        func b()
        func main()
        begin
            number a <- b()
        end
        func b() return "1"
        """
        expect = "Type Mismatch In Statement: Return(StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_413(self):
        input = """
        func b()
        func main()
        begin
            number a <- b()
        end
        """
        expect = "No Function Definition: b"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_414(self):
        input = """
        func foo() return "1"
        func main()
        begin
            number a <- 1
            dynamic c
            if (a > 1) c <- foo()
            elif (a = 1) c <- foo() ... "2"
            else c <- foo() ... "3"
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):
        input = """
        func foo2()
        func foo1() 
        func foo3()
        func main()
        begin
            number a <- 1
            bool b
            for a until foo1() by foo2()
                b <- foo1()
        end
        func foo1()
        begin
            return true
        end
        func foo2()
        begin
            return 2
        end
        func foo3() return 3
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_416(self):
        input = """
        dynamic c
        dynamic d
        number a <- 1
        func main()
        begin
            bool b
            for a until c by d
                b <- true
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):
        input = """
        func main()
        begin
            number a <- 1
            ## for a until a<10 by 1
                break
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
        input = """
        func main()
        begin
            number a[5] <- [1, 2, 3, 4]
            number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):
        input = """
        func foo()
        func main()
        begin
            number b[2, 3] <- [[1, 2, 3], [4, 5, foo()]]
        end
        func foo() return "1"
        """
        expect = "Type Mismatch In Statement: Return(StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):
        input = """
        func main()
        begin
            var a <- a
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
        input = """
        func main()
        begin
            number a <- a
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        input = """
        dynamic a
        func foo() return a
        func main()
        begin
            number num <- foo()
        end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
        input = """
        func main()
        begin
            dynamic x
            x <- (x = 1) or ("abc" == "abc")
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BinaryOp(or, BinaryOp(=, Id(x), NumLit(1.0)), BinaryOp(==, StringLit(abc), StringLit(abc))))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
        input = """
        func foo()
        func main()
        begin
            number a <- 1
        end
        func foo(number x)
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        input = """
        func f(number x)
        func main()
        begin
            number a <- 1
        end
        func f(number y) 
        begin
            return y
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):
        input = """
        func f(number x)
        func main()
        begin
            number a <- 1
        end
        func f(number y, number k) 
        begin
            return y + k
        end
        """
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_427(self):
        input = """
        func main()
        begin
            dynamic a
            a <- [1,2,3] 
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):
        input = """
        func foo(number a[5]) 
            return [1,2,3]
        func main()
        begin
            dynamic a
            a <- foo([1,2,3,4,5])
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_429(self):
        input = """
        func foo(number a[5])
        func main()
        begin
            dynamic a <- foo([1,2,3,4,5])
        end
        func foo(number a[5]) 
            return [1,2,3]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, CallExpr(Id(foo), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0))]))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_430(self):
        input = """
        func foo(number a[5])
        func main()
        begin
            dynamic a 
            a <- foo([1,2,3,4,5])
        end
        func foo(number a[5]) 
            return [1,2,3]
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), CallExpr(Id(foo), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0))]))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_431(self):
        input = """
        func main()
        begin
            number x[5] <- [1,2,3,4,5]
            x[1] <- "2"
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(x), [NumLit(1.0)]), StringLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_432(self):
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
        func main()
        begin
            number x[5] <- [1,2,3,4,5]
            string y <- "abc"
            var a <- foo(x, y)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_433(self):
        input = """
        func foo() return [5,4,3,2,1]
        func main()
        begin
            number a <- foo()[1]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_434(self):
        input = """
        func foo(number x)
        func main()
        begin
            number a[5] <- [1,2,3,4,5]
            number b[3,4]
            a[3 + foo(2)] <- a[b[2, 3]] + 4
        end
        func foo(number k) return 1
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        input = """
        func writeNumber(number x)
        func main()
        begin
            number a <- 1
        end
        func writeNumber(number x)
            return x
        """
        expect = "Redeclared Function: writeNumber"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_436(self):
        input = """
        func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main()
        begin
            var num1 <- readNumber()
            var num2 <- readNumber()
            if (areDivisors(num1, num2)) writeString("Yes")
            else writeString("No")
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_437(self):
        input = """
        func isPrime(number x)
        func main()
        begin
            number a <- readNumber()
            if (isPrime(a)) writeString("Yes")
            else writeString("No")
        end
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_438(self):
        input = """
        func isPrime(number x)
        func main()
        begin
            number a <- readNumber()
            if (isPrime(a)) writeString("Yes")
            elif (1+1 = 3) writeString("No")
            else writeNumber(1)
        end
        func isPrime(number x)
        begin
            if (x <= 1) return false
            var i <- 2
            for i until i > x / 2 by 1
            begin
                if (x % i = 0) return false
                else 
                begin
                    begin
                        return false
                    end
                    return false
                end
            end
            return true
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_439(self):
        input = """
        func foo()
        func main()
        begin
            number a <- foo()
        end
        func foo()
        begin
            
        end
        """
        # ko co return
        expect = "Type Mismatch In Statement: FuncDecl(Id(foo), [], Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_440(self):
        input = """
        func foo() 
        begin
            dynamic a
            return a
        end
        func main()
        begin
            return
        end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_441(self):
        input = """
        func main()
        begin
            number a[1,2] <- [[1,2]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_442(self):
        input = """
        func foo(number a, string a) return 1
        func main()
        begin
            number x <- foo(1, "2")
        end
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_443(self):
        input = """
        func foo(number a, string b) 
        begin
            number a <- 1
            begin
                number a <- 2
            end
        end
        func main()
        begin
            return
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_444(self):
        input = """
        dynamic x
        dynamic a
        func main()
        begin 
            x <- [a, 1, 2]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):
        input = """
        dynamic a
        dynamic b
        dynamic c
        func main()
        begin 
            number x[3,3] <- [a,b,c]
            a <- [1,2,3]
            b <- [4,5,6]
            c <- [7,8,9]
            writeNumber(a[0] + b[0] + c[0])
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_446(self):
        input = """
        func main()
        begin 
            x <- 1
        end
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_447(self):
        input = """
        func main()
        begin 
            number x <- foo()
        end
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_448(self):
        input = """
        func foo(number foo)
        func main()
        begin 
            number foo <- foo(1)
        end
        func foo(number foo)
            return foo
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        input = """
        dynamic a
        func main()
        begin 
            bool x <- (a ... "1") == "21"
            writeNumber(x)
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(writeNumber), [Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_450(self):
        input = """
        func a() return "1"
        dynamic a
        func main()
        begin 
            writeNumber(a)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        input = """
        func a()
        func main()
        begin 
            writeNumber(a())
        end
        func a()
            return "2"
        """
        expect = "Type Mismatch In Statement: Return(StringLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
        input = """
        number a[5]
        number b
        func foo()
        func main()
        begin 
            a <- [1,b,3,4,foo()]
        end
        func foo()
            return "1"
        """
        expect = "Type Mismatch In Statement: Return(StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        input = """
        dynamic a
        func foo()
        func main()
        begin 
            a <- ["1", foo()]
        end
        func foo()
            return 1
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_454(self):
        input = """
        dynamic a
        dynamic b
        dynamic c
        dynamic d
        func main()
        begin
            var e <- 1
            number x[4,1,1,2] <- [[[[d, e]]], [[c]], [b], a]
            c <- [-10, 2 / 3 % 0.75]
            b <- [c]
            a <- [b]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_455(self):
        input = """
        number a[3]
        dynamic b
        dynamic c
        dynamic x
        func main()
        begin 
            x <- [a,b,c]
            a <- [1,2,3]
            b <- [4,5,6]
            c <- [7,8,9]
            writeNumber(a[0] + b[0] + c[0])
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_456(self):
        input = """
        dynamic a
        dynamic b
        dynamic c
        dynamic d
        func main()
        begin
            var e <- 1
            number x[4,1,1,2] <- [a, [b], [[[d, e]]], [[c]]]
            c <- [-10, 2 / 3 % 0.75]
            b <- [c]
            a <- [b]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_457(self):
        input = """
        dynamic a
        dynamic b
        dynamic c
        dynamic d
        dynamic x
        func main()
        begin
            var e <- 1
            x <- [a, [b], [[[d, e]]], [[c]]]
            c <- [-10, 2 / 3 % 0.75]
            b <- [c]
            a <- [b]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_458(self):
        input = """
        number a
        func main()
        begin
            number a
            a <- 1
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_459(self):
        input = """
        number a
        func foo()
        begin
            return b
            return 4
            return "foo"
        end
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test460(self):
        input = """
        func main()
        begin
            dynamic a
            dynamic b
            dynamic c
            dynamic x 
            x <- [a, [b, c], [2, 3]]
            writeNumber(a[0] + a[1] + b + c)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 460))
    
    def test461(self):
        input = """
        func main()
        begin
            dynamic a
            dynamic b
            dynamic c
            dynamic d
            dynamic x
            x <- [a, [b, c], [2, d]]
            d <- x[0, 0] + x[0, 1]
            writeNumber(a[0] + a[1] + b + c + d)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test462(self):
        input = """
        func main()
        begin
            dynamic a
            var b <- a + (a < a)
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), BinaryOp(<, Id(a), Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test463(self):
        input = """
        func main()
        begin
            dynamic a
            var b <- a and (a < a)
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(<, Id(a), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test464(self):
        input = """
        func foo() return
        func main()
        begin
            var x <- foo()
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test465(self):
        input = """
        func foo() return
        func main()
        begin
            foo()
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test466(self):
        input = """
        func foo() return
        func foo1() return 1
        func main()
        begin
            foo()
            foo1()
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo1), [])"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test467(self):
        input = """
        func foo()
        begin
            dynamic x
            x <- [[1, 2, 3], [4, 5, 6]]
            return x[0, 0]
        end

        func main()
        begin
            number x <- foo()
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test468(self):
        input = """
        number x[1,1]
        func main()
        begin
            var y <- x[0, 0] + 1
            writeNumber(y)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test469(self):
        input = """
        dynamic x
        func main()
        begin
            x <- [1, 2, 3, 4, 5, 6]
            var y <- x[0, 0] + 1
            writeNumber(y)
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(0.0), NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 469))
    
    def test470(self):
        input = """
        func f()
        begin
            dynamic x
            x <- (x - 2) * (x + true)
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 470))
    
    def test471(self):
        input = """
func add(number x, number y)

func main()
begin
    number x <- readNumber()
    number y <- readNumber()
    writeNumber(add(x, y))
end

func add(number i, number j)
begin
    return i*1*1*-1*-1 - -j
end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test472(self):
        input = """
        func foo() 
        begin
            dynamic d
            return d
        end
        func main() 
        begin 
        end
        """
        expect = "Type Cannot Be Inferred: Return(Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test473(self):
        input = """
        func main() 
        """
        expect = "No Function Definition: main"
        self.assertTrue(TestChecker.test(input, expect, 473))
    
    def test474(self):
        input = """
        func f(number x, number x)
        func main() return
        func f(number x, number y) 
        begin
            return x + y
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 474))
    
    def test475(self):
        input = """
        func f(number x, number x) return
        func main() return
        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 475))
    
    def test476(self):
        input = """
        func main()
        func foo()
        begin
            number a <- main()
        end
        func main() return 
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test477(self):
        input = """
        func main()
        func main() return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test478(self):
        input = """
        func foo()
        func main()
        begin
            
        end
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test479(self):
        input = """
        func foo()
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 479))
    
    def test480(self):
        input = """
        func foo(number x, string y)
        func foo(number x, number x) return 1
        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 480))
    
    def test481(self):
        input = """
        dynamic x
        number a[2,2] <- [[1,1], [x,x]]
        func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test482(self):
        input = """
        dynamic x
        number a[2,2] <- [x, [x,x]]
        func main() return
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test483(self):
        input = """
        dynamic x
        number a[1,3] <- [[1,x], [x,x]]
        func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), Id(x)), ArrayLit(Id(x), Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 483))
    

    def test484(self):
        input = """
        func foo()
        func main()
        begin
            number a <- foo()
        end
        func foo()
        begin
            dynamic x
            return x
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 484))
    

    def test485(self):
        input = """
        func foo()
        begin
            number i
            for i until i > 10 by 1
                if (i = 1) return "1"
                else return 2
            return
        end
        func main() 
        begin
        end
        """
        expect = "Type Mismatch In Statement: Return(NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 485))
    

    def test486(self):
        input = """
        func foo(number a[2,2])
            return 1
        dynamic x
        dynamic a
        func main()
        begin
            x <- [[[1,2,3], [a,1]]]
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(a), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 486))
    

    def test487(self):
        input = """
            func main() begin
                var i <- 2
                for i until true by 1
                begin
                    break
                    continue
                    begin
                        break
                        continue
                    end
                    
                    for i until true by 1
                    begin
                        break
                        continue
                    end
                    break
                    continue
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))
    

    def test488(self):
        input = """
            func main() begin
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 488))
    

    def test489(self):
        input = """
            number a[1,2,3] <- [[1,2]]
            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 489))
    

    def test490(self):
        input = """
            number a[1] <- [[1,2]]
            func main() return
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))))"
        self.assertTrue(TestChecker.test(input, expect, 490))
    

    def test491(self):
        input = """
            func foo(number a) return

            func main()
            begin
                dynamic a
                foo(a)
                number c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 491))
    

    def test492(self):
        input = """
            func foo() 
            begin
                dynamic a 
                dynamic b
                dynamic c <- "1"
                for a until b by c return
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(b), Id(c), Return())"
        self.assertTrue(TestChecker.test(input, expect, 492))
    

    def test493(self):
        input = """
            func a()
            func main() 
            begin 
                a()
            end
            func a() return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))
    

    def test494(self):
        input = """
            func a()
            func main() 
            begin 
                a()
            end
            func a() return 1
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 494))
    

    def test495(self):
        input = """
            func main() 
            begin 
                number a[1,3]
                dynamic c
                c <- [[1,2,3]]
                c <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 495))
    

    def test496(self):
        input = """
            func main() 
            begin 
                number a
                dynamic b
                dynamic c
                b <- c
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 496))
    

    def test497(self):
        input = """
            func main() 
            begin 
                number a
                dynamic b
                dynamic c
                a <- c
                b <- c
                return a
                return b
                return c
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 497))
    

    def test498(self):
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                foo([x, x])
                x <- [1, 1]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498))
    

    def test499(self):
        input = """
            func foo(number a[2,2]) return
            func main() 
            begin
                dynamic x
                foo([x])
                x <- [1]
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [ArrayLit(Id(x))])"
        self.assertTrue(TestChecker.test(input, expect, 499))
    

    def test500(self):
        input = """
            func foo() begin
                dynamic x
                dynamic y
                return [[y], [y]]
                return x
                return [[1], [2]]
            end
            func main() return 
        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(y)), ArrayLit(Id(y))))"
        self.assertTrue(TestChecker.test(input, expect, 500))
