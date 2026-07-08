---
id: UDG@20.15.2@MMLCommand@SET SAIFUNC
type: MMLCommand
name: SET SAIFUNC（设置SAI差异化控制功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SAIFUNC
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 无线资源优化
- SAI
status: active
---

# SET SAIFUNC（设置SAI差异化控制功能）

## 功能

**适用NF：UPF、PGW-U**

该命令用于设置SAI差异化控制功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置SAI差异化控制功能开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SAIFUNC]] · SAI差异化控制功能（SAIFUNC）

## 使用实例

设置SAI差异化控制功能为使能：

```
SET SAIFUNC: SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SAIFUNC.md`
