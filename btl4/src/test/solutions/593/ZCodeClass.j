.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [[[F from Label0 to Label1
	iconst_2
	iconst_2
	iconst_2
	multianewarray [[[F 3
	astore_1
	aload_1
	dup
	iconst_0
	aaload
	dup
	iconst_0
	aaload
	dup
	iconst_0
	ldc 1.0
	fastore
	iconst_1
	ldc 2.0
	fastore
	iconst_1
	aaload
	dup
	iconst_0
	ldc 3.0
	fastore
	iconst_1
	ldc 4.0
	fastore
	iconst_1
	aaload
	dup
	iconst_0
	aaload
	dup
	iconst_0
	ldc 1.0
	fastore
	iconst_1
	ldc 1.0
	fastore
	iconst_1
	aaload
	dup
	iconst_0
	ldc 1.0
	fastore
	iconst_1
	ldc 1.0
	fastore
	aload_1
	ldc 0.0
	f2i
	aaload
	ldc 1.0
	f2i
	aaload
	ldc 1.0
	f2i
	faload
	invokestatic io/writeNumber(F)V
	return
Label1:
	return
.limit stack 6
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
