import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_500(self):
        input = """
        number a <- 2
        func main()
        begin
            writeNumber(1)
            writeBool(true)
            writeString("abc")
        end
        """
        expect = "1.0trueabc"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_501(self):
        input = """func main()
        begin
            writeNumber(1 + 2)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_502(self):
        input = """
        number a <- 1
        func main()
        begin
            writeNumber(a)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_503(self):
        input = """
        number a
        func main()
        begin
            a <- 2
            writeNumber(a)
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_504(self):
        input = """
        func foo()
        func main()
        begin
            foo()
        end
        func foo()
        begin
            number a <- 3
            writeNumber(a)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_505(self):
        input = """
        number b <- -1
        func main()
        begin
            number a <- -2
            writeNumber(a + 10*-b - 1)
        end
        """
        expect = "7.0"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_506(self):
        input = """
        func foo() 
        begin
            return 1
        end
        func main()
        begin
            number a <- foo()
            writeNumber(a)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_507(self):
        input = """
        func foo() 
        begin
            number b <- 1
            if (b < 2) return 10
            elif (b > 3) return 11
            else return 12
        end
        func main()
        begin
            number a <- foo()
            writeNumber(a)
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_508(self):
        input = """
        func foo()
        begin
            number b <- 1
            for b until b > 5 by 1 
                return 1
            return 2
        end
        func main()
        begin
            number a <- foo()
            writeNumber(a)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_509(self):
        input = """
        var a <- 11
        func main()
        begin
            dynamic b <- 12
            writeNumber(a + b)
        end
        """
        expect = "23.0"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_510(self):
        input = """
        func main()
        begin
            number a[3] <- [1,2,3]
            writeNumber(a[1])
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_511(self):
        input = """
        func foo(number a)
        begin
            return 2
        end
        func main()
        begin
            number x <- foo(1)
            writeNumber(x)
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_512(self):
        input = """
        func main()
        begin
            number a[2,3] <- [[1,2,3], [4,5,6]]
            writeNumber(a[1,2])
        end
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_513(self):
        input = """
        func foo()
        begin
            number x <- 1
            dynamic a 
            a <- x + 2
            return a
        end
        func main()
        begin
            dynamic x <- foo()
            writeNumber(x)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_514(self):
        input = """
        dynamic x
        dynamic y
        func foo()
        begin
            x <- 1
            dynamic a 
            a <- x + 3
            return a
        end
        func main()
        begin
            y <- foo()
            writeNumber(y)
        end
        """
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_515(self):
        input = """
        func a() 
        begin
            number a <- 2
            if (a = 1) 
            begin 
                return 3
            end
            elif (a = 2)
            begin
                return 5
            end
            else 
            begin 
                return 4
            end
        end
        func main()
        begin
            number a <- a()
            writeNumber(a)
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_516(self):
        input = """
        func a() 
        begin
            number a <- 2
            for a until a > 3 by 1
            begin
                if (a = 2)
                begin
                    return a
                end 
            end
            return 100
        end
        func main()
        begin
            writeNumber(a())
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_517(self):
        input = """
        func areDivisors(number num1, number num2)
            return (num2 % num1 = 0) or (num1 % num2 = 0)
        func main()
        begin
            var num1 <- 4
            var num2 <- 8
            if (areDivisors(num1, num2)) writeString("Yes")
            else writeString("No")
        end
        """
        expect = "Yes"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_518(self):
        input = """
        func main()
        begin
            number x <- 5
            if (isPrime(x)) writeString("Yes")
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
        expect = "Yes"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_519(self):
        input = """
        func main()
        begin
            number a[5] <- [1,2,3,4,5]
            a[0] <- 2
            writeNumber(a[0])
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_520(self):
        input = """
        func main()
        begin
            string a[3] <- ["1", "2", "3"]
            string b[1] <- [a[2]]
            writeString(b[0])
        end
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_521(self):
        input = """
        func main()
        begin
            writeString("a" ... "b")
        end
        """
        expect = "ab"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_522(self):
        input = """
        func main()
        begin
            string a[2,2] <- [["a", "b"], ["c", "d"]]
            string b[2,2] <- [[a[0,0], a[0,1]], [a[1,0], a[1,1]]]
            writeString((b[0,0] ... b[0,1]) ... (b[1,0] ... b[1,1]))
        end
        """
        expect = "abcd"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_523(self):
        input = """
        func foo()
        begin
            number a[1,3] <- [[10,20,30]]
            return a
        end
        func main()
        begin
            number a[1,3] <- foo()
            writeNumber(a[0,0])
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_524(self):
        input = """
        func foo()
        begin
            return [10, 20, 30]
        end
        func main()
        begin
            number a[3] <- foo()
            writeNumber(a[0])
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_525(self):
        input = """
        func foo()
        begin
            return [[10, 20, 30]]
        end
        func main()
        begin
            number a[1,3] <- foo()
            writeNumber(a[0,2])
        end
        """
        expect = "30.0"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_526(self):
        input = """
        func foo()
        begin
            dynamic a
            a <- [[10,20,30]]
            return a
        end
        func main()
        begin
            number a[1,3] <- foo()
            writeNumber(a[0,2])
        end
        """
        expect = "30.0"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_527(self):
        input = """
        dynamic a
        func foo()
        begin
            a <- [[10,20,30]]
            return a
        end
        func main()
        begin
            number x[1,3] <- foo()
            writeNumber(x[0,2])
        end
        """
        expect = "30.0"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_528(self):
        input = """
        dynamic a
        func foo()
        begin
            a <- [[10,20,30]]
            return a
        end
        func main()
        begin
            number x <- (foo())[0,2]
            writeNumber(x)
        end
        """
        expect = "30.0"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_529(self):
        input = """
        func main()
        begin
            number i <- 1
            for i until i >= 10 by 1
            begin
                if (i % 2 = 0) continue
                writeNumber(i)
                writeString("\\n")
            end
        end
        """
        expect = "1.0\n3.0\n5.0\n7.0\n9.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_530(self):
        input = """
        func main()
        begin
            number i <- 1
            for i until i >= 10 by 1
            begin
                if (i = 6) break
                writeNumber(i)
                writeString("\\n")
            end
            return
        end
        """
        expect = "1.0\n2.0\n3.0\n4.0\n5.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_531(self):
        input = """
        number a
        func main()
        begin
            number i <- 1
            for i until i = 5 by 1
            begin
                a <- i
                writeNumber(a)
                writeString("\\n")
            end
            writeNumber(a)
        end
        """
        expect = "1.0\n2.0\n3.0\n4.0\n4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_532(self):
        input = """
        func main()
        begin
            number i <- 1
            for i until i = 5 by 1
            begin
                number a <- i
                writeNumber(a)
                writeString("\\n")
            end
        end
        """
        expect = "1.0\n2.0\n3.0\n4.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_533(self):
        input = """
        func main()
        begin
            number i <- 1
            number a
            for i until i = 5 by 1
            begin
                a <- i
                writeNumber(a)
                writeString("\\n")
            end
            writeNumber(a)
        end
        """
        expect = "1.0\n2.0\n3.0\n4.0\n4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_534(self):
        input = """
        func main()
        begin
            number a <- 1
            begin
                number a <- 2
                writeNumber(a)
            end
            writeNumber(a)
        end
        """
        expect = "2.01.0"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_535(self):
        input = """
        func foo(number a)
        begin
            number a <- 1
            return a
        end
        func main()
        begin
            number x <- 2
            number y <- foo(x)
            writeNumber(y)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_536(self):
        input = """
        func foo(number a)
        begin
            var i <- a % 5
            for i until i >= a by 1
            begin
                if (i = 5) return i
            end
        end
        func main()
        begin
            number a <- 10
            writeNumber(foo(a))
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_537(self):
        input = """
        func foo() 
        begin
            string a <- "1"
            string b <- "2"
            return [a,b,"3"]
        end

        func main()
        begin
            dynamic x
            x <- foo()
            number i <- 0
            for i until i = 3 by 1
            begin
                writeString(x[i])
                writeString(" ")
            end
        end
        """
        expect = "1 2 3 "
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_538(self):
        input = """
        func main()
        begin
            string a[7] <- ["t", "h", "a", "i", "t", "a", "n"]
            number i <- 0
            string b[7]
            for i until i = 7 by 1
                b[i] <- a[i]
            i <- 0
            for i until i = 7 by 1
            begin
                writeString(b[i])
            end
        end
        """
        expect = "thaitan"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_539(self):
        input = """
        func main()
        begin
            number a[7]
            a[0] <- 1
            a[1] <- 1
            number i <- 2
            for i until i=7 by 1
                a[i] <- a[i-1] + a[i-2]
            i <- 0
            for i until i=7 by 1
            begin
                writeNumber(a[i])
                writeString(" ")
            end
        end
        """
        expect = "1.0 1.0 2.0 3.0 5.0 8.0 13.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_540(self):
        input = """
        number a[7]
        func foo()
        begin
            a[0] <- 1
            a[1] <- 1
            number i <- 2
            for i until i=7 by 1
                a[i] <- a[i-1] + a[i-2]
            return
        end

        func main()
        begin
            foo()
            number i <- 0
            for i until i=7 by 1
            begin
                writeNumber(a[i])
                writeString(" ")
            end
            return
        end
        """
        expect = "1.0 1.0 2.0 3.0 5.0 8.0 13.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_541(self):
        input = """
        func foo()
        begin
            number i <- 1
            for i until i=10 by 1
                if (i = 1) 
                    return true
        end
        func main()
        begin
            writeBool(foo())
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_542(self):
        input = """
        func foo()
        begin
            number i <- 0
            number j <- 0   
            for i until i=10 by 1
                for j until j=10 by 1
                    return true
        end
        func main()
        begin
            writeBool(foo())
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_543(self):
        input = """
        func foo()
        begin
            number i <- 0
            number a[2,3]
            for i until i=2 by 1
            begin
                number j <- 0   
                for j until j=3 by 1
                    a[i,j] <- i*j
            end
            return a
        end
        func main()
        begin
            number i <- 0
            for i until i=2 by 1
            begin
                number j <- 0   
                for j until j=3 by 1
                begin
                    writeNumber(foo()[i,j])
                    writeString(" ")
                end
            end
        end
        """
        expect = "0.0 0.0 0.0 0.0 1.0 2.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_544(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i=10 by 1
            begin
                number j <- 0   
                for j until j=10 by 1
                begin
                    if (j=2) break
                    writeNumber(j)
                    writeString(" ")
                end
                if (i=3) break
                writeNumber(i)
                writeString("\\n")
            end
        end
        """
        expect = "0.0 1.0 0.0\n0.0 1.0 1.0\n0.0 1.0 2.0\n0.0 1.0 "
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_545(self):
        input = """
        func foo()
        begin
            begin
                return true
            end
        end
        func main()
        begin
            writeBool(foo())
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_546(self):
        input = """
        func foo(number a[2])
        begin
            a[1] <- a[1] + 1 + 0 + 0
        end
        func main()
        begin
            number a[2] <- [0, 2]
            foo(a)
            writeNumber(a[1])
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_547(self):
        input = """
        number a[3] <- [1,1,1]
        func sum_1(number b[3])
        begin
            number i <- 0
            for i until i=3 by 1
                b[i] <- b[i] + 1
            number sum <- 0
            i <- 0
            for i until i=3 by 1
                sum <- sum + b[i]
            return sum
        end
        func main()
        begin
            writeNumber(sum_1(a))
            number i <- 0
            for i until i=3 by 1
                writeNumber(a[i])
        end
        """
        expect = "6.02.02.02.0"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_548(self):
        input = """
        func main()
        begin
            writeBool(not not not not not not false and true or not true and false or true and not false)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_549(self):
        input = """
        func foo (number a, string b)
        begin
            if (a = 1) return b
            return b ... "a"
        end
        func main()
        begin
            writeString(foo(10000, "a"))
        end
        """
        expect = "aa"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_550(self):
        input = """
        func main()
        begin
            string a[5] <- ["#####", "####", "###", "##", "#"]
            number i <- 0
            for i until i >= 5 by 1
                writeString(a[i])
        end
        """
        expect = "###############"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_551(self):
        input = """
        func main()
        begin
            string a[5] <- ["#####", "####", "###", "##", "#"]
            number i <- 0
            string result <- ""
            for i until i >= 5 by 1
                result <- result ... a[i]
            writeString(result)
        end
        """
        expect = "###############"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_552(self):
        input = """
        func main()
        begin
            bool a[3] <- [true, false, false]
            writeBool(a[0])
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_553(self):
        input = """
        func main()
        begin
            bool a[2] <- [true, false]
            number b[2] <- [1, 2]
            if (a[0]) writeNumber(b[0])
            elif (a[1]) writeNumber(b[1])
            else writeString("tan")
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_554(self):
        input = """
        func main()
        begin
            bool a[2] <- [true, false]
            if (a[0] and a[1]) writeNumber(1)
            else writeString("abc")
        end
        """
        expect = "abc"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_555(self):
        input = """
        func foo(number a, number b[3])
        begin
            number c[3] <- [1,2,3]
            number i <- 0
            for i until i=3 by 1
                b[i] <- c[i] + a
        end 
        func main()
        begin
            number a[3] <- [0,0,0]
            foo(1, a)
            writeNumber(a[0])
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_556(self):
        input = """
        func main()
        begin
            number a <- 1
            writeNumber(-------------a)
        end
        """
        expect = "-1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_557(self):
        input = """
        func main()
        begin
            number a <- 1
            writeBool((a=1) or (a=2))
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_558(self):
        input = """
        func main()
        begin
            number a <- 1
            writeBool((a=1) and (a=2))
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_559(self):
        input = """
        number a <- 1
        number b <- a / 1
        func main()
        begin
            writeNumber(b)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_560(self):
        input = """
        number a <- 1
        number b <- a % 1
        func main()
        begin
            writeNumber(b)
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_561(self):
        input = """
        func foo() return 2
        number a <- foo()
        func main()
        begin
            writeNumber(a)
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_562(self):
        input = """
        func foo()
        number a <- foo()
        func main()
        begin
            writeNumber(a)
            return
        end
        func foo() return 1
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_563(self):
        input = """
        number a <- 1
        number b <- 2
        func foo(number a, number b)
        begin   
            return a + b
        end
        number c <- foo(a, b)
        func main()
        begin
            writeNumber(c)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_564(self):
        input = """
        dynamic x
        number b <- 2
        func foo(number b)
        begin
            x <- "tan"
            return b
        end
        number c <- foo(b)
        func main()
        begin
            writeString(x)
        end
        """
        expect = "tan"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_565(self):
        input = """
        number a <- 1
        number b <- a
        func foo(number a, number b)
        begin
            return a + b
        end
        number c <- foo(a, b)
        func main()
        begin
            writeNumber(c)
            return
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_566(self):
        input = """
        number a <- 1
        number b[3] <- [a, a, a]
        func foo(number a, number b[3])
        begin
            return a + b[0] + b[1] + b[2]
        end
        number c <- foo(a, b)
        func main()
        begin
            writeNumber(c)
        end
        """
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_567(self):
        input = """
        number a[3] <- [1,2,3]
        number b[3] <- a
        func foo(number a[3], number b[3])
        begin
            return a[0] + a[1] + a[2] + b[0] + b[1] + b[2]
        end
        number c <- foo(a, b)
        func main()
        begin
            writeNumber(c)
            return
        end
        """
        expect = "12.0"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_568(self):
        input = """
        number a[3] <- [1,2,3]
        number b[3] <- a
        func main()
        begin
            b[0] <- 10
            writeNumber(a[0])
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_569(self):
        input = """
        number a[3] <- [1,2,3]
        number b[3] <- [a[0], a[1], a[2]]
        func main()
        begin
            b[0] <- 10
            writeNumber(a[0])
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_570(self):
        input = """
        number a[3] <- [1,2,3]
        dynamic b
        func main()
        begin
            b <- [a[0], a[1], a[2]]
            b[0] <- 10
            writeNumber(a[0])
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_571(self):
        input = """
        number a[3] <- [1,2,3]
        dynamic b
        func main()
        begin
            b <- a
            b[0] <- 10
            writeNumber(a[0])
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_572(self):
        input = """
        number a[3] <- [1,2,3]
        func foo()
            return a
        dynamic b
        func main()
        begin
            b <- foo()
            b[0] <- 10
            writeNumber(a[0])
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_573(self):
        input = """
        number a[3] <- [1,2,3]
        func foo()
            return [a[0], a[1], a[2]]
        dynamic b
        func main()
        begin
            b <- foo()
            b[0] <- 10
            writeNumber(a[0])
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_574(self):
        input = """
        number a[2,3] <- [[1,2,3], [4,5,6]]
        func foo()
            return a
        dynamic b
        func main()
        begin
            b <- foo()
            b[0,0] <- 10
            writeNumber(a[0,0])
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_575(self):
        input = """
        number a[2,3] <- [[1,2,3], [4,5,6]]
        func foo()
            return [[a[0,0], a[0,1], a[0,2]], [a[1,0], a[1,1], a[1,2]]]
        dynamic b
        func main()
        begin
            b <- foo()
            b[0,0] <- 10
            writeNumber(a[0,0])
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_576(self):
        input = """
        func foo(string x, string y)
        func main()
        begin
            writeString(foo("abc", "abc"))
        end
        func foo(string x, string y)
        begin
            return x ... y
        end
        """
        expect = "abcabc"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_577(self):
        input = """
        func foo(string x[3])
        func main()
        begin
            var a <- foo(["1", "2", "3"])
            var b <- a[0]
            writeString(b)
        end
        func foo(string y[3])
        begin
            dynamic x
            x <- ["", "", ""]
            number i <- 0
            for i until i=3 by 1
                x[i] <- y[3-i-1]
            return x
        end
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_578(self):
        input = """
        func foo(number x[3])
        func main()
        begin
            writeNumber(foo([1, 2, 3]))
        end
        func foo(number y[3])
        begin
            dynamic x
            x <- [0, 0, 0]
            number i <- 0
            var sum <- 0
            for i until i=3 by 1
            begin
                x[i] <- y[3-i-1]
                sum <- sum + x[i]
            end
            return sum + i
        end
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_579(self):
        input = """
        func foo(number x[3])
        func main()
        begin
            foo([1, 2, 3])
        end
        func foo(number y[3])
        begin
            dynamic x
            x <- [0, 0, 0]
            number i <- 0
            var sum <- 0
            for i until i=3 by 1
            begin
                x[i] <- y[3-i-1]
                sum <- sum + x[i]
            end
            writeNumber(sum)
        end
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_580(self):
        input = """
        func foo(number x[2,3])
        func main()
        begin
            writeNumber(foo([[1,2,3], [4,5,6]]))
        end
        func foo(number y[2,3])
        begin
            dynamic x
            x <- [[0,0,0], [0,0,0]]
            number i <- 0
            number j <- 0
            var sum <- 0
            for i until i=2 by 1
            begin
                for j until j=3 by 1
                begin
                    x[i, j] <- y[i, 3-j-1]
                    sum <- sum + x[i, j]
                end
            end
            return sum + i + j
        end
        """
        expect = "21.0"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_581(self):
        input = """
        func foo(number x[2,3])
        func main()
        begin
            foo([[1,2,3], [4,5,6]])
        end
        func foo(number y[2,3])
        begin
            dynamic x
            x <- [[0,0,0], [0,0,0]]
            number i <- 0
            number j <- 0
            var sum <- 0
            for i until i=2 by 1
            begin
                for j until j=3 by 1
                begin
                    x[i, j] <- y[i, 3-j-1]
                    sum <- sum + x[i, j]
                end
            end
            writeNumber(sum + i + j)
        end
        """
        expect = "21.0"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_582(self):
        input = """
        func foo()
        begin
            number i <- 0
            for i until i=10 by 1
            begin
                if (i=10) return 10
                elif (i=8) break
            end
            return i
        end
        func main()
        begin
            number a <- foo()
            writeNumber(a)
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_583(self):
        input = """
        func foo()
        begin
            number i <- 0
            for i until i=10 by 1
            begin
                if (i=12) return i
            end
            return i
        end
        func main()
        begin
            number a <- foo() + foo() + foo() + foo() * 1 + 1
            writeNumber(a)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_584(self):
        input = """
        func foo()
        begin
            number i <- 0
            for i until i=10 by 1
            begin
                if (i=3)
                    return [[i,i], [i,i]]
            end
        end
        number y[2,2]
        func main()
        begin
            dynamic x
            x <- foo()
            y <- foo()
            writeNumber(x[0,0] + y[1,1])
        end
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_585(self):
        input = """
        func main()
        begin
            writeNumber(1 + 2 * 3 / 4 % 5)
        end
        """
        expect = "2.5"
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_586(self):
        input = """
        func main()
        begin
            writeBool(true and false and not true)
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_587(self):
        input = """
        func main()
        begin
            number a <- 1
            bool b <- (a=1)
            writeBool(not (b and false))
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_588(self):
        input = """
        dynamic x
        func main()
        begin
            x <- (1+1 = 2)
            writeBool(not x)
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_589(self):
        input = """
        bool x[2,2] <- [[true, true], [false, false]]
        func main()
        begin
            writeBool(x[0,0])
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_590(self):
        input = """
        func main()
        begin
            bool a <- true
            writeBool((a and false) or (true or false))
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_591(self):
        input = """
        func main()
        begin
            number a <- 3.14
            writeNumber(a * 2)
        end
        """
        expect = "6.28"
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_592(self):
        input = """
        dynamic x
        func foo()
        begin
            x <- [1,2,3]
        end
        func main()
        begin
            foo()
            writeNumber(x[0] * 10)
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_593(self):
        input = """
        func main()
        begin
            number a[2,2,2] <- [[[1,2], [3,4]], [[1,1], [1,1]]]
            writeNumber(a[0,1,1])
            return
        end
        """
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_594(self):
        input = """
        string a[1] <- ["1"]
        func main()
        begin
            writeString("GenG" ... a[0])
        end
        """
        expect = "GenG1"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_595(self):
        input = """
        func foo()
        func main()
        begin
            foo() 
        end
        func foo()
        begin

        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_596(self):
        input = """
        dynamic x
        func foo(number x[1])
        begin
            writeNumber(x[0])
        end
        func main()
        begin
            x <- [1]
            foo(x)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test_597(self):
        input = """
        func foo(number a)
            return a+1
        func main()
        begin
            writeNumber(foo(foo(foo(1))))
        end
        """
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_598(self):
        input = """
        func foo(number a)
            return a+1
        func bar(number a)
            return a*a
        func main()
        begin
            writeNumber(foo(bar(foo(1))))
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_599(self):
        input = """
        func foo() 
        begin
            return
        end
        func main()
        begin
            foo()
            return
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 599))

    def test_600(self):
        input = """
        func foo() return
        func a() 
        begin
            if (true) return
        end
        func b() 
        begin
            number i <- 1
            for i until i<10 by 1
                return
        end
        func main()
        begin
            foo()
            a()
            b()
            return
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 600))

    # def test_601(self):
    #     input = """
    #     func main()
    #     begin
    #         number a <- readNumber()
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "2.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 601))    



