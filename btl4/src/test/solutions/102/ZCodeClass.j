.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a F
.field static c F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b F from Label0 to Label1
	ldc 3.0
	fstore_1
	getstatic ZCodeClass.a F
	invokestatic io/writeNumber(F)V
	getstatic ZCodeClass.c F
	invokestatic io/writeNumber(F)V
	fload_1
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 1
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
	putstatic ZCodeClass.a F
	ldc 2.0
	putstatic ZCodeClass.c F
Label1:
	return
.limit stack 2
.limit locals 0
.end method
