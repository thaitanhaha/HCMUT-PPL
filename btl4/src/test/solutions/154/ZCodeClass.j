.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	ldc 1.0
	fstore_1
.var 2 is b F from Label0 to Label1
	ldc 2.0
	fstore_2
.var 3 is for F from Label0 to Label1
	fload_1
	fstore_3
Label6:
	fload_1
	fload_2
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
	fload_1
	ldc 1.0
	fcmpl
	ifne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label7
Label13:
	fload_1
	invokestatic io/writeNumber(F)V
	goto Label5
Label14:
	goto Label10
Label7:
	fload_1
	ldc 2.0
	fcmpl
	ifne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label8
Label17:
	fload_1
	invokestatic io/writeNumber(F)V
	goto Label5
Label18:
	goto Label10
Label8:
	fload_1
	ldc 3.0
	fcmpl
	ifne Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label9
Label21:
	fload_1
	invokestatic io/writeNumber(F)V
	goto Label5
Label22:
	goto Label10
Label9:
	ldc "abc"
	invokestatic io/writeString(Ljava/lang/String;)V
Label10:
	goto Label4
Label4:
	fload_1
	ldc 1.0
	fadd
	fstore_1
	goto Label6
Label5:
	fload_3
	fstore_1
Label1:
	return
.limit stack 9
.limit locals 4
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
