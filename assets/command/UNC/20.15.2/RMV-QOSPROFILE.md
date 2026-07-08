---
id: UNC@20.15.2@MMLCommand@RMV QOSPROFILE
type: MMLCommand
name: RMV QOSPROFILE（删除QoS描述配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOSPROFILE
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- QoS模板
status: active
---

# RMV QOSPROFILE（删除QoS描述配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于删除QosProfile的配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoSProfile名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数不能和命令SET QOSGLOBAL的QosProfileName重复。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSPROFILE]] · QoS描述配置（QOSPROFILE）

## 使用实例

删除QosProfile名字为test的配置信息：

```
RMV QOSPROFILE:QOSPROFILENAME="test";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-QOSPROFILE.md`
