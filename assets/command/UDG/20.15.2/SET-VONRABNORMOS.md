---
id: UDG@20.15.2@MMLCommand@SET VONRABNORMOS
type: MMLCommand
name: SET VONRABNORMOS（指定MOS值的异常门限值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: VONRABNORMOS
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- VoNR质量监控配置
- VoNR MOS值的异常门限值
status: active
---

# SET VONRABNORMOS（指定MOS值的异常门限值）

## 功能

**适用NF：UPF**

该命令用于设置MOS（Mean Opinion Score）值的异常门限值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | MOSABNORMTHD |
| --- | --- |
| 初始值 | 10 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOSABNORMTHD | VoNR MOS值的异常门限 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MOS值的异常门限值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～20, 粒度是200。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [MOS值的异常门限为系统初始设置值（VONRABNORMOS）](configobject/UDG/20.15.2/VONRABNORMOS.md)

## 使用实例

设置异常MOS值的门限值为15：

```
SET VONRABNORMOS: MOSABNORMTHD=15;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/指定MOS值的异常门限值（SET-VONRABNORMOS）_94614217.md`
