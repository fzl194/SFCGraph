---
id: UNC@20.15.2@MMLCommand@SET SRROUTEFRR
type: MMLCommand
name: SET SRROUTEFRR（设置静态路由FRR）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SRROUTEFRR
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 静态路由管理
- 设置静态路由FRR功能
status: active
---

# SET SRROUTEFRR（设置静态路由FRR）

## 功能

该命令用来使能静态路由FRR功能。

为了对静态路由实行保护，配置主备链路保护时需要配置静态路由的FRR功能。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。支持IPv4和IPv6单播地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>- 需要确保指定的VPN实例在设备上已经通过ADD L3VPNINST创建，公网除外。<br>- 必须已经通过ADD VPNINSTAF使能了该VPN的地址族。 |
| FRRENABLE | 是否使能FRR | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否使能静态路由FRR功能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：初始值为FALSE。 |

## 操作的配置对象

- [静态路由FRR（SRROUTEFRR）](configobject/UNC/20.15.2/SRROUTEFRR.md)

## 使用实例

配置IPv4公网静态路由FRR：

```
SET SRROUTEFRR:AFTYPE=ipv4unicast,VRFNAME="_public_",FRRENABLE=TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置静态路由FRR（SET-SRROUTEFRR）_49960966.md`
