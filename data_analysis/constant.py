import sys

class Const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:  # 判断是否已经被赋值，如果是则报错
            raise self.ConstError("Can't change const.%s" % name)
        if not name.isupper():  # 判断所赋值是否是全部大写，用来做第一次赋值的格式判断，也可以根据需要改成其他判断条件
            raise self.ConstCaseError('const name "%s" is not all supercase' % name)

        self.__dict__[name] = value


const = Const()

# 判断数据类型的正则表达式
const.DATA_HEADER='(?P<header>@@@\s*\w{1,30}\s+\w{1,30}\s*\w{1,30})'

# Business Reject Event
const.DATE = '(?P<Date>\d{4}\d{4}-\d{2}:\d{2}:\d{2}.\d{1,9})'
const.INVACCTID = '(?P<invAcctId>invAcctId\[(.*?)\])'
const.CLSEQNO = '(?P<clSeqNo>clSeqNo\[(.*?)\])'
const.SECURITYID = '(?P<securityId>securityId\[(.*?)\])'
const.MKTID = '(?P<mktId>mktId\[(.*?)\])'
const.BSTYPE = '(?P<bsType>bsType\[(.*?)\])'
const.ORDQTY = '(?P<ordQty>ordQty\[(.*?)\])'
const.ORDPRICE = '(?P<ordPrice>ordPrice\[(.*?)\])'
const.ORIGCLSEQNO = '(?P<origClSeqNo>origClSeqNo\[(.*?)\])'
const.ORIGCLORDID = '(?P<origClOrdId>origClOrdId\[(.*?)\])'
const.SOURCEIP = '(?P<sourceIp>sourceIp\[(.*?)\])'
const.SOURCEMAC = '(?P<sourceMac>sourceMac\[(.*?)\])'
const.SOURCEDRIVER = '(?P<sourceDriver>sourceDriver\[(.*?)\])'
const.SOURCETYPE = '(?P<sourceType>sourceType\[(.*?)\])'
const.ORDREQORIGSENDTIME = '(?P<ordReqOrigSendTime>__ordReqOrigSendTime\[(.*?)\])'
const.ORDREQORIGRECVTIME = '(?P<ordReqOrigRecvTime>__ordReqOrigRecvTime\[(.*?)\])'
const.ORDREQCOLLECTEDTIME = '(?P<ordReqCollectedTime>__ordReqCollectedTime\[(.*?)\])'
const.ORDREQACTUALDEALTIME = '(?P<ordReqActualDealTime>__ordReqActualDealTime\[(.*?)\])'
const.ERRMSG = '(?<=errMsg\[)\d*'

# Order Report Event
const.CLORDID = '(?P<clOrdId>clOrdId\[(.*?)\])'
const.EXCHORDID = 'exchOrdId\[(.*?)\]'
const.ORDTYPE = '(?P<ordType>ordType\[(.*?)\])'
const.ORDSTATUS = '(?P<ordStatus>ordStatus\[(.*?)\])'
const.ORDCNFMSTS = '(?P<ordCnfmSts>ordCnfmSts\[(.*?)\])'
const.ORDTIME = '(?P<ordTime>ordTime\[(.*?)\])'
const.ORDCNFMTIME = '(?P<ordCnfmTime>ordCnfmTime\[(.*?)\])'
const.ORDREJREASON = '(?P<ordRejReason>ordRejReason\[(.*?)\])'
const.EXCHERRCODE = '(?P<exchErrCode>exchErrCode\[(.*?)\])'
const.EXECTYPE = '(?P<execType>execType\[(.*?)\])'
const.BRANCHORDSEQNO = '(?P<branchOrdSeqNo>branchOrdSeqNo\[(.*?)\])'
const.TGWGRPNO = '(?P<tgwGrpNo>__tgwGrpNo\[(.*?)\])'
const.TGWPARTITIONNO = '(?P<tgwPartitionNo>__tgwPartitionNo\[(.*?)\])'
const.ROWNUM = '(?P<rowNum>__rowNum\[(.*?)\])'
const.CUMQTY = '(?P<cumQty>cumQty\[(.*?)\])'
const.CUMAMT = '(?P<cumAmt>cumAmt\[(.*?)\])'
const.CUMINTEREST = '(?P<cumInterest>cumInterest\[(.*?)\])'
const.CUMFEE = '(?P<cumFee>cumFee\[(.*?)\])'
const.CANCELEDQTY = '(?P<canceledQty>canceledQty\[(.*?)\])'
const.ORDREQPROCESSEDTIME = '(?P<ordReqProcessedTime>__ordReqProcessedTime\[(.*?)\])'
const.ORDDECLARETIME = '(?P<ordDeclareTime>__ordDeclareTime\[(.*?)\])'
const.ORDDECLAREDONETIME = '(?P<ordDeclareDoneTime>__ordDeclareDoneTime\[(.*?)\])'
const.ORDCNFMORIGRECVTIME = '(?P<ordCnfmOrigRecvTime>__ordCnfmOrigRecvTime\[(.*?)\])'
const.ORDCNFMCOLLECTEDTIME = '(?P<ordCnfmCollectedTime>__ordCnfmCollectedTime\[(.*?)\])'
const.ORDCNFMACTUALDEALTIME = '(?P<ordCnfmActualDealTime>__ordCnfmActualDealTime\[(.*?)\])'
const.ORDCNFMPROCESSEDTIME = '(?P<ordCnfmProcessedTime>__ordCnfmProcessedTime\[(.*?)\])'
const.OCTOTALINTERNALLATENCY = '(?P<ocTotalInternalLatency>ocTotalInternalLatency\[(.*?)\])'
const.OCCOLLECTLATENCY = '(?P<ocCollectLatency>ocCollectLatency\[(.*?)\])'
const.OCPROCESSLATENCY = '(?P<ocProcessLatency>ocProcessLatency\[(.*?)\])'
const.OCPROCESSWAITLATENCY = '(?P<ocProcessWaitLatency>ocProcessWaitLatency\[(.*?)\])'
const.TOTALORDCNFMLATENCY = '(?P<totalOrdCnfmLatency>totalOrdCnfmLatency\[(.*?)\])'
const.TOTALORDDECLLATENCY = '(?P<totalOrdDeclLatency>totalOrdDeclLatency\[(.*?)\])'
const.TOTALORDRISKLATENCY = '(?P<totalOrdRiskLatency>totalOrdRiskLatency\[(.*?)\])'
const.WAITDECLARELATENCY = '(?P<waitDeclareLatency>waitDeclareLatency\[(.*?)\])'
const.DECLARELATENCY = '(?P<declareLatency>declareLatency\[(.*?)\])'
const.EXCHANGELATENCY = '(?P<exchangeLatency>exchangeLatency\[(.*?)\])'

# # Order Insert Event
const.FRZPRC = '(?P<frzPrc>frzPrc\[(.*?)\])'
const.FRZAMT = '(?P<frzAmt>frzAmt\[(.*?)\])'
const.FRZINTEREST = '(?P<frzInterest>frzInterest\[(.*?)\])'
const.FRZFEE = '(?P<frzFee>frzFee\[(.*?)\])'
const.FRZMARGIN = '(?P<frzMargin>frzMargin\[(.*?)\])'
const.ORIGRECNUM = '(?P<origRecNum>origRecNum\[(.*?)\])'
const.SECURITYTYPE = '(?P<securityType>securityType\[(.*?)\])'
const.SUBSECURITYTYPE = '(?P<subSecurityType>subSecurityType\[(.*?)\])'
const.RECNUM = '(?P<recNum>recNum\[(.*?)\])'
const.PLATFORMID = '(?P<platformId>__platformId\[(.*?)\])'
const.PBUID = '(?P<pbuId>pbuId\[(.*?)\])'
const.BRANCHID = '(?P<branchId>branchId\[(.*?)\])'
const.COLLECTLATENCY = '(?P<collectLatency>collectLatency\[(.*?)\])'
const.PROCESSLATENCY = '(?P<processLatency>processLatency\[(.*?)\])'
const.PROCESSWAITLATENCY = '(?P<processWaitLatency>processWaitLatency\[(.*?)\])'

# # Trade report Event
const.TRDSIDE = '(?P<trdSide>trdSide\[(.*?)\])'
const.EXCHTRDNUM = '(?P<exchTrdNum>exchTrdNum\[(.*?)\])'
const.TRDCNFMTYPE = '(?P<trdCnfmType>trdCnfmType\[(.*?)\])'
const.ETFTRDCNFMSEQ = '(?P<etfTrdCnfmSeq>etfTrdCnfmSeq\[(.*?)\])'
const.TRDTIME = '(?P<trdTime>trdTime\[(.*?)\])'
const.TRDQTY = '(?P<trdQty>trdQty\[(.*?)\])'
const.TRDPRICE = '(?P<trdPrice>trdPrice\[(.*?)\])'
const.TRDAMT = '(?P<trdAmt>trdAmt\[(.*?)\])'
const.TRDCNFMORIGRECVTIME = '(?P<trdCnfmOrigRecvTime>__trdCnfmOrigRecvTime\[(.*?)\])'
const.TRDCNFMCOLLECTEDTIME = '(?P<trdCnfmCollectedTime>__trdCnfmCollectedTime\[(.*?)\])'
const.TRDCNFMACTUALDEALTIME = '(?P<trdCnfmActualDealTime>__trdCnfmActualDealTime\[(.*?)\])'
const.TRDCNFMPROCESSEDTIME = '(?P<trdCnfmProcessedTime>__trdCnfmProcessedTime\[(.*?)\])'
const.TOTALINTERNALLATENCY = '(?P<totalInternalLatency>totalInternalLatency\[(.*?)\])'

# # FundTrsf Report Event
const.CASHACCTID = '(?P<cashAcctId>cashAcctId\[(.*?)\])'
const.DIRECT = '(?P<direct>direct\[(.*?)\])'
const.ISALLOTONLY = '(?P<isAllotOnly>isAllotOnly\[(.*?)\])'
const.OCCURAMT = '(?P<occurAmt>occurAmt\[(.*?)\])'
const.FUNDTRSFID = '(?P<fundTrsfId>fundTrsfId\[(.*?)\])'
const.COUNTERENTRUSTNO = '(?P<counterEntrustNo>counterEntrustNo\[(.*?)\])'
const.COUNTERALLOTNO = '(?P<counterAllotNo>counterAllotNo\[(.*?)\])'
const.OPERTIME = '(?P<operTime>operTime\[(.*?)\])'
const.DCLRTIME = '(?P<dclrTime>dclrTime\[(.*?)\])'
const.DONETIME = '(?P<doneTime>doneTime\[(.*?)\])'
const.TRSFSTATUS = '(?P<trsfStatus>trsfStatus\[(.*?)\])'
const.CNFMSTATUS = '(?P<cnfmStatus>cnfmStatus\[(.*?)\])'
const.BANKTRSFSTS = '(?P<bankTrsfSts>bankTrsfSts\[(.*?)\])'
const.BANKOCCURAMT = '(?P<bankOccurAmt>bankOccurAmt\[(.*?)\])'
const.CUSTID = '(?P<custId>custId\[(.*?)\])'
const.BANKID = '(?P<bankId>bankId\[(.*?)\])'
const.REJREASON = '(?P<rejReason>rejReason\[(.*?)\])'
const.COUNTERERRCODE = '(?P<counterErrCode>counterErrCode\[(.*?)\])'
const.ALLOTSERIALNO = '(?P<allotSerialNo>allotSerialNo\[(.*?)\])'
const.ERRORINFO = '(?P<errorInfo>errorInfo\[(.*?)\])'
const.HASCOUNTERTRANSFERED = '(?P<hasCounterTransfered>hasCounterTransfered\[(.*?)\])'

# # 四个不同的数据字段的表头
const.DATA_PART=['Business Reject Event','Order Report Event','Order Insert Event',
                 'Trade Report Event','FundTrsf Report Event']

const.HEADER_BUSINESS_REJECT = ['type', 'date', 'invAcctId','clSeqNo', 'securityId', 'mktId', 'bsType', 'ordType', 'ordQty',
                                'ordPrice','origClSeqNo','origClOrdId', 'ordReqOrigSendTime', 'ordReqOrigRecvTime',
                                'ordReqCollectedTime','ordReqActualDealTime','errMsg']

const.HEADER_ORDER_REPORT = ['type', 'date', 'invAcctId', 'clSeqNo', 'clOrdId', 'exchOrdId', 'securityId', 'mktId',
                             'bsType', 'ordType', 'ordStatus',
                             'ordCnfmSts', 'ordTime', 'ordCnfmTime', 'ordRejReason', 'exchErrCode', 'execType',
                             'origClSeqNo', 'origClOrdId',
                             'branchOrdSeqNo', 'recNum', 'platformId', 'tgwGrpNo', 'tgwPartitionNo', 'rowNum', 'cumQty',
                             'cumAmt', 'cumInterest',
                             'cumFee', 'canceledQty','ordReqOrigRecvTime', 'ordReqProcessedTime', 'ordDeclareTime',
                             'ordDeclareDoneTime', 'ordCnfmOrigRecvTime',
                             'ordCnfmCollectedTime', 'ordCnfmActualDealTime', 'ordCnfmProcessedTime',
                             'ocTotalInternalLatency',
                             'ocCollectLatency', 'ocProcessLatency', 'ocProcessWaitLatency', 'totalOrdCnfmLatency',
                             'totalOrdDeclLatency',
                             'totalOrdRiskLatency', 'waitDeclareLatency', 'declareLatency', 'exchangeLatency']

const.HEADER_ORDER_INSERT = ['type', 'date', 'invAcctId', 'clSeqNo', 'securityId', 'mktId', 'bsType', 'ordType',
                             'ordQty', 'ordPrice',
                             'frzPrc',
                             'frzAmt', 'frzInterest', 'frzFee', 'frzMargin', 'origClSeqNo', 'origClOrdId', 'origRecNum',
                             'ordTime', 'sourceIp', 'sourceMac', 'sourceDriver', 'sourceType', 'securityType',
                             'branchOrdSeqNo',
                             'recNum', 'platformId', 'tgwGrpNo', 'tgwPartitionNo', 'pbuId', 'branchId',
                             'ordReqOrigSendTime',
                             'ordReqOrigRecvTime',
                             'ordReqCollectedTime', 'ordReqActualDealTime', 'ordReqProcessedTime',
                             'totalInternalLatency',
                             'collectLatency',
                             'processLatency', 'processWaitLatency']

const.HEADER_TRADE_REPORT = ['type', 'date', 'invAcctId', 'clSeqNo', 'securityId', 'mktId', 'bsType',
                             'trdSide', 'exchTrdNum', 'platformId', 'trdCnfmType', 'etfTrdCnfmSeq',
                             'ordStatus', 'ordType', 'securityType', 'subSecurityType', 'trdTime',
                             'trdQty', 'trdPrice', 'trdAmt', 'cumQty', 'cumAmt', 'cumInterest', 'cumFee', 'rowNum',
                             'tgwGrpNo', 'tgwPartitionNo',
                             'pbuId', 'branchId', 'trdCnfmOrigRecvTime', 'trdCnfmCollectedTime', 'totalInternalLatency',
                             'collectLatency', 'processLatency',
                             'processWaitLatency']

const.HEADER_FOUND_REPORT = ['type', 'date', 'cashAcctId', 'clSeqNo', 'direct',
                             'isAllotOnly', 'occurAmt', 'fundTrsfId', 'counterEntrustNo',
                             'counterAllotNo', 'operTime', 'dclrTime', 'doneTime',
                             'trsfStatus', 'cnfmStatus', 'bankTrsfSts', 'bankOccurAmt', 'custId', 'bankId',
                             'rejReason', 'counterErrCode', 'allotSerialNo', 'errorInfo', 'hasCounterTransfered']

# # 正则表达式数组
const.PATTERNS_BUSINESS_REJECT = [const.DATE,const.INVACCTID,const.CLSEQNO, const.SECURITYID, const.MKTID, const.BSTYPE, const.ORDTYPE,
                                  const.ORDQTY,
                                  const.ORDPRICE, const.ORIGCLSEQNO, const.ORIGCLORDID, const.ORDREQORIGSENDTIME,
                                  const.ORDREQORIGRECVTIME,
                                  const.ORDREQCOLLECTEDTIME, const.ORDREQACTUALDEALTIME,const.ERRMSG]

const.PATTERNS_ORDER_REPORT = [const.DATE, const.INVACCTID, const.CLSEQNO, const.CLORDID, const.EXCHORDID,
                               const.SECURITYID, const.MKTID, const.BSTYPE, const.ORDTYPE, const.ORDSTATUS,
                               const.ORDCNFMSTS, const.ORDTIME, const.ORDCNFMTIME, const.ORDREJREASON,
                               const.EXCHERRCODE, const.EXECTYPE, const.ORIGCLSEQNO, const.ORIGCLORDID,
                               const.BRANCHORDSEQNO, const.RECNUM, const.PLATFORMID, const.TGWGRPNO,
                               const.TGWPARTITIONNO, const.ROWNUM, const.CUMQTY, const.CUMAMT, const.CUMINTEREST,
                               const.CUMFEE,const.CANCELEDQTY,const.ORDREQORIGRECVTIME, const.ORDREQPROCESSEDTIME, const.ORDDECLARETIME,
                               const.ORDDECLAREDONETIME, const.ORDCNFMORIGRECVTIME,
                               const.ORDCNFMCOLLECTEDTIME, const.ORDCNFMACTUALDEALTIME, const.ORDCNFMPROCESSEDTIME,
                               const.OCTOTALINTERNALLATENCY,
                               const.OCCOLLECTLATENCY, const.OCPROCESSLATENCY, const.OCPROCESSWAITLATENCY,
                               const.TOTALORDCNFMLATENCY, const.TOTALORDDECLLATENCY,
                               const.TOTALORDRISKLATENCY, const.WAITDECLARELATENCY, const.DECLARELATENCY,
                               const.EXCHANGELATENCY]

const.PATTERNS_ORDER_INSERT = [const.DATE, const.INVACCTID, const.CLSEQNO, const.SECURITYID, const.MKTID, const.BSTYPE,
                               const.ORDTYPE, const.ORDQTY, const.ORDPRICE,
                               const.FRZPRC, const.FRZAMT, const.FRZINTEREST, const.FRZFEE, const.FRZMARGIN,
                               const.ORIGCLSEQNO, const.ORIGCLORDID, const.ORIGRECNUM,
                               const.ORDTIME, const.SOURCEIP, const.SOURCEMAC, const.SOURCEDRIVER, const.SOURCETYPE,
                               const.SECURITYTYPE, const.BRANCHORDSEQNO,
                               const.RECNUM, const.PLATFORMID, const.TGWGRPNO, const.TGWPARTITIONNO, const.PBUID,
                               const.BRANCHID, const.ORDREQORIGSENDTIME,
                               const.ORDREQORIGRECVTIME, const.ORDREQCOLLECTEDTIME, const.ORDREQACTUALDEALTIME,
                               const.ORDREQPROCESSEDTIME,
                               const.TOTALINTERNALLATENCY, const.COLLECTLATENCY, const.PROCESSLATENCY,
                               const.PROCESSWAITLATENCY]

const.PATTERNS_TRADE_REPORT = [const.DATE, const.INVACCTID, const.CLSEQNO, const.SECURITYID, const.MKTID, const.BSTYPE,
                               const.TRDSIDE, const.EXCHTRDNUM, const.PLATFORMID,
                               const.TRDCNFMTYPE, const.ETFTRDCNFMSEQ, const.ORDSTATUS, const.ORDTYPE,
                               const.SECURITYTYPE, const.SUBSECURITYTYPE,
                               const.TRDTIME, const.TRDQTY, const.TRDPRICE, const.TRDAMT, const.CUMQTY, const.CUMAMT,
                               const.CUMINTEREST, const.CUMFEE, const.ROWNUM,
                               const.TGWGRPNO, const.TGWPARTITIONNO, const.PBUID, const.BRANCHID,
                               const.TRDCNFMORIGRECVTIME, const.TRDCNFMCOLLECTEDTIME,
                               const.TOTALINTERNALLATENCY, const.COLLECTLATENCY, const.PROCESSLATENCY,
                               const.PROCESSWAITLATENCY]

const.PATTERNS_FOUND_REPORT = [const.DATE, const.CASHACCTID, const.CLSEQNO, const.DIRECT,
                               const.ISALLOTONLY, const.OCCURAMT, const.FUNDTRSFID, const.COUNTERENTRUSTNO,
                               const.COUNTERALLOTNO, const.OPERTIME, const.DCLRTIME, const.DONETIME,
                               const.TRSFSTATUS, const.CNFMSTATUS, const.BANKTRSFSTS, const.BANKOCCURAMT, const.CUSTID,
                               const.BANKID,
                               const.REJREASON, const.COUNTERERRCODE, const.ALLOTSERIALNO, const.ERRORINFO,
                               const.HASCOUNTERTRANSFERED]

# 正则表示与表头的二维数组
const.MATCH_PATTERN = [const.PATTERNS_BUSINESS_REJECT, const.PATTERNS_ORDER_REPORT, const.PATTERNS_ORDER_INSERT,
                       const.PATTERNS_TRADE_REPORT, const.PATTERNS_FOUND_REPORT]
const.MATCH_HEADER = [const.HEADER_BUSINESS_REJECT, const.HEADER_ORDER_REPORT, const.HEADER_ORDER_INSERT,
                      const.HEADER_TRADE_REPORT, const.HEADER_FOUND_REPORT]

const.SQL_TABLE = ['Business_Reject_Event','Order_Report_Event','Order_Insert_Event','Trade_Report_Event','FundTrsf_Report_Event']


# file是原始数据位置，to—file为生成csv文件路径
const.FILE = './data'
const.TO_FILE = './csv/datass.csv'

#原始数据目录文件的最大深度
const.FILE_DEPTH = 2

# SQL_lite数据库名称
const.DB_NAME = 'test.db'

const.TIME_LIMIT = 93010000
const.CSV_PATH = './csv/'

const.START_TIME = 93000000
const.END_TIME = 103000000
const.RATE = 0.85