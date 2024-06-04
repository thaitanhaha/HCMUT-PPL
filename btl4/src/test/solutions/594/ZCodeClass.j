.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static a [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "GenG"
	getstatic ZCodeClass.a [Ljava/lang/String;
	ldc 0.0
	f2i
	aaload
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
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
	iconst_1
	anewarray java/lang/String
	putstatic ZCodeClass.a [Ljava/lang/String;
	getstatic ZCodeClass.a [Ljava/lang/String;
	iconst_0
	ldc "1"
	aastore
Label1:
	return
.limit stack 4
.limit locals 0
.end method
