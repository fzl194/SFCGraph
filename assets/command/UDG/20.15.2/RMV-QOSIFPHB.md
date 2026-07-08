---
id: UDG@20.15.2@MMLCommand@RMV QOSIFPHB
type: MMLCommand
name: RMV QOSIFPHB（删除禁止QoS优先级映射的类型）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: QOSIFPHB
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- QoS IF PHB
status: active
---

# RMV QOSIFPHB（删除禁止QoS优先级映射的类型）

## 功能

该命令用于删除接口下的禁止PHB映射的实例。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| PHBTYPE | 出接口报文的优先级字段映射类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置出接口报文的优先级字段映射类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- dscp：IP报文的DSCP。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@QOSIFPHB]] · 禁止QoS优先级映射的类型（QOSIFPHB）

## 使用实例

在接口Ethernet66/0/3下删除禁止DSCP映射：

```
RMV QOSIFPHB : IFNAME="Ethernet66/0/3",PHBTYPE=dscp;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-QOSIFPHB.md`
