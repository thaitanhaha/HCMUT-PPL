from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
                Symbol("readNumber", MType(list(), NumberType()), CName(self.libName)),
                Symbol("writeNumber", MType([NumberType()], VoidType()), CName(self.libName)),
                Symbol("readBool", MType(list(), BoolType()), CName(self.libName)),
                Symbol("writeBool", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("readString", MType(list(), StringType()), CName(self.libName)),
                Symbol("writeString", MType([StringType()], VoidType()), CName(self.libName)),
            ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value

class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "ZCodeClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.globalVarDecl = []
        self.globalDynamic = []

    def visitProgram(self, ast, c):
        self.emit.sub_printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)

        for x in ast.decl:
            if type(x) is FuncDecl and x.name.name == "main":
                continue
            e = self.visit(x, e)

        for x in ast.decl:
            if type(x) is FuncDecl and x.name.name == "main":
                e = self.visit(x, e)
        for var in self.globalDynamic:
            for i in e.sym:
                if i.name == var.name.name:
                    if type(i.mtype) is ArrayType:
                        self.emit.var_sub_printout(self.emit.emitATTRIBUTE(i.name, self.reformat_array_type(i.mtype), False, 0))
                    else:
                        self.emit.var_sub_printout(self.emit.emitATTRIBUTE(i.name, i.mtype, False, 0))
        self.genMETHOD(FuncDecl(Id("<init>"), [], Block([])), e.sym, Frame("<init>", VoidType))
        self.genMETHOD(FuncDecl(Id("<clinit>"), [], Block([])), e.sym, Frame("<clinit>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame, need_to_infer_sym=[]):
        isInit = consdecl.name.name == "<init>"
        isClinit = consdecl.name.name == "<clinit>"
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0
        return_type = VoidType() if isInit or isClinit else frame.returnType
        if type(return_type) is ArrayType:
            return_type = self.reformat_array_type(return_type)
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayType([0], StringType())] if isMain else list()

        param_list = []
        for stmt in consdecl.param:
            if type(stmt.varType) is ArrayType:
                param_list.append(self.reformat_array_type(stmt.varType))
            else:
                param_list.append(stmt.varType)

        intype = [ArrayType([0], StringType())] if isMain else param_list
        mtype = MType(intype, return_type)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o # sym

        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([0], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        if isClinit:
            for vardecl in self.globalVarDecl:
                var_sym = next(filter(lambda x: x.name == vardecl.name.name, o))
                var_name = var_sym.name
                var_type = var_sym.mtype
                val = var_sym.value
                var_init = vardecl.varInit

                if type(var_type) is ArrayType:
                    self.emit.printout(self.emit.emitARRAY(var_type, frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(val.value + "." + var_name, self.reformat_array_type(var_type), frame))

                if var_init:
                    if type(var_init) is ArrayLiteral:
                        self.emit.printout(self.initialize_array(var_sym, var_init, Access(frame, o, False)))
                    else:
                        code, _ = self.visit(var_init, Access(frame, o, False))
                        self.emit.printout(code)
                        self.emit.printout(self.emit.emitPUTSTATIC(val.value + "." + var_name, var_type, frame))

        for ele in consdecl.param:
            glenv = self.visitVarDecl(ele, SubBody(frame, glenv), True).sym

        temp = SubBody(frame, glenv)
        if type(body) is Block:
            for x in body.stmt:
                if type(x) is VarDecl:
                    a = self.visitVarDecl(x, temp, False, need_to_infer_sym)
                elif type(x) is Block:
                    a = self.visitBlock(x, temp, need_to_infer_sym)
                elif type(x) is If:
                    a = self.visitIf(x, temp, need_to_infer_sym)
                elif type(x) is For:
                    a = self.visitFor(x, temp, need_to_infer_sym)
                else:
                    a = self.visit(x, temp)
                if type(a) is SubBody:
                    temp = a
        else:
            self.visit(body, temp)
                
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        if type(return_type) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        elif type(return_type) is NumberType or type(return_type) is BoolType \
          or type(return_type) is StringType or type(return_type) is ArrayType:
            self.emit.printout(self.emit.emitRETURN_HELP(return_type))
            
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        
        return param_list
            
    def find_dynamic_help(self, list, dynamic_name):
        for element in list:
            if element.name == dynamic_name and element.mtype is None:
                return element
        return None

    def infer_func_type(self, param, body, c, for_block=False):
        need_to_infer_sym = []
        o = SubBody(c.frame, c.sym.copy())
        index = 1
        if not for_block:
            for stmt in param:
                o.sym.append(Symbol(stmt.name.name, stmt.varType, Index(index)))
                index += 1
            if type(body) is Block:
                for stmt in body.stmt:
                    if type(stmt) is not VarDecl:
                        continue
                    else:
                        typ = stmt.varType
                        if stmt.varType is None:
                            if stmt.varInit is not None:
                                if type(stmt.varInit) is CallExpr:
                                    typ = self.visitCallExpr(stmt.varInit, Access(o.frame, o.sym, isLeft=False, isFirst=False), True)[1]
                                else:
                                    typ = self.visit(stmt.varInit, Access(o.frame, o.sym, isLeft=False, isFirst=False))[1]
                            else:
                                pass
                        o.sym.append(Symbol(stmt.name.name, typ, Index(index)))
                        index += 1
        else:
            for stmt in body.stmt:
                if type(stmt) is not VarDecl:
                    continue
                else:
                    typ = stmt.varType
                    if stmt.varType is None:
                        if stmt.varInit is not None:
                            if type(stmt.varInit) is CallExpr:
                                typ = self.visitCallExpr(stmt.varInit, Access(o.frame, o.sym, isLeft=False, isFirst=False), True)[1]
                            else:
                                typ = self.visit(stmt.varInit, Access(o.frame, o.sym, isLeft=False, isFirst=False))[1]
                        else:
                            pass
                    o.sym.append(Symbol(stmt.name.name, typ, Index(index)))
                    index += 1
            

        return_type = VoidType()
        access = Access(o.frame, o.sym, isLeft=False, isFirst=False)
        if type(body) is Return:
            if type(body.expr) is ArrayLiteral:
                return_type = self.visitArrayLiteral(body.expr, access, True)[-1]
            elif body.expr is not None:
                return_type = self.visit(body.expr, access)[-1]
        else:
            for stmt in body.stmt:
                if type(stmt) is Assign:
                    if type(stmt.lhs) is Id:
                        dynamic_sym = self.find_dynamic_help(o.sym, stmt.lhs.name)
                        if dynamic_sym is not None:
                            if type(stmt.rhs) is ArrayLiteral:
                                dynamic_typ = self.visitArrayLiteral(stmt.rhs, access, True)[-1]
                            else:
                                dynamic_typ = self.visit(stmt.rhs, access)[1]
                            dynamic_sym.mtype = dynamic_typ
                            need_to_infer_sym.append(dynamic_sym)

                if type(stmt) is Return:
                    if type(stmt.expr) is ArrayLiteral:
                        return_type = self.visitArrayLiteral(stmt.expr, access, True)[-1]
                    elif stmt.expr is not None:
                        return_type = self.visit(stmt.expr, access)[-1]
                    break
                elif type(stmt) is If:
                    has_ret, typ, more_infer = self.visitIfHelp(stmt, access)
                    need_to_infer_sym += more_infer
                    if has_ret:
                        return_type = typ
                        break
                elif type(stmt) is For:
                    has_ret, typ, more_infer = self.visitForHelp(stmt, access)
                    need_to_infer_sym += more_infer
                    if has_ret:
                        return_type = typ
                        break
                elif type(stmt) is Block:
                    ret_typ, more_infer = self.infer_func_type(o.sym, stmt, access, True)
                    need_to_infer_sym += more_infer
                    if type(ret_typ) is not VoidType:
                        return_type = ret_typ
                        break

        return return_type, need_to_infer_sym

    def visitFuncDecl(self, ast, o):
        return_type = VoidType()
        param_list = []
        if ast.body is not None:
            return_type, need_to_infer_sym = self.infer_func_type(ast.param, ast.body, SubBody(Frame(ast.name.name, VoidType()), o.sym))
            frame = Frame(ast.name.name, return_type)
            param_list = self.genMETHOD(ast, o.sym, frame, need_to_infer_sym)
        return SubBody(None, [Symbol(ast.name.name, MType(param_list, return_type), CName(self.className))] + o.sym)

    def visitVarDecl(self, ast, c, isParam=False, need_to_infer_sym=[]):
        var_name = ast.name.name
        var_init = ast.varInit
        var_type = ast.varType
        initCode = ""
        if var_type is None: 
            if var_init is not None:
                initCode, var_type = self.visit(var_init, Access(c.frame, c.sym, isLeft=False, isFirst=False))
            else:
                # dynamic x
                for sym in need_to_infer_sym:
                    if sym.name == var_name:
                        var_type = sym.mtype
        else:
            if var_init is not None and type(var_init) is not ArrayLiteral:
                initCode, _ = self.visit(var_init, Access(c.frame, c.sym, False, False))
            elif var_init is None and isParam == False:
                if type(var_type) is NumberType:
                    initCode, _ = self.visit(NumberLiteral(1.0), Access(c.frame, c.sym, False, False))
                    var_init = NumberType()
                elif type(var_type) is BoolType:
                    initCode, _ = self.visit(BooleanLiteral(True), Access(c.frame, c.sym, False, False))
                    var_init = BoolType()
                elif type(var_type) is StringType:
                    initCode, _ = self.visit(StringLiteral("0"), Access(c.frame, c.sym, False, False))
                    var_init = StringType()

        if c.frame is None:
            self.globalVarDecl.append(ast)
            val = CName(self.className)
            if var_type is not None:
                if type(var_type) is ArrayType:
                    self.emit.var_sub_printout(self.emit.emitATTRIBUTE(var_name, self.reformat_array_type(var_type), False, 0))
                else:
                    self.emit.var_sub_printout(self.emit.emitATTRIBUTE(var_name, var_type, False, 0))
            else:
                self.globalDynamic.append(ast)
        else:
            val = Index(c.frame.getNewIndex())
            if type(var_type) is ArrayType:
                temp = self.reformat_array_type(var_type)
                self.emit.printout(self.emit.emitVAR(val.value, var_name, temp, c.frame.getStartLabel(), c.frame.getEndLabel(), c.frame))
            else:
                self.emit.printout(self.emit.emitVAR(val.value, var_name, var_type, c.frame.getStartLabel(), c.frame.getEndLabel(), c.frame))

            if type(var_type) is ArrayType:
                if not isParam:
                    self.emit.printout(self.emit.emitARRAY(var_type, c.frame))
                    self.emit.printout(self.emit.emitWRITEVAR(var_name, var_type, val.value, c.frame))

            if var_init:
                if type(var_init) is ArrayLiteral:
                    self.emit.printout(self.initialize_array(Symbol(var_name, var_type, val), var_init, c))
                else:
                    self.emit.printout(initCode)
                    self.emit.printout(self.emit.emitWRITEVAR(var_name, var_type, val.value, c.frame))
        return SubBody(c.frame, [Symbol(var_name, var_type, val)] + c.sym)

    def visitId(self, ast, c):
        sym = None

        for x in c.sym:
            if x.name == ast.name:
                sym = x
                break
        
        typ = sym.mtype
        if type(sym.mtype) is ArrayType:
            typ = self.reformat_array_type(typ)

        if type(sym.value) is Index:
            if c.isLeft:
                return self.emit.emitWRITEVAR(sym.name, typ, sym.value.value, c.frame), typ
            return self.emit.emitREADVAR(sym.name, typ, sym.value.value, c.frame), typ
        else:
            name = sym.value.value + "." + sym.name
            if c.isLeft:
                return self.emit.emitPUTSTATIC(name, typ, c.frame), typ
            return self.emit.emitGETSTATIC(name, typ, c.frame), typ

    def visitAssign(self, ast, c):
        if type(ast.rhs) is ArrayLiteral:
            name = ast.lhs.name # vi luc nay auto ve trai la ID
            typ = None
            for i in c.sym:
                if i.name == name:
                    typ = i.mtype
            self.emit.printout(self.emit.emitARRAY(typ, c.frame))
            self.emit.printout(self.emit.emitDUP(c.frame))
            rCode, _ = self.visit(ast.rhs, Access(c.frame, c.sym, isLeft=False))
        else:
            rCode, _ = self.visit(ast.rhs, Access(c.frame, c.sym, isLeft=False))
        lCode, lType = self.visit(ast.lhs, Access(c.frame, c.sym, isLeft=True))

        if type(lType) is ArrayType and type(ast.rhs) is ArrayLiteral:
            self.emit.printout(lCode + ''.join(rCode))
        elif type(lType) is not ArrayType and type(ast.lhs) is ArrayCell:
            c.frame.push()
            c.frame.push()
            self.emit.printout(lCode + rCode)
            self.emit.printout(self.emit.emitASTORE(lType, c.frame))
        else:
            self.emit.printout(rCode + lCode)

    def visitCallStmt(self, ast, c):
        sym = None
        for x in c.sym:
            if ast.name.name == x.name:
                sym = x
        cname = sym.value.value
        ctype = sym.mtype

        in_ = ("", [])
        # args_list = []
        for x in ast.args:
            if type(x) is ArrayLiteral:
                temp1 = self.visitArrayLiteral(x, Access(c.frame, c.sym, False), True)[1]
                list_code = self.emit.emitARRAY(temp1, c.frame)
                self.emit.printout(list_code)
                self.emit.printout(self.emit.emitDUP(c.frame))
                str1, typ1 = self.visitArrayLiteral(x, Access(c.frame, c.sym, False))
            else:
                str1, typ1 = self.visit(x, Access(c.frame, c.sym, False))
            if type(typ1) is ArrayType:
                typ1 = self.reformat_array_type(typ1)

            a = in_[0]
            if type(str1) is list:
                for i in str1:
                    a += i
            else:
                a += str1
            b = in_[1].copy()
            b.append(typ1)
            in_ = (a, b)

        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.name.name, \
                                                      MType(in_[1], ctype.rettype), c.frame))

    def visitCallExpr(self, ast, c, for_infer=False):
        funcSym = next(filter(lambda x: x.name == ast.name.name, c.sym), None)

        result = []
        args_list = []
        for param in ast.args:
            access = Access(c.frame, c.sym, False)
            if type(param) is ArrayLiteral:
                if for_infer:
                    temp = self.visitArrayLiteral(param, access, True)
                else:
                    temp1 = self.visitArrayLiteral(param, access, True)[1]
                    list_code = self.emit.emitARRAY(temp1, c.frame)
                    result.append(list_code)
                    result.append(self.emit.emitDUP(c.frame))
                    temp = self.visitArrayLiteral(param, access, False)
            else:
                temp = self.visit(param, access)
            if type(temp[0]) is list:
                for i in temp[0]:
                    result.append(i)
            else:
                result.append(temp[0])

            if type(temp[1]) is ArrayType:
                args_list.append(self.reformat_array_type(temp[1]))
            else:
                args_list.append(temp[1])

        methodname = funcSym.value.value + "/" + funcSym.name
        if type(funcSym.mtype.rettype) is ArrayType:
            methodtype = MType(args_list, self.reformat_array_type(funcSym.mtype.rettype))
        else:
            methodtype = MType(args_list, funcSym.mtype.rettype)
        result.append(self.emit.emitINVOKESTATIC(methodname, methodtype, c.frame))
        return ''.join(result), methodtype.rettype

    def visitNumberLiteral(self, ast, o):
        if o.frame is None:
            return "", NumberType()
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), NumberType()
    
    def visitStringLiteral(self, ast, o):
        if o.frame is None:
            return "", StringType()
        return self.emit.emitPUSHCONST(str(ast.value), StringType(), o.frame), StringType()
    
    def visitBooleanLiteral(self, ast, o):
        if o.frame is None:
            return "", BoolType()
        return self.emit.emitPUSHICONST(str(ast.value).lower(), o.frame), BoolType()
    
    def infer_array_help(self, ast, c):
        if type(ast.value[0]) is ArrayLiteral:
            return ArrayType([len(ast.value)] + self.infer_array_help(ast.value[0], c).size, self.infer_array_help(ast.value[0], c).eleType)
        else:
            return ArrayType([len(ast.value)], self.visit(ast.value[0], c)[1])

    def visitArrayLiteral(self, ast, c, for_infer=False):
        if for_infer == False:
            return self.store_array(ast, c), self.infer_array_help(ast, c)
        else:
            return "", self.infer_array_help(ast, c)
    
    def initialize_array(self, sym, arrayLiteral, c):
        result = []
        if type(sym.value) is Index:
            result.append(self.emit.emitREADVAR(sym.name, self.reformat_array_type(sym.mtype), sym.value.value, c.frame))
        else:
            result.append(self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, self.reformat_array_type(sym.mtype), c.frame))

        result += self.store_array(arrayLiteral, c)
        return ''.join(result)

    def store_array(self, ast, c):
        result = []
        n = len(ast.value)
        for _ in range(n - 1):
            result.append(self.emit.emitDUP(c.frame))

        if type(ast.value[0]) is ArrayLiteral:
            for index, literal in zip(range(n), ast.value):
                result.append(self.emit.emitPUSHICONST(index, c.frame))
                result.append(self.emit.emitALOAD(ArrayType([0], None), c.frame))
                result += self.store_array(literal, c)
            return result
        else:
            for index, literal in zip(range(n), ast.value):
                result.append(self.emit.emitPUSHICONST(index, c.frame))
                code, typ = self.visit(literal, Access(c.frame, c.sym, False, False))
                result.append(code)
                result.append(self.emit.emitASTORE(typ, c.frame))
            return result

    def visitArrayCell(self, ast, c):
        result = []

        arr_code, arr_type = self.visit(ast.arr, Access(c.frame, c.sym, False))
        index_code_list = [self.visit(i, Access(c.frame, c.sym, False))[0] for i in ast.idx]

        typ = arr_type
        if type(arr_type) is ArrayType:
            typ = self.reformat_array_type(arr_type)

        result.append(arr_code)
        for index_code in index_code_list[:-1]:
            result.append(index_code)
            result.append(self.emit.emitF2I())
            result.append(self.emit.emitALOAD(typ.eleType, c.frame))
            typ = typ.eleType
        
        if type(typ.eleType) is not ArrayType and c.isLeft:
            result.append(index_code_list[-1])
            result.append(self.emit.emitF2I())
        else:
            result.append(index_code_list[-1])
            result.append(self.emit.emitF2I())
            result.append(self.emit.emitALOAD(typ.eleType, c.frame))

        return ''.join(result), typ.eleType
    
    def reformat_array_type(self, arrType):
        typ = arrType.eleType
        for size in arrType.size[::-1]:
            typ = ArrayType([size], typ)
        return typ

    def visitBinaryOp(self, ast, c):
        if ast.op in ['and', 'or']:
            result = []

            lCode, _ = self.visit(ast.left, Access(c.frame, c.sym, False))
            result.append(lCode)

            labelF = c.frame.getNewLabel()
            labelT = c.frame.getNewLabel()
            labelN = c.frame.getNewLabel()

            if ast.op == 'and':
                result.append(self.emit.emitIFFALSE(labelF, c.frame))
            else:
                result.append(self.emit.emitIFTRUE(labelT, c.frame))
            
            rCode, _ = self.visit(ast.right, Access(c.frame, c.sym, False))
            result.append(lCode)
            result.append(rCode)

            if ast.op == 'and':
                result.append(self.emit.emitANDOP(c.frame))
            else:
                result.append(self.emit.emitOROP(c.frame))
            result.append(self.emit.emitGOTO(labelN, c.frame))

            result.append(self.emit.emitLABEL(labelT, c.frame))
            result.append(self.emit.emitPUSHICONST("true", c.frame))
            result.append(self.emit.emitGOTO(labelN, c.frame))
            result.append(self.emit.emitLABEL(labelF, c.frame))
            result.append(self.emit.emitPUSHICONST("false", c.frame))

            result.append(self.emit.emitLABEL(labelN, c.frame))
            return ''.join(result), BoolType()

        lCode, lType = self.visit(ast.left, Access(c.frame, c.sym, False, False))
        rCode, rType = self.visit(ast.right, Access(c.frame, c.sym, False, False))
        
        if ast.op in ['+', '-']:
            return lCode + rCode + self.emit.emitADDOP(ast.op, NumberType(), c.frame), NumberType()
        elif ast.op in ['*', '/']:
            return lCode + rCode + self.emit.emitMULOP(ast.op, NumberType(), c.frame), NumberType()
        elif ast.op == '%':
            return lCode + rCode + self.emit.emitMOD(c.frame), NumberType()
        elif ast.op in ['=', '!=', '>', '>=', '<', '<=']:
            return lCode + rCode + self.emit.emitREOP(ast.op, c.frame), BoolType()
        elif ast.op == '==':
            return lCode + rCode + self.emit.emitREOP(ast.op, c.frame), BoolType()
        elif ast.op == '...':
            return lCode + rCode + self.emit.emitCONCAT(c.frame), StringType()
    
    def visitUnaryOp(self, ast, c):
        eCode, eType = self.visit(ast.operand, Access(c.frame, c.sym, False))
        if ast.op == '-':
            return eCode + self.emit.emitNEGOP(NumberType(), c.frame), NumberType()
        # eCode += self.emit.emitI2F(c.frame)
        elif ast.op == 'not':
            return eCode + self.emit.emitNOT(BoolType(), c.frame), BoolType()
        
    def visitReturn(self, ast, c):
        rettype = c.frame.returnType
        if type(rettype) is not VoidType:
            if type(ast.expr) is ArrayLiteral:
                self.emit.printout(self.emit.emitARRAY(rettype, c.frame))
                self.emit.printout(self.emit.emitDUP(c.frame))
            eCode, eType = self.visit(ast.expr, Access(c.frame, c.sym, False))
            self.emit.printout(eCode)
        self.emit.printout(self.emit.emitRETURN(rettype, c.frame))
        return True

    def visitIf(self, ast, c, need_to_infer_sym=[]):
        if_then_stmt = [(ast.expr, ast.thenStmt)] + ast.elifStmt
        labels = list(map(lambda x: c.frame.getNewLabel(), if_then_stmt))
        endLabel = c.frame.getNewLabel()
        has_return_stmt = False

        for block, nextLabel in zip(if_then_stmt, labels):
            self.emit.printout(self.visit(block[0], Access(c.frame, c.sym, False))[0])
            self.emit.printout(self.emit.emitIFFALSE(nextLabel, c.frame))

            if type(block[1]) is Block:
                has_return_stmt = self.visitBlock(block[1], SubBody(c.frame, c.sym), need_to_infer_sym)
            else:
                has_return_stmt = self.visit(block[1], SubBody(c.frame, c.sym))
            if not has_return_stmt:
                self.emit.printout(self.emit.emitGOTO(endLabel, c.frame))
            self.emit.printout(self.emit.emitLABEL(nextLabel, c.frame))

        if ast.elseStmt:
            if type(ast.elseStmt) is Block:
                has_return_stmt = (self.visitBlock(ast.elseStmt, SubBody(c.frame, c.sym), need_to_infer_sym)) \
                                    and has_return_stmt
            else:
                has_return_stmt = (self.visit(ast.elseStmt, SubBody(c.frame, c.sym))) and has_return_stmt
        
        self.emit.printout(self.emit.emitLABEL(endLabel, c.frame))
        return has_return_stmt
    
    def visitIfHelp(self, ast, c):
        need_to_infer_sym = []
        if type(ast.thenStmt) is Return:
            if type(ast.thenStmt.expr) is ArrayLiteral:
                access = Access(c.frame, c.sym, isLeft=False, isFirst=False)
                typ = self.visitArrayLiteral(ast.thenStmt.expr, access, True)[-1]
                return True, typ, []
            else:
                if ast.thenStmt.expr is not None:
                    typ = self.visit(ast.thenStmt.expr, c)[1]
                    return True, typ, []
                else:
                    return True, VoidType(), []
        elif type(ast.thenStmt) is Block:
            access = Access(c.frame, c.sym, isLeft=False, isFirst=False)
            return_typ, more_infer = self.infer_func_type(c.sym, ast.thenStmt, access, True) 
            need_to_infer_sym += more_infer
            if type(return_typ) is not VoidType:
                return True, return_typ, need_to_infer_sym
            
        for stmt in ast.elifStmt:
            if type(stmt[1]) is Return:
                if type(stmt[1].expr) is ArrayLiteral:
                    access = Access(c.frame, c.sym, isLeft=False, isFirst=False)
                    typ = self.visitArrayLiteral(ast.thenStmt.expr, access, True)[-1]
                    return True, typ, []
                else:
                    if stmt[1].expr is not None:
                        typ = self.visit(stmt[1].expr, c)[1]
                        return True, typ, []
                    else:
                        return True, VoidType(), []
            elif type(stmt[1]) is Block:
                access = Access(c.frame, c.sym, isLeft=False, isFirst=False)
                return_typ, more_infer = self.infer_func_type(c.sym, stmt[1], access, True) 
                need_to_infer_sym += more_infer
                if type(return_typ) is not VoidType:
                    return True, return_typ, need_to_infer_sym

        if type(ast.elseStmt) is Return:
            if type(ast.elseStmt.expr) is ArrayLiteral:
                access = Access(c.frame, c.sym, isLeft=False, isFirst=False)
                typ = self.visitArrayLiteral(ast.elseStmt.expr, access, True)[-1]
                return True, typ, []
            else:
                if ast.elseStmt.expr is not None:
                    typ = self.visit(ast.elseStmt.expr, c)[1]
                    return True, typ, []
                else:
                    return True, VoidType(), []
        elif type(ast.elseStmt) is Block:
            access = Access(c.frame, c.sym, isLeft=False, isFirst=False)
            return_typ, more_infer = self.infer_func_type(c.sym, ast.elseStmt, access, True) 
            need_to_infer_sym += more_infer
            if type(return_typ) is not VoidType:
                return True, return_typ, more_infer
        return False, None, need_to_infer_sym
    
    def visitFor(self, ast, c, need_to_infer_sym=[]):
        cond_expr_code, _ = self.visit(ast.condExpr, Access(c.frame, c.sym, False))
        upd_expr_code, _ = self.visit(ast.updExpr, Access(c.frame, c.sym, False))
        for_write_code, _ = self.visit(ast.name, Access(c.frame, c.sym, True))
        for_read_code, _ = self.visit(ast.name, Access(c.frame, c.sym, False))

        temp_index = c.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(temp_index, "for", NumberType(), c.frame.getStartLabel(), c.frame.getEndLabel(), c.frame))
        self.emit.printout(for_read_code)
        self.emit.printout(self.emit.emitWRITEVAR("for", NumberType(), temp_index, c.frame))

        c.frame.enterLoop()
        initLabel = c.frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(initLabel, c.frame))

        self.emit.printout(cond_expr_code)
        self.emit.printout(self.emit.emitIFTRUE(c.frame.getBreakLabel(), c.frame))

        if type(ast.body) is Block:
            has_return_stmt = self.visitBlock(ast.body, SubBody(c.frame, c.sym), need_to_infer_sym)
        else:
            has_return_stmt = self.visit(ast.body, SubBody(c.frame, c.sym))
        if not has_return_stmt:
            self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))

        self.emit.printout(self.emit.emitLABEL(c.frame.getContinueLabel(), c.frame))
        self.emit.printout(for_read_code)
        self.emit.printout(upd_expr_code)
        self.emit.printout(self.emit.emitADDOP('+', NumberType(), c.frame))
        self.emit.printout(for_write_code)
        
        self.emit.printout(self.emit.emitGOTO(initLabel, c.frame))
        self.emit.printout(self.emit.emitLABEL(c.frame.getBreakLabel(), c.frame))
        c.frame.exitLoop()

        self.emit.printout(self.emit.emitREADVAR("for", NumberType(), temp_index, c.frame))
        self.emit.printout(for_write_code)

    def visitForHelp(self, ast, c):
        need_to_infer_sym = []
        if type(ast.body) is Return:
            if type(ast.body.expr) is ArrayLiteral:
                access = Access(c.frame, c.sym, isLeft=False, isFirst=False)
                typ = self.visitArrayLiteral(ast.body.expr, access, True)[-1]
                return True, typ, []
            else:
                if ast.body.expr is not None:
                    typ = self.visit(ast.body.expr, c)[1]
                    return True, typ, []
                else:
                    return True, VoidType(), []
        elif type(ast.body) is Block:
            access = Access(c.frame, c.sym, isLeft=False, isFirst=False)
            return_typ, more_infer = self.infer_func_type(c.sym, ast.body, access, True) 
            need_to_infer_sym += more_infer
            if type(return_typ) is not VoidType:
                return True, return_typ, need_to_infer_sym
        elif type(ast.body) is If:
            return self.visitIfHelp(ast.body, c)
        elif type(ast.body) is For:
            return self.visitForHelp(ast.body, c)
        return False, None, need_to_infer_sym

    def visitBlock(self, ast, c, need_to_infer_sym=[]):
        has_return_stmt = False
        temp = SubBody(c.frame, c.sym)
        c.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(c.frame.getStartLabel(), c.frame))
        for stmt in ast.stmt:
            if type(stmt) is Return:
                has_return_stmt = self.visit(stmt, temp) or has_return_stmt
            elif type(stmt) is If:
                has_return_stmt = self.visitIf(stmt, temp, need_to_infer_sym) or has_return_stmt
            elif type(stmt) is For:
                has_return_stmt = self.visitFor(stmt, temp, need_to_infer_sym) or has_return_stmt
            elif type(stmt) is Block:
                has_return_stmt = self.visitBlock(stmt, temp, need_to_infer_sym) or has_return_stmt
            elif type(stmt) is VarDecl:
                a = self.visitVarDecl(stmt, temp, False, need_to_infer_sym)
                temp = a
            else:
                self.visit(stmt, temp)
        self.emit.printout(self.emit.emitLABEL(c.frame.getEndLabel(), c.frame))
        c.frame.exitScope()
        return has_return_stmt

    def visitContinue(self, ast, c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))
    
    def visitBreak(self, ast, c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getBreakLabel(), c.frame))


