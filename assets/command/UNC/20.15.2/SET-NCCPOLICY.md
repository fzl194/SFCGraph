---
id: UNC@20.15.2@MMLCommand@SET NCCPOLICY
type: MMLCommand
name: SET NCCPOLICY（设置NCC策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NCCPOLICY
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 配置服务管理
- 维护管理
status: active
---

# SET NCCPOLICY（设置NCC策略）

## 功能

![](设置NCC策略(SET NCCPOLICY)_69678032.assets/notice_3.0-zh-cn_2.png)

该命令设置后可能影响特定微服务的内存，需谨慎执行。

该命令用于设置NCC策略。

## 注意事项

该命令为ACS内部设置策略命令，不支持MML导出功能。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| POLICYITEM | 策略标识 | 可选必选说明：必选参数。<br>参数含义：用于指定待设置策略的策略标识。<br>取值范围：枚举类型。<br>MemOptFlag(内存优化开关策略)：特定微服务的内存优化功能开关标志，默认开启。<br>默认值：无。<br>配置原则：<br>- MemOptFlag(内存优化开关策略) 默认打开，只有手动设置关闭的情况下才可能生效。<br>- MemOptFlag(内存优化开关策略) 设置关闭后，对应的微服务重启后生效。 |
| POLICYVALUE | 策略内容 | 可选必选说明：该参数在<br>“策略标识”<br>配置为<br>“MemOptFlag(内存优化开关策略)”<br>时为条件必选参数。<br>参数含义：用于指定对应策略的开关。<br>取值范围：枚举类型。<br>- OFF(关闭)：该策略关闭。<br>- ON(开启)：该策略开启。<br>默认值：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NCCPOLICY]] · NCC策略（NCCPOLICY）

## 使用实例

设置NCC内存优化开关 “策略内容” 为 “OFF(关闭)” 时，执行以下命令：

```
SET NCCPOLICY: POLICYITEM=MemOptFlag, POLICYVALUE=OFF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NCCPOLICY.md`
