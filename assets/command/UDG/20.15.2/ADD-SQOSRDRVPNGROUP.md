---
id: UDG@20.15.2@MMLCommand@ADD SQOSRDRVPNGROUP
type: MMLCommand
name: ADD SQOSRDRVPNGROUP（增加QoS重定向VPN组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SQOSRDRVPNGROUP
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
- 重定向VPN组
status: active
---

# ADD SQOSRDRVPNGROUP（增加QoS重定向VPN组）

## 功能

该命令用来配置重定向VPN。通过流策略将该动作应用于具体接口，对匹配类的流量进行重定向。在网络部署中，如果用户希望一部分流量不按照报文的正常路由路径转发而是由用户来指定这部分流量的转发VPN，这种情况下需要部署重定向特性。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1024。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNGROUPNAME | VPN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定重定向VPN组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。字符串由数字、字母、“.”、“-”或“_”组成。默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 需要先使用ADD SQOSVPNGROUP命令添加VPN组，使用ADD L3VPNINST命令添加VPN实例，使用ADD SQOSVPNGROUPMEM命令向VPN组添加VPN成员。 |
| BEHAVIORNAME | 行为名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流动作。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 需要先使用ADD MQCBEHAVIOR命令添加流行为。 |

## 操作的配置对象

- [QoS重定向VPN组（SQOSRDRVPNGROUP）](configobject/UDG/20.15.2/SQOSRDRVPNGROUP.md)

## 使用实例

在流行为b5中配置重定向VPN动作：

```
ADD SQOSRDRVPNGROUP:BEHAVIORNAME="b5",VPNGROUPNAME="vg1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加QoS重定向VPN组（ADD-SQOSRDRVPNGROUP）_00441265.md`
