.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static x [F

.method public static foo()V
Label0:
	iconst_3
	newarray float
	dup
	putstatic ZCodeClass.x [F
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
Label1:
	return
.limit stack 6
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic ZCodeClass/foo()V
	getstatic ZCodeClass.x [F
	ldc 0.0
	f2i
	faload
	ldc 10.0
	fmul
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 2
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
	iconst_3
	newarray float
	putstatic ZCodeClass.x [F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
