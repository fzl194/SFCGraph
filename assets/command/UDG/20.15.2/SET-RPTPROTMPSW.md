---
id: UDG@20.15.2@MMLCommand@SET RPTPROTMPSW
type: MMLCommand
name: SET RPTPROTMPSW（设置业务报表承载协议映射开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: RPTPROTMPSW
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务报表管理
- 报表功能管理
- 报表承载协议映射开关
status: active
---

# SET RPTPROTMPSW（设置业务报表承载协议映射开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用来设置业务报表承载协议映射开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 此命令的生效范围为整机。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用来配置业务报表承载协议映射功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTPROTMPSW]] · 业务报表承载协议映射开关（RPTPROTMPSW）

## 使用实例

假如运营商需使能业务报表承载协议映射功能：

```
SET RPTPROTMPSW: SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置业务报表承载协议映射开关（SET-RPTPROTMPSW）_19410198.md`
