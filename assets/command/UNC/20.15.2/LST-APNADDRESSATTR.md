---
id: UNC@20.15.2@MMLCommand@LST APNADDRESSATTR
type: MMLCommand
name: LST APNADDRESSATTR（查询基于APN的地址分配属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNADDRESSATTR
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- 基于APN的地址管理控制参数
status: active
---

# LST APNADDRESSATTR（查询基于APN的地址分配属性）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询APN地址分配属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNADDRESSATTR]] · 基于APN的地址分配属性（APNADDRESSATTR）

## 使用实例

查询APN名称为"demo.com"的地址分配属性。

```
LST APNADDRESSATTR: APN="demo.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNADDRESSATTR.md`
