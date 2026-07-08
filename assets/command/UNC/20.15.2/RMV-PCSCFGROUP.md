---
id: UNC@20.15.2@MMLCommand@RMV PCSCFGROUP
type: MMLCommand
name: RMV PCSCFGROUP（删除P-CSCF组配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PCSCFGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- IMS管理
- P-CSCF管理
- P-CSCF组
status: active
---

# RMV PCSCFGROUP（删除P-CSCF组配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除UNC设备P-CSCF组配置信息。网络中规划IMS业务，当不需要进行IMS业务或某个P-CSCF组被取消时，使用该命令可以删除不再使用的P-CSCF组信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | P-CSCF组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定P-CSCF组的名字，在系统内唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCSCFGROUP]] · P-CSCF组配置（PCSCFGROUP）

## 使用实例

网络中规划IMS网络，在需要删除指定P-CSCF组的信息时举例：P-CSCF组名为mygroup：

```
RMV PCSCFGROUP:GROUPNAME="mygroup";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除P-CSCF组配置（RMV-PCSCFGROUP）_09651437.md`
