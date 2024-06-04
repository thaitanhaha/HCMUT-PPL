.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a [F

.method public static foo()V
Label0:
	getstatic ZCodeClass.a [F
	ldc 0.0
	f2i
	ldc 1.0
	fastore
	getstatic ZCodeClass.a [F
	ldc 1.0
	f2i
	ldc 1.0
	fastore
.var 0 is i F from Label0 to Label1
	ldc 2.0
	fstore_0
.var 1 is for F from Label0 to Label1
	fload_0
	fstore_1
Label6:
	fload_0
	ldc 7.0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
	getstatic ZCodeClass.a [F
	fload_0
	f2i
	getstatic ZCodeClass.a [F
	fload_0
	ldc 1.0
	fsub
	f2i
	faload
	getstatic ZCodeClass.a [F
	fload_0
	ldc 2.0
	fsub
	f2i
	faload
	fadd
	fastore
	goto Label4
Label4:
	fload_0
	ldc 1.0
	fadd
	fstore_0
	goto Label6
Label5:
	fload_1
	fstore_0
	return
Label1:
	return
.limit stack 11
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic ZCodeClass/foo()V
.var 1 is i F from Label0 to Label1
	ldc 0.0
	fstore_1
.var 2 is for F from Label0 to Label1
	fload_1
	fstore_2
Label6:
	fload_1
	ldc 7.0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
Label7:
	getstatic ZCodeClass.a [F
	fload_1
	f2i
	faload
	invokestatic io/writeNumber(F)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
Label8:
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
	return
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
	bipush 7
	newarray float
	putstatic ZCodeClass.a [F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
