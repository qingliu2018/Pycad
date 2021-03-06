from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System import ValueType as _n_0_t_4
from __clrclasses__.System import Guid as _n_0_t_5
from __clrclasses__.System import Array as _n_0_t_6
from __clrclasses__.System import IntPtr as _n_0_t_7
from __clrclasses__.System import Byte as _n_0_t_8
import typing
class ADVF(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    ADVF_DATAONSTOP: int
    ADVF_NODATA: int
    ADVF_ONLYONCE: int
    ADVF_PRIMEFIRST: int
    ADVFCACHE_FORCEBUILTIN: int
    ADVFCACHE_NOHANDLER: int
    ADVFCACHE_ONSAVE: int
    value__: int
class BIND_OPTS(_n_0_t_4):
    cbStruct: int
    dwTickCountDeadline: int
    grfFlags: int
    grfMode: int
class BINDPTR(_n_0_t_4):
    lpfuncdesc: int
    lptcomp: int
    lpvardesc: int
class CALLCONV(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    CC_CDECL: int
    CC_MACPASCAL: int
    CC_MAX: int
    CC_MPWCDECL: int
    CC_MPWPASCAL: int
    CC_MSCPASCAL: int
    CC_PASCAL: int
    CC_RESERVED: int
    CC_STDCALL: int
    CC_SYSCALL: int
    value__: int
class CONNECTDATA(_n_0_t_4):
    dwCookie: int
    pUnk: int
class DATADIR(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    DATADIR_GET: int
    DATADIR_SET: int
    value__: int
class DESCKIND(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    DESCKIND_FUNCDESC: int
    DESCKIND_IMPLICITAPPOBJ: int
    DESCKIND_MAX: int
    DESCKIND_NONE: int
    DESCKIND_TYPECOMP: int
    DESCKIND_VARDESC: int
    value__: int
class DISPPARAMS(_n_0_t_4):
    cArgs: int
    cNamedArgs: int
    rgdispidNamedArgs: int
    rgvarg: int
class DVASPECT(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    DVASPECT_CONTENT: int
    DVASPECT_DOCPRINT: int
    DVASPECT_ICON: int
    DVASPECT_THUMBNAIL: int
    value__: int
class ELEMDESC(_n_0_t_4):
    desc: int
    tdesc: int
    class DESCUNION(_n_0_t_4):
        idldesc: int
        paramdesc: int
class EXCEPINFO(_n_0_t_4):
    bstrDescription: int
    bstrHelpFile: int
    bstrSource: int
    dwHelpContext: int
    pfnDeferredFillIn: int
    pvReserved: int
    scode: int
    wCode: int
    wReserved: int
class FILETIME(_n_0_t_4):
    dwHighDateTime: int
    dwLowDateTime: int
class FORMATETC(_n_0_t_4):
    cfFormat: int
    dwAspect: int
    lindex: int
    ptd: int
    tymed: int
class FUNCDESC(_n_0_t_4):
    callconv: int
    cParams: int
    cParamsOpt: int
    cScodes: int
    elemdescFunc: int
    funckind: int
    invkind: int
    lprgelemdescParam: int
    lprgscode: int
    memid: int
    oVft: int
    wFuncFlags: int
class FUNCFLAGS(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    FUNCFLAG_FBINDABLE: int
    FUNCFLAG_FDEFAULTBIND: int
    FUNCFLAG_FDEFAULTCOLLELEM: int
    FUNCFLAG_FDISPLAYBIND: int
    FUNCFLAG_FHIDDEN: int
    FUNCFLAG_FIMMEDIATEBIND: int
    FUNCFLAG_FNONBROWSABLE: int
    FUNCFLAG_FREPLACEABLE: int
    FUNCFLAG_FREQUESTEDIT: int
    FUNCFLAG_FRESTRICTED: int
    FUNCFLAG_FSOURCE: int
    FUNCFLAG_FUIDEFAULT: int
    FUNCFLAG_FUSESGETLASTERROR: int
    value__: int
class FUNCKIND(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    FUNC_DISPATCH: int
    FUNC_NONVIRTUAL: int
    FUNC_PUREVIRTUAL: int
    FUNC_STATIC: int
    FUNC_VIRTUAL: int
    value__: int
class IAdviseSink():
    def OnClose(self):...
    def OnDataChange(self, format: FORMATETC, stgmedium: STGMEDIUM):...
    def OnRename(self, moniker: IMoniker):...
    def OnSave(self):...
    def OnViewChange(self, aspect: int, index: int):...
class IBindCtx():
    def EnumObjectParam(self, ppenum: IEnumString):...
    def GetBindOptions(self, pbindopts: BIND_OPTS):...
    def GetObjectParam(self, pszKey: str, ppunk: object):...
    def GetRunningObjectTable(self, pprot: IRunningObjectTable):...
    def RegisterObjectBound(self, punk: object):...
    def RegisterObjectParam(self, pszKey: str, punk: object):...
    def ReleaseBoundObjects(self):...
    def RevokeObjectBound(self, punk: object):...
    def RevokeObjectParam(self, pszKey: str) -> int:...
    def SetBindOptions(self, pbindopts: BIND_OPTS):...
class IConnectionPoint():
    def Advise(self, pUnkSink: object, pdwCookie: int):...
    def EnumConnections(self, ppEnum: IEnumConnections):...
    def GetConnectionInterface(self, pIID: _n_0_t_5):...
    def GetConnectionPointContainer(self, ppCPC: IConnectionPointContainer):...
    def Unadvise(self, dwCookie: int):...
class IConnectionPointContainer():
    def EnumConnectionPoints(self, ppEnum: IEnumConnectionPoints):...
    def FindConnectionPoint(self, riid: _n_0_t_5, ppCP: IConnectionPoint):...
class IDataObject():
    def DAdvise(self, pFormatetc: FORMATETC, advf: ADVF, adviseSink: IAdviseSink, connection: int) -> int:...
    def DUnadvise(self, connection: int):...
    def EnumDAdvise(self, enumAdvise: IEnumSTATDATA) -> int:...
    def EnumFormatEtc(self, direction: DATADIR) -> IEnumFORMATETC:...
    def GetCanonicalFormatEtc(self, formatIn: FORMATETC, formatOut: FORMATETC) -> int:...
    def GetData(self, format: FORMATETC, medium: STGMEDIUM):...
    def GetDataHere(self, format: FORMATETC, medium: STGMEDIUM):...
    def QueryGetData(self, format: FORMATETC) -> int:...
    def SetData(self, formatIn: FORMATETC, medium: STGMEDIUM, release: bool):...
class IDLDESC(_n_0_t_4):
    dwReserved: int
    wIDLFlags: int
class IDLFLAG(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    IDLFLAG_FIN: int
    IDLFLAG_FLCID: int
    IDLFLAG_FOUT: int
    IDLFLAG_FRETVAL: int
    IDLFLAG_NONE: int
    value__: int
class IEnumConnectionPoints():
    def Clone(self, ppenum: IEnumConnectionPoints):...
    def Next(self, celt: int, rgelt: _n_0_t_6[IConnectionPoint], pceltFetched: _n_0_t_7) -> int:...
    def Reset(self):...
    def Skip(self, celt: int) -> int:...
class IEnumConnections():
    def Clone(self, ppenum: IEnumConnections):...
    def Next(self, celt: int, rgelt: _n_0_t_6[CONNECTDATA], pceltFetched: _n_0_t_7) -> int:...
    def Reset(self):...
    def Skip(self, celt: int) -> int:...
class IEnumFORMATETC():
    def Clone(self, newEnum: IEnumFORMATETC):...
    def Next(self, celt: int, rgelt: _n_0_t_6[FORMATETC], pceltFetched: _n_0_t_6[int]) -> int:...
    def Reset(self) -> int:...
    def Skip(self, celt: int) -> int:...
class IEnumMoniker():
    def Clone(self, ppenum: IEnumMoniker):...
    def Next(self, celt: int, rgelt: _n_0_t_6[IMoniker], pceltFetched: _n_0_t_7) -> int:...
    def Reset(self):...
    def Skip(self, celt: int) -> int:...
class IEnumSTATDATA():
    def Clone(self, newEnum: IEnumSTATDATA):...
    def Next(self, celt: int, rgelt: _n_0_t_6[STATDATA], pceltFetched: _n_0_t_6[int]) -> int:...
    def Reset(self) -> int:...
    def Skip(self, celt: int) -> int:...
class IEnumString():
    def Clone(self, ppenum: IEnumString):...
    def Next(self, celt: int, rgelt: _n_0_t_6[str], pceltFetched: _n_0_t_7) -> int:...
    def Reset(self):...
    def Skip(self, celt: int) -> int:...
class IEnumVARIANT():
    def Clone(self) -> IEnumVARIANT:...
    def Next(self, celt: int, rgVar: _n_0_t_6[object], pceltFetched: _n_0_t_7) -> int:...
    def Reset(self) -> int:...
    def Skip(self, celt: int) -> int:...
class IMoniker():
    def BindToObject(self, pbc: IBindCtx, pmkToLeft: IMoniker, riidResult: _n_0_t_5, ppvResult: object):...
    def BindToStorage(self, pbc: IBindCtx, pmkToLeft: IMoniker, riid: _n_0_t_5, ppvObj: object):...
    def CommonPrefixWith(self, pmkOther: IMoniker, ppmkPrefix: IMoniker):...
    def ComposeWith(self, pmkRight: IMoniker, fOnlyIfNotGeneric: bool, ppmkComposite: IMoniker):...
    def Enum(self, fForward: bool, ppenumMoniker: IEnumMoniker):...
    def GetClassID(self, pClassID: _n_0_t_5):...
    def GetDisplayName(self, pbc: IBindCtx, pmkToLeft: IMoniker, ppszDisplayName: str):...
    def GetSizeMax(self, pcbSize: int):...
    def GetTimeOfLastChange(self, pbc: IBindCtx, pmkToLeft: IMoniker, pFileTime: FILETIME):...
    def Hash(self, pdwHash: int):...
    def Inverse(self, ppmk: IMoniker):...
    def IsDirty(self) -> int:...
    def IsEqual(self, pmkOtherMoniker: IMoniker) -> int:...
    def IsRunning(self, pbc: IBindCtx, pmkToLeft: IMoniker, pmkNewlyRunning: IMoniker) -> int:...
    def IsSystemMoniker(self, pdwMksys: int) -> int:...
    def Load(self, pStm: IStream):...
    def ParseDisplayName(self, pbc: IBindCtx, pmkToLeft: IMoniker, pszDisplayName: str, pchEaten: int, ppmkOut: IMoniker):...
    def Reduce(self, pbc: IBindCtx, dwReduceHowFar: int, ppmkToLeft: IMoniker, ppmkReduced: IMoniker):...
    def RelativePathTo(self, pmkOther: IMoniker, ppmkRelPath: IMoniker):...
    def Save(self, pStm: IStream, fClearDirty: bool):...
class IMPLTYPEFLAGS(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    IMPLTYPEFLAG_FDEFAULT: int
    IMPLTYPEFLAG_FDEFAULTVTABLE: int
    IMPLTYPEFLAG_FRESTRICTED: int
    IMPLTYPEFLAG_FSOURCE: int
    value__: int
class INVOKEKIND(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    INVOKE_FUNC: int
    INVOKE_PROPERTYGET: int
    INVOKE_PROPERTYPUT: int
    INVOKE_PROPERTYPUTREF: int
    value__: int
class IPersistFile():
    def GetClassID(self, pClassID: _n_0_t_5):...
    def GetCurFile(self, ppszFileName: str):...
    def IsDirty(self) -> int:...
    def Load(self, pszFileName: str, dwMode: int):...
    def Save(self, pszFileName: str, fRemember: bool):...
    def SaveCompleted(self, pszFileName: str):...
class IRunningObjectTable():
    def EnumRunning(self, ppenumMoniker: IEnumMoniker):...
    def GetObject(self, pmkObjectName: IMoniker, ppunkObject: object) -> int:...
    def GetTimeOfLastChange(self, pmkObjectName: IMoniker, pfiletime: FILETIME) -> int:...
    def IsRunning(self, pmkObjectName: IMoniker) -> int:...
    def NoteChangeTime(self, dwRegister: int, pfiletime: FILETIME):...
    def Register(self, grfFlags: int, punkObject: object, pmkObjectName: IMoniker) -> int:...
    def Revoke(self, dwRegister: int):...
class IStream():
    def Clone(self, ppstm: IStream):...
    def Commit(self, grfCommitFlags: int):...
    def CopyTo(self, pstm: IStream, cb: int, pcbRead: _n_0_t_7, pcbWritten: _n_0_t_7):...
    def LockRegion(self, libOffset: int, cb: int, dwLockType: int):...
    def Read(self, pv: _n_0_t_6[_n_0_t_8], cb: int, pcbRead: _n_0_t_7):...
    def Revert(self):...
    def Seek(self, dlibMove: int, dwOrigin: int, plibNewPosition: _n_0_t_7):...
    def SetSize(self, libNewSize: int):...
    def Stat(self, pstatstg: STATSTG, grfStatFlag: int):...
    def UnlockRegion(self, libOffset: int, cb: int, dwLockType: int):...
    def Write(self, pv: _n_0_t_6[_n_0_t_8], cb: int, pcbWritten: _n_0_t_7):...
class ITypeComp():
    def Bind(self, szName: str, lHashVal: int, wFlags: int, ppTInfo: ITypeInfo, pDescKind: DESCKIND, pBindPtr: BINDPTR):...
    def BindType(self, szName: str, lHashVal: int, ppTInfo: ITypeInfo, ppTComp: ITypeComp):...
class ITypeInfo():
    def AddressOfMember(self, memid: int, invKind: INVOKEKIND, ppv: _n_0_t_7):...
    def CreateInstance(self, pUnkOuter: object, riid: _n_0_t_5, ppvObj: object):...
    def GetContainingTypeLib(self, ppTLB: ITypeLib, pIndex: int):...
    def GetDllEntry(self, memid: int, invKind: INVOKEKIND, pBstrDllName: _n_0_t_7, pBstrName: _n_0_t_7, pwOrdinal: _n_0_t_7):...
    def GetDocumentation(self, index: int, strName: str, strDocString: str, dwHelpContext: int, strHelpFile: str):...
    def GetFuncDesc(self, index: int, ppFuncDesc: _n_0_t_7):...
    def GetIDsOfNames(self, rgszNames: _n_0_t_6[str], cNames: int, pMemId: _n_0_t_6[int]):...
    def GetImplTypeFlags(self, index: int, pImplTypeFlags: IMPLTYPEFLAGS):...
    def GetMops(self, memid: int, pBstrMops: str):...
    def GetNames(self, memid: int, rgBstrNames: _n_0_t_6[str], cMaxNames: int, pcNames: int):...
    def GetRefTypeInfo(self, hRef: int, ppTI: ITypeInfo):...
    def GetRefTypeOfImplType(self, index: int, href: int):...
    def GetTypeAttr(self, ppTypeAttr: _n_0_t_7):...
    def GetTypeComp(self, ppTComp: ITypeComp):...
    def GetVarDesc(self, index: int, ppVarDesc: _n_0_t_7):...
    def Invoke(self, pvInstance: object, memid: int, wFlags: int, pDispParams: DISPPARAMS, pVarResult: _n_0_t_7, pExcepInfo: _n_0_t_7, puArgErr: int):...
    def ReleaseFuncDesc(self, pFuncDesc: _n_0_t_7):...
    def ReleaseTypeAttr(self, pTypeAttr: _n_0_t_7):...
    def ReleaseVarDesc(self, pVarDesc: _n_0_t_7):...
class ITypeInfo2(ITypeInfo):
    def GetAllCustData(self, pCustData: _n_0_t_7):...
    def GetAllFuncCustData(self, index: int, pCustData: _n_0_t_7):...
    def GetAllImplTypeCustData(self, index: int, pCustData: _n_0_t_7):...
    def GetAllParamCustData(self, indexFunc: int, indexParam: int, pCustData: _n_0_t_7):...
    def GetAllVarCustData(self, index: int, pCustData: _n_0_t_7):...
    def GetCustData(self, guid: _n_0_t_5, pVarVal: object):...
    def GetDocumentation2(self, memid: int, pbstrHelpString: str, pdwHelpStringContext: int, pbstrHelpStringDll: str):...
    def GetFuncCustData(self, index: int, guid: _n_0_t_5, pVarVal: object):...
    def GetFuncIndexOfMemId(self, memid: int, invKind: INVOKEKIND, pFuncIndex: int):...
    def GetImplTypeCustData(self, index: int, guid: _n_0_t_5, pVarVal: object):...
    def GetParamCustData(self, indexFunc: int, indexParam: int, guid: _n_0_t_5, pVarVal: object):...
    def GetTypeFlags(self, pTypeFlags: int):...
    def GetTypeKind(self, pTypeKind: TYPEKIND):...
    def GetVarCustData(self, index: int, guid: _n_0_t_5, pVarVal: object):...
    def GetVarIndexOfMemId(self, memid: int, pVarIndex: int):...
class ITypeLib():
    def FindName(self, szNameBuf: str, lHashVal: int, ppTInfo: _n_0_t_6[ITypeInfo], rgMemId: _n_0_t_6[int], pcFound: int):...
    def GetDocumentation(self, index: int, strName: str, strDocString: str, dwHelpContext: int, strHelpFile: str):...
    def GetLibAttr(self, ppTLibAttr: _n_0_t_7):...
    def GetTypeComp(self, ppTComp: ITypeComp):...
    def GetTypeInfo(self, index: int, ppTI: ITypeInfo):...
    def GetTypeInfoCount(self) -> int:...
    def GetTypeInfoOfGuid(self, guid: _n_0_t_5, ppTInfo: ITypeInfo):...
    def GetTypeInfoType(self, index: int, pTKind: TYPEKIND):...
    def IsName(self, szNameBuf: str, lHashVal: int) -> bool:...
    def ReleaseTLibAttr(self, pTLibAttr: _n_0_t_7):...
class ITypeLib2(ITypeLib):
    def GetAllCustData(self, pCustData: _n_0_t_7):...
    def GetCustData(self, guid: _n_0_t_5, pVarVal: object):...
    def GetDocumentation2(self, index: int, pbstrHelpString: str, pdwHelpStringContext: int, pbstrHelpStringDll: str):...
    def GetLibStatistics(self, pcUniqueNames: _n_0_t_7, pcchUniqueNames: int):...
class LIBFLAGS(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    LIBFLAG_FCONTROL: int
    LIBFLAG_FHASDISKIMAGE: int
    LIBFLAG_FHIDDEN: int
    LIBFLAG_FRESTRICTED: int
    value__: int
class PARAMDESC(_n_0_t_4):
    lpVarValue: int
    wParamFlags: int
class PARAMFLAG(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    PARAMFLAG_FHASCUSTDATA: int
    PARAMFLAG_FHASDEFAULT: int
    PARAMFLAG_FIN: int
    PARAMFLAG_FLCID: int
    PARAMFLAG_FOPT: int
    PARAMFLAG_FOUT: int
    PARAMFLAG_FRETVAL: int
    PARAMFLAG_NONE: int
    value__: int
class STATDATA(_n_0_t_4):
    advf: int
    advSink: int
    connection: int
    formatetc: int
class STATSTG(_n_0_t_4):
    atime: int
    cbSize: int
    clsid: int
    ctime: int
    grfLocksSupported: int
    grfMode: int
    grfStateBits: int
    mtime: int
    pwcsName: int
    reserved: int
    type: int
class STGMEDIUM(_n_0_t_4):
    pUnkForRelease: int
    tymed: int
    unionmember: int
class SYSKIND(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    SYS_MAC: int
    SYS_WIN16: int
    SYS_WIN32: int
    SYS_WIN64: int
    value__: int
class TYMED(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    TYMED_ENHMF: int
    TYMED_FILE: int
    TYMED_GDI: int
    TYMED_HGLOBAL: int
    TYMED_ISTORAGE: int
    TYMED_ISTREAM: int
    TYMED_MFPICT: int
    TYMED_NULL: int
    value__: int
class TYPEATTR(_n_0_t_4):
    cbAlignment: int
    cbSizeInstance: int
    cbSizeVft: int
    cFuncs: int
    cImplTypes: int
    cVars: int
    dwReserved: int
    guid: int
    idldescType: int
    lcid: int
    lpstrSchema: int
    MEMBER_ID_NIL: int
    memidConstructor: int
    memidDestructor: int
    tdescAlias: int
    typekind: int
    wMajorVerNum: int
    wMinorVerNum: int
    wTypeFlags: int
class TYPEDESC(_n_0_t_4):
    lpValue: int
    vt: int
class TYPEFLAGS(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    TYPEFLAG_FAGGREGATABLE: int
    TYPEFLAG_FAPPOBJECT: int
    TYPEFLAG_FCANCREATE: int
    TYPEFLAG_FCONTROL: int
    TYPEFLAG_FDISPATCHABLE: int
    TYPEFLAG_FDUAL: int
    TYPEFLAG_FHIDDEN: int
    TYPEFLAG_FLICENSED: int
    TYPEFLAG_FNONEXTENSIBLE: int
    TYPEFLAG_FOLEAUTOMATION: int
    TYPEFLAG_FPREDECLID: int
    TYPEFLAG_FPROXY: int
    TYPEFLAG_FREPLACEABLE: int
    TYPEFLAG_FRESTRICTED: int
    TYPEFLAG_FREVERSEBIND: int
    value__: int
class TYPEKIND(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    TKIND_ALIAS: int
    TKIND_COCLASS: int
    TKIND_DISPATCH: int
    TKIND_ENUM: int
    TKIND_INTERFACE: int
    TKIND_MAX: int
    TKIND_MODULE: int
    TKIND_RECORD: int
    TKIND_UNION: int
    value__: int
class TYPELIBATTR(_n_0_t_4):
    guid: int
    lcid: int
    syskind: int
    wLibFlags: int
    wMajorVerNum: int
    wMinorVerNum: int
class VARDESC(_n_0_t_4):
    desc: int
    elemdescVar: int
    lpstrSchema: int
    memid: int
    varkind: int
    wVarFlags: int
    class DESCUNION(_n_0_t_4):
        lpvarValue: int
        oInst: int
class VARFLAGS(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    value__: int
    VARFLAG_FBINDABLE: int
    VARFLAG_FDEFAULTBIND: int
    VARFLAG_FDEFAULTCOLLELEM: int
    VARFLAG_FDISPLAYBIND: int
    VARFLAG_FHIDDEN: int
    VARFLAG_FIMMEDIATEBIND: int
    VARFLAG_FNONBROWSABLE: int
    VARFLAG_FREADONLY: int
    VARFLAG_FREPLACEABLE: int
    VARFLAG_FREQUESTEDIT: int
    VARFLAG_FRESTRICTED: int
    VARFLAG_FSOURCE: int
    VARFLAG_FUIDEFAULT: int
class VARKIND(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    value__: int
    VAR_CONST: int
    VAR_DISPATCH: int
    VAR_PERINSTANCE: int
    VAR_STATIC: int
