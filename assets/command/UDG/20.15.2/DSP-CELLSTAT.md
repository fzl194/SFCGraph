---
id: UDG@20.15.2@MMLCommand@DSP CELLSTAT
type: MMLCommand
name: DSP CELLSTAT（显示微服务进程可用状态统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CELLSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP CELLSTAT（显示微服务进程可用状态统计信息）

## 功能

该命令用于查询进程可用状态统计信息，支持基于POD类型查询和整系统查询。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJECT | 对象类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询的对象类型，根据Pod类型查询或查询整系统。<br>数据来源：本端规划<br>取值范围：<br>- “PODTYPE（POD类型）”：升级，实例化场景下检查POD是否就绪。<br>- “VNF（网元）”：查询整个网元<br>默认值：无<br>配置原则：<br>“PODTYPE”用于Pod升级、实例化场景下，检查Pod是否就绪。“VNF”用于查询整个网元内的进程是否处于就绪状态。 |
| PODTYPE | POD类型 | 可选必选说明：该参数在"OBJECT"配置为"PODTYPE"时为条件可选参数。<br>参数含义：该参数用于查询该类型POD内的进程信息。当不输入该参数时，按POD名称返回整个网元的进程统计信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PODINFO**](../../编排管理/POD管理/显示已部署的Pod实例信息（DSP PODINFO）_09587375.md)<br>命令获取POD类型作为该参数的输入。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CELLSTAT]] · 微服务进程可用状态统计信息（CELLSTAT）

## 使用实例

查询整网元进程统计信息

```
%%DSP CELLSTAT: OBJECT=VNF;%%
RETCODE = 0  操作成功

结果如下
--------
    对象名称  =  VNF
  就绪进程数  =  176
未就绪进程数  =  25
  故障进程数  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示微服务进程可用状态统计信息（DSP-CELLSTAT）_94730396.md`
