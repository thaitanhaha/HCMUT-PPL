.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static foo(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
Label0:
.var 0 is x Ljava/lang/String; from Label0 to Label1
.var 1 is y Ljava/lang/String; from Label0 to Label1
	aload_0
	aload_1
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	areturn
Label1:
	ldc "0"
	areturn
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "abc"
	ldc "abc"
	invokestatic ZCodeClass/foo(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
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
