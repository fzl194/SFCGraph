---
id: UNC@20.15.2@MMLCommand@SET N7RCVATTRCTRL
type: MMLCommand
name: SET N7RCVATTRCTRL（设置N7接收信元处理控制）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: N7RCVATTRCTRL
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- N7接收分发控制
status: active
---

# SET N7RCVATTRCTRL（设置N7接收信元处理控制）

## 功能

**适用NF：SMF**

该命令用于设置对接收到的N7接口消息中部分信元的处理方式。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NOPKTFLTUSAGE | MODQOSKEYATTR | DFTQOSRULEGEN | NTFRSRURI | SCELLCHNR | RSPLOCURI |
| --- | --- | --- | --- | --- | --- |
| SEND_PKTFLT_TO_UE | MOD_QOSFLOW | PCC_RULE | DISABLE | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOPKTFLTUSAGE | 无PacketFilterUsage | 可选必选说明：可选参数<br>参数含义：设置从N7接口收到的flowInfos属性中不包含PacketFilterUsage属性时的处理。<br>数据来源：本端规划<br>取值范围：<br>- “NOT_SEND_PKTFLT_TO_UE（不发送Packet Fliter给UE）”：对于PCF下发的动态规则，当PCF没有下发packFilterUsage属性时，SMF不将FlowInformation映射成的Filter推送给UE。注意：当规则上的Filter均没有推送给UE时，才允许PCF为该规则指定激活或去活时间，否则规则将安装失败。<br>- “SEND_PKTFLT_TO_UE（发送Packet Fliter给UE）”：对于PCF下发的动态规则，当PCF没有下发packFilterUsage属性时，SMF都将FlowInformation映射成的Filter推送给UE。注意：当规则上的Filter均没有推送给UE时，才允许PCF为该规则指定激活或去活时间，否则规则将安装失败。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RCVATTRCTRL查询当前参数配置值。<br>配置原则：无 |
| MODQOSKEYATTR | 修改QoSData关键属性 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当收到PCF修改QoSData关键属性消息时是更新QoSFlow还是删除当前QoSFlow重新创建QoSFlow。关键属性包括：5QI，Arp，QNC，priorityLevel，averWindow和maxDataBurstVol。<br>数据来源：本端规划<br>取值范围：<br>- “MOD_QOSFLOW（修改QoSFlow）”：根据PCF下发的QoS关键属性修改QoSFlow。<br>- “DEL_ADD_QOSFLOW（删除原有QoSFlow，新建QoSFlow）”：删除原有QoSFlow，新建QoSFlow。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RCVATTRCTRL查询当前参数配置值。<br>配置原则：无 |
| DFTQOSRULEGEN | 缺省QosRule生成方法 | 可选必选说明：可选参数<br>参数含义：该参数用于设置生成缺省QosRule的方法。<br>数据来源：本端规划<br>取值范围：<br>- “PCC_RULE（PCC规则）”：优先选择安装到缺省qosflow中match-all类型的PccRule作为缺省QosRule。如果缺省qosflow没有安装match-all类型的PccRule，并且PCF下发了预定义规则或者ADC规则，SMF生成match-all类型的PccRule作为缺省QosRule；否则选择优先级最低的PccRule作为缺省QosRule。<br>- “MATCH_ALL_RULE（匹配所有流的规则）”：优先选择安装到缺省qosflow中match-all类型的PccRule作为缺省QosRule。如果缺省qosflow没有安装match-all类型的PccRule，SMF生成match-all类型的PccRule作为缺省QosRule。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RCVATTRCTRL查询当前参数配置值。<br>配置原则：无 |
| NTFRSRURI | 基于Notify消息ResourceURI触发PCF重选 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当收到PCF发送的UpdateNotify携带的ResourceURI与当前会话使用的PCF不同时，是否允许触发PCF重选。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：忽略PCF发送的UpdateNotify携带的ResourceURI，不触发PCF重选。<br>- “ENABLE（使能）”：根据PCF发送的UpdateNotify携带的ResourceURI触发PCF重选。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RCVATTRCTRL查询当前参数配置值。<br>配置原则：无 |
| SCELLCHNR | SCELL_CH是否允许上报NCGI | 可选必选说明：可选参数<br>参数含义：该参数用于控制当PCF下发SCELL_CH trigger或USER_LOCATION_CH trigger时，是否支持在NCGI变化时向PCF发送NCGI值。<br>数据来源：对端协商<br>取值范围：<br>- “DISABLE（不使能）”：PCF下发SCELL_CH trigger时不支持上报NCGI。<br>- “ENABLE（使能）”：PCF下发SCELL_CH trigger时支持上报NCGI。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RCVATTRCTRL查询当前参数配置值。<br>配置原则：无 |
| RSPLOCURI | 是否使用PCF返回的URI进行转发 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当收到PCF发送的激活响应的消息头中携带URI变化时，是否使用响应消息中的URI用于后续消息发送。<br>数据来源：全网规划<br>取值范围：如需向新的URI标识的PCF进行转发，请使能该参数。<br>- “DISABLE（不使能）”：当收到PCF发送的激活响应的消息头中携带URI变化时，不使用响应消息中的URI用于后续消息发送。<br>- “ENABLE（使能）”：当收到PCF发送的激活响应的消息头中携带URI变化时，使用响应消息中的URI用于后续消息发送。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RCVATTRCTRL查询当前参数配置值。<br>配置原则：<br>- 该参数使能时，更新或去活失败时不进行Failover。<br>- 非直连组网模式下，该参数仅支持控制Model C模式下N7接口接收到的消息中部分信元的处理方式，Model D模式下的控制方式参考软参DWORD548 BIT4。 |

## 操作的配置对象

- [N7接收信元处理控制（N7RCVATTRCTRL）](configobject/UNC/20.15.2/N7RCVATTRCTRL.md)

## 使用实例

假设与UNC对接的PCF未遵循3GPP协议，对于需要给UE下发packet filter的场景不携带PacketUsageFilter属性，运营商可以通过设置此命令实现UNC对于不携带PacketUsageFilter属性的场景默认向UE推送Packet Filter。

```
%%SET N7RCVATTRCTRL: NOPKTFLTUSAGE=NOT_SEND_PKTFLT_TO_UE;%%
RETCODE = 0  Operation succeeded
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置N7接收信元处理控制（SET-N7RCVATTRCTRL）_09653677.md`
