---
id: UNC@20.15.2@MMLCommand@MOD CPUABILITYCFG
type: MMLCommand
name: MOD CPUABILITYCFG（修改不同CPU类型的能力系数和基础消耗。）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CPUABILITYCFG
command_category: 配置类
applicable_nf:
- GGSN
- SGW-C
- SMF
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 权重分配管理
- CPU能力系数策略
status: active
---

# MOD CPUABILITYCFG（修改不同CPU类型的能力系数和基础消耗。）

## 功能

![](修改不同CPU类型的能力系数和基础消耗。（MOD CPUABILITYCFG）_51335397.assets/notice_3.0-zh-cn_2.png)

如果配置不合理会导致会动态权重失效以及token迁移不能处于稳态。

**适用NF：GGSN、SGW-C、SMF、PGW-C**

该命令用于修改不同CPU类型的能力系数和基础消耗。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPUTYPE | CPU类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CPU类型。<br>数据来源：本端规划<br>取值范围：<br>- X86_64（X86机器CPU类型）<br>- Aarch（ARM机器CPU类型）<br>默认值：无<br>配置原则：无 |
| CPUGENERATE | CPU代际 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CPU代际。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。当cpu类型是ARM时，固定字符“arch64”，其他字符不生效。<br>默认值：无<br>配置原则：无 |
| CPUFREQUENCY | CPU主频 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CPU主频。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~32767。<br>默认值：无<br>配置原则：无 |
| COEFFICIENT | 能力系数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CPU能力系数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是500~32767。<br>默认值：无<br>配置原则：无 |
| BASECOST | 基础消耗 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CPU基础消耗。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15。<br>默认值：无<br>配置原则：<br>执行DSP PODCPUSTAT查看调整pod的CPU利用率，若查询所得CPU利用率小于基础消耗，动态权重不调整。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CPUABILITYCFG]] · 不同CPU类型的能力系数和基础消耗。（CPUABILITYCFG）

## 使用实例

修改一个服务类型为x86_64、代际为1、主频为1的CPU的能力系数为32767、基础消耗为0，执行如下命令：

```
MOD CPUABILITYCFG: CPUTYPE=X86_64, CPUGENERATE="1", CPUFREQUENCY=1, COEFFICIENT=32767, BASECOST=0, CONFIRM=Y;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-CPUABILITYCFG.md`
