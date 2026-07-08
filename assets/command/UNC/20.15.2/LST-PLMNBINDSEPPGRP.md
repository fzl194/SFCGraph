---
id: UNC@20.15.2@MMLCommand@LST PLMNBINDSEPPGRP
type: MMLCommand
name: LST PLMNBINDSEPPGRP（查询PLMN与SEPP组的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PLMNBINDSEPPGRP
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
- SEPP组PLMN管理
status: active
---

# LST PLMNBINDSEPPGRP（查询PLMN与SEPP组的绑定关系）

## 功能

**适用NF：AMF、SMF**

该命令用于查询PLMN与SEPP组的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~3。<br>默认值：无<br>配置原则：<br>本参数只能由3个十进制数字组成或者配置为“*”。 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~3。<br>默认值：无<br>配置原则：<br>本参数只能由2~3个十进制数字组成或者配置为“*”。 |
| GROUPID | 组号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SEPP组号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是2~65。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLMNBINDSEPPGRP]] · PLMN与SEPP组的绑定关系（PLMNBINDSEPPGRP）

## 使用实例

查询PLMN与SEPP组的绑定关系。

```
%%LST PLMNBINDSEPPGRP:;%%
RETCODE = 0 操作成功

结果如下
------------------------
  移动国家码 = 123
    移动网号 = 03
        组号 = 3
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PLMN与SEPP组的绑定关系（LST-PLMNBINDSEPPGRP）_30840094.md`
