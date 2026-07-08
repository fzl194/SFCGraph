---
id: UNC@20.15.2@MMLCommand@LST FAULTUPBINDGRP
type: MMLCommand
name: LST FAULTUPBINDGRP（查询N3接口故障UPF与UPF组的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FAULTUPBINDGRP
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
- N3接口故障UPF组绑定管理
status: active
---

# LST FAULTUPBINDGRP（查询N3接口故障UPF与UPF组的绑定关系）

## 功能

**适用NF：SGW-C、SMF**

该命令用于查询N3接口故障UPF与故障UPF组的绑定关系，当N3接口出现故障，如果故障UPF与UPF组绑定，SMF在为通过与UPF组绑定的故障RAN组内的RAN接入的用户选择UPF时，会自动过滤掉该故障UPF。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFID | UPF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。UPFID参数不区分大小写且必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD UPNODE中参数“NFINSTANCENAME”保持一致，使用该前需通过ADD UPNODE添加一组记录。 |
| UPFGRPNAME | UPF组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头或结尾，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD FAULTUPGRP命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@FAULTUPBINDGRP]] · N3接口故障UPF与UPF组的绑定关系（FAULTUPBINDGRP）

## 使用实例

查询绑定在UPF组“group1”上的所有UPF实例：

```
%%LST FAULTUPBINDGRP: UPFGRPNAME="group1";%%
RETCODE = 0  操作成功

结果如下
--------
UPF实例标识  =  upf_instance_0
    UPF组名  =  group1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-FAULTUPBINDGRP.md`
