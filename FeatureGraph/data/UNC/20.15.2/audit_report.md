# FeatureGraph 审计报告 UNC@20.15.2

## 概要
- Feature 节点: 629
- License 节点: 448
- Feature<->Feature 边: 409 (depends_on=245, conflicts_with=6, 候选=158)
- 悬空 target: depends_on=1, conflicts_with=0
- requires_license 边: 472 (未对齐 License 节点: 16)

## feature_category 分布
- enhanced: 418
- protocol: 127
- base: 53
- operations: 31

## config_relevance 分布
- required: 601
- ops_only: 21
- none: 7

## depends_on 悬空 target (前20)
- WSFD-209001 -> SFFD-010010

## requires_license 未对齐 License 节点 (前20)
- WSFD-011603 -> LKV2USRF01
- WSFD-104412 -> LKV2INLINS01
- WSFD-106101-2 -> LKV2ESTAM03
- WSFD-106201 -> LKV2PWSR01
- WSFD-110001 -> LKV2BNSFNS01
- WSFD-110011 -> LKV2ASNSSR01
- WSFD-110012 -> LKV2DLNSSR01
- WSFD-130001 -> LKV2SMSSAU01
- WSFD-201208 -> LKV2BHVT01
- WSFD-206101 -> LKV2UDMBPSM01
- WSFD-217001 -> LKV2ULIVE1
- WSFD-217001 -> LKV2ULIVE2
- WSFD-220001 -> LKV2NIMRR01
- WSFD-221001 -> LKV2VCHSM01
- WSFD-223003 -> LKV2DTSPCINRA01
- WSFD-223003 -> LKV2TDPCODSRA01
