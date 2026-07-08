---
id: UNC@20.15.2@MMLCommand@LST VNFEVICTION
type: MMLCommand
name: LST VNFEVICTION（查询网元重调度策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VNFEVICTION
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 网元管理
status: active
---

# LST VNFEVICTION（查询网元重调度策略）

## 功能

用于查询网元的重调度策略。

> **说明**
> 该命令仅在 Full-stack 虚机场景下支持。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| VNFID | 网元ID | 可选必选说明：必选参数。<br>参数含义：网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VNFEVICTION]] · 网元重调度策略（VNFEVICTION）

## 使用实例

查询网元ID为0的网元重调度策略。

```
%%LST VNFEVICTION: VNFID=0;%%
RETCODE = 0  操作成功

操作结果如下
------------
网元ID  节点名称        节点IP          虚拟机ID                            重调度策略  

0       10.113.112.79   10.113.112.79   070b9dad6fd94a43af459db975465baf    开启        
0       10.113.112.197  10.113.112.197  d9524ba42dcf4d8fac2943666c3ca5dd    开启        
0       10.113.112.222  10.113.112.222  8cde48ddba05482bb0d03d01f824577b    开启        
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VNFEVICTION.md`
