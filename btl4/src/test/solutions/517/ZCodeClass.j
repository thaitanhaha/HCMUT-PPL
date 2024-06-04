.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static areDivisors(FF)Z
Label0:
.var 0 is num1 F from Label0 to Label1
.var 1 is num2 F from Label0 to Label1
	fload_1
	fload_0
	frem
	ldc 0.0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label5
	fload_1
	fload_0
	frem
	ldc 0.0
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	fload_0
	fload_1
	frem
	ldc 0.0
	fcmpl
	ifne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ior
	goto Label6
Label5:
	iconst_1
	goto Label6
Label4:
	iconst_0
Label6:
	ireturn
Label1:
	iconst_1
	ireturn
.limit stack 8
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is num1 F from Label0 to Label1
	ldc 4.0
	fstore_1
.var 2 is num2 F from Label0 to Label1
	ldc 8.0
	fstore_2
	fload_1
	fload_2
	invokestatic ZCodeClass/areDivisors(FF)Z
	ifle Label2
	ldc "Yes"
	invokestatic io/writeString(Ljava/lang/String;)V
	goto Label3
Label2:
	ldc "No"
	invokestatic io/writeString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 2
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
