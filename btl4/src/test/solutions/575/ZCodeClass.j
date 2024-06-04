.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a [[F
.field static b [[F

.method public static foo()[[F
Label0:
	iconst_2
	iconst_3
	multianewarray [[F 2
	dup
	dup
	iconst_0
	aaload
	dup
	dup
	iconst_0
	getstatic ZCodeClass.a [[F
	ldc 0.0
	f2i
	aaload
	ldc 0.0
	f2i
	faload
	fastore
	iconst_1
	getstatic ZCodeClass.a [[F
	ldc 0.0
	f2i
	aaload
	ldc 1.0
	f2i
	faload
	fastore
	iconst_2
	getstatic ZCodeClass.a [[F
	ldc 0.0
	f2i
	aaload
	ldc 2.0
	f2i
	faload
	fastore
	iconst_1
	aaload
	dup
	dup
	iconst_0
	getstatic ZCodeClass.a [[F
	ldc 1.0
	f2i
	aaload
	ldc 0.0
	f2i
	faload
	fastore
	iconst_1
	getstatic ZCodeClass.a [[F
	ldc 1.0
	f2i
	aaload
	ldc 1.0
	f2i
	faload
	fastore
	iconst_2
	getstatic ZCodeClass.a [[F
	ldc 1.0
	f2i
	aaload
	ldc 2.0
	f2i
	faload
	fastore
	areturn
Label1:
	iconst_1
	iconst_1
	multianewarray [[F 2
	areturn
.limit stack 9
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic ZCodeClass/foo()[[F
	putstatic ZCodeClass.b [[F
	getstatic ZCodeClass.b [[F
	ldc 0.0
	f2i
	aaload
	ldc 0.0
	f2i
	ldc 10.0
	fastore
	getstatic ZCodeClass.a [[F
	ldc 0.0
	f2i
	aaload
	ldc 0.0
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 6
.limit locals 1
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
	iconst_2
	iconst_3
	multianewarray [[F 2
	putstatic ZCodeClass.a [[F
	getstatic ZCodeClass.a [[F
	dup
	iconst_0
	aaload
	dup
	dup
	iconst_0
	ldc 1.0
	fastore
	iconst_1
	ldc 2.0
	fastore
	iconst_2
	ldc 3.0
	fastore
	iconst_1
	aaload
	dup
	dup
	iconst_0
	ldc 4.0
	fastore
	iconst_1
	ldc 5.0
	fastore
	iconst_2
	ldc 6.0
	fastore
	iconst_3
	iconst_2
	multianewarray [[F 2
	putstatic ZCodeClass.b [[F
Label1:
	return
.limit stack 7
.limit locals 0
.end method
