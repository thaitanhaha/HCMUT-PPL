.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static foo()V
Label0:
	return
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public static a()V
Label0:
	iconst_1
	ifle Label2
	return
Label2:
Label3:
Label1:
	return
.limit stack 2
.limit locals 0
.end method

.method public static b()V
Label0:
.var 0 is i F from Label0 to Label1
	ldc 1.0
	fstore_0
.var 1 is for F from Label0 to Label1
	fload_0
	fstore_1
Label6:
	fload_0
	ldc 10.0
	fcmpl
	ifge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
	return
Label4:
	fload_0
	ldc 1.0
	fadd
	fstore_0
	goto Label6
Label5:
	fload_1
	fstore_0
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic ZCodeClass/foo()V
	invokestatic ZCodeClass/a()V
	invokestatic ZCodeClass/b()V
	return
Label1:
	return
.limit stack 0
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
