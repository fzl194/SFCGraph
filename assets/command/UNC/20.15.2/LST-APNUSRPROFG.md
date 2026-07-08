---
id: UNC@20.15.2@MMLCommand@LST APNUSRPROFG
type: MMLCommand
name: LST APNUSRPROFG（查询APN用户模板组绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNUSRPROFG
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- APN用户模板组绑定
status: active
---

# LST APNUSRPROFG（查询APN用户模板组绑定关系）

## 功能

**适用NF：PGW-C、SMF**

本命令用于查询APN下绑定的UsrProfGroup。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN对象名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD APN命令配置生成。<br>- 配置的APN必须是系统已经存在的APN对象名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNUSRPROFG]] · APN用户模板组绑定关系（APNUSRPROFG）

## 使用实例

查询Apn名称为apn1的ApnUsrProfG配置：

```
LST APNUSRPROFG:APN="apn1";
```

```

RETCODE = 0  操作成功。

APN用户模板组绑定关系信息
-------------------------
           APN  =  apn1
用户模板组名称  =  usrprofilegroup1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNUSRPROFG.md`
