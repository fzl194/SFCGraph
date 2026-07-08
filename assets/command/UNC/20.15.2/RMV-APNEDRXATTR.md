---
id: UNC@20.15.2@MMLCommand@RMV APNEDRXATTR
type: MMLCommand
name: RMV APNEDRXATTR（删除APN的终端接入eDRX模式属性）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNEDRXATTR
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- eDRX模式管理
status: active
---

# RMV APNEDRXATTR（删除APN的终端接入eDRX模式属性）

## 功能

**适用NF：SMF**

该命令用于删除指定APN的终端接入的eDRX模式。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 当APN对应的APNEDRXATTR命令记录不存在时，EDRXSW、PKTCNTPRIORITY、DLBUFFPKTCNT和EXTDLBUFFTIME的默认值为SET GLBEDRXATTR命令中同名参数的值。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNEDRXATTR]] · APN的终端接入eDRX模式属性（APNEDRXATTR）

## 使用实例

假如用户需要删除对APN为“apn1”的终端接入的eDRX模式，则使用该实例：

```
RMV APNEDRXATTR: APN="apn1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APNEDRXATTR.md`
