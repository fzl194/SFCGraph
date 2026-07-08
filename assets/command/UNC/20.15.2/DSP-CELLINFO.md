---
id: UNC@20.15.2@MMLCommand@DSP CELLINFO
type: MMLCommand
name: DSP CELLINFO（显示微服务进程信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CELLINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP CELLINFO（显示微服务进程信息）

## 功能

此命令用于显示微服务进程信息，如进程运行状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJECT | 对象类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询可用状态的对象类型：包括进程类型，进程ID，POD名称。<br>数据来源：本端规划<br>取值范围：<br>- “PROCESSTYPE（进程类型）”：问题定位相同类型异常进程原因<br>- “PROCESSID（进程ID）”：问题定位单个进程异常原因<br>- “PODNAME（POD名称）”：问题定位未ready的Pod内异常进程原因<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：该参数在"OBJECT"配置为"PODNAME"时为条件必选参数。<br>参数含义：该参数用于表示按Pod名称查询进程可用状态。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP CELLSTAT**](显示微服务进程可用状态统计信息（DSP CELLSTAT）_94730396.md)<br>命令获取POD名称作为输入。 |
| PROCID | 进程ID | 可选必选说明：该参数在"OBJECT"配置为"PROCESSID"时为条件必选参数。<br>参数含义：参数用于表示微服务进程ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>可通过<br>[**DSP MSPROCESS**](显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>命令查询进程ID。 |
| PROCTYPE | 进程类型 | 可选必选说明：该参数在"OBJECT"配置为"PROCESSTYPE"时为条件必选参数。<br>参数含义：该参数用于表示微服务进程所属的进程类型名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。<br>默认值：无<br>配置原则：<br>可通过<br>[**DSP MSPROCTYPE**](显示微服务进程类型（DSP MSPROCTYPE）_09587905.md)<br>命令查询进程类型名。 |
| PROCSTATE | 进程状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示微服务进程状态，根据进程状态筛选查询结果，进程状态有Ready、Not Ready、Fault三种，分别对应就绪状态、未就绪状态、故障状态。<br>数据来源：本端规划<br>取值范围：<br>- “NotReady（未就绪状态）”：进程是未就绪状态<br>- “Fault（故障状态）”：进程是故障状态<br>- “Ready（就绪状态）”：进程是就绪状态<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CELLINFO]] · 微服务进程信息（CELLINFO）

## 使用实例

基于Pod名称查询进程信息

```
%%DSP CELLINFO: OBJECT=PODNAME, PODNAME="cmf-pod-2";%%
RETCODE = 0  操作成功

结果如下
--------
进程类型       进程ID             进程状态  节点名称      故障原因      故障描述

CELL_CMF      cmf-pod-2__167__0  就绪状态  10.0.0.1     0x00000000   
CELL_SCFA     cmf-pod-2__103__1  就绪状态  10.0.0.1     0x00000000   
CELL_SDRE     cmf-pod-2__103__0  就绪状态  10.0.0.1     0x00000000   
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示微服务进程信息（DSP-CELLINFO）_94730395.md`
