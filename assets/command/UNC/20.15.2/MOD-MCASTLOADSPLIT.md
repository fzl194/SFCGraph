---
id: UNC@20.15.2@MMLCommand@MOD MCASTLOADSPLIT
type: MMLCommand
name: MOD MCASTLOADSPLIT（修改组播负载分担配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: MCASTLOADSPLIT
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- MRM
- 组播负载分担配置
status: active
---

# MOD MCASTLOADSPLIT（修改组播负载分担配置）

## 功能

该命令用来修改组播负载分担配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| LOADSPLITTING | 负载分担方式 | 可选必选说明：必选参数<br>参数含义：该参数用来表示负载分担方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BALANCE：稳定优先方式的组播路由负载分担。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MCASTLOADSPLIT]] · 组播负载分担配置（MCASTLOADSPLIT）

## 使用实例

修改组播负载分担类型为稳定优先：

```
MOD MCASTLOADSPLIT:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,LOADSPLITTING=BALANCE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-MCASTLOADSPLIT.md`
