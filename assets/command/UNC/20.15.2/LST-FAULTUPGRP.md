---
id: UNC@20.15.2@MMLCommand@LST FAULTUPGRP
type: MMLCommand
name: LST FAULTUPGRP（查询N3接口故障UPF组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FAULTUPGRP
command_category: 查询类
applicable_nf:
- SGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP故障管理
- N3接口故障UPF组管理
status: active
---

# LST FAULTUPGRP（查询N3接口故障UPF组）

## 功能

**适用NF：SGW-C、SMF**

该命令用于查询N3接口故障UPF组，当N3接口出现故障，如果该故障UPF组与故障RAN组绑定，SMF在为通过RAN组内的RAN接入的用户选择UPF时，会自动过滤掉该UPF组内的UPF。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头或结尾，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FAULTUPGRP]] · N3接口故障UPF组（FAULTUPGRP）

## 使用实例

查询所有N3接口故障UPF组：

```
%%LST FAULTUPGRP:;%%
RETCODE = 0  操作成功

结果如下
--------
UPF组名  =  group1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-FAULTUPGRP.md`
