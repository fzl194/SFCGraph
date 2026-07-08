---
id: UNC@20.15.2@MMLCommand@MOD APNPROFSPACE
type: MMLCommand
name: MOD APNPROFSPACE（修改APN与Profile Space的绑定关系）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD APNPROFSPACE（修改APN与Profile Space的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

本命令用于修改APN与Profile Space的绑定关系。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| PROFSPACENAME | Profile Space名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ProfileSpace实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNPROFSPACE]] · APN与Profile Space的绑定关系（APNPROFSPACE）

## 使用实例

修改APNProfSpace配置，APN为“apn1”，PROFSPACENAME为“profilespace2”：

```
MOD APNPROFSPACE:APN="apn1",PROFSPACENAME="profilespace2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN与Profile-Space的绑定关系（MOD-APNPROFSPACE）_09897053.md`
