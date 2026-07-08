---
id: UDG@20.15.2@MMLCommand@DSP CNTMEMSTAT
type: MMLCommand
name: DSP CNTMEMSTAT（查询容器内存信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CNTMEMSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# DSP CNTMEMSTAT（查询容器内存信息）

## 功能

该命令用于查询所有被资源管理器管理的容器或指定容器的容器内存信息。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CNTTYPE | 容器类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定容器类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的容器类型。 |
| CNTID | 容器ID | 可选必选说明：可选参数<br>参数含义：本参数用于指定容器ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的容器ID。 |
| MEID | 网元 ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元来查询容器的内存信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>本命令不加参数可以查询所有支持的网元ID。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CNTMEMSTAT]] · 容器内存信息（CNTMEMSTAT）

## 使用实例

- 查询所有被资源管理器管理的容器内存信息。
  ```
  %%DSP CNTMEMSTAT:;%%
  RETCODE = 0  操作成功 

  结果如下
  ------------------------
  容器类型               容器ID                                       网元ID  节点ID       内存配额(KB)      内存使用量(KB)   内存使用率(%)
  
  CONTAINER_Scfm         sfm-pod-845bfd885d-njv9l192-168-0-39__107    0  192.168.0.1    31995             7080            22.13
  CONTAINER_Scfm         sfm-pod-845bfd885d-tnt46192-168-0-52__107    0  192.168.0.2    31995             7070            22.10
  CONTAINER_SdbSim       sdbsim-pod-1192-168-1-242__139               0  192.168.0.3    31995             5065            15.83
  CONTAINER_Sm           vsm-pod-57b8dd4ff6-4rj4g192-168-1-106__1005  0  192.168.0.4    31995             5064            15.83
  (结果个数 = 4)
  ```
- 查询容器类型为CONTAINER_Scfm的所有容器内存信息。
  ```
  %%DSP CNTMEMSTAT: CNTTYPE="CONTAINER_Scfm";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  容器类型        容器ID                                    网元ID  节点ID     内存配额(KB)   内存使用量(KB)    内存使用率(%)
  
  CONTAINER_Scfm  sfm-pod-845bfd885d-njv9l192-168-0-39__107  0  192.168.0.1  31995           11386         35.59
  CONTAINER_Scfm  sfm-pod-845bfd885d-tnt46192-168-0-52__107  0  192.168.0.2  31995           10543         32.95
  (结果个数 = 2)
  ```
- 查询容器id为sfm-pod-845bfd885d-njv9l192-168-0-39__107的容器内存信息。
  ```
  %%DSP CNTMEMSTAT: CNTID="sfm-pod-845bfd885d-njv9l192-168-0-39__107";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
       容器类型   =  CONTAINER_Scfm
         容器ID   =  sfm-pod-845bfd885d-njv9l192-168-0-39__107
         网元ID  = 0
         节点ID  =   192.168.0.1
    内存配额(KB)  =  31995
  内存使用量(KB)  =  7978
  内存使用率(%)   =  24.94
  (结果个数 = 1)
  ```
- 查询容器类型为CONTAINER_Scfm，容器id为sfm-pod-845bfd885d-njv9l192-168-0-39__107的容器内存信息。
  ```
  %%DSP CNTMEMSTAT: CNTTYPE="CONTAINER_Scfm", CNTID="sfm-pod-845bfd885d-njv9l192-168-0-39__107";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
       容器类型   =  CONTAINER_Scfm
         容器ID   =  sfm-pod-845bfd885d-njv9l192-168-0-39__107
         网元ID   =  0
         节点ID   =  192.168.0.1
    内存配额(KB)  =  31995
  内存使用量(KB)  =  7978
  内存使用率(%)   =  24.94
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-CNTMEMSTAT.md`
