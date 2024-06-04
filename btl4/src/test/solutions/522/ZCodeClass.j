.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [[Ljava/lang/String; from Label0 to Label1
	iconst_2
	iconst_2
	multianewarray [[Ljava/lang/String; 2
	astore_1
	aload_1
	dup
	iconst_0
	aaload
	dup
	iconst_0
	ldc "a"
	aastore
	iconst_1
	ldc "b"
	aastore
	iconst_1
	aaload
	dup
	iconst_0
	ldc "c"
	aastore
	iconst_1
	ldc "d"
	aastore
.var 2 is b [[Ljava/lang/String; from Label0 to Label1
	iconst_2
	iconst_2
	multianewarray [[Ljava/lang/String; 2
	astore_2
	aload_2
	dup
	iconst_0
	aaload
	dup
	iconst_0
	aload_1
	ldc 0.0
	f2i
	aaload
	ldc 0.0
	f2i
	aaload
	aastore
	iconst_1
	aload_1
	ldc 0.0
	f2i
	aaload
	ldc 1.0
	f2i
	aaload
	aastore
	iconst_1
	aaload
	dup
	iconst_0
	aload_1
	ldc 1.0
	f2i
	aaload
	ldc 0.0
	f2i
	aaload
	aastore
	iconst_1
	aload_1
	ldc 1.0
	f2i
	aaload
	ldc 1.0
	f2i
	aaload
	aastore
	aload_2
	ldc 0.0
	f2i
	aaload
	ldc 0.0
	f2i
	aaload
	aload_2
	ldc 0.0
	f2i
	aaload
	ldc 1.0
	f2i
	aaload
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aload_2
	ldc 1.0
	f2i
	aaload
	ldc 0.0
	f2i
	aaload
	aload_2
	ldc 1.0
	f2i
	aaload
	ldc 1.0
	f2i
	aaload
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/writeString(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
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
