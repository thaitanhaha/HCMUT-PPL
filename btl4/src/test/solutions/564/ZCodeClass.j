.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static b F
.field static c F
.field static x Ljava/lang/String;

.method public static foo(F)F
Label0:
.var 0 is b F from Label0 to Label1
	ldc "tan"
	putstatic ZCodeClass.x Ljava/lang/String;
	fload_0
	freturn
Label1:
	fconst_0
	freturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic ZCodeClass.x Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
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
	ldc 2.0
	putstatic ZCodeClass.b F
	getstatic ZCodeClass.b F
	invokestatic ZCodeClass/foo(F)F
	putstatic ZCodeClass.c F
Label1:
	return
.limit stack 2
.limit locals 0
.end method
