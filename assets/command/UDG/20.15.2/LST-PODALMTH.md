---
id: UDG@20.15.2@MMLCommand@LST PODALMTH
type: MMLCommand
name: LST PODALMTH（查询POD资源告警阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PODALMTH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# LST PODALMTH（查询POD资源告警阈值）

## 功能

该命令用于查询POD资源告警阈值。

> **说明**
> 该命令仅在FusionStage裸机场景下生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | POD类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定POD类型。该值来自于<br>[**DSP PODCPUSTAT**](查询pod CPU信息（DSP PODCPUSTAT）_94730422.md)<br>/<br>[**PODMEMSTAT**](查询pod内存信息（DSP PODMEMSTAT）_94730425.md)<br>返回结果中的POD类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PODALMTH]] · POD资源告警阈值（PODALMTH）

## 使用实例

查询POD类型为smf-pod的POD已添加的告警阈值配置。

```
%% LST PODALMTH: PODTYPE="sfm-pod";%%
RETCODE = 0  操作成功
结果如下
--------
POD类型         告警上报阈值(%)     告警恢复阈值(%)       阈值类型
sfm-pod  	         80		           70               CPU
sfm-pod              80                70               MEMORY
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PODALMTH.md`
