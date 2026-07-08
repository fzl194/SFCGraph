---
id: UNC@20.15.2@MMLCommand@RMV AUTHNAMEPWDCTRL
type: MMLCommand
name: RMV AUTHNAMEPWDCTRL（删除对鉴权信元用户名和密码的控制）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AUTHNAMEPWDCTRL
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
- 接入管理
- APN管理
- APN鉴权属性
status: active
---

# RMV AUTHNAMEPWDCTRL（删除对鉴权信元用户名和密码的控制）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除对鉴权信元用户名和密码的控制。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EFFECTIVESCOPE | 生效范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定单APN生效或全局生效。<br>数据来源：本端规划<br>取值范围：<br>- “GLOBAL（全局生效）”：全局生效<br>- “SINGLE_APN（单个APN生效）”：单个APN生效<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：该参数在"EFFECTIVESCOPE"配置为"SINGLE_APN"时为条件必选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PCONAME | PCO是否携带用户名 | 可选必选说明：必选参数<br>参数含义：该参数表示PCO是否携带用户名。<br>数据来源：本端规划<br>取值范围：<br>- “PCO_NAME_FALSE（PCO未携带用户名）”：PCO未携带用户名。<br>- “PCO_NAME_TRUE（PCO携带用户名）”：PCO携带用户名。<br>- “PCO_NAME_UNLIMITED（不限制PCO是否携带用户名）”：不限制PCO是否携带用户名。<br>默认值：无<br>配置原则：无 |
| PCOPWD | PCO是否携带密码 | 可选必选说明：必选参数<br>参数含义：该参数表示PCO是否携带密码。<br>数据来源：本端规划<br>取值范围：<br>- “PCO_PWD_FALSE（PCO未携带密码）”：PCO未携带密码。<br>- “PCO_PWD_TRUE（PCO携带密码）”：PCO携带密码。<br>- “PCO_PWD_UNLIMITED（不限制PCO是否携带密码）”：不限制PCO是否携带密码。<br>默认值：无<br>配置原则：无 |
| ACCESSMODE | 接入模式 | 可选必选说明：必选参数<br>参数含义：该参数表示接入模式。<br>数据来源：本端规划<br>取值范围：<br>- “TRANS_AUTH（透明鉴权）”：指定为透明并需要鉴权。这种鉴权方式对用户是透明的，不需要用户感知，鉴权使用的用户名和密码一般由PGW/GGSN配置。<br>- “TRANS_NON_AUTH（透明不鉴权）”：指定为透明不需要鉴权。这种接入方式不需要去RADIUS服务器鉴权。<br>- “NON_TRANS（不透明）”：指定为不透明接入，需要鉴权。这种鉴权方式可以继续配置鉴权使用的用户名和密码。<br>- “LOC_AUTH（本地鉴权）”：指定为本地鉴权。这种接入方式不需要去RADIUS服务器鉴权，通过PGW/GGSN完成鉴权功能。<br>- “ACCESS_MODE_UNLIMITED（接入模式无限制）”：接入模式无限制。<br>默认值：无<br>配置原则：无 |
| AUTHMODE | 鉴权模式 | 可选必选说明：必选参数<br>参数含义：该参数表示鉴权模式。<br>数据来源：本端规划<br>取值范围：<br>- “PCO（使用PCO）”：表示鉴权和计费消息使用PCO中携带的用户名和密码。<br>- “APN（使用APN）”：表示鉴权和计费消息使用APN作为用户名，密码由参数PASSWORD配置。<br>- “MSISDN（使用MSISDN）”：表示鉴权和计费消息使用MSISDN作为用户名，密码由PASSWORD配置。<br>- “AUTH_MODE_UNLIMITED（鉴权模式无限制）”：鉴权模式无限制。<br>默认值：无<br>配置原则：无 |
| PCOPRIORITY | PCO优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定当鉴权方式选择为APN或者MSISDN的时候，如果PCO携带了用户名、密码，是否优先采用PCO中的携带的用户名密码。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能<br>- “ENABLE（使能）”：使能<br>- “UNLIMITED（无限制）”：无限制<br>默认值：无<br>配置原则：无 |
| PWDUSEPCO | 使用PCO中的密码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定当鉴权方式选择为APN或者MSISDN的时候，密码是否优先采用PCO中携带的密码。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能<br>- “ENABLE（使能）”：使能<br>- “UNLIMITED（无限制）”：无限制<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AUTHNAMEPWDCTRL]] · 对鉴权信元用户名和密码的控制（AUTHNAMEPWDCTRL）

## 使用实例

如果需要删除某条鉴权信元内用户名和密码的填写方式记录，如删除在透明鉴权下，所有APN下，通过读取配置填入鉴权的用户名，通过配置中的CommonUserPass填充密码信元，可以使用该实例：

```
RMV AUTHNAMEPWDCTRL: EFFECTIVESCOPE=GLOBAL, PCONAME=PCO_NAME_UNLIMITED, PCOPWD=PCO_PWD_UNLIMITED, ACCESSMODE=TRANS_AUTH, AUTHMODE=AUTH_MODE_UNLIMITED, PCOPRIORITY=UNLIMITED, PWDUSEPCO=UNLIMITED;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-AUTHNAMEPWDCTRL.md`
