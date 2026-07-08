---
id: UDG@20.15.2@MMLCommand@RMV PODALMTH
type: MMLCommand
name: RMV PODALMTH（删除POD资源告警阈值）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PODALMTH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# RMV PODALMTH（删除POD资源告警阈值）

## 功能

该命令用于删除POD资源告警阈值。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令仅在FusionStage裸机场景下生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | POD类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定POD类型。该值来自于<br>[**DSP PODCPUSTAT**](查询pod CPU信息（DSP PODCPUSTAT）_94730422.md)<br>/<br>[**PODMEMSTAT**](查询pod内存信息（DSP PODMEMSTAT）_94730425.md)<br>返回结果中的POD类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：无 |
| THTYPE | 阈值类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定告警阈值类型。<br>数据来源：本端规划<br>取值范围：<br>- “CPU（阈值类型为CPU）”：阈值类型为CPU<br>- “MEMORY（阈值类型为内存）”：阈值类型为内存<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PODALMTH]] · POD资源告警阈值（PODALMTH）

## 使用实例

删除POD类型为sfm-pod的POD中CPU的告警阈值。

```
RMV PODALMTH: PODTYPE="sfm-pod",THTYPE=CPU;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-PODALMTH.md`
