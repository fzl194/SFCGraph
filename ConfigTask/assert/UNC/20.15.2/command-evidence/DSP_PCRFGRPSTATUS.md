# 命令证据包：DSP PCRFGRPSTATUS
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组状态/显示PCRF组状态（DSP PCRFGRPSTATUS）_09897121.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、GGSN**

此命令用来查询指定PCRF组状态信息，包括PCRF分组内每个PCRF的通信状态和master/slave状态。
**notes（规格/上限→应投影 atom rule）**：
- - 查询PCRF分组状态信息时，前提条件为PCRFGRPNAME在对象PCRFGROUP中已配置。
- 只有当PCRF绑定到PCRF Group并且PCRF有链路时，才可以查询到PCRF Group状态信息。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PCRFGRPNAME | PCRF组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/调测PCC业务_31422956.md`**
- 任务示例脚本（该命令行）：
  `DSP PCRFGRPSTATUS:PCRFGRPNAME="pcrf_group_2";`
- 操作步骤上下文（±2 行原文）：
  L62:
    >     - 如果规则安装失败，请执行[步骤 6](#ZH-CN_OPI_0231422956__stp4)。
    > 6. 请查看GGSN/PGW-C上的消息跟踪，查看PCRF下发策略后，GGSN/PGW-C上报的Credit Control Request-Update消息中的rule-failure-code，该信元上报表示在PCC用户激活过程中，PCRF下发的所有规则中的某一些规则在GGSN/PGW-C上安装失败。该rule-failure-code的含义与解决办法请参考 [表1](#ZH-CN_OPI_0231422956__tab1) 中描述。
    > 7. 进入 “MML命令行-UNC” 窗口。 执行 [**DSP PCRFGRPSTATUS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组状态/显示PCRF组状态（DSP PCRFGRPSTATUS）_09897121.md) 命令，查看使用的PCRF组的状态是否正常。
    >   ```
    >   DSP PCRFGRPSTATUS:PCRFGRPNAME="pcrf_group_2";
  L64:
    > 7. 进入 “MML命令行-UNC” 窗口。 执行 [**DSP PCRFGRPSTATUS**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组状态/显示PCRF组状态（DSP PCRFGRPSTATUS）_09897121.md) 命令，查看使用的PCRF组的状态是否正常。
    >   ```
    >   DSP PCRFGRPSTATUS:PCRFGRPNAME="pcrf_group_2";
    >   ```
    >   ```

## ④ 自动比对
- 命令真相参数（1）：['PCRFGRPNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
