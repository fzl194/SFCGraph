---
id: UDG@20.15.2@MMLCommand@ADD SQOSVPNGROUP
type: MMLCommand
name: ADD SQOSVPNGROUP（增加VPN组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SQOSVPNGROUP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- VPN组
status: active
---

# ADD SQOSVPNGROUP（增加VPN组）

## 功能

该命令用来配置VPN组。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1024。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNGROUPNAME | VPN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SQOSVPNGROUP]] · VPN组（SQOSVPNGROUP）

## 使用实例

配置VPN组：

```
ADD SQOSVPNGROUP:VPNGROUPNAME="vg1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-SQOSVPNGROUP.md`
