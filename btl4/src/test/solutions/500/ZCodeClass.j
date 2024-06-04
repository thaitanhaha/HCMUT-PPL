.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1.0
	invokestatic io/writeNumber(F)V
	iconst_1
	invokestatic io/writeBool(Z)V
	ldc "abc"
	invokestatic io/writeString(Ljava/lang/String;)V
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
	ldc 2.0
	putstatic ZCodeClass.a F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
