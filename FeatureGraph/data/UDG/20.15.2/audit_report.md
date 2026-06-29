# FeatureGraph 审计报告 UDG@20.15.2

## 概要
- Feature 节点: 313
- License 节点: 187
- Feature<->Feature 边: 285 (depends_on=193, conflicts_with=58, 候选=34)
- 悬空 target: depends_on=3, conflicts_with=1
- requires_license 边: 154 (未对齐 License 节点: 1)

## feature_category 分布
- base: 133
- enhanced: 127
- operations: 30
- protocol: 23

## config_relevance 分布
- required: 269
- ops_only: 30
- none: 14

## depends_on 悬空 target (前20)
- GWFD-110481 -> SFFD-010010
- GWFD-020531 -> GWFD-030501
- GWFD-111286 -> GWFD-111283

## conflicts_with 悬空 target (前20)
- GWFD-111251 -> GWFD-113005

## requires_license 未对齐 License 节点 (前20)
- GWFD-110501 -> LKV6CKTSOU0
