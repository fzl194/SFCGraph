---
id: UNC@20.15.2@MMLCommand@LST PCCPBINDUPG
type: MMLCommand
name: LST PCCPBINDUPG（查询用户模板组和PccProfile的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCCPBINDUPG
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 用户PCC模板绑定
status: active
---

# LST PCCPBINDUPG（查询用户模板组和PccProfile的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

本命令用于查询UsrProfGroup下绑定的PccProfile。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFGNAME | 用户模板组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的USERPROFGNAME必须是系统已经存在的USRPROFGROUP对象名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCPBINDUPG]] · 用户模板组和PccProfile的绑定关系（PCCPBINDUPG）

## 使用实例

查询UserProfGName为userprofg1的PCCPBindUPG配置：

```
LST PCCPBINDUPG:USERPROFGNAME="userprofg1";
```

```

RETCODE = 0  操作成功。

用户PCC模板组与用户模板绑定信息
-------------------------------
 用户模板组名称  =  userprofg1
用户PCC模板名称  =  userprofile
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PCCPBINDUPG.md`
