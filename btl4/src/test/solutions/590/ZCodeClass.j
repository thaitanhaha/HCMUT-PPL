.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a Z from Label0 to Label1
	iconst_1
	istore_1
	iload_1
	ifle Label2
	iload_1
	iconst_0
	iand
	goto Label4
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	ifgt Label6
	iload_1
	ifle Label2
	iload_1
	iconst_0
	iand
	goto Label4
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	iconst_1
	ifgt Label9
	iconst_1
	iconst_0
	ior
	goto Label10
Label9:
	iconst_1
	goto Label10
Label8:
	iconst_0
Label10:
	ior
	goto Label7
Label6:
	iconst_1
	goto Label7
Label5:
	iconst_0
Label7:
	invokestatic io/writeBool(Z)V
Label1:
	return
.limit stack 14
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
