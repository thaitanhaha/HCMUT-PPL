.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	ldc 1.0
	fstore_1
	fload_1
	invokestatic io/writeNumber(F)V
.var 2 is b Ljava/lang/String; from Label0 to Label1
	ldc "hi"
	astore_2
	aload_2
	invokestatic io/writeString(Ljava/lang/String;)V
.var 3 is c Z from Label0 to Label1
	iconst_1
	istore_3
	iload_3
	invokestatic io/writeBool(Z)V
Label1:
	return
.limit stack 2
.limit locals 4
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
