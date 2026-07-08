---
id: UNC@20.15.2@MMLCommand@LST SEPPBINDGRP
type: MMLCommand
name: LST SEPPBINDGRP（查询SEPP绑定组关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SEPPBINDGRP
command_category: 查询类
applicable_nf:
- AMF
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- SEPP管理
- SEPP组管理
status: active
---

# LST SEPPBINDGRP（查询SEPP绑定组关系）

## 功能

**适用NF：AMF、SMF**

该命令用于查询SEPP绑定组关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。NFINSTANCEID参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.不区分大小写。<br>默认值：无<br>配置原则：无 |
| GROUPID | 组号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SEPP组号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是2~65。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SEPP绑定组关系（SEPPBINDGRP）](configobject/UNC/20.15.2/SEPPBINDGRP.md)

## 使用实例

查询SEPP绑定组关系。

```
%%LST SEPPBINDGRP:;%%
RETCODE = 0 操作成功

结果如下
------------------------
  NF实例标识 = sepp_instance_1
        组号 = 3
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SEPP绑定组关系（LST-SEPPBINDGRP）_31000042.md`
