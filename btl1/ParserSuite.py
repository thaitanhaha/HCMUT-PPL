import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_program_201(self):
        """test BKEL"""
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_program_202(self):
        """test BKEL"""
        input = """func main() begin
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_program_203(self):
        """test variable declaration: some normal cases"""
        input = """ 
            number a
            
            ## abc
            number a <- 0
            bool a[122,15]
            bool a[122,15] <- 1
            string b[3]
            ## 12 
            
            string b[3] <- 2
            var i <- 0
            dynamic i
            dynamic i <- 0
            ## abc
             
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_program_204(self):
        """test variable declaration: var must have initialize"""
        input = """ 
            var a
        """
        expect = """Error on line 2 col 18: 
"""
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_program_205(self):
        """test variable declaration: array cannot be dynamic"""
        input = """ 
            dynamic a[5] <- 3
        """
        expect = "Error on line 2 col 21: ["
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_program_206(self):
        """test variable declaration: array size must be number literal"""
        input = """ 
            bool a["string"]
        """
        expect = "Error on line 2 col 19: string"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_program_207(self):
        """test variable declaration: array size must be seperated by comma"""
        input = """ 
            bool a[1,]
        """
        expect = "Error on line 2 col 21: ]"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_program_208(self):
        """test variable declaration: var cannot be used for array"""
        input = """ 
            var a[1]
        """
        expect = "Error on line 2 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_program_209(self):
        """test function declaration: some normal cases"""
        input = """ 
            func f()
            func f(number f1)
            func f(number a[5], bool x[5,2,3], bool a[5,2,3], string b, bool c)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_program_210(self):
        """test function declaration: parameter cannot be assigned"""
        input = """ 
            func f(number f1 <- c)
        """
        expect = "Error on line 2 col 29: <-"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_program_211(self):
        """test function declaration: parameter cannot be dynamic"""
        input = """
            func main(dynamic a)
        """
        expect = "Error on line 2 col 22: dynamic"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_program_212(self):
        """test function declaration: parameter cannot be var"""
        input = """ 
            func main(var a)
        """
        expect = "Error on line 2 col 22: var"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_program_213(self):
        """test function declaration: must have new line after parameterlist"""
        input = """
            func main(number a) var c <- 1
        """
        expect = "Error on line 2 col 32: var"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_program_214(self):
        """test function declaration: body must be block or return or nothing"""
        input = """ 
            func main(number a[1,2,3])
                break
        """
        expect = "Error on line 3 col 16: break"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_program_215(self):
        """test function declaration: normal case"""
        input = """ 
            ##12
            func main(number a) 
                ##12
                
                begin 
                    break
                end
                
                ##12
                ##12
            func main(number a)
            ##12        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_program_216(self):
        """test function declaration: normal case"""
        input = """ 
            ## 12
            
            var a <- 1 ## 12
            ## 12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_program_217(self):
        """test declaration: must have newline at the end"""
        input = """var a <- 1"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_program_218(self):
        """test declaration: must have newline at the end"""
        input = """func main(number a) """
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_program_219(self):
        """test declaration: some more cases"""
        input = """func f(number a, string b, bool c)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_program_220(self):
        """test declaration: some more cases"""
        input = """var a <- f(1,2,3) + a[2]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_program_221(self):
        """test expression: concat normal case"""
        input = """var ab <- "a" ... "b" 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_program_222(self):
        """test expression: concat has no association"""
        input = """var abc <- "a" ... "b" ... "c" 
        """
        expect = "Error on line 1 col 23: ..."
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_program_223(self):
        """test expression: relation normal cases"""
        input = """ 
            var a <- a > a
            var b <- b >= b
            var c <- c = c
            var d <- d == d
            var e <- e < e
            var f <- f <= f
            var g <- g >= g
            var h <- h > h ... h > h
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_program_224(self):
        """test expression: relation has no association"""
        input = """ var abc <- a > b >= c 
        """
        expect = "Error on line 1 col 18: >="
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_program_225(self):
        """test expression: add, sub, mul, div, mod"""
        input = """ 
            var a <- 1 + 2
            var b <- 1 - 2
            var c <- 1 * 2
            var d <- 1 / 2
            var e <- 1 % 2
            var f <- a + b*c - d/e + 2%100
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_program_226(self):
        """test expression: """
        input = """var a <- true >= "true" and 1 > 2
        """
        expect = "Error on line 1 col 30: >"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_program_227(self):
        """test expression: not"""
        input = """ 
            var a <- not 1
            var b <- not not 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_program_228(self):
        """test expression: - """
        input = """ 
            var a <- -1
            var b <- ----a
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_program_229(self):
        """test expression: not and - normal case"""
        input = """var a <- not -1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_program_230(self):
        """test expression: not and - in wrong case"""
        input = """var a <- - not 1
        """
        expect = "Error on line 1 col 11: not"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_program_231(self):
        """test expression: array index"""
        input = """ 
            var a <- a[1] + 1
            var b <- array[1,1+2]
            var c <- 1[1]
            var d <- a[1+a, 2+b]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_program_232(self):
        """test expression: array index"""
        input = """ var a <- a[1,1+2][1][1,2]
        """
        expect = "Error on line 1 col 18: ["
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_program_233(self):
        """test expression: array index"""
        input = """var a <- a[1, (1)...2, a[a[(1*2) and 1]], a[2]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_program_234(self):
        """test expression: array index"""
        input = """var a <- a[1] + fun()[1, fun()] 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_program_235(self):
        """test expression: array index must have something inside"""
        input = """var a <- a[]
        """
        expect = "Error on line 1 col 11: ]"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_program_236(self):
        """test expression: array index with function call"""
        input = """ 
            var a <- a()[1]
            var b <- a(1,2)[1,2,3,4]
            var c <- a(x, array[1,2])[2]
            var d <- a(z, not k[3])[1,2]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_program_237(self):
        # """test expression: """
        # input = """var a <- a()()
        # """
        # expect = "Error on line 1 col 17: ("
        """test expression: some cases"""
        input = """number a <- c()[]
        """
        expect = "Error on line 1 col 16: ]"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_program_238(self):
        """test expression: some cases"""
        input = """var a <- a()[1,2,3] + true + "abc"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_program_239(self):
        """test expression: some cases"""
        input = """string a <- a() + 1/2*3 <= 3 ... "abc" >= 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_program_240(self):
        """test expression: some cases"""
        input = """var a <- ["a",1,2,3,4] + [[1,1+2*3/4,5], [6,7,8,9,10]]
        """
        expect = "Error on line 1 col 23: +"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_program_241(self):
        """test statement: assignment"""
        input = """
        func main()
            begin
                a <- 1 + 2 
                b <- 1
                c[1+2,3+4,5+6] <- [1,2,3]
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_program_242(self):
        """test statement: assignment with error in lhs"""
        input = """
        func main()
            begin
                a + 1 <- 2
            end
        """
        expect = "Error on line 4 col 18: +"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_program_243(self):
        """test statement: assignment with error in lhs"""
        input = """
        func main()
            begin
                a() <- 1
            end
        """
        expect = "Error on line 4 col 20: <-"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_program_244(self):
        """test statement: assignment with error in lhs"""
        input = """
        func main()
            begin
                (a)[1] <- 3.14
            end
        """
        expect = "Error on line 4 col 16: ("
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_program_245(self):
        """test statement: if statement"""
        input = """
        func main()
            begin   
                if (a=b) a <- 1

                if (a+b) 
                    a <- 1
                else a <- 1

                if (1+2) a <- 1
                elif (1 ... 2)
                    a <- 1
                elif (1) a <- 1

                if (1) a <- 1
                elif (1 ... 2) a <- 1
                elif (1) a <- 1
                else a <- 1   
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_program_246(self):
        """test statement: if statement with error in _statement"""
        input = """
        func main()
            begin   
                if (a) <- 1
            end
        """
        expect = "Error on line 4 col 23: <-" 
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_program_247(self):
        """test statement: for statement"""
        input = """
        func main()
            begin
            for i until i != 10 by 1
                a <- a + 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_program_248(self):
        """test statement: for statement with number variable error"""
        input = """
        func main()
            begin
            for i[1] until i != 10 by 1
                a <- a + 1
            end
        """
        expect = "Error on line 4 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_program_249(self):
        """test statement: for with break, continue"""
        input = """
        func main()
            begin 
                break
                for i until i != 10 by 1
                    begin
                        continue
                    end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_program_250(self):
        """test statement: for statement error with no statement"""
        input = """
        func main()
            begin
                for i until i != 10 by 1
            end
        """
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_program_251(self):
        """test statement: for statement with update error"""
        input = """
        func main()
            begin
                for i until i != 10 by a <- 1
                    a <- a + 1
            end
        """
        expect = "Error on line 4 col 41: <-"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_program_252(self):
        """test statement: return"""
        input = """
        func main() return 1+2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_program_253(self):
        """test statement: return with newline"""
        input = """
        func main() 
            return 1+2
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_program_254(self):
        """test statement: return an expression"""
        input = """
        func main()
        begin 
            return [1, 2, 3]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_program_255(self):
        """test statement: return keyword will be an error"""
        input = """
        func main()
            return func
        """
        expect = "Error on line 3 col 19: func"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_program_256(self):
        """test statement: return keyword will be an error"""
        input = """
        func main()
            return func()
        """
        expect = "Error on line 3 col 19: func"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_program_257(self):
        """test statement: return a function call"""
        input = """
        func main()
            return a()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_program_258(self):
        """test statement: return with some cases"""
        input = """
        func main()
            begin
                begin
                    begin
                        x <- 1
                    end
                    
                    begin
                        return true
                    end
                    
                    return false
                end
                
                begin
                end
                return true
            end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_program_259(self):
        """test statement"""
        input = """
        func main()
            begin
                a()[1] <- f()[1] + f()[2]
            end
        """
        expect = "Error on line 4 col 19: ["
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_program_260(self):
        """test statement"""
        input = """func main()
            begin
                number a <- a[1,2,3] * (1 > 2)
                for a until a > "YES" by 1
                    begin
                        if (x == "YES") continue
                        elif (x == "NO") return
                    end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_program_261(self):
        """test statement"""
        input = """
        func main()
            begin
                a <- f()[1]
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_program_262(self):
        """test statement"""
        input = """
        func main()
            begin
                a[1] <- f()[1]
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_program_263(self):
        """test with error token"""
        input = """func main() {
            return 1
        }
        """
        expect = "{"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_program_264(self):
        """test with error token"""
        input = """var a <- !1
        """
        expect = "!"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_program_265(self):
        """test with error token"""
        input = """string a = 'aaaa'
        """
        expect = "'"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_program_266(self):
        """test with error token"""
        input = """func main(1|2|3)
        """
        expect = "|"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_program_267(self):
        """test with error token"""
        input = """var a <- x = 2 ? 1 : 0
        """
        expect = "?"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_program_268(self):
        """test some source code"""
        input = """func main(int x)
        """
        expect = "Error on line 1 col 10: int"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_program_269(self):
        """test some source code"""
        input = """func main([])
            return 1
        """
        expect = "Error on line 1 col 10: ["
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_program_270(self):
        """test some source code"""
        input = """
        func isEven(number x)
            begin
                return x % 2 = 0
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_program_271(self):
        """test some source code"""
        input = """
        func isEven(number x)
            begin
                return x % 2 = 0
            end
        func main()
            begin
                a <- 10
                if (isEven(a)) print(a)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_program_272(self):
        """test some source code"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_program_273(self):
        """test some source code"""
        input = """
        func isEven(number x)
            begin
                return ## x % 2 == "0"
            end
        func main()
            begin 
                a <- 10
                if (isEven(a)) print(a)
            ## end
        """
        expect = "Error on line 11 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_program_274(self):
        """test some source code"""
        input = """
        func a()
            begin
                number a[12.e-13] <- [1,2,3]
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_program_275(self):
        """test some source code"""
        input = """

        ## bool c = false
        bool c <- false
        bool c[1,2,3]

        func main()
            begin
                print(c)
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_program_276(self):
        """test some source code"""
        input = """
        bool c = 10
        """
        expect = "Error on line 2 col 15: ="
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_program_277(self):
        """test some source code"""
        input = """
        func main()
            begin
                return c() ... "YES" == "YESS"
                return c() ... "YES" == "YESS"
                return c() ... "YES" == "YESS"
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_program_278(self):
        """test some source code"""
        input = """
        func a() return 1 ## 12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_program_279(self):
        """test some source code"""
        input = """
            number x <- x number x <- y
        """
        expect = "Error on line 2 col 26: number"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_program_280(self):
        """test some source code"""
        input = """
        func a()
        begin
        end
        
        func a()
        begin

            number x <- x
            
        end
        
        func a()
        begin 
        end
        func a() begin 
        end
        func a() begin 
        end
        func a() begin ## comment
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_program_281(self):
        """test some source code"""
        input = """
        func a()
        begin
            break continue
        end
        """
        expect = "Error on line 4 col 18: continue"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_program_282(self):
        """test some source code"""
        input = """
        func a()
        begin
            return 1 break
        end
        """
        expect = "Error on line 4 col 21: break"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_program_283(self):
        """test some source code"""
        input = """    
        func a()
        begin
            if (x <= 1) return false
            if (x <= 1)
                return false 
        end ## comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_program_284(self):
        """test some source code"""
        input = """    
        func a()
            fun()
        """
        expect = "Error on line 3 col 12: fun"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_program_285(self):
        """test some source code"""
        input = """
        func a()
            if (x <= 1) return false
        """
        expect = "Error on line 3 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_program_286(self):
        """test some source code"""
        input = """    
        func a()
            return if (x <= 1) return false
        """
        expect = "Error on line 3 col 19: if"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_program_287(self):
        """test some source code"""
        input = """    
        func a()
            return 
        var a <- []
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_program_288(self):
        """test some source code"""
        input = """    
        func a(number a[1+1])
        """
        expect = "Error on line 2 col 25: +"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_program_289(self):
        """test some source code"""
        input = """    
            var a <- a[1][1]
        """
        expect = "Error on line 2 col 25: ["
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_program_290(self):
        """test some source code"""
        input = """
        """
        expect = "Error on line 2 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_program_291(self):
        """test some source code"""
        input = """    
        func a()
            begin
                a[1][2] <- 1
            end
        """
        expect = "Error on line 4 col 20: ["
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_program_292(self):
        """test some source code"""
        input = """    
            var a <- [1,2,3][1]
        """
        expect = "Error on line 2 col 28: ["
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_program_293(self):
        """test some source code"""
        input = """    
            string a[1+1]
        """
        expect = "Error on line 2 col 22: +"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_program_294(self):
        """test some source code"""
        input = """    
        func a()
            begin a <- 1
            end
        """
        expect = "Error on line 3 col 18: a"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_program_295(self):
        """test some source code"""
        input = """    
        func a()
            begin
            end var c <- 1
        """
        expect = "Error on line 4 col 16: var"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_program_296(self):
        """test some source code"""
        input = """
        func a()
            begin
                c()[1] <- 1
            end
        """
        expect = "Error on line 4 col 19: ["
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_program_297(self):
        """test some source code"""
        input = """
        func a()
            begin
                c()[1] <- 1
            end
        """
        expect = "Error on line 4 col 19: ["
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_program_298(self):
        """test some source code"""
        input = """    
        func a()
            begin
                var c <- 1 var c <- 1
            end
        """
        expect = "Error on line 4 col 27: var"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_program_299(self):
        """test some source code"""
        input = """
        func isPrime(number x)
        func main()
            begin
                number x <- readNumber()
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_program_300(self):
        """test some source code"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))

