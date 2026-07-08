---
id: UNC@20.15.2@MMLCommand@LST DNAIINFO
type: MMLCommand
name: LST DNAIINFO（查询DNAI信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNAIINFO
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- DNAI管理
- DNAI信息管理
status: active
---

# LST DNAIINFO（查询DNAI信息）

## 功能

**适用NF：SMF、PGW-C**

该命令用于查询DNAI信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DNAI信息（DNAIINFO）](configobject/UNC/20.15.2/DNAIINFO.md)

## 使用实例

查询DNAI信息

```
LST DNAIINFO: DNAI="cmnet_dnai";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNAI信息（LST-DNAIINFO）_11085190.md`
