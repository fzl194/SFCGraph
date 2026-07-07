# 命令证据包：DSP SMPDPNUM
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文数/查询会话管理的PDP上下文数（DSP SMPDPNUM）_09653799.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查看SMF/PGW-C/SGW-C/GGSN-C的PDP上下文数、承载上下文、QFI上下文。
**notes（规格/上限→应投影 atom rule）**：
- - “查询分类”参数不输入时，表示查询汇总的信息。
- 在本命令中，指定查询条件指的是指定查询范围（ALL_POD_INFO、SPECIFIED_POD_INFO）。例如：指定查询条件的PGW-C上激活的5G承载上下文数，指的是查询范围（ALL_POD_INFO、SPECIFIED_POD_INFO）的PGW-C上激活的5G承载上下文数。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| QRY_SCOPE | 查询范围 | local_planned | optional | SUMMARY | <br>- “SUMMARY（汇总信息）”：查询汇总信息。以汇总方式呈现。 |
| QRY_CLASS | 查询分类 | local_planned | optional | SUMMARY | <br>- “APN（APN）”：查询使用该APN激活的当前在线PDP上下文数。 |
| APN | APN | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~63。 |
| RAT | 无线接入类型 | global_planned | conditional | 无 | <br>- “UTRAN（UTRAN）”：通用陆地无线接入网。 |
| UPF_NAME | UPF名称 | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~255。 |
| SST | 切片/服务类型 | global_planned | conditional | 无 | 整数类型，取值范围是0~255。 |
| POD_ID | POD名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~255。 |
| SD | 切片区分码 | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~8。只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感 |
| ALIASAPN | 别名APN | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~63。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-010112

**md：`WSFD-010112/参考信息_16583333.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - **[LST FWAMATCHRULE](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/FWA用户匹配规则管理/查询FWA用户匹配规则（LST FWAMATCHRULE）_90852869.md)**
    > - **[DSP SMSESSIONNUM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询会话上下文数/显示会话管理的会话上下文数（DSP SMSESSIONNUM）_09652085.md)**
    > - **[DSP SMPDPNUM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文数/查询会话管理的PDP上下文数（DSP SMPDPNUM）_09653799.md)**
    > 
    > #### [告警](#ZH-CN_TOPIC_0000001616583333)

**md：`WSFD-010112/调测支持FWA接入_53227418.md`**
- 任务示例脚本（该命令行）：
  `%%DSP SMPDPNUM: QRY_SCOPE=SUMMARY, QRY_CLASS=FWA;%%`
- 操作步骤上下文（±2 行原文）：
  L27:
    > 2. 进入 “MML命令行-UNC” 窗口。
    > 3. 查询当前在线的FWA用户的PDP上下文数。
    >   **[DSP SMPDPNUM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文数/查询会话管理的PDP上下文数（DSP SMPDPNUM）_09653799.md)** : QRY_SCOPE=SUMMARY, QRY_CLASS=FWA;
    >   预期结果：当前在线的FWA用户的PDP上下文数与实际规划一致。
    >   ```
  L30:
    >   预期结果：当前在线的FWA用户的PDP上下文数与实际规划一致。
    >   ```
    >   %%DSP SMPDPNUM: QRY_SCOPE=SUMMARY, QRY_CLASS=FWA;%%
    >   RETCODE = 0  操作成功
    > 

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L49:
    > - [**ADD CPCGGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/抄送CG组/增加抄送CG组（ADD CPCGGRP）_09896864.md)
    > - [**ADD CPCGBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/抄送CG绑定/增加抄送CG绑定（ADD CPCGBINDING）_09896869.md)
    > - **[DSP SMPDPNUM](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文数/查询会话管理的PDP上下文数（DSP SMPDPNUM）_09653799.md)**
    > 
    > #### [告警](#ZH-CN_TOPIC_0229423866)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L50:
    > - [**ADD SUBSCRIBERIDSEGGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md)
    > - [**ADD VIRTUALAPNRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/虚拟APN映射策略/增加虚拟APN映射策略配置（ADD VIRTUALAPNRULE）_09652380.md)
    > - **[DSP SMPDPNUM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文数/查询会话管理的PDP上下文数（DSP SMPDPNUM）_09653799.md)**
    > 
    > #### [告警](#ZH-CN_TOPIC_0229035079)

## ④ 自动比对
- 命令真相参数（9）：['ALIASAPN', 'APN', 'POD_ID', 'QRY_CLASS', 'QRY_SCOPE', 'RAT', 'SD', 'SST', 'UPF_NAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
