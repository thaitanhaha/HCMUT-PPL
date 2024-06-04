.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i F from Label0 to Label1
	ldc 0.0
	fstore_1
.var 2 is for F from Label0 to Label1
	fload_1
	fstore_2
Label6:
	fload_1
	ldc 10.0
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
Label7:
	fload_1
	invokestatic io/writeNumber(F)V
.var 3 is for F from Label7 to Label8
	fload_1
	fstore_3
Label13:
	fload_1
	ldc 10.0
	fcmpl
	ifle Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label12
	goto Label11
	goto Label11
Label11:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label13
Label12:
	fload_3
	fstore_1
Label8:
	goto Label4
Label4:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label6
Label5:
	fload_2
	fstore_1
	fload_1
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 6
.limit locals 4
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
