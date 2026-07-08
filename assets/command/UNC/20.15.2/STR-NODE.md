---
id: UNC@20.15.2@MMLCommand@STR NODE
type: MMLCommand
name: STR NODE（启动节点）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: NODE
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 节点管理
status: active
---

# STR NODE（启动节点）

## 功能

本命令用于启动网元下指定名称的节点。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。
>
> - 在存储故障期间，执行本命令启动已关闭的节点，该节点以及节点中的容器和进程，在存储故障恢复前都无法启动。
> - 执行该命令返回成功，表明命令成功下发到MANO，节点上电是否成功需要稍后执行[DSP NODE](节点查询（DSP NODE）_71678755.md)命令来查看。

## 注意事项

- 避免对刚下电的节点立即执行上电操作。由于节点状态变更需要一段时间，该行为会由于节点状态仍为Normal，MML返回该节点状态正常，不需要执行上电操作。
- 避免短时间内对同一节点反复执行上电操作。该行为可能会导致MANO执行多次上电任务，请稍后使用[**DSP NODE**](节点查询（DSP NODE）_71678755.md)命令查看具体执行结果。
- 节点处于非Normal状态时，对其进行上电操作，MANO可能不会对该节点执行上电操作，请稍后使用[**DSP NODE**](节点查询（DSP NODE）_71678755.md)命令查看具体执行结果。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| NODENAME | 节点名称 | 可选必选说明：必选参数。<br>参数含义：用于指示系统需要启动哪个节点。<br>取值范围：不超过128位的字符串。<br>默认值：无。<br>配置原则：操作员可以使用<br>[**DSP NODE**](节点查询（DSP NODE）_71678755.md)<br>命令查询获得。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NODE]] · 节点信息（NODE）

## 使用实例

启动 “节点名称” 为 “10.0.0.1” 。

```
%%STR NODE: NODENAME="10.0.0.1";%%
RETCODE = 0  操作成功
操作结果如下
------------
    状态  =  Success
详细信息  =  操作成功
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动节点（STR-NODE）_92785240.md`
