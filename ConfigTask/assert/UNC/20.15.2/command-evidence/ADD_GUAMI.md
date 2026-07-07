# 命令证据包：ADD GUAMI
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/本局信息管理/AMF/AMF全局标识符管理/增加AMF全局标识（ADD GUAMI）_09653726.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：AMF**

该命令用于为AMF实例配置全局AMF标识符（GUAMI）。GUAMI的组成是[MCC] + [MNC] + [AMF Region ID] + [AMF Set ID] + [AMF Pointer]。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 同一个AMF Set内，各AMF配置的GUAMI不能相同。
- AMF实例支持以GUAMI粒度指定备用AMF。
- 对于同一个AMF实例，多个GUAMI配置间，AMFREGIONID和AMFSETID必须相同，当两条记录的PLMNIDX相同时，AMFPOINTER必须不同；当两条记录的PLMNIDX不同时，AMFPOINTER可以相同，也可以不同。
- 本命令配置

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| INDEX | GUAMI索引 | local_planned | required | 无 | 整数类型，取值范围是0~255。 |
| PLMNIDX | PLMN索引 | global_planned | required | 无 | 整数类型，取值范围是0~127。 |
| AMFREGIONID | AMF区域标识 | global_planned | required | 无 | 字符串类型，输入长度是2。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A- |
| AMFSETID | AMF集合标识 | global_planned | required | 无 | 字符串类型，输入长度是3。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A- |
| AMFPOINTER | AMF指示符 | global_planned | required | 无 | 字符串类型，输入长度是2。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A- |
| BACKUPAMFNAME | 备用AMF名称 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~150。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-104301

**md：`WSFD-104301/特性概述_60374820.md`**
- 操作步骤上下文（±2 行原文）：
  L64:
    > AMF Pool如 [图1](#ZH-CN_CONCEPT_0160374820__fig9858143493911) 所示，一组AMF（AMF1~AMF3）可以构成一个AMF Pool。当一个用户在一个AMF Pool区范围内移动，可持续由某个特定AMF提供服务，只要用户在Pool区内活动，就不会发生区域内的跨AMF重注册和切换。这使得用户在活动时产生的Inter AMF Registration和Handover流程大大减少，从而降低了AMF与AMF之间、AMF和UDM之间的信令，降低网络负荷。
    > 
    > AMF Set就对应一个AMF Pool，Pool内所有AMF支持相同的切片类型，不同的Pool所支持的切片类型不相同。GUAMI中的MCC、MNC 、AMF Region ID和AMF Set ID全球唯一标识一个AMF Set，所有在部署AMF Pool的时候，可以通过 [**ADD GUAMI**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/本局信息管理/AMF/AMF全局标识符管理/增加AMF全局标识（ADD GUAMI）_09653726.md) 命令，为Pool内AMF配置相同的PLMN、AMF Region ID和AMF Set ID。增加GUAMI需要在 “初始配置 > 配置AMF” 的时候完成。
    > 
    > **图1** AMF Pool示意图

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L19:
    > - [**ADD RULE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD GUAMI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/本局信息管理/AMF/AMF全局标识符管理/增加AMF全局标识（ADD GUAMI）_09653726.md)
    > - [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)
    > - [**ADD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)

## ④ 自动比对
- 命令真相参数（6）：['AMFPOINTER', 'AMFREGIONID', 'AMFSETID', 'BACKUPAMFNAME', 'INDEX', 'PLMNIDX']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
