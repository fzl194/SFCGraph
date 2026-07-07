# 命令证据包：DSP CGSTATUS
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG状态/查询CG状态（DSP CGSTATUS）_09896853.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询所有CG或指定CG的工作状态。如果不输入要查询CG的IP地址，则显示所有CG信息。
**notes（规格/上限→应投影 atom rule）**：
- 返回的记录数超过300条时，可能不全。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CGIPVERSION | CG IP版本 | global_planned | optional | 无 | 枚举类型。 |
| CGIPV4ADDR | CG IPv4地址 | global_planned | conditional | 无 | IPv4地址类型。 |
| CGIPV6ADDR | CG IPv6地址 | global_planned | conditional | 无 | IPv6地址类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/调测CG指示重定向功能_95923589.md`**
- 任务示例脚本（该命令行）：
  `DSP CGSTATUS:;`
- 操作步骤上下文（±2 行原文）：
  L58:
    > 3. 停止CG1服务器的服务（具体操作请参考CG的手册），以此模拟CG1服务器故障，1分钟后查看CG1的状态是否为abnormal。
    >   ```
    >   DSP CGSTATUS:;
    >   ```
    >   ```

**md：`WSFD-011201/调测到CG的数据_95923534.md`**
- 操作步骤上下文（±2 行原文）：
  L43:
    > ## [操作步骤](#ZH-CN_OPI_0295923534)
    > 
    > 1. 进入 “MML命令行-UNC” 窗口。 执行 **DSP CGSTATUS** 命令，查看CG状态是否正常。
    >     - 如果CG状态为normal，表明通信正常，则调测任务结束。
    >     - 如果CG状态为abnormal，请继续执行[步骤 2](#ZH-CN_OPI_0295923534__stp20)。

**md：`WSFD-011201/调测话单缓存功能_95923427.md`**
- 任务示例脚本（该命令行）：
  `DSP CGSTATUS:;`
- 操作步骤上下文（±2 行原文）：
  L53:
    >     - 如果测试终端成功接入网络，请执行[步骤 2](#ZH-CN_OPI_0295923427__step30-1)。
    >     - 如果测试终端无法接入网络，请调测UNC的接入功能。
    > 2. 通过在GGSN/SGW-C/PGW-C上删除到CG的路由的方式断开与CG的连接，1分钟后执行 **DSP CGSTATUS** 命令查看对应的CG状态是否为abnormal。
    >   > **说明**
    >   > 如果不产生话单数据时，使用echo消息维护链路，一般需要3～4分钟才检测到链路abnormal状态（默认消息发送间隔是1分钟，重发次数是3次）。
  L57:
    >   > 如果不产生话单数据时，使用echo消息维护链路，一般需要3～4分钟才检测到链路abnormal状态（默认消息发送间隔是1分钟，重发次数是3次）。
    >   ```
    >   DSP CGSTATUS:;
    > 
    >   CG Status
  L73:
    >     - 如果硬盘上缓存的话单数为0，请执行[步骤 6](#ZH-CN_OPI_0295923427__step1829245425110)。
    >     - 如果硬盘上缓存的话单数不为0，请继续执行[步骤 4](#ZH-CN_OPI_0295923427__stp3)。
    > 4. 恢复CG与GGSN/SGW-C/PGW-C的路由，1分钟后通过命令 **DSP CGSTATUS** 查看CG的状态是否是normal。
    >     - 如果**CG状态**为**normal**，则继续执行[步骤 5](#ZH-CN_OPI_0295923427__stp4)。
    >     - 如果**CG状态**为**abnormal**，请参考[调测到CG的数据](../../../../../业务专题/5G Core 计费解决方案/计费解决方案概述/计费方案部署与调测/调测Ga接口离线计费/调测到CG的数据_01_10024.md)调测CG链路。

## ④ 自动比对
- 命令真相参数（3）：['CGIPV4ADDR', 'CGIPV6ADDR', 'CGIPVERSION']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
