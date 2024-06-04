.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a Ljava/lang/String; from Label0 to Label1
	ldc "a"
	astore_1
.var 2 is b Ljava/lang/String; from Label0 to Label1
	ldc "b"
	astore_2
.var 3 is c Ljava/lang/String; from Label0 to Label1
	ldc "0"
	astore_3
	aload_1
	aload_2
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_3
	aload_3
	invokestatic io/writeString(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
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
