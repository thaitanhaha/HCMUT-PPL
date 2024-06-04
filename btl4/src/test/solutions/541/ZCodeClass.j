.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static foo()Z
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
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
	fload_0
	ldc 1.0
	fcmpl
	ifne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label7
	iconst_1
	ireturn
Label7:
Label8:
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
	iconst_1
	ireturn
.limit stack 6
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic ZCodeClass/foo()Z
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
