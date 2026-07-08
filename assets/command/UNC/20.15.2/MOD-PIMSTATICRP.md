---
id: UNC@20.15.2@MMLCommand@MOD PIMSTATICRP
type: MMLCommand
name: MOD PIMSTATICRP（修改PIM静态RP配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PIMSTATICRP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- PIM静态RP
status: active
---

# MOD PIMSTATICRP（修改PIM静态RP配置）

## 功能

该命令用于修改静态RP配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| STATICRPADDR | 静态RP的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用于表示静态RP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| STATICRPPLYIPV4 | 静态RP策略 | 可选必选说明：可选参数<br>参数含义：该参数用于表示静态RP名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| PREFERENCE | 静态RP的优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于表示静态RP优先。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1。<br>默认值：无 |
| BIDIRENABLE | 静态RP使能双向PIM | 可选必选说明：可选参数<br>参数含义：该参数用于表示静态RP使能双向PIM。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |

## 操作的配置对象

- [PIM静态RP配置（PIMSTATICRP）](configobject/UNC/20.15.2/PIMSTATICRP.md)

## 使用实例

修改PIM静态RP配置(192.168.0.2)：

```
MOD PIMSTATICRP:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,STATICRPADDR="192.168.0.2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改PIM静态RP配置（MOD-PIMSTATICRP）_50281162.md`
