# ZCode language

## Introduction
This is the assignment of Principle of Programming Language Course at HCMUT. The main task of the assignment is to create a compiler for a new language named ZCode. This big assignment is divided into 4 smaller assignments. 

## Assignment 1
Use ANTLR tool to make Parser, Lexer. 
+ [ZCode.g4](btl1/ZCode.g4)

Use python *unittest* to make testcases.
+ [LexerSuite.py](btl1/LexerSuite.py)
+ [ParserSuite.py](btl1/ParserSuite.py)
  
**Result:** 
+ Parser: 100/100
+ Lexer: 96/100

## Assignment 2
Use the result of Parser and Lexer from assignment 1 to create abstract syntax tree (AST). 
+ [ZCode.g4](btl2/ZCode.g4)
+ [ASTGeneration.py](btl2/ASTGeneration.py)
  
Use python *unittest* to make testcases.
+ [ASTGenSuite.py](btl2/ASTGenSuite.py)
  
**Result:** 100/100

## Assignment 3
Use the result of AST from assignment 2 to create static check.
+ [StaticCheck.py](btl3/StaticCheck.py)
  
Use python *unittest* to make testcases.
+ [CheckSuite.py](btl3/CheckSuite.py)
  
**Result:** 94/100

## Assignment 4
Use the result of AST from assignment 2 to generate Jasmin code, the Jasmin code then is transfered to Java bytecode which must be run correctly in a Java
Virtual Machine (JVM). 
+ [CodeGenerator.py](btl4/src/main/zcode/codegen/CodeGenerator.py)
+ [Emitter.py](btl4/src/main/zcode/codegen/Emitter.py)
  
Use python *unittest* to make testcases.
+ [CodeGenSuite.py](btl4/src/test/CodeGenSuite.py)
  
**Result:** 69/100
