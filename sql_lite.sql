

DROP TABLE IF EXISTS `Business_Reject_Event`;


CREATE TABLE `Business_Reject_Event` (
  `date` date DEFAULT NULL,
  `invAcctId` int(64) DEFAULT NULL,
  `clSeqNo` varchar(20) DEFAULT NULL,
  `securityId` int(64) DEFAULT NULL,
  `mktId` int(64) DEFAULT NULL,
  `bsType` int(64) DEFAULT NULL,
  `ordType` int(64) DEFAULT NULL,
  `ordQty` int(64) DEFAULT NULL,
  `ordPrice` numeric(128,64) DEFAULT NULL,
  `origClSeqNo` varchar(30) DEFAULT NULL,
  `origClOrdId` int(64) DEFAULT NULL,
  `ordReqOrigSendTime` numeric(128,64) DEFAULT NULL,
  `ordReqOrigRecvTime` numeric(128,64) DEFAULT NULL,
  `ordReqCollectedTime` numeric(128,64) DEFAULT NULL,
  `ordReqActualDealTime` numeric(128,64) DEFAULT NULL,
  `errMsg` int(64) DEFAULT NULL
);


DROP TABLE IF EXISTS `Order_Report_Event`;

CREATE TABLE `Order_Report_Event` (
  `date` date DEFAULT NULL,
  `invAcctId` int(64) DEFAULT NULL,
  `clSeqNo` varchar(30) DEFAULT NULL,
  `clOrdId` int(64) DEFAULT NULL,
  `exchOrdId` numeric(128,64) DEFAULT NULL,
  `securityId` int(64) DEFAULT NULL,
  `mktId` int(64) DEFAULT NULL,
  `bsType` int(64) DEFAULT NULL,
  `ordType` int(64) DEFAULT NULL,
  `ordStatus` int(64) DEFAULT NULL,
  `ordCnfmSts` int(64) DEFAULT NULL,
  `ordTime` int(64) DEFAULT NULL,
  `ordCnfmTime` int(64) DEFAULT NULL,
  `ordRejReason` int(64) DEFAULT NULL,
  `exchErrCode` int(64) DEFAULT NULL,
  `execType` int(64) DEFAULT NULL,
  `origClSeqNo` int(64) DEFAULT NULL,
  `origClOrdId` varchar(30) DEFAULT NULL,
  `branchOrdSeqNo` int(64) DEFAULT NULL,
  `recNum` int(64) DEFAULT NULL,
  `platformId` int(64) DEFAULT NULL,
  `tgwGrpNo` int(64) DEFAULT NULL,
  `tgwPartitionNo` int(64) DEFAULT NULL,
  `rowNum` int(64) DEFAULT NULL,
  `cumQty` int(64) DEFAULT NULL,
  `cumAmt` int(64) DEFAULT NULL,
  `cumInterest` int(64) DEFAULT NULL,
  `cumFee` int(64) DEFAULT NULL,
  `canceledQty` int(64) DEFAULT NULL,
  `ordReqOrigRecvTime` numeric(128,64) DEFAULT NULL,
  `ordReqProcessedTime` numeric(128,64) DEFAULT NULL,
  `ordDeclareTime` numeric(128,64) DEFAULT NULL,
  `ordDeclareDoneTime` numeric(128,64) DEFAULT NULL,
  `ordCnfmOrigRecvTime` numeric(128,64) DEFAULT NULL,
  `ordCnfmCollectedTime` numeric(128,64) DEFAULT NULL,
  `ordCnfmActualDealTime` numeric(128,64) DEFAULT NULL,
  `ordCnfmProcessedTime` numeric(128,64) DEFAULT NULL,
  `ocTotalInternalLatency` int(64) DEFAULT NULL,
  `ocCollectLatency` int(64) DEFAULT NULL,
  `ocProcessLatency` int(64) DEFAULT NULL,
  `ocProcessWaitLatency` int(64) DEFAULT NULL,
  `totalOrdCnfmLatency` int(64) DEFAULT NULL,
  `totalOrdDeclLatency` int(64) DEFAULT NULL,
  `totalOrdRiskLatency` int(64) DEFAULT NULL,
  `waitDeclareLatency` int(64) DEFAULT NULL,
  `declareLatency` int(64) DEFAULT NULL,
  `exchangeLatency` int(64) DEFAULT NULL

);


DROP TABLE IF EXISTS `Order_Insert_Event`;

CREATE TABLE `Order_Insert_Event` (
  `date` date DEFAULT NULL,
  `invAcctId` int(64) DEFAULT NULL,
  `clSeqNo` varchar(30) DEFAULT NULL,
  `securityId` int(64) DEFAULT NULL,
  `mktId` int(64) DEFAULT NULL,
  `bsType` int(64) DEFAULT NULL,
  `ordType` int(64) DEFAULT NULL,
  `ordQty` int(64) DEFAULT NULL,
  `ordPrice` int(64) DEFAULT NULL,
  `frzPrc` int(64) DEFAULT NULL,
  `frzAmt` int(64) DEFAULT NULL,
  `frzInterest` int(64) DEFAULT NULL,
  `frzFee` int(64) DEFAULT NULL,
  `frzMargin` int(64) DEFAULT NULL,
  `origClSeqNo` int(64) DEFAULT NULL,
  `origClOrdId` int(64) DEFAULT NULL,
  `origRecNum` int(64) DEFAULT NULL,
  `ordTime` int(64) DEFAULT NULL,
  `sourceIp` int(64) DEFAULT NULL,
  `sourceMac` varchar(30) DEFAULT NULL,
  `sourceDriver` int(64) DEFAULT NULL,
  `sourceType` int(64) DEFAULT NULL,
  `securityType` int(64) DEFAULT NULL,
  `branchOrdSeqNo` int(64) DEFAULT NULL,                
  `recNum` int(64) DEFAULT NULL,
  `platformId` int(64) DEFAULT NULL,
  `tgwGrpNo` int(64) DEFAULT NULL,
  `tgwPartitionNo` int(64) DEFAULT NULL,
  `pbuId` int(64) DEFAULT NULL,
  `branchId` numeric(128,64) DEFAULT NULL,
  `ordReqOrigSendTime` numeric(128,64) DEFAULT NULL,
  `ordReqOrigRecvTime` numeric(128,64) DEFAULT NULL,
  `ordReqCollectedTime` numeric(128,64) DEFAULT NULL,
  `ordReqActualDealTime` numeric(128,64) DEFAULT NULL,
  `ordReqProcessedTime` numeric(128,64) DEFAULT NULL,
  `totalInternalLatency` numeric(128,64) DEFAULT NULL,
  `collectLatency` numeric(128,64) DEFAULT NULL,
  `processLatency` int(64) DEFAULT NULL,
  `processWaitLatency` int(64) DEFAULT NULL

);


DROP TABLE IF EXISTS `FundTrsf_Report_Event`;
CREATE TABLE `FundTrsf_Report_Event` (
  `date` date DEFAULT NULL,
  `cashAcctId` int(64) DEFAULT NULL,
  `clSeqNo` int(64) DEFAULT NULL,
  `direct` int(64) DEFAULT NULL,
  `isAllotOnly` int(64) DEFAULT NULL,
  `occurAmt` int(64) DEFAULT NULL,
  `fundTrsfId` int(64) DEFAULT NULL,
  `counterEntrustNo` int(64) DEFAULT NULL,
  `counterAllotNo` int(64) DEFAULT NULL,
  `operTime` int(64) DEFAULT NULL,
  `dclrTime` int(64) DEFAULT NULL,
  `doneTime` int(64) DEFAULT NULL,
  `trsfStatus` int(64) DEFAULT NULL,
  `cnfmStatus` int(64) DEFAULT NULL,
  `bankTrsfSts` int(64) DEFAULT NULL,
  `bankOccurAmt` int(64) DEFAULT NULL,
  `custId` int(64) DEFAULT NULL,
  `bankId` int(64) DEFAULT NULL,
  `rejReason` int(64) DEFAULT NULL,
  `counterErrCode` int(64) DEFAULT NULL,
  `allotSerialNo` int(64) DEFAULT NULL,
  `errorInfo` numeric(128,64) DEFAULT NULL,
  `hasCounterTransfered` int(64) DEFAULT NULL

);

DROP TABLE IF EXISTS `Trade_Report_Event`;
CREATE TABLE `Trade_Report_Event` (
  `date` date DEFAULT NULL,
  `invAcctId` int(64) DEFAULT NULL,
  `clSeqNo` varchar(30) DEFAULT NULL,
  `securityId` int(64) DEFAULT NULL,
  `mktId` int(64) DEFAULT NULL,
  `bsType` int(64) DEFAULT NULL,
  `trdSide` int(64) DEFAULT NULL,
  `exchTrdNum` int(64) DEFAULT NULL,
  `platformId` int(64) DEFAULT NULL,
  `trdCnfmType` int(64) DEFAULT NULL,
  `etfTrdCnfmSeq` int(64) DEFAULT NULL,
  `ordStatus` int(64) DEFAULT NULL,
  `ordType` int(64) DEFAULT NULL,
  `securityType` int(64) DEFAULT NULL,
  `subSecurityType` int(64) DEFAULT NULL,
  `trdTime` int(64) DEFAULT NULL,
  `trdQty` int(64) DEFAULT NULL,
  `trdPrice` int(64) DEFAULT NULL,
  `trdAmt` int(64) DEFAULT NULL,
  `cumQty` int(64) DEFAULT NULL,
  `cumAmt` int(64) DEFAULT NULL,
  `cumInterest` int(64) DEFAULT NULL,
  `cumFee` int(64) DEFAULT NULL,
  `rowNum` int(64) DEFAULT NULL,
  `tgwGrpNo` int(64) DEFAULT NULL,
  `tgwPartitionNo` int(64) DEFAULT NULL,
  `pbuId` int(64) DEFAULT NULL,
  `branchId` int(64) DEFAULT NULL,
  `trdCnfmOrigRecvTime` numeric(128,64) DEFAULT NULL,
  `trdCnfmCollectedTime` numeric(128,64) DEFAULT NULL,
  `totalInternalLatency` int(64) DEFAULT NULL,
  `collectLatency` int(64) DEFAULT NULL,
  `processLatency` int(64) DEFAULT NULL,
  `processWaitLatency` int(64) DEFAULT NULL

);



-- (?<=errMsg\[\w{0,10})\d+

-- (?<=ordPrice\[)\d+\.\d+|(?<=__ordReqOrigSendTime\[)\d*