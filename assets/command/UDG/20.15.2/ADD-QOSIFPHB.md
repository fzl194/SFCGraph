---
id: UDG@20.15.2@MMLCommand@ADD QOSIFPHB
type: MMLCommand
name: ADD QOSIFPHB（添加禁止QoS优先级映射的类型）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: QOSIFPHB
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- QoS IF PHB
status: active
---

# ADD QOSIFPHB（添加禁止QoS优先级映射的类型）

## 功能

该命令用于添加接口下的禁止PHB映射的实例。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：区分大小写，不支持空格，下发本MML命令前可LST INTERFACE命令查看可用接口。 |
| PHBTYPE | 出接口报文的优先级字段映射类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置出接口报文的优先级字段映射类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- dscp：IP报文的DSCP。<br>默认值：无 |

## 操作的配置对象

- [禁止QoS优先级映射的类型（QOSIFPHB）](configobject/UDG/20.15.2/QOSIFPHB.md)

## 使用实例

在接口Ethernet66/0/3下添加禁止DSCP映射：

```
ADD QOSIFPHB : IFNAME="Ethernet66/0/3",PHBTYPE=dscp;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加禁止QoS优先级映射的类型（ADD-QOSIFPHB）_00841181.md`
