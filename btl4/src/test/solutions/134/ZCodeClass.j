.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static isPrime(F)Z
Label0:
.var 0 is n F from Label0 to Label1
	fload_0
	ldc 2.0
	fcmpl
	ifge Label4
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
.var 1 is i F from Label0 to Label1
	ldc 2.0
	fstore_1
.var 2 is for F from Label0 to Label1
	fload_1
	fstore_2
Label10:
	fload_1
	fload_1
	fmul
	fload_0
	fcmpl
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label9
	fload_0
	fload_1
	frem
	ldc 0.0
	fcmpl
	ifne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label11
	iconst_0
	ireturn
Label11:
Label12:
Label8:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label10
Label9:
	fload_2
	fstore_1
	iconst_1
	ireturn
Label1:
	iconst_1
	ireturn
.limit stack 12
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1.0
	invokestatic ZCodeClass/isPrime(F)Z
	invokestatic io/writeBool(Z)V
	ldc 2.0
	invokestatic ZCodeClass/isPrime(F)Z
	invokestatic io/writeBool(Z)V
	ldc 3.0
	invokestatic ZCodeClass/isPrime(F)Z
	invokestatic io/writeBool(Z)V
	ldc 4.0
	invokestatic ZCodeClass/isPrime(F)Z
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
