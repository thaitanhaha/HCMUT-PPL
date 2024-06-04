.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	ldc 15.0
	fstore_1
.var 2 is b F from Label0 to Label1
	ldc 5.0
	fstore_2
	fload_1
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 1
.limit locals 3
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
	ldc 5.0
	putstatic ZCodeClass.a F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
