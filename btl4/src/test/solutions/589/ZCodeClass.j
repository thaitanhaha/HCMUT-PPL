.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object
.field static x [[Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic ZCodeClass.x [[Z
	ldc 0.0
	f2i
	aaload
	ldc 0.0
	f2i
	baload
	invokestatic io/writeBool(Z)V
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
	iconst_2
	iconst_2
	multianewarray [[Z 2
	putstatic ZCodeClass.x [[Z
	getstatic ZCodeClass.x [[Z
	dup
	iconst_0
	aaload
	dup
	iconst_0
	iconst_1
	bastore
	iconst_1
	iconst_1
	bastore
	iconst_1
	aaload
	dup
	iconst_0
	iconst_0
	bastore
	iconst_1
	iconst_0
	bastore
Label1:
	return
.limit stack 8
.limit locals 0
.end method
