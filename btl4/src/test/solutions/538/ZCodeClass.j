.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [Ljava/lang/String; from Label0 to Label1
	bipush 7
	anewarray java/lang/String
	astore_1
	aload_1
	dup
	dup
	dup
	dup
	dup
	dup
	iconst_0
	ldc "t"
	aastore
	iconst_1
	ldc "h"
	aastore
	iconst_2
	ldc "a"
	aastore
	iconst_3
	ldc "i"
	aastore
	iconst_4
	ldc "t"
	aastore
	iconst_5
	ldc "a"
	aastore
	bipush 6
	ldc "n"
	aastore
.var 2 is i F from Label0 to Label1
	ldc 0.0
	fstore_2
.var 3 is b [Ljava/lang/String; from Label0 to Label1
	bipush 7
	anewarray java/lang/String
	astore_3
.var 4 is for F from Label0 to Label1
	fload_2
	fstore 4
Label6:
	fload_2
	ldc 7.0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
	aload_3
	fload_2
	f2i
	aload_1
	fload_2
	f2i
	aaload
	aastore
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
	ldc 0.0
	fstore_2
.var 5 is for F from Label0 to Label1
	fload_2
	fstore 5
Label11:
	fload_2
	ldc 7.0
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label10
Label12:
	aload_3
	fload_2
	f2i
	aaload
	invokestatic io/writeString(Ljava/lang/String;)V
Label13:
	goto Label9
Label9:
	fload_2
	ldc 1.0
	fadd
	fstore_2
	goto Label11
Label10:
	fload 5
	fstore_2
Label1:
	return
.limit stack 9
.limit locals 6
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
