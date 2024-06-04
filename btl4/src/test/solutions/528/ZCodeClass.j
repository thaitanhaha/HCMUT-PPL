.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a [[F

.method public static foo()[[F
Label0:
	iconst_1
	iconst_3
	multianewarray [[F 2
	dup
	putstatic ZCodeClass.a [[F
	iconst_0
	aaload
	dup
	dup
	iconst_0
	ldc 10.0
	fastore
	iconst_1
	ldc 20.0
	fastore
	iconst_2
	ldc 30.0
	fastore
	getstatic ZCodeClass.a [[F
	areturn
Label1:
	iconst_1
	iconst_1
	multianewarray [[F 2
	areturn
.limit stack 6
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x F from Label0 to Label1
	invokestatic ZCodeClass/foo()[[F
	ldc 0.0
	f2i
	aaload
	ldc 2.0
	f2i
	faload
	fstore_1
	fload_1
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LZCodeClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_1
	iconst_3
	multianewarray [[F 2
	putstatic ZCodeClass.a [[F
Label1:
	return
.limit stack 2
.limit locals 0
.end method
