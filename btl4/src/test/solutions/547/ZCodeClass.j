.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a [F

.method public static sum_1([F)F
Label0:
.var 0 is b [F from Label0 to Label1
.var 1 is i F from Label0 to Label1
	ldc 0.0
	fstore_1
.var 2 is for F from Label0 to Label1
	fload_1
	fstore_2
Label6:
	fload_1
	ldc 3.0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
	aload_0
	fload_1
	f2i
	aload_0
	fload_1
	f2i
	faload
	ldc 1.0
	fadd
	fastore
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
.var 3 is sum F from Label0 to Label1
	ldc 0.0
	fstore_3
	ldc 0.0
	fstore_1
.var 4 is for F from Label0 to Label1
	fload_1
	fstore 4
Label11:
	fload_1
	ldc 3.0
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label10
	fload_3
	aload_0
	fload_1
	f2i
	faload
	fadd
	fstore_3
	goto Label9
Label9:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label11
Label10:
	fload 4
	fstore_1
	fload_3
	freturn
Label1:
	fconst_0
	freturn
.limit stack 9
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic ZCodeClass.a [F
	invokestatic ZCodeClass/sum_1([F)F
	invokestatic io/writeNumber(F)V
.var 1 is i F from Label0 to Label1
	ldc 0.0
	fstore_1
.var 2 is for F from Label0 to Label1
	fload_1
	fstore_2
Label6:
	fload_1
	ldc 3.0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
	getstatic ZCodeClass.a [F
	fload_1
	f2i
	faload
	invokestatic io/writeNumber(F)V
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
Label1:
	return
.limit stack 4
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
	iconst_3
	newarray float
	putstatic ZCodeClass.a [F
	getstatic ZCodeClass.a [F
	dup
	dup
	iconst_0
	ldc 1.0
	fastore
	iconst_1
	ldc 1.0
	fastore
	iconst_2
	ldc 1.0
	fastore
Label1:
	return
.limit stack 6
.limit locals 0
.end method
