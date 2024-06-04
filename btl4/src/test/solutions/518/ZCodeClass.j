.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static isPrime(F)Z
Label0:
.var 0 is x F from Label0 to Label1
	fload_0
	ldc 1.0
	fcmpl
	ifgt Label4
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
	fload_0
	ldc 2.0
	fdiv
	fcmpl
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label9
Label11:
	fload_0
	fload_1
	frem
	ldc 0.0
	fcmpl
	ifne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label13
	iconst_0
	ireturn
Label13:
Label14:
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
.var 1 is x F from Label0 to Label1
	ldc 5.0
	fstore_1
	fload_1
	invokestatic ZCodeClass/isPrime(F)Z
	ifle Label2
	ldc "Yes"
	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label3
Label2:
	ldc "No"
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
