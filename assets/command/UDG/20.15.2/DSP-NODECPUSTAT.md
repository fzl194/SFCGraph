---
id: UDG@20.15.2@MMLCommand@DSP NODECPUSTAT
type: MMLCommand
name: DSP NODECPUSTAT（查询Node的CPU信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NODECPUSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# DSP NODECPUSTAT（查询Node的CPU信息）

## 功能

该命令用于查询所有节点或者指定节点的CPU信息。

> **说明**
> - 该命令执行后立即生效。
> - 该命令仅在虚机场景下支持。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODETYPE | 节点类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定节点类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>虚拟机类型，例如OMU。 |
| NODEID | 节点ID | 可选必选说明：可选参数<br>参数含义：本参数用于指定节点ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：无 |
| MEID | 网元 ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元来查询node的cpu信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的网元ID。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NODECPUSTAT]] · Node的CPU信息（NODECPUSTAT）

## 使用实例

- 查询所有节点CPU信息。
  ```
  %%DSP NODECPUSTAT:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  节点类型   节点ID         网元ID CPU核数         CPU使用率(%)

  UPU        192.168.55.84   0   12.00              17.40
  OMU        192.168.55.71   0   8.00               38.48
  PBU_A      192.168.15.151  0   8.00               20.88
  PBU_A      192.168.15.11   0   8.00               27.83
  (结果个数 = 4)
  ```
- 查询节点类型为PBU_A的所有节点CPU信息。
  ```
  %%DSP NODECPUSTAT: NODETYPE="PBU_A";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  节点类型   节点ID         网元ID  CPU核数         CPU使用率(%)
     
  PBU_A      192.168.15.151  0     8.00             20.88
  PBU_A      192.168.15.11   0     8.00             27.83
  (结果个数 = 2)
  ```
- 查询节点id为192.168.15.151的节点CPU信息。
  ```
  %%DSP NODECPUSTAT: NODEID="192.168.15.151";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
     节点类型  =  PBU_A
       节点ID  =  192.168.15.151
       网元ID  =  0
      CPU核数  =  8.00
  CPU使用率(%) =  43.90
  (结果个数 = 1)
  ```
- 查询节点类型为PBU_A，且节点id为192.168.15.151的节点CPU信息。
  ```
  %%DSP NODECPUSTAT: NODETYPE="PBU_A", NODEID="192.168.15.151";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
     节点类型  =  PBU_A
       节点ID  =  192.168.15.151
       网元ID  =  0
      CPU核数  =  8.00
  CPU使用率(%) =  43.90
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-NODECPUSTAT.md`
