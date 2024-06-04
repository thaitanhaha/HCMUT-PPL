.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static foo()[[F
Label0:
.var 0 is i F from Label0 to Label1
	ldc 0.0
	fstore_0
.var 1 is a [[F from Label0 to Label1
	iconst_2
	iconst_3
	multianewarray [[F 2
	astore_1
.var 2 is for F from Label0 to Label1
	fload_0
	fstore_2
Label6:
	fload_0
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
.var 3 is j F from Label7 to Label8
	ldc 0.0
	fstore_3
.var 4 is for F from Label7 to Label8
	fload_3
	fstore 4
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
	aload_1
	fload_0
	f2i
	aaload
	fload_3
	f2i
	fload_0
	fload_3
	fmul
	fastore
	goto Label11
Label11:
	fload_3
	ldc 1.0
	fadd
	fstore_3
	goto Label13
Label12:
	fload 4
	fstore_3
Label8:
	goto Label4
Label4:
	fload_0
	ldc 1.0
	fadd
	fstore_0
	goto Label6
Label5:
	fload_2
	fstore_0
	aload_1
	areturn
Label1:
	iconst_1
	iconst_1
	multianewarray [[F 2
	areturn
.limit stack 9
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i F from Label0 to Label1
	ldc 0.0
	fstore_1
.var 2 is for F from Label0 to Label1
	fload_1
	fstore_2
Label6:
	fload_1
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
.var 3 is j F from Label7 to Label8
	ldc 0.0
	fstore_3
.var 4 is for F from Label7 to Label8
	fload_3
	fstore 4
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
	invokestatic ZCodeClass/foo()[[F
	fload_1
	f2i
	aaload
	fload_3
	f2i
	faload
	invokestatic io/writeNumber(F)V
	ldc " "
	invokestatic io/writeString(Ljava/lang/String;)V
Label15:
	goto Label11
Label11:
	fload_3
	ldc 1.0
	fadd
	fstore_3
	goto Label13
Label12:
	fload 4
	fstore_3
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
Label1:
	return
.limit stack 7
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
