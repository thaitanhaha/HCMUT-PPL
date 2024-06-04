.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a F
.field static b [F
.field static c F

.method public static foo(F[F)F
Label0:
.var 0 is a F from Label0 to Label1
.var 1 is b [F from Label0 to Label1
	fload_0
	aload_1
	ldc 0.0
	f2i
	faload
	fadd
	aload_1
	ldc 1.0
	f2i
	faload
	fadd
	aload_1
	ldc 2.0
	f2i
	faload
	fadd
	freturn
Label1:
	fconst_0
	freturn
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic ZCodeClass.c F
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 1
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
	ldc 1.0
	putstatic ZCodeClass.a F
	iconst_3
	newarray float
	putstatic ZCodeClass.b [F
	getstatic ZCodeClass.b [F
	dup
	dup
	iconst_0
	getstatic ZCodeClass.a F
	fastore
	iconst_1
	getstatic ZCodeClass.a F
	fastore
	iconst_2
	getstatic ZCodeClass.a F
	fastore
	getstatic ZCodeClass.a F
	getstatic ZCodeClass.b [F
	invokestatic ZCodeClass/foo(F[F)F
	putstatic ZCodeClass.c F
Label1:
	return
.limit stack 7
.limit locals 0
.end method
