.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static a()F
Label0:
.var 0 is a F from Label0 to Label1
	ldc 2.0
	fstore_0
	fload_0
	ldc 1.0
	fcmpl
	ifne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label2
Label7:
	ldc 3.0
	freturn
Label8:
Label2:
	fload_0
	ldc 2.0
	fcmpl
	ifne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label3
Label11:
	ldc 5.0
	freturn
Label12:
Label3:
Label13:
	ldc 4.0
	freturn
Label14:
Label4:
Label1:
	fconst_0
	freturn
.limit stack 5
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	invokestatic ZCodeClass/a()F
	fstore_1
	fload_1
	invokestatic io/writeNumber(F)V
Label1:
	return
.limit stack 1
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
