---
id: UNC@20.15.2@MMLCommand@DSP BYPASSMODE
type: MMLCommand
name: DSP BYPASSMODE（查询节点BYPASS模式）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BYPASSMODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- Bypass模式管理
status: active
---

# DSP BYPASSMODE（查询节点BYPASS模式）

## 功能

![](查询节点BYPASS模式（DSP BYPASSMODE）_47816794.assets/notice_3.0-zh-cn_2.png)

该功能仅支持华为虚拟化层软件FusionSphere，不支持第三方虚拟化层软件。

存储BYPASS指VNF运行和存储解耦，当存储故障后，支持存储BYPASS的VNF在内存中继续正常运行， 减少磁阵故障对业务的影响 ，该命令用于查询节点的BYPASS的运行状态。

> **说明**
> 该命令仅在 Full-stack 虚机场景下支持。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数<br>参数含义：用于指示系统需要查询指定网元ID下的节点数据。当参数为空时查询所有网元下的节点数据。<br>“网元ID”<br>可以通过执行<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>查询。<br>取值范围：0～65535。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BYPASSMODE]] · 节点BYPASS模式（BYPASSMODE）

## 使用实例

1. “网元ID”为空时，查询所有节点的信息
  ```
  %%DSP BYPASSMODE:;%%
  RETCODE = 0  操作成功
  操作结果如下
  ------------
  网元ID  节点IP           节点BYPASS的运行状态  
  0       10.0.0.3          MemoryDiskMode                    
  0       10.0.0.2          MemoryDiskMode                    
  0       10.0.0.1          MemoryDiskMode
  (结果个数 = 5)
  ---    END
  ```
2. 查询“网元ID”为“0”的所有节点的信息
  ```
  %%DSP BYPASSMODE: MEID=0;%%
  RETCODE = 0  操作成功
  操作结果如下
  ------------
  网元ID  节点IP           节点BYPASS的运行状态  
  0       10.0.0.3          MemoryDiskMode                    
  0       10.0.0.2          MemoryDiskMode                    
  0       10.0.0.1          MemoryDiskMode                    
  (结果个数 = 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-BYPASSMODE.md`
