# 命令证据包：SET N7SNDATTRCTRL
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/23G接入控制/设置N7发送信元处理控制（SET N7SNDATTRCTRL）_72001557.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：GGSN**

该命令用于设置N7接口发送的消息中部分信元的处理方式。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 修改GERAN和UTRAN为TRUE时，需要提前和对端PCF确认是否支持23G接入。
- GERAN和UTRAN为FALSE时，RatType和位置相关的Trigger不生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| GERAN | UTRAN |
| --- | --- |
| FALSE | FALSE |

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| GERAN | 携带GERAN类信元 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7SN | <br>- TRUE(TRUE) |
| UTRAN | 携带UTRAN类信元 | local_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N7SN | <br>- TRUE(TRUE) |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 操作步骤上下文（±2 行原文）：
  L147:
    >       SMF向PCF上报ECGI时，没有开关控制，默认支持。
    >     6. （可选）2G用户接入场景，使用N7接口获取策略信息时需要配置。设置N7接口在2G用户接入时支持发送携带2G相关的接入类型、位置和服务节点类型等信息。
    >       [**SET N7SNDATTRCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/23G接入控制/设置N7发送信元处理控制（SET N7SNDATTRCTRL）_72001557.md) : GERAN=TRUE;
    >       对端PCF不支持GERAN时， “GERAN” 设置为 “FALSE” 。设置为FALSE的场景下，SMF向PCF发送的N7消息不携带RAT-Type，RAT切换不会触发N7更新流程。
    >     7. （可选）3G用户接入场景，使用N7接口获取策略信息时需要配置。设置N7接口在3G用户接入时支持发送携带3G相关的接入类型、位置和服务节点类型等信息。
  L151:
    >     7. （可选）3G用户接入场景，使用N7接口获取策略信息时需要配置。设置N7接口在3G用户接入时支持发送携带3G相关的接入类型、位置和服务节点类型等信息。
    >       此时需要 [**SET PCCFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md) 命令中参数“ **N7FEATURELIST** ”的取值中包括“UtranSupport”。
    >       [**SET N7SNDATTRCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/23G接入控制/设置N7发送信元处理控制（SET N7SNDATTRCTRL）_72001557.md) : UTRAN=TRUE;
    >       对端PCF不支持UTRAN时， “UTRAN” 设置为 “FALSE” 。设置为FALSE的场景下，SMF向PCF发送的N7消息不携带RAT-Type，RAT切换不会触发N7更新流程。
    >     8. （可选）NB-IoT用户接入场景，设置SMF向PCF发送消息时的RAT信元值。

## ④ 自动比对
- 命令真相参数（2）：['GERAN', 'UTRAN']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
