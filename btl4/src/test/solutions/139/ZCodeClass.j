.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static isOdd(F)Z
Label0:
.var 0 is n F from Label0 to Label1
	fload_0
	ldc 2.0
	frem
	ldc 0.0
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	iconst_0
	ireturn
Label2:
Label3:
	iconst_1
	ireturn
Label1:
	iconst_1
	ireturn
.limit stack 6
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1.0
	invokestatic ZCodeClass/isOdd(F)Z
	invokestatic io/writeBool(Z)V
Label1:
	return
.limit stack 1
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
