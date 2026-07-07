# 命令证据包：ADD TSTPCFBINDING
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF拨测管理/增加拨测用户和PCF的绑定关系（ADD TSTPCFBINDING）_22438289.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、PGW-C、GGSN**

该命令用于配置用户和PCF的绑定关系。一般用于拨测场景，将指定APN和IMSI的用户激活到指定PCF，测试该PCF的基本功能。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。

- 拨测PCF完成后，要删除该配置。
- 不支持failover功能，若绑定的PCF故障，则用户激活失败。

- 最多可输入100条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APN | APN名称 | local_planned | required | 无 | 字符串类型，输入长度范围是1~63。大小写不敏感。 |
| IMSI | IMSI | local_planned | required | 无 | 字符串类型，输入长度范围是6~15。每个字符只能是十进制数字。 |
| PCFINSTANCEID | PCF实例标识 | global_planned | required | 无 | 字符串类型，输入长度范围是1~50。构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/调测PCC基本功能_45059543.md`**
- 任务示例脚本（该命令行）：
  `ADD TSTPCFBINDING: APN="apn-test",IMSI="460000123456789",PCFINSTANCEID="testPcfInstanceID";`
- 操作步骤上下文（±2 行原文）：
  L45:
    > 
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 执行 [**ADD TSTPCFBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF拨测管理/增加拨测用户和PCF的绑定关系（ADD TSTPCFBINDING）_22438289.md) 命令，配置拨测用户和PCF的绑定关系。
    >   ```
    >   ADD TSTPCFBINDING: APN="apn-test",IMSI="460000123456789",PCFINSTANCEID="testPcfInstanceID";
  L47:
    > 2. 执行 [**ADD TSTPCFBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF拨测管理/增加拨测用户和PCF的绑定关系（ADD TSTPCFBINDING）_22438289.md) 命令，配置拨测用户和PCF的绑定关系。
    >   ```
    >   ADD TSTPCFBINDING: APN="apn-test",IMSI="460000123456789",PCFINSTANCEID="testPcfInstanceID";
    >   ```
    > 3. 创建用户跟踪任务，消息类型选择N4和N7。

## ④ 自动比对
- 命令真相参数（3）：['APN', 'IMSI', 'PCFINSTANCEID']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
