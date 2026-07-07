# 命令证据包：DSP PCCSESSINFO
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCC维护/PCC会话查询/显示PCC会话信息（DSP PCCSESSINFO）_09897070.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于查询指定IMSI、MSISDN或IMEI的会话中所有的承载、PCC规则的安装情况，以及规则的生效失效时间、流量监控、profile-space、PRA等相关信息，适用于PCC用户。
**notes（规格/上限→应投影 atom rule）**：
- 无。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| USERIDTYPE | 用户标识类型 | local_planned | required | 无 | 枚举类型。 |
| MSISDN | MSISDN | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 |
| IMSI | IMSI | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 |
| IMEI | IMEI | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～16。每个字符必须为0~9的数字。 |
| DISPLAYMODE | 显示方式 | local_planned | optional | SIMPLE | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109304

**md：`WSFD-109304/调测缺省承载GBR保障_40491397.md`**
- 任务示例脚本（该命令行）：
  `DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="460000123456789";`
- 操作步骤上下文（±2 行原文）：
  L49:
    >     - 包含，则说明PCRF下发了创建default-gbr承载的规则，请执行[步骤 7](#ZH-CN_OPI_0000001240491397__step1883014119126)。
    >     - 不包含，则说明PCRF未下发创建default-gbr承载的规则，请参考[激活缺省承载GBR保障](激活缺省承载GBR保障_95771466.md)重新配置，并再次执行[步骤 3](#ZH-CN_OPI_0000001240491397__step1816324655316)。
    > 7. 执行 [**DSP PCCSESSINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCC维护/PCC会话查询/显示PCC会话信息（DSP PCCSESSINFO）_09897070.md) 命令，查询指定IMSI的会话中是否存在缺省GBR承载。
    >   ```
    >   DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="460000123456789";
  L51:
    > 7. 执行 [**DSP PCCSESSINFO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCC维护/PCC会话查询/显示PCC会话信息（DSP PCCSESSINFO）_09897070.md) 命令，查询指定IMSI的会话中是否存在缺省GBR承载。
    >   ```
    >   DSP PCCSESSINFO:USERIDTYPE=IMSI,IMSI="460000123456789";
    >   ```
    >     - 存在，调测结束。

### WSFD-109101

**md：`WSFD-109101/调测PCC业务_31422956.md`**
- 操作步骤上下文（±2 行原文）：
  L58:
    >     - 如果Gx接口消息不存在，Create Session Response中的返回码不为request accepted (16)，请执行[步骤 11](#ZH-CN_OPI_0231422956__stp9)。
    >     - 如果Gx接口消息存在，但是Create Session Response中的返回码不为request accepted (16)，请执行[步骤 12](#ZH-CN_OPI_0231422956__stp10)。
    > 5. 进入 “MML命令行-UNC” 窗口。 执行 [**DSP PCCSESSINFO**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCC维护/PCC会话查询/显示PCC会话信息（DSP PCCSESSINFO）_09897070.md) 命令，查看指定用户的所有规则是否安装成功。
    >     - 如果规则安装成功，根据[调测离线计费](../../../../计费管理功能/WSFD-011201 支持离线计费/调测离线计费_25768970.md)验证PCRF下发的规则执行正确，则本任务调测结束。
    >     - 如果规则安装失败，请执行[步骤 6](#ZH-CN_OPI_0231422956__stp4)。

**md：`WSFD-109101/调测PCC基本功能_45059543.md`**
- 任务示例脚本（该命令行）：
  `DSP PCCSESSINFO: USERIDTYPE=IMSI,IMSI="460000123456789";`
- 操作步骤上下文（±2 行原文）：
  L69:
    >     - 正确，请执行[步骤 8](#ZH-CN_OPI_0000001245059543__step1883014119126)。
    >     - 不正确，请执行[步骤 11](#ZH-CN_OPI_0000001245059543__step114691314193316)。
    > 8. 执行 [**DSP PCCSESSINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCC维护/PCC会话查询/显示PCC会话信息（DSP PCCSESSINFO）_09897070.md) 命令，查询指定IMSI的会话中是否存在PCF创建的规则。
    >   ```
    >   DSP PCCSESSINFO: USERIDTYPE=IMSI,IMSI="460000123456789";
  L71:
    > 8. 执行 [**DSP PCCSESSINFO**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCC维护/PCC会话查询/显示PCC会话信息（DSP PCCSESSINFO）_09897070.md) 命令，查询指定IMSI的会话中是否存在PCF创建的规则。
    >   ```
    >   DSP PCCSESSINFO: USERIDTYPE=IMSI,IMSI="460000123456789";
    >   ```
    >     - 存在，调测结果正常，请执行[步骤 9](#ZH-CN_OPI_0000001245059543__step1829759115218)。

## ④ 自动比对
- 命令真相参数（5）：['DISPLAYMODE', 'IMEI', 'IMSI', 'MSISDN', 'USERIDTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
