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
	ldc 12.0
	fcmpl
	ifne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label9
	fload_0
	freturn
Label9:
Label10:
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
	fload_0
	freturn
Label1:
	fconst_0
	freturn
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	invokestatic ZCodeClass/foo()F
	invokestatic ZCodeClass/foo()F
	fadd
	invokestatic ZCodeClass/foo()F
	fadd
	invokestatic ZCodeClass/foo()F
	ldc 1.0
	fmul
	fadd
	ldc 1.0
	fadd
	fstore_1
	fload_1
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 3
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
