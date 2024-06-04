.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static foo([F)F
Label0:
.var 0 is y [F from Label0 to Label1
.var 1 is x [F from Label0 to Label1
	iconst_3
	newarray float
	astore_1
	iconst_3
	newarray float
	dup
	astore_1
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
.var 2 is i F from Label0 to Label1
	ldc 0.0
	fstore_2
.var 3 is sum F from Label0 to Label1
	ldc 0.0
	fstore_3
.var 4 is for F from Label0 to Label1
	fload_2
	fstore 4
Label6:
	fload_2
	ldc 3.0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
Label7:
	aload_1
	fload_2
	f2i
	aload_0
	ldc 3.0
	fload_2
	fsub
	ldc 1.0
	fsub
	f2i
	faload
	fastore
	fload_3
	aload_1
	fload_2
	f2i
	faload
	fadd
	fstore_3
Label8:
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
	fload_3
	fload_2
	fadd
	freturn
Label1:
	fconst_0
	freturn
.limit stack 8
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	newarray float
	dup
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
	invokestatic ZCodeClass/foo([F)F
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 7
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
