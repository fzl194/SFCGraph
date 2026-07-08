---
id: UNC@20.15.2@MMLCommand@LST GXUPFGROUP
type: MMLCommand
name: LST GXUPFGROUP（查询Gx UPF组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GXUPFGROUP
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- UPF管理
- Gx UPF组
status: active
---

# LST GXUPFGROUP（查询Gx UPF组）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查看指定Gx Upf组或者已配置所有Gx Upf组的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | Gx UPF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GXUPFGROUP]] · Gx UPF组（GXUPFGROUP）

## 使用实例

查看所有GxUpfGroup配置：

```
LST GXUPFGROUP:;
```

```

RETCODE = 0  操作成功

Gx UPF组配置信息
--------------------------
Gx UPF组名称  

huawei          
huawei1         
upfgrp          
upfgrp1         
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GXUPFGROUP.md`
