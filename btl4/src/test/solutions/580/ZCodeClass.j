.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static foo([[F)F
Label0:
.var 0 is y [[F from Label0 to Label1
.var 1 is x [[F from Label0 to Label1
	iconst_2
	iconst_3
	multianewarray [[F 2
	astore_1
	iconst_2
	iconst_3
	multianewarray [[F 2
	dup
	astore_1
	dup
	iconst_0
	aaload
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
	iconst_1
	aaload
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
.var 3 is j F from Label0 to Label1
	ldc 0.0
	fstore_3
.var 4 is sum F from Label0 to Label1
	ldc 0.0
	fstore 4
.var 5 is for F from Label0 to Label1
	fload_2
	fstore 5
Label6:
	fload_2
	ldc 2.0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
Label7:
.var 6 is for F from Label7 to Label8
	fload_3
	fstore 6
Label13:
	fload_3
	ldc 3.0
	fcmpl
	ifne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label12
Label14:
	aload_1
	fload_2
	f2i
	aaload
	fload_3
	f2i
	aload_0
	fload_2
	f2i
	aaload
	ldc 3.0
	fload_3
	fsub
	ldc 1.0
	fsub
	f2i
	faload
	fastore
	fload 4
	aload_1
	fload_2
	f2i
	aaload
	fload_3
	f2i
	faload
	fadd
	fstore 4
Label15:
	goto Label11
Label11:
	fload_3
	ldc 1.0
	fadd
	fstore_3
	goto Label13
Label12:
	fload 6
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
	fload 5
	fstore_2
	fload 4
	fload_2
	fadd
	fload_3
	fadd
	freturn
Label1:
	fconst_0
	freturn
.limit stack 12
.limit locals 7
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	iconst_3
	multianewarray [[F 2
	dup
	dup
	iconst_0
	aaload
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
	iconst_1
	aaload
	dup
	dup
	iconst_0
	ldc 4.0
	fastore
	iconst_1
	ldc 5.0
	fastore
	iconst_2
	ldc 6.0
	fastore
	invokestatic ZCodeClass/foo([[F)F
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 9
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
