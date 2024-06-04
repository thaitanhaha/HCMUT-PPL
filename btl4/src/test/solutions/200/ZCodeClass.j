.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static add(F)F
Label0:
.var 0 is a F from Label0 to Label1
	fload_0
	ldc 5.0
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	ldc 1.0
	freturn
Label2:
	ldc 2.0
	freturn
Label3:
Label1:
	fconst_0
	freturn
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label0 to Label1
	ldc 6.0
	fstore_1
	fload_1
	invokestatic ZCodeClass/add(F)F
	invokestatic io/writeNumber(F)V
	fload_1
	ldc 5.0
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	ldc 1.0
	invokestatic io/writeNumber(F)V
	goto Label3
Label2:
	ldc 0.0
	invokestatic io/writeNumber(F)V
Label3:
Label1:
	return
.limit stack 3
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
