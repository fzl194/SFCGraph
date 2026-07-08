---
id: UNC@20.15.2@MMLCommand@FOC GENERATECDR
type: MMLCommand
name: FOC GENERATECDR（强制生成话单）
nf: UNC
version: 20.15.2
verb: FOC
object_keyword: GENERATECDR
command_category: 调测类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费维护
- 强制生成话单
status: active
---

# FOC GENERATECDR（强制生成话单）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

![](强制生成话单（FOC GENERATECDR）_09897016.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，如果在大量用户的场景下执行该命令，可能导致CG侧收到大量的话单消息，对CG造成冲击，可能导致用户无法计费。

该命令用来强制产生话单，主要用于测试计费系统是否正常。如果在测试过程中，UNC产生话单的各种阈值未到，还不具备自动产生话单的条件时，用户可采用本命令手动产生话单。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定强制产生话单的粒度。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL：指定所有用户强制产生话单。<br>- MSISDN：指定MSISDN粒度强制产生话单。<br>- IMSI：指定IMSI粒度强制产生话单。<br>- POD：指定Pod粒度强制产生话单。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“RANGE”配置为“MSISDN”时为必选参数。<br>参数含义：该参数用于指定用户的MSISDN号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“RANGE”配置为“IMSI”时为必选参数。<br>参数含义：该参数用于指定用户的IMSI号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RANGE”配置为“POD”时为必选参数。<br>参数含义：该参数用于指定POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GENERATECDR]] · 立即生成话单（GENERATECDR）

## 使用实例

强制IMSI为13631112221的用户产生话单：

```
FOC GENERATECDR:RANGE=IMSI,IMSI="13631112221";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/强制生成话单（FOC-GENERATECDR）_09897016.md`
