---
id: UNC@20.15.2@MMLCommand@MOD CCPFOT
type: MMLCommand
name: MOD CCPFOT（修改融合计费Proxy Failover模板）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CCPFOT
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 融合计费Proxy Failover模板
status: active
---

# MOD CCPFOT（修改融合计费Proxy Failover模板）

## 功能

**适用NF：NCG**

该命令用于修改融合计费Proxy Failover模板。

## 注意事项

- 该命令执行后立即生效。

- 本命令配置的所有参数可用于ADD/MOD CCPCCACT命令。
- 本命令配置的“Failover模板标识”、“是否支持Failover开关”和“FailureHandling枚举值”可用于ADD/MOD CCPRCACT命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FOTNM | Failover模板标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定融合计费Proxy Failover模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |
| FOENABLE | 是否支持Failover开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否支持Failover开关。<br>数据来源：本端规划<br>取值范围：<br>- TRUE（TRUE）<br>- FALSE（FALSE）<br>默认值：无<br>配置原则：无 |
| FH | FailureHandling枚举值 | 可选必选说明：该参数在"FOENABLE"配置为"TRUE"时为条件可选参数。<br>参数含义：该参数用于设置FailureHandling枚举值。<br>数据来源：本端规划<br>取值范围：<br>- TERMINATE（TERMINATE）<br>- CONTINUE（CONTINUE）<br>- RETRYANDTERM（RETRYANDTERM）<br>- ALWAYSCONTINUE（ALWAYSCONTINUE）<br>默认值：无<br>配置原则：无 |
| UVDQ | 默认上行流量额度(KB) | 可选必选说明：该参数在"FOENABLE"配置为"TRUE"时为条件可选参数。<br>参数含义：该参数用于设置默认上行流量额度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295，单位是千字节。<br>默认值：无<br>配置原则：无 |
| DVDQ | 默认下行流量额度(KB) | 可选必选说明：该参数在"FOENABLE"配置为"TRUE"时为条件可选参数。<br>参数含义：该参数用于设置默认下行流量额度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295，单位是千字节。<br>默认值：无<br>配置原则：无 |
| TQ | 默认时长额度(s) | 可选必选说明：该参数在"FOENABLE"配置为"TRUE"时为条件可选参数。<br>参数含义：该参数用于设置默认时长额度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~86400，单位是秒。<br>默认值：无<br>配置原则：无 |
| EVTQ | 默认事件额度(次) | 可选必选说明：该参数在"FOENABLE"配置为"TRUE"时为条件可选参数。<br>参数含义：该参数用于设置默认事件额度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1000。<br>默认值：无<br>配置原则：无 |
| RESPPLCY | NCG代应答时的配额类型选择 | 可选必选说明：该参数在"FOENABLE"配置为"TRUE"时为条件可选参数。<br>参数含义：该参数用于指定NCG代应答时的配额类型选择。<br>数据来源：本端规划<br>取值范围：<br>- “TIME（时长额度）”：根据TIME选择RESP<br>- “UPVOLUME（上行流量额度）”：根据UPVOLUME选择RESP<br>- “DOWNVOLUME（下行流量额度）”：根据DOWNVOLUME选择RESP<br>- “SUMVOLUME（流量总额度）”：根据SUMVOLUME选择RESP<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CCPFOT]] · 融合计费Proxy Failover模板（CCPFOT）

## 使用实例

修改Failover模板标识名称为“ccpfot1”的融合计费Proxy Failover模板，设置默认上行流量额度为“5120”：

```
MOD CCPFOT: FOTNM="ccpfot1", FOENABLE=TRUE, DVDQ=5120;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-CCPFOT.md`
