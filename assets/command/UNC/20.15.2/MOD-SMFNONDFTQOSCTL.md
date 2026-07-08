---
id: UNC@20.15.2@MMLCommand@MOD SMFNONDFTQOSCTL
type: MMLCommand
name: MOD SMFNONDFTQOSCTL（修改SMF的非Default QoS Flow配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SMFNONDFTQOSCTL
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 5GC非缺省Flow QoS
status: active
---

# MOD SMFNONDFTQOSCTL（修改SMF的非Default QoS Flow配置）

## 功能

**适用NF：SMF**

该命令用来修改SMF的非Default QoS Flow配置。

## 注意事项

命令执行后只对新接入用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成QoS控制的用户归属地网络的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成QoS控制的用户归属地网络的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| CTRLTYPE | 控制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS控制的类型。<br>数据来源：全网规划<br>取值范围：<br>- DNN_LEVEL（DNN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：该参数在"CTRLTYPE"配置为"DNN_LEVEL"时为条件必选参数。<br>参数含义：该参数用于指定组成QoS控制的DNN，即用户请求的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| MFBRUL | 上行最大速率 (千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的上行最大速率 (千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65000000。本参数不配置时为无效值0，表示不进行限速或管控。<br>默认值：无<br>配置原则：无 |
| MFBRDL | 下行最大速率 (千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的下行最大速率 (千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65000000。本参数不配置时为无效值0，表示不进行限速或管控。<br>默认值：无<br>配置原则：无 |
| GFBRUL | 上行保证速率 (千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的上行保证大速率 (千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65000000。本参数不配置时为无效值0，表示不进行限速或管控。<br>默认值：无<br>配置原则：无 |
| GFBRDL | 下行保证速率 (千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的下行保证大速率 (千比特/秒)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65000000。本参数不配置时为无效值0，表示不进行限速或管控。<br>默认值：无<br>配置原则：无 |
| QOSACTION | 超过带宽的处理 | 可选必选说明：可选参数<br>参数含义：该参数用于表示超过带宽的处理行为。<br>数据来源：本端规划<br>取值范围：<br>- “DEGRADE（降级）”：表示如果请求的级别大于配置最高级别，则请求的级别自动降为配置的最高级别。<br>- “REJECT（拒绝）”：表示如果请求的级别超过配置的最高级别，则协商结束，激活失败。<br>默认值：无<br>配置原则：无 |
| BINDALLOWED5QIS | 绑定允许的5QI列表 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否绑定允许的5QI列表。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |
| ALLOWED5QIS | 允许的5QI列表索引 | 可选必选说明：该参数在"BINDALLOWED5QIS"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于指定允许的5QI列表索引，用来绑定允许的5QI列表。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| BINDALLOWEDARPS | 绑定允许的ARP列表 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否绑定允许的ARP列表。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |
| ALLOWEDARPS | 允许的ARP列表索引 | 可选必选说明：该参数在"BINDALLOWEDARPS"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于指定允许的ARP列表索引，用来绑定允许的ARP列表。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SMF的非Default QoS Flow配置（SMFNONDFTQOSCTL）](configobject/UNC/20.15.2/SMFNONDFTQOSCTL.md)

## 使用实例

将“移动国家码”为“460”，“移动网号”为“00”，控制类型为GLOBAL_LEVEL的QoS配置修改为“上行最大速率(千比特/秒)”为5000，执行如下命令：

```
MOD SMFNONDFTQOSCTL:MCC="460",MNC="00",CTRLTYPE=GLOBAL_LEVEL,MFBRUL=5000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SMF的非Default-QoS-Flow配置（MOD-SMFNONDFTQOSCTL）_13800470.md`
