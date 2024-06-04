from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class Symbol:
    def __init__(self, name, mtype, params=None, is_defined=False, is_void=False):
        self.name = name
        self.mtype = mtype
        self.params = params
        self.is_defined = is_defined
        self.is_void = is_void

    def __str__(self):
        if self.params is not None:
            return "Symbol("+self.name+","+str(self.mtype)+","+str(self.params)+","+str(self.is_defined)+")"
        else:
            return "Symbol("+self.name+","+str(self.mtype)+")"

class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
            Symbol("readNumber", NumberType(), [], True),
            Symbol("writeNumber", VoidType(), [Symbol("anArg", NumberType())], True),
            Symbol("readBool", BoolType(), [], True),
            Symbol("writeBool", VoidType(), [Symbol("anArg", BoolType())], True),
            Symbol("readString", StringType(), [], True),
            Symbol("writeString", VoidType(), [Symbol("anArg", StringType())], True),
        ]

    def check(self):
        return self.visit(self.ast, None)
    
    def get_kind(self, ast):
        return Function() if type(ast) == FuncDecl else Variable()

    def infer(self, env, name, mtype, for_function=False):
        for symbol_list in env:
            for symbol in symbol_list:
                if symbol.name == name:
                    if for_function == False:
                        if symbol.params is None:
                            symbol.mtype = mtype
                            return mtype
                    else:
                        if symbol.params is not None:
                            symbol.mtype = mtype
                            return mtype
                
    def print_to_debug(self, o):
        print("[",end="\n")
        for symbol_list in o:
            print("\t[",end="")
            for symbol in symbol_list:
                print(symbol,end=" ")
            print("]",end="\n")
        print("]")

    def visitNumberType(self, ast, o):
        return NumberType()
    
    def visitBoolType(self, ast, o):
        return BoolType()
    
    def visitStringType(self, ast, o):
        return StringType()
    
    def visitArrayType(self, ast, o):
        return ArrayType(ast.size, ast.eleType)
    
    def visitVoidType(self, ast, o):
        return VoidType()
    
    def visitNumberLiteral(self, ast, o):
        return NumberType()
    
    def visitStringLiteral(self, ast, o):
        return StringType()
    
    def visitBooleanLiteral(self, ast, o):
        return BoolType()

    def visitProgram(self, ast, o):
        global_scope = [[]]
        for built_in_func in self.global_envi:
            global_scope[0] += [built_in_func]

        env = global_scope
        for decl in ast.decl:
            self.visit(decl, env)
                        
        main_flag = False
        all_func = {}
        for decl in env[0]:
            if decl.params is not None:
                all_func.update({decl.name: decl.is_defined})
            if decl.name == "main" and type(decl.mtype) is VoidType and decl.params == []:
                main_flag = True
        self.print_to_debug(env)
        for key, value in all_func.items():
            if value == False:
                raise NoDefinition(key)
        if not main_flag:
            raise NoEntryPoint()

    def visitVarDecl(self, ast, o, is_param=False, is_check_same_param=False):
        for symbol in o[0]:
            if symbol.name == ast.name.name and symbol.params is None:
                if is_param == False:
                    raise Redeclared(Variable(), ast.name.name)
                else:
                    if is_check_same_param:
                        raise Redeclared(Parameter(), ast.name.name)

        if ast.varInit is None:
            if ast.modifier == "var":
                raise TypeCannotBeInferred(ast)
        o[0] += [Symbol(ast.name.name, None)]
        
        if ast.varInit is None: 
            o[0][-1] = Symbol(ast.name.name, ast.varType)
        else:
            initType = self.visit(ast.varInit, o)
            # Implicit Conversion
            if type(initType) is ArrayType and type(ast.varType) is ArrayType:
                if len(initType.size) < len(ast.varType.size):
                    temp = []
                    if initType.eleType is None:
                        for i in range(0, len(initType.size)):
                            if int(initType.size[i]) != int(ast.varType.size[i]):
                                raise TypeMismatchInStatement(ast)
                        for i in range(len(ast.varType.size) - len(initType.size), len(ast.varType.size)):
                            temp.append(ast.varType.size[i])
                        # initType = self.visitArrayLiteral(ast.varInit, o, ArrayType(temp, ast.varType.eleType))
                        # initType = self.visitArrayLiteral(ast.varInit, o, ast.varType)
                        initType = self.visitArrayLiteral(ast.varInit, o, ArrayType(temp, ast.varType.eleType))
                    else:
                        raise TypeMismatchInStatement(ast)    
                elif len(initType.size) > len(ast.varType.size):
                    raise TypeMismatchInStatement(ast)
                else:
                    for i in range(0, len(initType.size)):
                        if int(initType.size[i]) != int(ast.varType.size[i]):
                            raise TypeMismatchInStatement(ast)
                    if initType.eleType is None:
                        initType = self.visitArrayLiteral(ast.varInit, o, ast.varType.eleType)
                if type(initType.eleType) is not type(ast.varType.eleType) and initType.eleType is not None:
                    if not (type(initType.eleType) is NumberType and type(ast.varType.eleType) is NumberType): 
                        # print(2222222)
                        raise TypeMismatchInStatement(ast)
                if isinstance(ast.varInit, ArrayLiteral):
                    # number a[5] <- [1, 2, 3, 4, 5]
                    for exp in ast.varInit.value:
                        if isinstance(exp, Id):
                            typ = self.visit(exp, o)
                            if type(typ) is None:
                                self.infer(o, exp.name, ast.varType.eleType, False)
                        else:
                            typ = self.visit(exp, o)
                            if type(typ) is None:
                                self.infer(o, exp.name.name, ast.varType.eleType, True)
                o[0][-1] = Symbol(ast.name.name, ast.varType)
            elif type(initType) is ArrayType and ast.varType is None:
                if initType.eleType is None:
                    raise TypeCannotBeInferred(ast)
                else:
                    o[0][-1] = Symbol(ast.name.name, initType)
            elif initType is None and ast.varType is not None: 
                if type(ast.varInit) is Id:
                    self.infer(o, ast.varInit.name, ast.varType, False)
                else:
                    self.infer(o, ast.varInit.name.name, ast.varType, True)
                o[0][-1] = Symbol(ast.name.name, ast.varType)
            elif initType is not None and ast.varType is not None and type(initType) is not type(ast.varType):
                if type(initType) is ArrayType and initType.eleType is None:
                    raise TypeCannotBeInferred(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            elif initType is None and ast.varType is None:
                # print(555555)
                raise TypeCannotBeInferred(ast)
            else:
                o[0][-1] = Symbol(ast.name.name, initType)
        
    def visitFuncDecl(self, ast, o):
        is_inferred = False

        for symbol in o[-1] + o[0]:
            if symbol.name == ast.name.name and symbol.params is not None:
                inferred_typ = symbol.mtype
                inferred_params = symbol.params
                is_inferred = True
                if symbol.is_defined == True:
                    raise Redeclared(Function(), ast.name.name)
                
                # neu da duoc declared tu truoc do
                temp = [[]]
                # for i in ast.param:
                #     self.visitVarDecl(i, temp, True)

                if ast.body is None:
                    for i in ast.param:
                        self.visitVarDecl(i, temp, True, False)
                else:
                    for i in ast.param:
                        self.visitVarDecl(i, temp, True, True)

                if len(temp[0]) != len(inferred_params):
                    raise Redeclared(Function(), ast.name.name)
                for i in range(0, len(temp[0])):
                    if type(temp[0][i].mtype) is not type(inferred_params[i].mtype):
                        raise Redeclared(Function(), ast.name.name)
                    if type(temp[0][i].mtype) is ArrayType and type(inferred_params[i].mtype) is ArrayType:
                        if temp[0][i].mtype.size != inferred_params[i].mtype.size:
                            raise Redeclared(Function(), ast.name.name)
                        elif type(temp[0][i].mtype.eleType) is not type(inferred_params[i].mtype.eleType):
                            raise Redeclared(Function(), ast.name.name)
                        
                temp1 = temp + o
                if ast.body is not None: 
                    has_return_stmt = False
                    if type(ast.body) is Block:
                        has_return_stmt = self.visitBlock(ast.body, temp1, ast.name.name)
                    else:
                        has_return_stmt = self.visitReturn(ast.body, temp1, ast.name.name)
                    symbol.is_defined = True
                else:
                    raise Redeclared(Function(), ast.name.name)
                inferred_typ = symbol.mtype
                if inferred_typ is not None:
                    if has_return_stmt == False and type(inferred_typ) is not VoidType:
                        raise TypeMismatchInStatement(ast)
                else:
                    inferred_typ = VoidType()
                    symbol.mtype = VoidType()
                return
        
        # neu day la mot ham moi hoan toan
        o_1 = [[Symbol(ast.name.name, None, [], False)]] + o
        if ast.body is None:
            for i in ast.param:
                self.visitVarDecl(i, o_1, True, False)
        else:
            for i in ast.param:
                self.visitVarDecl(i, o_1, True, True)
        lst_param = []
        for i in range(1, len(ast.param) + 1):
            lst_param += [Symbol(o_1[0][i].name, o_1[0][i].mtype)]
            
        if ast.body is not None: 
            if is_inferred == False:
                o_1[0][0].mtype = VoidType()
                
            if type(ast.body) is Block:
                self.visitBlock(ast.body, o_1, ast.name.name)
            else:
                self.visitReturn(ast.body, o_1, ast.name.name)
            o_1[0][0].is_defined = True

        o[0] += [Symbol(ast.name.name, o_1[0][0].mtype, lst_param, o_1[0][0].is_defined)]

    def visitId(self, ast, o):
        for symbol_list in o:
            for symbol in symbol_list:
                if ast.name == symbol.name and symbol.params is None:
                    return symbol.mtype
        raise Undeclared(Identifier(), ast.name)
    
    def visitUnaryOp(self, ast, o):
        op = ast.op
        need_type = None
        return_type = None

        if op in ['-']:
            need_type = NumberType()
            return_type = NumberType()

        if op in ['not']:
            need_type = BoolType()
            return_type = BoolType()

        operand = self.visit(ast.operand, o)
        operandType = type(operand)
        
        if operand is None:
            if type(ast.operand) is Id:
                operandType = type(self.infer(o, ast.operand.name, need_type, False))
            else: 
                operandType = type(self.infer(o, ast.operand.name.name, need_type, True))

        if operandType is not type(need_type):
            raise TypeMismatchInExpression(ast)
        else:
            return return_type

    def visitBinaryOp(self, ast, o):
        op = ast.op
        need_type = None
        return_type = None
        if op in ['+', '-', '*', '/', '%']:
            need_type = NumberType()
            return_type = NumberType()
        elif op in ['and', 'or']:
            need_type = BoolType()
            return_type = BoolType()
        elif op in ['...']:
            need_type = StringType()
            return_type = StringType()
        elif op in ['=', '!=', '<', '>', '<=', '>=']:
            need_type = NumberType()
            return_type = BoolType()
        elif op in ['==']:
            need_type = StringType()
            return_type = BoolType()

        left = self.visit(ast.left, o)
        lefttype = type(left)
        if left is None:
            if type(ast.left) is Id:
                lefttype = type(self.infer(o, ast.left.name, need_type, False))
            else: 
                lefttype = type(self.infer(o, ast.left.name.name, need_type, True))

        right = self.visit(ast.right, o)
        righttype = type(right)
        if right is None:
            if type(ast.right) is Id:
                righttype = type(self.infer(o, ast.right.name, need_type, False))
            else:
                righttype = type(self.infer(o, ast.right.name.name, need_type, True))
        
        if lefttype is not righttype:
            raise TypeMismatchInExpression(ast)
        elif lefttype is not type(need_type):
            raise TypeMismatchInExpression(ast)
        else:
            return return_type
            
    def visitBlock(self, ast, o, curr=None):
        o1 = [[]] + o
        has_return_stmt = False
        for stmt_decl in ast.stmt:
            if type(stmt_decl) is Return:
                has_return_stmt = self.visitReturn(stmt_decl, o1, curr) or has_return_stmt
            elif type(stmt_decl) is If:
                has_return_stmt = self.visitIf(stmt_decl, o1, curr) or has_return_stmt
            elif type(stmt_decl) is For:
                has_return_stmt = self.visitFor(stmt_decl, o1, curr) or has_return_stmt
            elif type(stmt_decl) is Block:
                has_return_stmt = self.visitBlock(stmt_decl, o1, curr) or has_return_stmt
            else:
                self.visit(stmt_decl, o1)
        return has_return_stmt
    
    def visitAssign(self, ast, o):
        rtype = self.visit(ast.rhs, o)
        ltype = self.visit(ast.lhs, o)

        if ltype is None and rtype is None:
            raise TypeCannotBeInferred(ast)
        if ltype is None and type(rtype) is ArrayType:
            if rtype.eleType is None:
                raise TypeCannotBeInferred(ast)
        if type(ltype) is ArrayType and type(rtype) is ArrayType:
            if ltype.size != rtype.size:
                raise TypeMismatchInStatement(ast)
            if type(rtype.eleType) is not type(ltype.eleType):
                raise TypeMismatchInStatement(ast)
        if ltype is None:
            ltype = self.infer(o, ast.lhs.name, rtype, False)
            return ltype
        if rtype is None:
            if type(ast.rhs) is Id:
                rtype = self.infer(o, ast.rhs.name, ltype, False)
            else:
                rtype = self.infer(o, ast.rhs.name.name, ltype, True)
            return rtype
        if type(rtype) is type(ltype):
            return rtype
        else:
            raise TypeMismatchInStatement(ast)
        
    def visitIf(self, ast, o, curr=None):
        ctype = self.visit(ast.expr, o)
        if type(ctype) is not BoolType:
            if ctype is None:
                if type(ast.expr) is Id:
                    self.infer(o, ast.expr.name, BoolType(), False)
                else:
                    self.infer(o, ast.expr.name.name, BoolType(), True)
                ctype = BoolType()
            else:
                raise TypeMismatchInStatement(ast)
        # then
        has_return_stmt = False
        o1 = [[]] + o
        if type(ast.thenStmt) is Return:
            has_return_stmt = self.visitReturn(ast.thenStmt, o1, curr) or has_return_stmt
        elif type(ast.thenStmt) is If:
            has_return_stmt = self.visitIf(ast.thenStmt, o1, curr) or has_return_stmt
        elif type(ast.thenStmt) is For:
            has_return_stmt = self.visitFor(ast.thenStmt, o1, curr) or has_return_stmt
        elif type(ast.thenStmt) is Block:
            has_return_stmt = self.visitBlock(ast.thenStmt, o1, curr) or has_return_stmt
        else:
            self.visit(ast.thenStmt, o1)
        # elif
        has_return_stmt2 = False
        for stmt in ast.elifStmt:
            exprtype = self.visit(stmt[0], o)
            if type(exprtype) is not BoolType:
                if exprtype is None:
                    if type(ast.expr) is Id:
                        self.infer(o, ast.expr.name, BoolType(), False)
                    else:
                        self.infer(o, ast.expr.name.name, BoolType(), True)
                    exprtype = BoolType()
                else:
                    raise TypeMismatchInStatement(ast)
            o2 = [[]] + o
            if type(stmt[1]) is Return:
                has_return_stmt2 = self.visitReturn(stmt[1], o2, curr) or has_return_stmt2
            elif type(stmt[1]) is If:
                has_return_stmt2 = self.visitIf(stmt[1], o2, curr) or has_return_stmt2
            elif type(stmt[1]) is For:
                has_return_stmt2 = self.visitFor(stmt[1], o2, curr) or has_return_stmt2
            elif type(stmt[1]) is Block:
                has_return_stmt2 = self.visitBlock(stmt[1], o2, curr) or has_return_stmt2
            else:
                self.visit(stmt[1], o2)
            # self.visit(stmt[1], o2)
        # else
        o3 = [[]] + o
        has_return_stmt3 = False
        if ast.elseStmt is not None:
            if type(ast.elseStmt) is Return:
                has_return_stmt3 = self.visitReturn(ast.elseStmt, o3, curr) or has_return_stmt3
            elif type(ast.elseStmt) is If:
                has_return_stmt3 = self.visitIf(ast.elseStmt, o3, curr) or has_return_stmt3
            elif type(ast.elseStmt) is For:
                has_return_stmt3 = self.visitFor(ast.elseStmt, o3, curr) or has_return_stmt3
            elif type(ast.elseStmt) is Block:
                has_return_stmt3 = self.visitBlock(ast.elseStmt, o3, curr) or has_return_stmt3
            else:
                self.visit(ast.elseStmt, o3)
            # self.visit(ast.elseStmt, o3)
        return has_return_stmt or has_return_stmt2 or has_return_stmt3

    def visitFor(self, ast, o, curr=None):
        name_type = self.visit(ast.name, o)
        cond_type = self.visit(ast.condExpr, o)
        upd_type = self.visit(ast.updExpr, o)

        if name_type is None:
            if type(ast.name) is Id:
                self.infer(o, ast.name.name, NumberType(), False)
            else:
                self.infer(o, ast.name.name.name, NumberType(), True)
            name_type = NumberType()

        if cond_type is None:
            if type(ast.condExpr) is Id:
                self.infer(o, ast.condExpr.name, BoolType(), False)
            else:
                self.infer(o, ast.condExpr.name.name, BoolType(), True)
            cond_type = BoolType()

        if upd_type is None:
            if type(ast.updExpr) is Id:
                self.infer(o, ast.updExpr.name, NumberType(), False)
            else:
                self.infer(o, ast.updExpr.name.name, NumberType(), True)
            upd_type = NumberType()

        if not(type(name_type) is NumberType and type(cond_type) is BoolType and type(upd_type) is NumberType):
            raise TypeMismatchInStatement(ast)
        
        o1 = [[Symbol("<Loop>",VoidType)]] + o
        has_return_stmt = False
        if type(ast.body) is Return:
            has_return_stmt = self.visitReturn(ast.body, o1, curr) or has_return_stmt
        elif type(ast.body) is If:
            has_return_stmt = self.visitIf(ast.body, o1, curr) or has_return_stmt
        elif type(ast.body) is For:
            has_return_stmt = self.visitFor(ast.body, o1, curr) or has_return_stmt
        elif type(ast.body) is Block:
            has_return_stmt = self.visitBlock(ast.body, o1, curr) or has_return_stmt
        else:
            self.visit(ast.body, o1)
        # self.visit(ast.body, o1)
        return has_return_stmt

    def visitBreak(self, ast, o):
        flag = False
        for symbol_list in o:
            for symbol in symbol_list:
                if symbol.name == "<Loop>":
                    flag = True
                    return
        if not flag: 
            raise MustInLoop(ast)
        
    def visitContinue(self, ast, o):
        flag = False
        for symbol_list in o:
            for symbol in symbol_list:
                if symbol.name == "<Loop>": 
                    flag = True
                    return
        if not flag: 
            raise MustInLoop(ast)
        
    def visitReturn(self, ast, o, curr=None):
        if ast.expr is not None:
            return_typ = self.visit(ast.expr, o) 
        else:
            return_typ = VoidType()

        func_typ = VoidType()
        for sym in o[-1] + o[-2]:
            if sym.name == curr and sym.params is not None:
                func_typ = sym.mtype
                if type(func_typ) is not type(return_typ):
                    if not isinstance(func_typ, VoidType) and (return_typ is None or (type(return_typ) is ArrayType and return_typ.eleType is None)):
                    # if not isinstance(func_typ, VoidType) and return_typ is None:
                        if type(ast.expr) is Id:
                            self.infer(o, ast.expr.name, return_typ, False)
                        else:
                            self.infer(o, ast.expr.name.name, return_typ, True)
                    elif isinstance(func_typ, VoidType) and (return_typ is None or (type(return_typ) is ArrayType and return_typ.eleType is None)):
                        raise TypeCannotBeInferred(ast)
                    elif isinstance(func_typ, VoidType) and return_typ is not None:
                        if sym.is_void == True:
                            raise TypeMismatchInStatement(ast)
                        elif sym.is_defined == False:
                            sym.mtype = return_typ
                            sym.is_defined = True
                        else:
                            raise TypeMismatchInStatement(ast)
                    elif not isinstance(func_typ, VoidType) and return_typ is not None:
                        if func_typ is None:
                            sym.mtype = return_typ
                            sym.is_defined = True
                        else:
                            raise TypeMismatchInStatement(ast)
                elif type(func_typ) is ArrayType and type(return_typ) is ArrayType:
                    if type(ast.expr) is ArrayLiteral and return_typ.eleType is None and type(func_typ) is ArrayType:
                        if len(func_typ.size) > 1:
                            return_typ = self.visitArrayLiteral(ast.expr, o, ArrayType(func_typ.size[1:], func_typ.eleType))
                        else:
                            return_typ = self.visitArrayLiteral(ast.expr, o, func_typ.eleType)
                    if func_typ.size != return_typ.size:
                        raise TypeMismatchInStatement(ast)
                    if type(func_typ.eleType) is not type(return_typ.eleType):
                        raise TypeMismatchInStatement(ast)
                else:
                    if sym.is_defined == False:
                        sym.mtype = return_typ
                        sym.is_defined = True
        return True

    def visitCallExpr(self, ast, o):
        flag = False

        if len(o) > 2:
            temp = o[-2] + o[-1]
        else:
            temp = o[-1]
        for symbol in temp:
            if ast.name.name == symbol.name and symbol.params is not None:
                if type(symbol.mtype) is VoidType:
                    raise TypeMismatchInExpression(ast)
                else:
                    flag = True
                    break
        if not flag: 
            raise Undeclared(Function(), ast.name.name)
                
        # Check param compatibility
        for symbol in temp:
            if ast.name.name == symbol.name and symbol.params is not None:
                lst_param = symbol.params
                args = ast.args
                # length check
                if len(args) != len(lst_param):
                    raise TypeMismatchInExpression(ast)
                # argument and param
                # argument trong callstmt có thể var, param trong funcdecl thì chắc chắn đã có kiểu
                else:
                    for i in range(0, len(lst_param)):
                        param_typ = lst_param[i].mtype
                        if type(ast.args[i]) is ArrayLiteral and type(param_typ) is ArrayType:
                            if len(param_typ.size) > 1:
                                arg_typ = self.visitArrayLiteral(ast.args[i], o, ArrayType(param_typ.size[1:], param_typ.eleType))
                            else:
                                arg_typ = self.visitArrayLiteral(ast.args[i], o, param_typ.eleType)
                            arg_typ = self.visitArrayLiteral(ast.args[i], o, )
                        else:
                            arg_typ = self.visit(ast.args[i], o)
                        
                        if arg_typ is None and param_typ is not None:
                            if type(ast.args[i]) is Id:
                                self.infer(o, ast.args[i].name, param_typ, False)
                            else:
                                self.infer(o, ast.args[i].name.name, param_typ, True)
                            ast.args[i].mtype = param_typ
                            continue
                        
                        if type(arg_typ) is ArrayType and type(param_typ) is ArrayType:
                            if arg_typ.size != param_typ.size:
                                raise TypeMismatchInStatement(ast)
                            elif type(arg_typ.eleType) is not type(param_typ.eleType):
                                raise TypeMismatchInStatement(ast)
                            
                        if type(arg_typ) is not type(param_typ):
                            raise TypeMismatchInExpression(ast)
                return symbol.mtype

    def visitCallStmt(self, ast, o):
        flag = False

        if len(o) > 2:
            temp = o[-2] + o[-1]
        else:
            temp = o[-1]

        for symbol in temp:
            if ast.name.name == symbol.name and symbol.params is not None:
                if symbol.mtype is not None and type(symbol.mtype) is not VoidType:
                    raise TypeMismatchInStatement(ast)
                else:
                    if symbol.mtype is None:
                        symbol.mtype = VoidType()
                        symbol.is_void = True
                    flag = True
                    break
        if not flag: 
            raise Undeclared(Function(), ast.name.name)
                
        # Check param compatibility
        for symbol in temp:
            if ast.name.name == symbol.name and symbol.params is not None:
                lst_param = symbol.params
                args = ast.args
                # length check
                if len(args) != len(lst_param):
                    # print("AAAA")
                    raise TypeMismatchInStatement(ast)
                # argument and param
                # argument trong callstmt có thể var, param trong funcdecl thì chắc chắn đã có kiểu
                else:
                    for i in range(0, len(lst_param)):
                        param_typ = lst_param[i].mtype
                        if type(ast.args[i]) is ArrayLiteral and type(param_typ) is ArrayType:
                            if len(param_typ.size) > 1:
                                arg_typ = self.visitArrayLiteral(ast.args[i], o, ArrayType(param_typ.size[1:], param_typ.eleType))
                            else:
                                arg_typ = self.visitArrayLiteral(ast.args[i], o, param_typ.eleType)
                            arg_typ = self.visitArrayLiteral(ast.args[i], o, )
                        else:
                            arg_typ = self.visit(ast.args[i], o)
                        
                        if arg_typ is None and param_typ is not None:
                            if type(ast.args[i]) is Id:
                                self.infer(o, ast.args[i].name, param_typ, False)
                            else:
                                self.infer(o, ast.args[i].name.name, param_typ, True)
                            ast.args[i].mtype = param_typ
                            continue
                        
                        if type(arg_typ) is ArrayType and type(param_typ) is ArrayType:
                            if arg_typ.size != param_typ.size:
                                raise TypeMismatchInStatement(ast)
                            elif type(arg_typ.eleType) is not type(param_typ.eleType):
                                raise TypeMismatchInStatement(ast)
                            
                        if type(arg_typ) is not type(param_typ):
                            raise TypeMismatchInStatement(ast)
                return symbol.mtype

    def visitArrayLiteral(self, ast, o, recall=None):
        if recall is not None:
            array_typ = recall
        else:
            array_typ = None
        values = ast.value
        max_size = []
        for _ in range(0,2):
            for exp in values:
                # if type(exp) is ArrayLiteral and array_typ is not None:
                if type(exp) is ArrayLiteral and type(array_typ) is ArrayType:
                    if len(array_typ.size) > 1:
                        exp_typ = self.visitArrayLiteral(exp, o, ArrayType(array_typ.size[1:], array_typ.eleType))
                    else:
                        exp_typ = self.visitArrayLiteral(exp, o, array_typ.eleType)
                else:
                    exp_typ = self.visit(exp, o)

                if array_typ is None:
                    if exp_typ is not None: 
                        array_typ = exp_typ
                else:
                    if exp_typ is None:
                        if type(exp) is Id:
                            self.infer(o, exp.name, array_typ, False)
                        else:
                            self.infer(o, exp.name.name, array_typ, True)
                    elif type(exp_typ) is ArrayType and type(array_typ) is ArrayType:
                        if type(exp_typ.eleType) is not type(array_typ.eleType) and exp_typ.eleType is not None and array_typ.eleType is not None:
                            print(11111)
                            raise TypeMismatchInExpression(ast)
                        if len(exp_typ.size) < len(array_typ.size):
                            temp = []
                            if exp_typ.eleType is None:
                                for i in range(0, len(exp_typ.size)):
                                    if int(exp_typ.size[i]) != int(array_typ.size[i]):
                                        print(222222)
                                        raise TypeMismatchInExpression(ast)
                                for i in range(len(exp_typ.size), len(array_typ.size)):
                                    temp.append(array_typ.size[i])
                                exp_typ = self.visitArrayLiteral(exp, o, ArrayType(temp, array_typ.eleType))
                            # else:
                            #     print(33333)
                            #     raise TypeMismatchInExpression(ast)
                        elif len(exp_typ.size) > len(array_typ.size):
                            if array_typ.eleType is None:
                                for i in range(0, len(array_typ.size)):
                                    if int(array_typ.size[i]) != int(exp_typ.size[i]):
                                        print(444444)
                                        raise TypeMismatchInExpression(ast)
                                array_typ = exp_typ
                            else:
                                print(55555)
                                raise TypeMismatchInExpression(ast)
                        else:
                            if array_typ.eleType is None:
                                array_typ = exp_typ
                            if exp_typ.eleType is None:
                                exp_typ = array_typ

                            if type(exp) is Id:
                                self.infer(o, exp.name, array_typ, False)
                            elif type(exp) is FuncDecl:
                                self.infer(o, exp.name.name, array_typ, True)
                            elif type(exp) is CallExpr:
                                self.infer(o, exp.name.name, array_typ, True)

                            for i in range(0, len(array_typ.size)):
                                if int(array_typ.size[i]) != int(exp_typ.size[i]):
                                    print(66666666)
                                    raise TypeMismatchInExpression(ast)
                            # array_typ = exp_typ
                    elif type(array_typ) is not type(exp_typ):
                        print(777777)
                        print(array_typ, exp_typ)
                        raise TypeMismatchInExpression(ast)
            if _ == 0:
                if type(array_typ) is ArrayType:
                    max_size = array_typ.size
        
        if type(array_typ) is ArrayType and len(array_typ.size) > len(max_size):
            print("0000")
            # print(exp, array_typ, max_size)
            # if array_typ.eleType is not None:
            raise TypeMismatchInExpression(ast)

        if type(array_typ) is ArrayType:
            array_size = [len(ast.value)] + array_typ.size 
            array_type = array_typ.eleType 
        else:
            array_size = [len(ast.value)]
            array_type = array_typ
        return ArrayType(array_size, array_type)

    def visitArrayCell(self, ast, o):
        name_type = self.visit(ast.arr, o)
        if type(name_type) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        for idx in ast.idx:
            idx_typ = self.visit(idx, o)
            if type(idx_typ) is not NumberType:
                if idx_typ is None:
                    if type(idx) is Id:
                        self.infer(o, idx.name, NumberType(), False)
                    else:
                        self.infer(o, idx.name.name, NumberType(), True)
                else:
                    raise TypeMismatchInExpression(ast)
        if len(name_type.size) == len(ast.idx):
            # or len(name_type.size) == len(ast.idx) + 1:
            return name_type.eleType
        # elif len(name_type.size) > len(ast.idx) + 1:
        elif len(name_type.size) > len(ast.idx):
            temp = []
            for i in range(len(ast.idx), len(name_type.size)):
                temp.append(name_type.size[i])
            return ArrayType(temp, name_type.eleType)
        else:
            raise TypeMismatchInExpression(ast) 