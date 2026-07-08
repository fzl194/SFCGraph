---
id: UNC@20.15.2@MMLCommand@LST UPFBINDGXUPFGRP
type: MMLCommand
name: LST UPFBINDGXUPFGRP（查询UPF与Gx UPF组的关联关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPFBINDGXUPFGRP
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
- 关联UPF与Gx UPF组
status: active
---

# LST UPFBINDGXUPFGRP（查询UPF与Gx UPF组的关联关系）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用于查询UPF与GX UPF组的绑定信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | Gx UPF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：可选参数<br>参数含义：指定UPF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。UpfHostName参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：该参数使用ADD PNFPROFILE命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPFBINDGXUPFGRP]] · UPF与Gx UPF组的关联关系（UPFBINDGXUPFGRP）

## 使用实例

查看UPF绑定关系：

```
LST UPFBINDGXUPFGRP:;
```

```

RETCODE = 0  操作成功

Gx UPF组内UPF信息
-------------------------------
Gx UPF组名称       UPF实例标识  

huawei          upf_instance_1   
huawei          upf_instance_2   
huawei1         upf_instance_1   
huawei1         upf_instance_2   
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPFBINDGXUPFGRP.md`
