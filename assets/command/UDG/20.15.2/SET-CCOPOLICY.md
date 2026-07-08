---
id: UDG@20.15.2@MMLCommand@SET CCOPOLICY
type: MMLCommand
name: SET CCOPOLICY（设置CCO策略）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: CCOPOLICY
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 1
category_path:
- 智能板管理
- cco
- ccopolicy
status: active
---

# SET CCOPOLICY（设置CCO策略）

## 功能

**适用NF：UPF**

本条命令用于设置CCO拥塞控制策略开关。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | BWMCAR | BWMSHAPING | EFLOWTHROTTLE | TOPLY |
| --- | --- | --- | --- | --- |
| 初始值 | ENABLE | ENABLE | DISABLE | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BWMCAR | BWMCAR策略开关 | 可选必选说明：可选参数<br>参数含义：BWMCAR策略开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：ENABLE<br>配置原则：无 |
| BWMSHAPING | BWMSHAPING策略开关 | 可选必选说明：可选参数<br>参数含义：BWMSHAPING策略开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：ENABLE<br>配置原则：无 |
| EFLOWTHROTTLE | 大象流抑制策略开关 | 可选必选说明：可选参数<br>参数含义：大象流抑制策略开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：DISABLE<br>配置原则：无 |
| TOPLY | TO分流策略开关 | 可选必选说明：可选参数<br>参数含义：TO分流策略开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：ENABLE<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CCOPOLICY]] · CCO策略（CCOPOLICY）

## 使用实例

用户可以设置某种CCO拥塞控制策略是否生效; 例如：设置BWMCAR策略为可用，BWMSHAPING策略为可用，EFLOWTHROTTLE策略为不可用，TO策略为可用。

```
SET CCOPOLICY: BWMCAR=ENABLE, BWMSHAPING=ENABLE, EFLOWTHROTTLE=DISABLE, TOPLY=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-CCOPOLICY.md`
