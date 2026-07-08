---
id: UNC@20.15.2@MMLCommand@RMV MONVPN
type: MMLCommand
name: RMV MONVPN（删除监控VPN实例）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MONVPN
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# RMV MONVPN（删除监控VPN实例）

## 功能

该命令用于删除监控VPN实例。

## 注意事项

- 该命令执行后立即生效。

- 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRGROUPID | 容灾组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于配置容灾组标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：无 |
| VPNGRPID | VPN组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于配置VPN组标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~10。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置VPN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。VPN实例名称禁止相同。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MONVPN]] · 监控VPN实例（MONVPN）

## 使用实例

删除监控VPN实例:

```
%%RMV MONVPN:DRGROUPID=1,VPNGRPID=1,VPNINSTANCE="1";%%
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MONVPN.md`
