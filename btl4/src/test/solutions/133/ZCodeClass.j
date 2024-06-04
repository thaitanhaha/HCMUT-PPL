.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static sum(FF)F
Label0:
.var 0 is i F from Label0 to Label1
.var 1 is j F from Label0 to Label1
.var 2 is sum F from Label0 to Label1
	ldc 0.0
	fstore_2
.var 3 is for F from Label0 to Label1
	fload_0
	fstore_3
Label6:
	fload_0
	fload_1
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
	fload_2
	fload_0
	fadd
	fstore_2
	goto Label4
Label4:
	fload_0
	ldc 1.0
	fadd
	fstore_0
	goto Label6
Label5:
	fload_3
	fstore_0
	fload_2
	freturn
Label1:
	fconst_0
	freturn
.limit stack 4
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1.0
	ldc 10.0
	invokestatic ZCodeClass/sum(FF)F
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 2
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
