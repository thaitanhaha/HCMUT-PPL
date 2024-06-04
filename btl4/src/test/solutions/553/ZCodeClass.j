.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [Z from Label0 to Label1
	iconst_2
	newarray boolean
	astore_1
	aload_1
	dup
	iconst_0
	iconst_1
	bastore
	iconst_1
	iconst_0
	bastore
.var 2 is b [F from Label0 to Label1
	iconst_2
	newarray float
	astore_2
	aload_2
	dup
	iconst_0
	ldc 1.0
	fastore
	iconst_1
	ldc 2.0
	fastore
	aload_1
	ldc 0.0
	f2i
	baload
	ifle Label2
	aload_2
	ldc 0.0
	f2i
	faload
	invokestatic io/writeNumber(F)V
	goto Label4
Label2:
	aload_1
	ldc 1.0
	f2i
	baload
	ifle Label3
	aload_2
	ldc 1.0
	f2i
	faload
	invokestatic io/writeNumber(F)V
	goto Label4
Label3:
	ldc "tan"
	invokestatic io/writeString(Ljava/lang/String;)V
Label4:
Label1:
	return
.limit stack 6
.limit locals 3
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
