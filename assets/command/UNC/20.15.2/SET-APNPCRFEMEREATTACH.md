---
id: UNC@20.15.2@MMLCommand@SET APNPCRFEMEREATTACH
type: MMLCommand
name: SET APNPCRFEMEREATTACH（设置APN的MBR删除PCC回滚空闲上下文配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: APNPCRFEMEREATTACH
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- MBR 删除PCC回滚上下文
status: active
---

# SET APNPCRFEMEREATTACH（设置APN的MBR删除PCC回滚空闲上下文配置）

## 功能

**适用NF：SGW-C**

此命令用于收到恢复数据的Modify Bearer Request消息时，开启或关闭指定APN删除PCC回滚的IDLE上下文的配置。

## 注意事项

- 该命令执行后立即生效。

- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：MBRDELETESW：DISABLE。
- 当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无。<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| MBRDELETESW | APN MBR 删除承载配置 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN控制开启和关闭MBR消息删除PCC回滚的idle上下文的功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNPCRFEMEREATTACH查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [APN的MBR删除PCC回滚空闲上下文配置（APNPCRFEMEREATTACH）](configobject/UNC/20.15.2/APNPCRFEMEREATTACH.md)

## 使用实例

设置“APN名称”为“isp”，开启MBR消息删除PCC回滚的idle上下文的功能。

```
SET APNPCRFEMEREATTACH: APN="isp", MBRDELETESW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置APN的MBR删除PCC回滚空闲上下文配置（SET-APNPCRFEMEREATTACH）_67510500.md`
