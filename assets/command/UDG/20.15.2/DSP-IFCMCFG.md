---
id: UDG@20.15.2@MMLCommand@DSP IFCMCFG
type: MMLCommand
name: DSP IFCMCFG（查询IFCM配置信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IFCMCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- IFCM管理
status: active
---

# DSP IFCMCFG（查询IFCM配置信息）

## 功能

该命令用于查询IDRService配置信息。

> **说明**
> 无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：指定要查看哪个网元的配置信息。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IFCMCFG]] · IFCM配置信息（IFCMCFG）

## 使用实例

查询网元阈值配置信息：

```
%%DSP IFCMCFG: MEID=191;%%
RETCODE = 0  操作成功

操作结果如下：
-------------- 
网元ID    配置名称      配置阈值(%)    
191       网元故障阈值  5             
191       Pod故障阈值   5             
191       网元容灾阈值  15            
(结果个数 = 3)  
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-IFCMCFG.md`
