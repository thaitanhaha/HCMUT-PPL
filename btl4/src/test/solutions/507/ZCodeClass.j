.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static foo()F
Label0:
.var 0 is b F from Label0 to Label1
	ldc 1.0
	fstore_0
	fload_0
	ldc 2.0
	fcmpl
	ifge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label2
	ldc 10.0
	freturn
Label2:
	fload_0
	ldc 3.0
	fcmpl
	ifle Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
	ldc 11.0
	freturn
Label3:
	ldc 12.0
	freturn
Label4:
Label1:
	fconst_0
	freturn
.limit stack 5
.limit locals 1
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
