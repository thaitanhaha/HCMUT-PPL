.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static b F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	ldc 2.0
	fneg
	fstore_1
	fload_1
	ldc 10.0
	getstatic ZCodeClass.b F
	fneg
	fmul
	fadd
	ldc 1.0
	fsub
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
	ldc 1.0
	fneg
	putstatic ZCodeClass.b F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
