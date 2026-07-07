# 命令证据包：DSP PCRFSTATUS
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF状态/显示PCRF状态（DSP PCRFSTATUS）_09897111.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、GGSN**

此命令用来查询所有PCRF或者指定PCRF的连接状态。
**notes（规格/上限→应投影 atom rule）**：
- - 非直连（通过DRA连接）的PCRF的状态不显示。
- 如果只显示一条“Not Ready”记录，则说明此PCRF未配置Diameter链路。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PCRFNAME | PCRF主机名 | 对端协商 | optional | 无 | 字符串类型，输入长度范围为1～127。不支持空格，由软参BIT 150控制是否区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109304

**md：`WSFD-109304/调测缺省承载GBR保障_40491397.md`**
- 操作步骤上下文（±2 行原文）：
  L43:
    >     - 是，请执行[步骤 5](#ZH-CN_OPI_0000001240491397__step03685065417)。
    >     - 否，请联系华为技术工程师确保用户激活成功后，重新执行[步骤 3](#ZH-CN_OPI_0000001240491397__step1816324655316)。
    > 5. 执行命令 [**DSP PCRFSTATUS**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF状态/显示PCRF状态（DSP PCRFSTATUS）_09897111.md) ，查询PCRF状态是否正常。
    >     - 若PCRF状态正常，请执行[步骤 6](#ZH-CN_OPI_0000001240491397__step4630171816912)。
    >     - 若未部署PCRF或PCRF状态异常，请执行[步骤 7](#ZH-CN_OPI_0000001240491397__step1883014119126)。

### WSFD-109101

**md：`WSFD-109101/调测PCRF负荷分担功能_31422955.md`**
- 任务示例脚本（该命令行）：
  `DSP PCRFSTATUS:PCRFNAME="pcrf_1";`
  `DSP PCRFSTATUS:PCRFNAME="pcrf_2";`
- 操作步骤上下文（±2 行原文）：
  L47:
    >     - 如果GGSN/PGW-C与各PCRF交互的CCR-I消息数的比例和GGSN/PGW-C上配置的PCRF组内各PCRF的负荷分担比例一致，则调测结束。
    >     - 如果不一致，请执行[步骤 3](#ZH-CN_OPI_0231422955__stp5)。
    > 3. 进入 “MML命令行-UNC” 窗口。 执行 [**DSP PCRFSTATUS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF状态/显示PCRF状态（DSP PCRFSTATUS）_09897111.md) 命令，查看各PCRF的状态是否正常。
    >   ```
    >   DSP PCRFSTATUS:PCRFNAME="pcrf_1";
  L49:
    > 3. 进入 “MML命令行-UNC” 窗口。 执行 [**DSP PCRFSTATUS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF状态/显示PCRF状态（DSP PCRFSTATUS）_09897111.md) 命令，查看各PCRF的状态是否正常。
    >   ```
    >   DSP PCRFSTATUS:PCRFNAME="pcrf_1";
    >   ```
    >   ```
  L66:
    >   ```
    >   ```
    >   DSP PCRFSTATUS:PCRFNAME="pcrf_2";
    >   ```
    >   ```

**md：`WSFD-109101/调测到PCRF的数据_31422954.md`**
- 任务示例脚本（该命令行）：
  `DSP PCRFSTATUS:PCRFNAME="pcrf_1";`
  `DSP PCRFSTATUS:PCRFNAME="pcrf_2";`
- 操作步骤上下文（±2 行原文）：
  L46:
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0231422954__stp1)。
    >     - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    > 2. 执行 [**DSP PCRFSTATUS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF状态/显示PCRF状态（DSP PCRFSTATUS）_09897111.md) 命令，查看PCRF的状态是否正常。
    >   ```
    >   DSP PCRFSTATUS:PCRFNAME="pcrf_1";
  L48:
    > 2. 执行 [**DSP PCRFSTATUS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF状态/显示PCRF状态（DSP PCRFSTATUS）_09897111.md) 命令，查看PCRF的状态是否正常。
    >   ```
    >   DSP PCRFSTATUS:PCRFNAME="pcrf_1";
    >   ```
    >   ```
  L65:
    >   ```
    >   ```
    >   DSP PCRFSTATUS:PCRFNAME="pcrf_2";
    >   ```
    >   ```

### WSFD-104508

**md：`WSFD-104508/调测Gx over SCTP功能_30442392.md`**
- 任务示例脚本（该命令行）：
  `DSP PCRFSTATUS:PCRFNAME="pcrf";`
- 操作步骤上下文（±2 行原文）：
  L40:
    >     - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0230442392__stp1)。
    >     - 如果“SWITCH”为“DISABLE”，则执行**[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**命令打开本特性对应的License配置开关。
    > 2. 执行 **[DSP PCRFSTATUS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF状态/显示PCRF状态（DSP PCRFSTATUS）_09897111.md)** 命令，查看PCRF的状态是否正常。
    >   ```
    >   DSP PCRFSTATUS:PCRFNAME="pcrf";
  L42:
    > 2. 执行 **[DSP PCRFSTATUS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF状态/显示PCRF状态（DSP PCRFSTATUS）_09897111.md)** 命令，查看PCRF的状态是否正常。
    >   ```
    >   DSP PCRFSTATUS:PCRFNAME="pcrf";
    >   ```
    >   ```

## ④ 自动比对
- 命令真相参数（1）：['PCRFNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
