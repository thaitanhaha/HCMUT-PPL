.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static foo()F
Label0:
.var 0 is i F from Label0 to Label1
	ldc 0.0
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
Label7:
	fload_0
	ldc 10.0
	fcmpl
	ifne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label9
	ldc 10.0
	freturn
Label9:
	fload_0
	ldc 8.0
	fcmpl
	ifne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label10
	goto Label5
	goto Label11
Label10:
Label11:
Label8:
	goto Label4
Label4:
	fload_0
	ldc 1.0
	fadd
	fstore_0
	goto Label6
Label5:
	fload_1
	fstore_0
	fload_0
	freturn
Label1:
	fconst_0
	freturn
.limit stack 7
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	invokestatic ZCodeClass/foo()F
	fstore_1
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
