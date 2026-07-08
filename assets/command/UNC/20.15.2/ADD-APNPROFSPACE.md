---
id: UNC@20.15.2@MMLCommand@ADD APNPROFSPACE
type: MMLCommand
name: ADD APNPROFSPACE（增加APN与Profile Space的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNPROFSPACE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 3000
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- APN绑定Profile Space
status: active
---

# ADD APNPROFSPACE（增加APN与Profile Space的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

本命令用于配置APN与ProfileSpace的绑定关系。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为3000。
- 每个APN最多可以绑定一个ProfileSpace。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：配置的APN必须是系统已经存在的APN对象名称。 |
| PROFSPACENAME | Profile Space名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ProfileSpace实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD PROFILESPACE命令配置生成。<br>- 配置的ProfSpaceName必须是ProfileSpace的对象名。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNPROFSPACE]] · APN与Profile Space的绑定关系（APNPROFSPACE）

## 使用实例

将Profile Space名称为“profilespace1”的Profile Space绑定到指定APN “apn1”下：

```
ADD APNPROFSPACE:APN="apn1",PROFSPACENAME="profilespace1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APNPROFSPACE.md`
