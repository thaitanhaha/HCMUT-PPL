.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static f(FF)F
Label0:
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
	fload_0
	fload_1
	fadd
	ldc 1.0
	fsub
	freturn
Label1:
	fconst_0
	freturn
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1.0
	ldc 2.0
	invokestatic ZCodeClass/f(FF)F
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 2
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
