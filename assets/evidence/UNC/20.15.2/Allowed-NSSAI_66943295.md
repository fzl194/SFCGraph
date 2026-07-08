# Allowed NSSAI

- [属性](#ZH-CN_TOPIC_0166943295__1.3.1.1)
- [定义](#ZH-CN_TOPIC_0166943295__1.3.2.1)

#### [属性](#ZH-CN_TOPIC_0166943295)

| 名称 | 缩略语 | 同义词 |
| --- | --- | --- |
| Allowed Network Slice Selection Assistance Information | Allowed NSSAI | 无 |

#### [定义](#ZH-CN_TOPIC_0166943295)

注册流程中网络侧向UE下发的允许其使用的NSSAI，是UE请求的Request NSSAI和签约的Subscribed NSSAI取交集，如果UE没有携带Request NSSAI，则为标记为Default的Subscribed NSSAI。按照协议定义，Allowed NSSAI有以下两种决策方式：

1. 由AMF本地生成
2. 由NSSF决策生成

如果AMF无法提供切片服务，则查询NSSF由NSSF决策生成Allowed NSSAI信元，否则由AMF决策生成。
