---
id: UNC@20.15.2@MMLCommand@ADD PIMSTATICRP
type: MMLCommand
name: ADD PIMSTATICRP（添加PIM静态RP配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PIMSTATICRP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- PIM静态RP
status: active
---

# ADD PIMSTATICRP（添加PIM静态RP配置）

## 功能

该命令用于添加静态RP配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 通过重复执行该命令可以最多配置50个静态RP，但同一个ACL不能对应到多个静态RP，如果不引用ACL，则只能配置一个静态RP。
- 需要首先在公网或VPN实例下配置ADD MCASTENABLE命令。
- 需要首先通过命令ADD PIMSITE使能PIM。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| STATICRPADDR | 静态RP的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用于表示静态RP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| STATICRPPLYIPV4 | 静态RP策略 | 可选必选说明：可选参数<br>参数含义：该参数用于表示静态RP名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无 |
| PREFERENCE | 静态RP的优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于表示静态RP优先。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1。<br>默认值：0 |
| BIDIRENABLE | 静态RP使能双向PIM | 可选必选说明：可选参数<br>参数含义：该参数用于表示静态RP使能双向PIM。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：FALSE |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PIMSTATICRP]] · PIM静态RP配置（PIMSTATICRP）

## 使用实例

添加PIM静态RP配置(192.168.0.1)：

```
ADD PIMSTATICRP:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,STATICRPADDR="192.168.0.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PIMSTATICRP.md`
