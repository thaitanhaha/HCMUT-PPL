.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static foo(F[F)V
Label0:
.var 0 is a F from Label0 to Label1
.var 1 is b [F from Label0 to Label1
.var 2 is c [F from Label0 to Label1
	iconst_3
	newarray float
	astore_2
	aload_2
	dup
	dup
	iconst_0
	ldc 1.0
	fastore
	iconst_1
	ldc 2.0
	fastore
	iconst_2
	ldc 3.0
	fastore
.var 3 is i F from Label0 to Label1
	ldc 0.0
	fstore_3
.var 4 is for F from Label0 to Label1
	fload_3
	fstore 4
Label6:
	fload_3
	ldc 3.0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
	aload_1
	fload_3
	f2i
	aload_2
	fload_3
	f2i
	faload
	fload_0
	fadd
	fastore
	goto Label4
Label4:
	fload_3
	ldc 1.0
	fadd
	fstore_3
	goto Label6
Label5:
	fload 4
	fstore_3
Label1:
	return
.limit stack 7
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [F from Label0 to Label1
	iconst_3
	newarray float
	astore_1
	aload_1
	dup
	dup
	iconst_0
	ldc 0.0
	fastore
	iconst_1
	ldc 0.0
	fastore
	iconst_2
	ldc 0.0
	fastore
	ldc 1.0
	aload_1
	invokestatic ZCodeClass/foo(F[F)V
	aload_1
	ldc 0.0
	f2i
	faload
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 5
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
