.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static y [[F

.method public static foo()[[F
Label0:
.var 0 is i F from Label0 to Label1
	ldc 0.0
	fstore_0
.var 1 is for F from Label0 to Label1
	fload_0
	fstore_1
Label6:
	fload_0
	ldc 10.0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
Label7:
	fload_0
	ldc 3.0
	fcmpl
	ifne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label9
	iconst_2
	iconst_2
	multianewarray [[F 2
	dup
	dup
	iconst_0
	aaload
	dup
	iconst_0
	fload_0
	fastore
	iconst_1
	fload_0
	fastore
	iconst_1
	aaload
	dup
	iconst_0
	fload_0
	fastore
	iconst_1
	fload_0
	fastore
	areturn
Label9:
Label10:
Label8:
Label4:
	fload_0
	ldc 1.0
	fadd
	fstore_0
	goto Label6
Label5:
	fload_1
	fstore_0
Label1:
	iconst_1
	iconst_1
	multianewarray [[F 2
	areturn
.limit stack 10
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x [[F from Label0 to Label1
	iconst_2
	iconst_2
	multianewarray [[F 2
	astore_1
	invokestatic ZCodeClass/foo()[[F
	astore_1
	invokestatic ZCodeClass/foo()[[F
	putstatic ZCodeClass.y [[F
	aload_1
	ldc 0.0
	f2i
	aaload
	ldc 0.0
	f2i
	faload
	getstatic ZCodeClass.y [[F
	ldc 1.0
	f2i
	aaload
	ldc 1.0
	f2i
	faload
	fadd
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
	iconst_2
	iconst_2
	multianewarray [[F 2
	putstatic ZCodeClass.y [[F
Label1:
	return
.limit stack 2
.limit locals 0
.end method
