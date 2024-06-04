.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static compareString(Ljava/lang/String;Ljava/lang/String;)Z
Label0:
.var 0 is a Ljava/lang/String; from Label0 to Label1
.var 1 is b Ljava/lang/String; from Label0 to Label1
	aload_0
	aload_1
	if_acmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ireturn
Label1:
	iconst_1
	ireturn
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "1.0"
	ldc "abc"
	invokestatic ZCodeClass/compareString(Ljava/lang/String;Ljava/lang/String;)Z
	invokestatic io/writeBool(Z)V
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
