# Configured NSSAI

- [属性](#ZH-CN_TOPIC_0166943294__1.3.1.1)
- [定义](#ZH-CN_TOPIC_0166943294__1.3.2.1)

#### [属性](#ZH-CN_TOPIC_0166943294)

| 名称 | 缩略语 | 同义词 |
| --- | --- | --- |
| Configured Network Slice Selection Assistance Information | Configured NSSAI | 无 |

#### [定义](#ZH-CN_TOPIC_0166943294)

运营商网络支持的切片配置信息，由网络侧配置并在注册等流程下发UE，下发时需要考虑UE签约的Subscribed S-NSSAIs信息，两者取交集。按照协议定义，Configured NSSAI有以下两种决策方式：

1. 由AMF本地生成
2. 由NSSF决策生成

如果AMF无法提供切片服务，则查询NSSF由NSSF决策生成Configured NSSAI信元，否则由AMF决策生成。
