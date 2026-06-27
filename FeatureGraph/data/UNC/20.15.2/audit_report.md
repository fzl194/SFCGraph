# FeatureGraph 审计报告 UNC@20.15.2

## 概要
- Feature 节点: 664
- License 节点: 448
- Feature<->Feature 边: 104 (depends_on=64, conflicts_with=3, 候选=37)
- 悬空 target: depends_on=1, conflicts_with=0
- requires_license 边: 94 (未对齐 License 节点: 12)

## feature_category 分布
- enhanced: 454
- protocol: 97
- base: 92
- operations: 21

## config_relevance 分布
- required: 637
- ops_only: 21
- none: 6

## depends_on 悬空 target (前20)
- WSFD-209001 -> SFFD-010010

## requires_license 未对齐 License 节点 (前20)
- WSFD-010001 -> 81203322
- WSFD-010003 -> 81203323
- WSFD-011603 -> LKV2USRF01
- WSFD-104412 -> LKV2INLINS01
- WSFD-106101-2 -> LKV2ESTAM03
- WSFD-106201 -> LKV2PWSR01
- WSFD-206101 -> LKV2UDMBPSM01
- WSFD-209002 -> 81202579
- WSFD-221001 -> LKV2VCHSM01
- WSFD-221003 -> LKV2FRVNRPCF01
- WSFD-223003 -> LKV2DTSPCINRA01
- WSFD-223003 -> LKV2TDPCODSRA01
