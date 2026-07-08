---
id: UDG@20.15.2@MMLCommand@LST HTTPFCIPGRP
type: MMLCommand
name: LST HTTPFCIPGRP（查询HTTP流控组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HTTPFCIPGRP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP流控组管理
status: active
---

# LST HTTPFCIPGRP（查询HTTP流控组）

## 功能

该命令用于查询HTTP固定速率流控组的IP地址组信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUP | 流控组 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP固定速率流控组的唯一标识。一个流控组中可以包括多个IP地址索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |
| INDEX | IP地址索引 | 可选必选说明：可选参数<br>参数含义：该参数用于标识具有相同前缀的一组IP地址。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于填写HTTP固定速率流控地址组的描述信息，建议包含NF类型，实例名等，例如UDM_UDM001。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HTTP流控组（HTTPFCIPGRP）](configobject/UDG/20.15.2/HTTPFCIPGRP.md)

## 使用实例

查询HTTP固定速率流控地址组信息：

```
LST HTTPFCIPGRP:
%%LST HTTPFCIPGRP:;%%
RETCODE = 0  操作成功

结果如下
------------------------
    流控组  =  1
IP地址索引  =  1
      描述  =  NULL
IP地址类型  =  IPv4
  IPv4地址  =  192.168.4.15
  IPv4掩码  =  255.255.255.0
  IPv6地址  =  ::
  IPv6前缀  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTP流控组（LST-HTTPFCIPGRP）_83813632.md`
