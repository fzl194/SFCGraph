# 命令证据包：RMV TSTPCFBINDING
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF拨测管理/删除拨测用户和PCF的绑定关系（RMV TSTPCFBINDING）_22438295.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、PGW-C、GGSN**

该命令用于删除用户和PCF的绑定关系。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。

- 支持分别以APN、IMSI、PCFINSTANCEID以及其组合作为查询条件删除已有配置。
- 不输入任何参数默认删除所有配置。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APN | APN名称 | local_planned | optional | 无 | 字符串类型，输入长度范围是1~63。大小写不敏感。 |
| IMSI | IMSI | local_planned | optional | 无 | 字符串类型，输入长度范围是6~15。每个字符只能是十进制数字。 |
| PCFINSTANCEID | PCF实例标识 | global_planned | optional | 无 | 字符串类型，输入长度范围是1~50。构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/调测PCC基本功能_45059543.md`**
- 任务示例脚本（该命令行）：
  `RMV TSTPCFBINDING: APN="apn-test",IMSI="460000123456789",PCFINSTANCEID="testPcfInstanceID";`
- 操作步骤上下文（±2 行原文）：
  L75:
    >     - 存在，调测结果正常，请执行[步骤 9](#ZH-CN_OPI_0000001245059543__step1829759115218)。
    >     - 不存在，请执行[步骤 11](#ZH-CN_OPI_0000001245059543__step114691314193316)。
    > 9. 执行 [**RMV TSTPCFBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF拨测管理/删除拨测用户和PCF的绑定关系（RMV TSTPCFBINDING）_22438295.md) 命令，删除拨测用户和PCF的绑定关系。
    >   ```
    >   RMV TSTPCFBINDING: APN="apn-test",IMSI="460000123456789",PCFINSTANCEID="testPcfInstanceID";
  L77:
    > 9. 执行 [**RMV TSTPCFBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF拨测管理/删除拨测用户和PCF的绑定关系（RMV TSTPCFBINDING）_22438295.md) 命令，删除拨测用户和PCF的绑定关系。
    >   ```
    >   RMV TSTPCFBINDING: APN="apn-test",IMSI="460000123456789",PCFINSTANCEID="testPcfInstanceID";
    >   ```
    >   > **说明**

## ④ 自动比对
- 命令真相参数（3）：['APN', 'IMSI', 'PCFINSTANCEID']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
