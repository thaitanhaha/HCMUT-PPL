.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ifgt Label3
	iconst_1
	iconst_0
	ior
	goto Label4
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	ifgt Label6
	iconst_1
	ifgt Label3
	iconst_1
	iconst_0
	ior
	goto Label4
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	iconst_1
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ior
	goto Label7
Label6:
	iconst_1
	goto Label7
Label5:
	iconst_0
Label7:
	ifgt Label11
	iconst_1
	ifgt Label3
	iconst_1
	iconst_0
	ior
	goto Label4
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	ifgt Label6
	iconst_1
	ifgt Label3
	iconst_1
	iconst_0
	ior
	goto Label4
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	iconst_1
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ior
	goto Label7
Label6:
	iconst_1
	goto Label7
Label5:
	iconst_0
Label7:
	iconst_0
	ifgt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ior
	goto Label12
Label11:
	iconst_1
	goto Label12
Label10:
	iconst_0
Label12:
	ifgt Label16
	iconst_1
	ifgt Label3
	iconst_1
	iconst_0
	ior
	goto Label4
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	ifgt Label6
	iconst_1
	ifgt Label3
	iconst_1
	iconst_0
	ior
	goto Label4
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	iconst_1
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ior
	goto Label7
Label6:
	iconst_1
	goto Label7
Label5:
	iconst_0
Label7:
	ifgt Label11
	iconst_1
	ifgt Label3
	iconst_1
	iconst_0
	ior
	goto Label4
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	ifgt Label6
	iconst_1
	ifgt Label3
	iconst_1
	iconst_0
	ior
	goto Label4
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	iconst_1
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ior
	goto Label7
Label6:
	iconst_1
	goto Label7
Label5:
	iconst_0
Label7:
	iconst_0
	ifgt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ior
	goto Label12
Label11:
	iconst_1
	goto Label12
Label10:
	iconst_0
Label12:
	iconst_0
	ifgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifgt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ior
	goto Label17
Label16:
	iconst_1
	goto Label17
Label15:
	iconst_0
Label17:
	invokestatic io/writeBool(Z)V
Label1:
	return
.limit stack 30
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
