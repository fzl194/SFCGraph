---
id: UNC@20.15.2@MMLCommand@MOD SECPOLICYALARM
type: MMLCommand
name: MOD SECPOLICYALARM（修改安全策略告警配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SECPOLICYALARM
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略告警
status: active
---

# MOD SECPOLICYALARM（修改安全策略告警配置）

## 功能

该命令用来修改上送CPU报文产生告警参数的配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：必选参数<br>参数含义：安全策略编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |
| SECPOLICYTYPE | 安全策略类型 | 可选必选说明：必选参数<br>参数含义：策略类型，如应用层联动、TCP/IP防攻击、黑白名单等。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Tcpip：TCP/IP策略。<br>- TotalPkt：所有报文。<br>- WhiteList：白名单策略。<br>- BlackList：黑名单策略。<br>- Index：索引策略。<br>- UserFlow：用户自定义流策略。<br>- APP：APP应用策略。<br>- Urpf：URPF策略。<br>- WhiteListV6：IPv6白名单。<br>默认值：无 |
| SECPOLICYTYPEID | 安全策略类型编号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Index” 或 “UserFlow”时为必选参数。<br>参数含义：安全策略类型编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| SECALARMFLAG | 安全告警使能 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“WhiteList”、“Index”、“APP”、“UserFlow”、“BlackList”、“Urpf”、“Tcpip”、“WhiteListV6” 或 “TotalPkt”时为必选参数。<br>参数含义：策略告警是否使能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| SECALARMTHLD | 安全告警阈值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“WhiteList”、“Index”、“APP”、“UserFlow”、“BlackList”、“Urpf”、“Tcpip”、“WhiteListV6” 或 “TotalPkt”时为必选参数。<br>参数含义：告警阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1000000。<br>默认值：无 |
| SECALARMINT | 安全告警时间间隔（秒） | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“WhiteList”、“Index”、“APP”、“UserFlow”、“BlackList”、“Urpf”、“Tcpip”、“WhiteListV6” 或 “TotalPkt”时为必选参数。<br>参数含义：告警时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～3600，单位是秒。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECPOLICYALARM]] · 安全策略告警配置（SECPOLICYALARM）

## 使用实例

修改上送CPU报文产生告警参数的配置：

```
MOD SECPOLICYALARM:SECPOLICYID=1,SECPOLICYTYPE=WhiteList,SECALARMFLAG=TRUE,SECALARMTHLD=1,SECALARMINT=60;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SECPOLICYALARM.md`
