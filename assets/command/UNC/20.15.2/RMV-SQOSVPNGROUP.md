---
id: UNC@20.15.2@MMLCommand@RMV SQOSVPNGROUP
type: MMLCommand
name: RMV SQOSVPNGROUP（删除VPN组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SQOSVPNGROUP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- VPN组
status: active
---

# RMV SQOSVPNGROUP（删除VPN组）

## 功能

该命令用来删除VPN组。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNGROUPNAME | VPN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [VPN组（SQOSVPNGROUP）](configobject/UNC/20.15.2/SQOSVPNGROUP.md)

## 使用实例

删除VPN组：

```
RMV SQOSVPNGROUP:VPNGROUPNAME="vg1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除VPN组（RMV-SQOSVPNGROUP）_00440585.md`
