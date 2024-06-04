.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [F from Label0 to Label1
	bipush 7
	newarray float
	astore_1
	aload_1
	ldc 0.0
	f2i
	ldc 1.0
	fastore
	aload_1
	ldc 1.0
	f2i
	ldc 1.0
	fastore
.var 2 is i F from Label0 to Label1
	ldc 2.0
	fstore_2
.var 3 is for F from Label0 to Label1
	fload_2
	fstore_3
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
	aload_1
	fload_2
	f2i
	aload_1
	fload_2
	ldc 1.0
	fsub
	f2i
	faload
	aload_1
	fload_2
	ldc 2.0
	fsub
	f2i
	faload
	fadd
	fastore
	goto Label4
Label4:
	fload_2
	ldc 1.0
	fadd
	fstore_2
	goto Label6
Label5:
	fload_3
	fstore_2
	ldc 0.0
	fstore_2
.var 4 is for F from Label0 to Label1
	fload_2
	fstore 4
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
	aload_1
	fload_2
	f2i
	faload
	invokestatic io/writeNumber(F)V
	ldc " "
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
	fload 4
	fstore_2
Label1:
	return
.limit stack 12
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
