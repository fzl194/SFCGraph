---
id: UNC@20.15.2@MMLCommand@RMV PCCPBINDUPG
type: MMLCommand
name: RMV PCCPBINDUPG（删除用户模板组和PccProfile的绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PCCPBINDUPG
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 用户PCC模板绑定
status: active
---

# RMV PCCPBINDUPG（删除用户模板组和PccProfile的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

![](删除用户模板组和PccProfile的绑定关系（RMV PCCPBINDUPG）_09897038.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，如果不输入PccProfile名称，表示删除此UsrProfGroup和所有PccProfile的绑定关系。删除后使用该UsrProfGroup的用户可能会因为无法命中PccProfile导致业务受损，请谨慎使用并联系华为支持协助操作。

本命令用于解除UsrProfGroup与所有或某个PccProfile的绑定关系。

## 注意事项

- 该命令执行后立即生效。
- 该命令属于高危命令，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFGNAME | 用户模板组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的USERPROFGNAME必须是系统已经存在的USRPROFGROUP对象名称。 |
| PCCPROFILENAME | 用户PCC模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定USERPROFILE对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的PCCPROFILENAME必须是系统已经存在的USERPROFILE对象名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCPBINDUPG]] · 用户模板组和PccProfile的绑定关系（PCCPBINDUPG）

## 使用实例

删除PCCPBindUPG配置，UserProfGName为userprofg1，PccProfileName为userprofile1：

```
RMV PCCPBINDUPG:USERPROFGNAME="userprofg1",PCCPROFILENAME="userprofile1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PCCPBINDUPG.md`
