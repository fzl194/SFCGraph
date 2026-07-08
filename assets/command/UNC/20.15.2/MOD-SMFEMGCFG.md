---
id: UNC@20.15.2@MMLCommand@MOD SMFEMGCFG
type: MMLCommand
name: MOD SMFEMGCFG（修改运营商紧急呼叫会话功能配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SMFEMGCFG
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 紧急呼叫会话配置
status: active
---

# MOD SMFEMGCFG（修改运营商紧急呼叫会话功能配置）

## 功能

**适用NF：SMF**

该命令用于修改指定MNO或MVNO对应的紧急呼叫会话功能配置数据。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |
| ULSESSIONAMBR | 紧急会话上行Session AMBR(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定紧急会话的上行Session AMBR比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| DLSESSIONAMBR | 紧急会话下行session AMBR(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定紧急会话的下行Session AMBR比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| ARPPL | 紧急会话ARP优先级级别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定紧急会话的ARP优先级级别。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15。<br>默认值：无<br>配置原则：<br>取值越小，优先级越高。 |
| ARPPCI | 紧急会话ARP的Pre-emption Capability | 可选必选说明：可选参数<br>参数含义：该参数用于指定紧急会话ARP的Pre-emption Capability。<br>数据来源：本端规划<br>取值范围：<br>- NOT_PREEMPT（不抢占）<br>- MAY_PREEMPT（抢占）<br>默认值：无<br>配置原则：无 |
| ARPPVI | 紧急会话ARP的Pre-emption Vulnerability | 可选必选说明：可选参数<br>参数含义：该参数用于指定紧急会话ARP的Pre-emption Vulnerability。<br>数据来源：本端规划<br>取值范围：<br>- NOT_PREEMPTABLE（不可抢占）<br>- PREEMPTABLE（可抢占）<br>默认值：无<br>配置原则：无 |
| EMGMODE | 紧急会话创建模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定紧急会话创建模式。<br>数据来源：本端规划<br>取值范围：<br>- “VALIDUE（仅限合法用户）”：存在IMSI且IMSI鉴权通过的UE才可以使用紧急呼叫业务。<br>- “IMSIUE（存在IMSI的UE）”：存在IMSI的UE就可以使用紧急呼叫业务。<br>- “ALLUE（所有UE）”：所有UE包括无IMSI的UE都可以使用紧急呼叫业务。<br>默认值：无<br>配置原则：无 |
| FIVEQI | 紧急会话标准5QI | 可选必选说明：可选参数<br>参数含义：该参数用于指定紧急会话的默认QoS Flow的5QI，协议定义IMS信令承载推荐的5QI是5。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~9，69~70，79~80。<br>默认值：无<br>配置原则：无 |
| FIVEQIPL | 紧急会话5QI的优先级别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定紧急会话的5QI优先级别。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：<br>取值越小，优先级越高。取值为0时，表示无效值。此时给RAN的“Non Dynamic 5QI Descriptor”中不携带“Priority Level”。 |
| UDMREG | 紧急会话注册UDM功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地合法用户是否支持向UDM注册紧急呼叫会话信息。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：<br>对于Non-3GPP切换场景，为保证业务连续性，设置该参数为ENABLE。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFEMGCFG]] · 运营商紧急呼叫会话功能配置（SMFEMGCFG）

## 使用实例

修改一条运营商紧急呼叫功能的配置，“运营商标识”为“0”，“紧急会话注册UDM功能开关”为“ENABLE”，执行如下命令：

```
MOD SMFEMGCFG:NOID=0,UDMREG=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改运营商紧急呼叫会话功能配置（MOD-SMFEMGCFG）_37903905.md`
