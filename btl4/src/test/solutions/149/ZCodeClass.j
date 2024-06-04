.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b F from Label0 to Label1
	ldc 3.0
	fstore_1
	fload_1
	ldc 2.0
	fcmpl
	ifne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label2
	ldc 1.0
	invokestatic io/writeNumber(F)V
	goto Label4
Label2:
	fload_1
	ldc 3.0
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
	ldc "abc"
	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label4
Label3:
	ldc 2.0
	invokestatic io/writeNumber(F)V
Label4:
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
