.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [Ljava/lang/String; from Label0 to Label1
	iconst_5
	anewarray java/lang/String
	astore_1
	aload_1
	dup
	dup
	dup
	dup
	iconst_0
	ldc "#####"
	aastore
	iconst_1
	ldc "####"
	aastore
	iconst_2
	ldc "###"
	aastore
	iconst_3
	ldc "##"
	aastore
	iconst_4
	ldc "#"
	aastore
.var 2 is i F from Label0 to Label1
	ldc 0.0
	fstore_2
.var 3 is result Ljava/lang/String; from Label0 to Label1
	ldc ""
	astore_3
.var 4 is for F from Label0 to Label1
	fload_2
	fstore 4
Label6:
	fload_2
	ldc 5.0
	fcmpl
	iflt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
	aload_3
	aload_1
	fload_2
	f2i
	aaload
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_3
	goto Label4
Label4:
	fload_2
	ldc 1.0
	fadd
	fstore_2
	goto Label6
Label5:
	fload 4
	fstore_2
	aload_3
	invokestatic io/writeString(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
.limit locals 5
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
