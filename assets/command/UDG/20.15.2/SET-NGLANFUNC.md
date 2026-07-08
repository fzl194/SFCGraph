---
id: UDG@20.15.2@MMLCommand@SET NGLANFUNC
type: MMLCommand
name: SET NGLANFUNC（设置5G LAN功能配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NGLANFUNC
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN基础配置
- 5G LAN功能开关
status: active
---

# SET NGLANFUNC（设置5G LAN功能配置）

## 功能

**适用NF：UPF**

该命令用于配置开启或者关闭5G LAN功能开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 开关关闭不允许5G LAN用户接入。
- N19FORWARDSW开关关闭，只对新激活用户生效，已激活的用户数据正常转发，不受影响。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | NGLANSW | N19FORWARDSW |
| --- | --- | --- |
| 初始值 | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGLANSW | 5G LAN功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制开启和关闭5G LAN接入功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| N19FORWARDSW | N19数据转发开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“NGLANSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置是否开启5G LAN N19接口数据转发功能。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NGLANFUNC]] · 5G LAN功能配置（NGLANFUNC）

## 使用实例

开启5G LAN功能开关，开启N19数据转发开关：

```
SET NGLANFUNC: NGLANSW=ENABLE, N19FORWARDSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-NGLANFUNC.md`
