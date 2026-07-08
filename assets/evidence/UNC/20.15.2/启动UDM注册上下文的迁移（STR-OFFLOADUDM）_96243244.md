# 启动UDM注册上下文的迁移（STR OFFLOADUDM）

- [命令功能](#ZH-CN_MMLREF_0296243244__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296243244__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296243244__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296243244__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0296243244)

![](启动UDM注册上下文的迁移（STR OFFLOADUDM）_96243244.assets/notice_3.0-zh-cn_2.png)

执行该命令，如果参数设置不合理可能影响UDM间的用户数不均衡。

**适用NF：AMF、SMF**

该命令用于触发AMF或SMF在UDM的注册上下文的迁移流程，比如在特定的UDM发生故障或升级等场景下，AMF或SMF通过本命令触发将原本注册在该UDM上的上下文迁移到其它UDM。

## [注意事项](#ZH-CN_MMLREF_0296243244)

- 该命令执行后立即生效。

- 对于AMF，迁移的速率受SET AMFUDMRESET命令中的“IMMEDIATERATE”参数控制；扫描时长 = 5G用户数 / 扫描速率。其中，5G用户数可以通过DSP NGUSERNUM获取；扫描速率可以通过LST AMFUDMRESET中的扫描速率获取。
- 对于SMF，迁移的速率受SET SMFUDMRESET命令中的“SCANRATE”参数控制。
- 请先执行AMF迁移，再执行SMF迁移，并确保AMF和SMF均执行。

#### [操作用户权限](#ZH-CN_MMLREF_0296243244)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0296243244)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户（或者会话）上下文所在的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- “AMF（AMF）”：AMF<br>- “SMF（SMF）”：SMF<br>默认值：无<br>配置原则：无 |
| SRCUDMID | 源UDM实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要迁移的源UDM的实例标识，即AMF或SMF需要将原本注册在该UDM的用户或PDU会话重新选择其它UDM并再次发起注册，同时也包括取签约数据以及订阅签约数据变化的流程。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。UDM Instance ID使用UUID格式。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0296243244)

由于网络调整，A地数据中心的UDM1上的业务需要其它的UDM接管，为了配合该调整，需要手动执行如下命令，将AMF上原本注册在UDM1上的用户重新注册到其它UDM上：

```
STR OFFLOADUDM:NFTYPE=AMF,SRCUDMID="5EA7F228-47CC-2032-03A3-031313000001";
```
