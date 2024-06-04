.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

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
.var 3 is j F from Label7 to Label8
	ldc 0.0
	fstore_3
.var 4 is for F from Label7 to Label8
	fload_3
	fstore 4
Label13:
	fload_3
	ldc 10.0
	fcmpl
	ifne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label12
Label14:
	fload_3
	ldc 2.0
	fcmpl
	ifne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label16
	goto Label12
	goto Label17
Label16:
Label17:
	fload_3
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
	fload_1
	ldc 3.0
	fcmpl
	ifne Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label20
	goto Label5
	goto Label21
Label20:
Label21:
	fload_1
	invokestatic io/writeNumber(F)V
	ldc "\n"
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
Label1:
	return
.limit stack 9
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
