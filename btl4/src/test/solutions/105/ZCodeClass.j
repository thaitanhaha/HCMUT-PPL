.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1.0
	ldc 2.0
	ldc 9.0
	fmul
	fadd
	ldc 19.0
	ldc 67.0
	frem
	ldc 88.0
	fdiv
	fsub
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 3
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
