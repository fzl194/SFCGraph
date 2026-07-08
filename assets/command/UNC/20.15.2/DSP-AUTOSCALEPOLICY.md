---
id: UNC@20.15.2@MMLCommand@DSP AUTOSCALEPOLICY
type: MMLCommand
name: DSP AUTOSCALEPOLICY（查询自动弹性策略状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: AUTOSCALEPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 自动弹性管理
status: active
---

# DSP AUTOSCALEPOLICY（查询自动弹性策略状态）

## 功能

该命令用于查询自动弹性策略状态。

> **说明**
> 该命令仅在Full-stack裸机场景下支持。

## 注意事项

无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数。<br>参数含义：网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AUTOSCALEPOLICY]] · 自动弹性策略状态（AUTOSCALEPOLICY）

## 使用实例

查询自动弹性策略状态：

```
%%DSP AUTOSCALEPOLICY: MEID=0;%% 
RETCODE = 0  操作成功  
操作结果如下 
------------     
弹性策略名称  =  csdb-pod-autopolicy 
弹性策略是否激活  =  是 
弹性策略执行阶段  =  采集
弹性策略执行状态  =  执行中 

 (结果个数 = 1)  ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-AUTOSCALEPOLICY.md`
