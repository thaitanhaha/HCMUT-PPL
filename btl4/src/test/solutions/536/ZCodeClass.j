.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static foo(F)F
Label0:
.var 0 is a F from Label0 to Label1
.var 1 is i F from Label0 to Label1
	fload_0
	ldc 5.0
	frem
	fstore_1
.var 2 is for F from Label0 to Label1
	fload_1
	fstore_2
Label6:
	fload_1
	fload_0
	fcmpl
	iflt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
Label7:
	fload_1
	ldc 5.0
	fcmpl
	ifne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label9
	fload_1
	freturn
Label9:
Label10:
Label8:
Label4:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label6
Label5:
	fload_2
	fstore_1
Label1:
	fconst_0
	freturn
.limit stack 5
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	ldc 10.0
	fstore_1
	fload_1
	invokestatic ZCodeClass/foo(F)F
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
