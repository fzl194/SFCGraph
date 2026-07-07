# 命令证据包：SET N7RCVATTRCTRL
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/N7接收分发控制/设置N7接收信元处理控制（SET N7RCVATTRCTRL）_09653677.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF**

该命令用于设置对接收到的N7接口消息中部分信元的处理方式。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NOPKTFLTUSAGE | MODQOSKEYATTR | DFTQOSRULEGEN | NTFRSRURI | SCELLCHNR | RSPLOCURI |
| --- | --- | --- | --- | --- | --- |
| SEND_PKTFLT_TO_UE | MOD_QO

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| NOPKTFLTUSAGE | 无PacketFilterUsage | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RC | <br>- “NOT_SEND_PKTFLT_TO_UE（不发送Packet Fliter给UE）” |
| MODQOSKEYATTR | 修改QoSData关键属性 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RC | <br>- “MOD_QOSFLOW（修改QoSFlow）”：根据PCF下发的QoS关键属性修改Qo |
| DFTQOSRULEGEN | 缺省QosRule生成方法 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RC | <br>- “PCC_RULE（PCC规则）”：优先选择安装到缺省qosflow中match-all |
| NTFRSRURI | 基于Notify消息ResourceURI触发PCF重选 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RC | <br>- “DISABLE（不使能）”：忽略PCF发送的UpdateNotify携带的Resour |
| SCELLCHNR | SCELL_CH是否允许上报NCGI | 对端协商 | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RC | <br>- “DISABLE（不使能）”：PCF下发SCELL_CH trigger时不支持上报NC |
| RSPLOCURI | 是否使用PCF返回的URI进行转发 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7RC | 如需向新的URI标识的PCF进行转发，请使能该参数。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 操作步骤上下文（±2 行原文）：
  L142:
    >       [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    >     4. （可选）PCF不支持下发packetFilterUsage属性时需要配置。设置从N7接口收到的FlowInformation中不包含PacketFilterUsage时，SMF将FlowInformation映射成的Filter推送给UE。
    >       [**SET N7RCVATTRCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/N7接收分发控制/设置N7接收信元处理控制（SET N7RCVATTRCTRL）_09653677.md) : NOPKTFLTUSAGE=SEND_PKTFLT_TO_UE;
    >     5. （可选）PCF订阅SCELL_CH场景，SMF向PCF上报NCGI时，需要开启如下开关。
    >       [**SET N7RCVATTRCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/N7接收分发控制/设置N7接收信元处理控制（SET N7RCVATTRCTRL）_09653677.md) : SCELLCHNR=ENABLE;
  L144:
    >       [**SET N7RCVATTRCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/N7接收分发控制/设置N7接收信元处理控制（SET N7RCVATTRCTRL）_09653677.md) : NOPKTFLTUSAGE=SEND_PKTFLT_TO_UE;
    >     5. （可选）PCF订阅SCELL_CH场景，SMF向PCF上报NCGI时，需要开启如下开关。
    >       [**SET N7RCVATTRCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/N7接收分发控制/设置N7接收信元处理控制（SET N7RCVATTRCTRL）_09653677.md) : SCELLCHNR=ENABLE;
    >       SMF向PCF上报ECGI时，没有开关控制，默认支持。
    >     6. （可选）2G用户接入场景，使用N7接口获取策略信息时需要配置。设置N7接口在2G用户接入时支持发送携带2G相关的接入类型、位置和服务节点类型等信息。

## ④ 自动比对
- 命令真相参数（6）：['DFTQOSRULEGEN', 'MODQOSKEYATTR', 'NOPKTFLTUSAGE', 'NTFRSRURI', 'RSPLOCURI', 'SCELLCHNR']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
