.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	ldc 1.0
	fstore_1
.var 2 is b Z from Label0 to Label1
	fload_1
	ldc 1.0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_2
	iload_2
	ifle Label4
	iload_2
	iconst_0
	iand
	goto Label6
Label5:
	iconst_1
	goto Label6
Label4:
	iconst_0
Label6:
	ifgt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	invokestatic io/writeBool(Z)V
Label1:
	return
.limit stack 10
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
