# 命令证据包：SET GLBDFTCHFGROUP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/设置全局默认CHF组（SET GLBDFTCHFGROUP）_09651523.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于配置系统缺省的CHF组。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 该命令参数输入空格或者null（不区分大小写）清空参数值。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PRIMARYCHFGRP | SECONDARYCHFGRP |
| --- | --- |
| null | null |

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PRIMARYCHFGRP | 主CHF组 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLBD | 字符串类型，输入长度范围是1~63。 |
| SECONDARYCHFGRP | 备CHF组 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLBD | 字符串类型，输入长度范围是1~63。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/配置CHF选择方式_92091086.md`**
- 数据规划表（该命令的参数行）：
  | **SET GLBDFTCHFGROUP** | PRIMARYCHFGRP（主CHF组） | ChfGroup1 | 全网规划 | 配置基于全局默认的CHF组选择CHF。 |
  | **SET GLBDFTCHFGROUP** | SECONDARYCHFGRP（备CHF组） | ChfGroup2 | 全网规划 | 配置基于全局默认的CHF组选择CHF。 |
- 任务示例脚本（该命令行）：
  `SET GLBDFTCHFGROUP: PRIMARYCHFGRP="ChfGroup1", SECONDARYCHFGRP="ChfGroup2";`
- 操作步骤上下文（±2 行原文）：
  L103:
    >             **ADD TNFBINDGRP**
    >     2. 配置基于全局默认的CHF组选择CHF。
    >       **SET GLBDFTCHFGROUP**
    > 
    > ## [任务示例](#ZH-CN_OPI_0192091086)
  L196:
    > ADD TNFBINDGRP: TNFGRPINDEX=1, TNFINSINDEX=1;
    > ADD TNFBINDGRP: TNFGRPINDEX=2, TNFINSINDEX=2;
    > SET GLBDFTCHFGROUP: PRIMARYCHFGRP="ChfGroup1", SECONDARYCHFGRP="ChfGroup2";
    > ```

**md：`WSFD-011206/配置计费消息缓存_31702748.md`**
- 数据规划表（该命令的参数行）：
  | **SET GLBDFTCHFGROUP** | PRIMARYCHFGRP（主CHF组） | ChfGroup1 | 全网规划 | 配置全局默认CHF组，确保因配置修改导致CHF的FQDN、NFInstance ID、CHF Group删除的场景，有CHF可回放。<br>参数取值已在<br>[配置CHF选择方式](配置CHF选择方式_92091086.md)<br>配置。 |
  | **SET GLBDFTCHFGROUP** | SECONDARYCHFGRP（备CHF组） | ChfGroup2 | 全网规划 | 配置全局默认CHF组，确保因配置修改导致CHF的FQDN、NFInstance ID、CHF Group删除的场景，有CHF可回放。<br>参数取值已在<br>[配置CHF选择方式](配置CHF选择方式_92091086.md)<br>配置。 |
- 任务示例脚本（该命令行）：
  `SET GLBDFTCHFGROUP: PRIMARYCHFGRP="ChfGroup1", SECONDARYCHFGRP="ChfGroup2";`
- 操作步骤上下文（±2 行原文）：
  L65:
    >   **SET CNVRGDCHGPARA**
    > - 配置全局默认CHF组。
    >   **SET GLBDFTCHFGROUP**
    > - 配置缓存文件的超期时长。
    >   **SET CDRSTORAGECTRL**
  L118:
    > 
    > ```
    > SET GLBDFTCHFGROUP: PRIMARYCHFGRP="ChfGroup1", SECONDARYCHFGRP="ChfGroup2";
    > ```
    > 

**md：`WSFD-011206/调测融合计费的计费会话创建功能_89257219.md`**
- 操作步骤上下文（±2 行原文）：
  L64:
    >           - 如果有可用CHF，请执行[步骤 10](#ZH-CN_OPI_0289257219__step13334556133920)。
    >           - 如果没有可用CHF，请执行[步骤 9.b](#ZH-CN_OPI_0289257219__substep6959172620617)。
    >     b. 执行 [**SET GLBDFTCHFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/设置全局默认CHF组（SET GLBDFTCHFGROUP）_09651523.md) 、 [**MOD SELECTCHFGBYCC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/修改基于CC选择CHF处理（MOD SELECTCHFGBYCC）_09651411.md) 命令，按照规划配置当前用户可选择的CHF，请再次执行 [步骤 3](#ZH-CN_OPI_0289257219__step2585105420194) 。
    > 10. 检查是否产生 [ALM-100072 目的NF服务不可达](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-100072 目的NF服务不可达_26182301.md) 告警。
    >     a. 检查是否产生 [ALM-100072 目的NF服务不可达](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-100072 目的NF服务不可达_26182301.md) 告警，查询N40接口的通信是否存在故障。

## ④ 自动比对
- 命令真相参数（2）：['PRIMARYCHFGRP', 'SECONDARYCHFGRP']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 4}（多值→atom 应考虑 decision_driven）
