---
id: UDG@20.15.2@MMLCommand@RMV SQOSVPNGROUPMEM
type: MMLCommand
name: RMV SQOSVPNGROUPMEM（删除VPN组成员）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SQOSVPNGROUPMEM
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- VPN组成员
status: active
---

# RMV SQOSVPNGROUPMEM（删除VPN组成员）

## 功能

该命令用来删除VPN组成员。

## 注意事项

- 该命令执行后立即生效。

- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNGROUPNAME | VPN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| VPNNAME | VPN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| VPNPRIORITY | VPN优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～16。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SQOSVPNGROUPMEM]] · VPN组成员（SQOSVPNGROUPMEM）

## 使用实例

删除VPN组成员：

```
RMV SQOSVPNGROUPMEM:VPNGROUPNAME="vg1",VPNNAME="vpn1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-SQOSVPNGROUPMEM.md`
