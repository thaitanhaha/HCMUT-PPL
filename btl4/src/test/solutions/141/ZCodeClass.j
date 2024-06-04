.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static factorial(F)F
Label0:
.var 0 is n F from Label0 to Label1
	fload_0
	ldc 0.0
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	ldc 1.0
	freturn
Label2:
Label3:
.var 1 is i F from Label0 to Label1
	ldc 1.0
	fstore_1
.var 2 is sum F from Label0 to Label1
	ldc 1.0
	fstore_2
.var 3 is for F from Label0 to Label1
	fload_1
	fstore_3
Label10:
	fload_1
	fload_0
	fcmpl
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label9
	fload_2
	fload_1
	fmul
	fstore_2
	goto Label8
Label8:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label10
Label9:
	fload_3
	fstore_1
	fload_2
	freturn
Label1:
	fconst_0
	freturn
.limit stack 6
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 5.0
	invokestatic ZCodeClass/factorial(F)F
	invokestatic io/writeNumber(F)V
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
