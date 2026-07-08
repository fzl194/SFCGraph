---
id: UNC@20.15.2@MMLCommand@RMV APNPROFSPACE
type: MMLCommand
name: RMV APNPROFSPACE（删除APN与Profile Space的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNPROFSPACE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- APN绑定Profile Space
status: active
---

# RMV APNPROFSPACE（删除APN与Profile Space的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

本命令用于删除APN与Profile Space的绑定关系。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN与Profile Space的绑定关系（APNPROFSPACE）](configobject/UNC/20.15.2/APNPROFSPACE.md)

## 使用实例

删除APNProfSpace配置，APN为“apn1”：

```
RMV APNPROFSPACE:APN="apn1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN与Profile-Space的绑定关系（RMV-APNPROFSPACE）_09897054.md`
