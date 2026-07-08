---
id: UDG@20.15.2@MMLCommand@DSP OSPATCH
type: MMLCommand
name: DSP OSPATCH（查询OS补丁版本号）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPATCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- OS管理
status: active
---

# DSP OSPATCH（查询OS补丁版本号）

## 功能

该命令用于查询节点的OS补丁版本号。

> **说明**
> 该命令仅在 Full-stack 虚机场景下支持。

> **说明**
> 无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：用于指示系统需要查询指定网元ID下的节点数据。<br>取值范围：0～65535。<br>默认值：无。<br>配置原则：<br>- 网元ID可以通过执行[LST ME](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)查询。 |
| NODEIP | 节点IP | 可选必选说明：可选参数。<br>参数含义：用于指示系统需要查询哪个节点的数据。<br>取值范围：不超过128位字符串。<br>默认值：无。<br>配置原则：<br>- 若不输入，则表示查询所有节点的OS信息。 |

## 操作的配置对象

- [OS补丁版本号（OSPATCH）](configobject/UDG/20.15.2/OSPATCH.md)

## 使用实例

1. 查询“网元ID”为“0”的所有节点配置信息：
  ```
  #65 %%DSP OSPATCH: MEID=0;%% 
  RETCODE = 0  操作成功  
  操作结果如下 
  ------------ 
  网元ID  节点IP           内核版本号                        补丁列表       是否生效     
  0       10.0.0.0         xxxx-xxxx.x.x.xxxx.xxxxxx.xxxxx   xxx.xxx.xxx    yes
  0       10.0.0.0         xxxx-xxxx.x.x.xxxx.xxxxxx.xxxxx   xxx.xxx.xxx    yes
  0       10.0.0.0         xxxx-xxxx.x.x.xxxx.xxxxxx.xxxxx   xxx.xxx.xxx    yes
  (结果个数 = 3)  
  ---    END
  ```
2. 查询“网元ID”为“0”，“节点IP”为“10.0.0.0”的节点配置信息：
  ```
  #66 %%DSP OSPATCH: MEID=0, NODEIP="10.0.0.0";%% 
  RETCODE = 0  操作成功  
  操作结果如下 
  ------------     
      网元ID  =  0     
      节点IP  =  10.0.0.0 
  内核版本号  =  xxxx-xxxx.x.x.xxxx.xxxxxx.xxxxx 
    补丁列表  =  xxx.xxx.xxx
    是否生效  =  yes
  (结果个数 = 1)  
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OS补丁版本号（DSP-OSPATCH）_55368407.md`
