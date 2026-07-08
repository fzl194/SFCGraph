---
id: UNC@20.15.2@MMLCommand@LST UPFGBINDLOCG
type: MMLCommand
name: LST UPFGBINDLOCG（查询UPF组与Diameter本端主机组的关联关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPFGBINDLOCG
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- 关联UPF组与Diameter本端主机组的关联关系
status: active
---

# LST UPFGBINDLOCG（查询UPF组与Diameter本端主机组的关联关系）

## 功能

**适用NF：PGW-C、SMF**

此命令用于查询UPF组与Diameter本端主机组的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGLOCGBNDGNAME | UPF组与Diameter本端主机组的绑定关系组名称 | 可选必选说明：可选参数<br>参数含义：该参数设置UPF组与Diameter本端主机组的绑定关系组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPFGLOCGBNDGRP命令配置生成。 |
| UPFGRPNAME | Gx UPF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD GXUPFGROUP命令配置生成。 |

## 操作的配置对象

- [UPF组与Diameter本端主机组的关联关系（UPFGBINDLOCG）](configobject/UNC/20.15.2/UPFGBINDLOCG.md)

## 使用实例

查询Diameter本端主机名与Diameter本端主机组的绑定关系，绑定关系组名为“upfgroup1”：

```
LST UPFGBINDLOCG: UPFGLOCGBNDGNAME="upfgroup1";
```

```

RETCODE = 0  操作成功

UPF组与Diameter本端主机组的关联关系
----------------------------------------------------
UPF组与Diameter本端主机组的绑定关系组名称  =  upfgroup1
                             Gx UPF组名称  =  huawei1
                  Diameter 本端信息组名称  =  localhost1
                                   优先级  =  3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UPF组与Diameter本端主机组的关联关系（LST-UPFGBINDLOCG）_16858415.md`
