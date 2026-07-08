---
id: UNC@20.15.2@MMLCommand@RMV UNCLOGCTRL
type: MMLCommand
name: RMV UNCLOGCTRL（删除UNC日志控制记录）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UNCLOGCTRL
command_category: 配置类
applicable_nf:
- SMF
- AMF
- NRF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# RMV UNCLOGCTRL（删除UNC日志控制记录）

## 功能

**适用NF：SMF、AMF、NRF、NSSF、SMSF、NCG**

该命令用于删除一条UNC日志的控制记录。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：记录索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UNC日志控制记录（UNCLOGCTRL）](configobject/UNC/20.15.2/UNCLOGCTRL.md)

## 使用实例

如下命令用于删除一条记录

```
RMV UNCLOGCTRL: INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UNC日志控制记录（RMV-UNCLOGCTRL）_23736564.md`
