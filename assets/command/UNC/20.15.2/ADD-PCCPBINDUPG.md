---
id: UNC@20.15.2@MMLCommand@ADD PCCPBINDUPG
type: MMLCommand
name: ADD PCCPBINDUPG（增加用户模板组和PccProfile的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PCCPBINDUPG
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 用户PCC模板绑定
status: active
---

# ADD PCCPBINDUPG（增加用户模板组和PccProfile的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

本命令用于将PccProfile绑定到UserProfileGroup下，该PccProfile作为本地PCC用户的策略来源，或者会话创建时无法从PCRF/PCF获取有效规则时的策略来源。

## 注意事项

- 该命令执行后立即生效。
- 一个UsrProfGroup下面最多可以绑定32个UserProfile。
- 需要预先配置USRPROFGROUP和USERPROFILE。
- UNC整机支持最大的绑定规格是32000。
- 用户激活后优先安装ADD PCCPBINDUPG命令绑定的UserProfile，如果ADD PCCPBINDUPG命令未绑定任何UserProfile，则使用ADD UPBINDUPG中绑定的UserProfile。
- ADD PCCPBINDUPG命令配置后，common policy仍使用ADD UPBINDUPG中配置的匹配条件的UserProfile中的策略。（common policy的定义参见SET PCCFUNC）。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFGNAME | 用户模板组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的USERPROFGNAME必须是系统已经存在的USRPROFGROUP对象名称。 |
| PCCPROFILENAME | 用户PCC模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定USERPROFILE对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD USERPROFILE命令配置生成。<br>- 配置的PCCPROFILENAME必须是系统已经存在的USERPROFILE对象名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCPBINDUPG]] · 用户模板组和PccProfile的绑定关系（PCCPBINDUPG）

## 使用实例

假如运营商需要增加PCCPBindUPG配置，UserProfGName为userprofg1，PccProfileName为userprofile1：

```
ADD PCCPBINDUPG:USERPROFGNAME="userprofg1",PCCPROFILENAME="userprofile1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PCCPBINDUPG.md`
