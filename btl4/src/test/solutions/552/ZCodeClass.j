.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [Z from Label0 to Label1
	iconst_3
	newarray boolean
	astore_1
	aload_1
	dup
	dup
	iconst_0
	iconst_1
	bastore
	iconst_1
	iconst_0
	bastore
	iconst_2
	iconst_0
	bastore
	aload_1
	ldc 0.0
	f2i
	baload
	invokestatic io/writeBool(Z)V
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
