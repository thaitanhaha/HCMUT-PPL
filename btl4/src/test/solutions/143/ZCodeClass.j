.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ifle Label2
	iconst_1
	iconst_0
	iand
	goto Label4
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	ifle Label5
	iconst_1
	ifle Label2
	iconst_1
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
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iand
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
.limit stack 13
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
