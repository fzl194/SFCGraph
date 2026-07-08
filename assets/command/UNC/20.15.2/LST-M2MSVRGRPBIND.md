---
id: UNC@20.15.2@MMLCommand@LST M2MSVRGRPBIND
type: MMLCommand
name: LST M2MSVRGRPBIND（查询M2M服务器组绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: M2MSVRGRPBIND
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- M2M
- M2M服务器组绑定关系
status: active
---

# LST M2MSVRGRPBIND（查询M2M服务器组绑定关系）

## 功能

**适用NF：PGW-C、SMF**

命令是用来查询指定APN实例下绑定M2M服务器组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | M2M服务器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定M2M服务器组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>该参数使用ADD M2MSERVERGRP命令配置生成。 |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M2MSVRGRPBIND]] · M2M服务器组绑定关系（M2MSVRGRPBIND）

## 使用实例

查询指定的APN与M2M服务器组的绑定信息，APN为isp：

```
%%LST M2MSVRGRPBIND: APN="isp";%%
RETCODE = 0  操作成功

结果如下
--------
M2M服务器组名称  =  m2msrvgroup01
        APN名称  =  isp
      UPF组名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询M2M服务器组绑定关系（LST-M2MSVRGRPBIND）_73321235.md`
