---
id: UNC@20.15.2@MMLCommand@DSP DBNODE
type: MMLCommand
name: DSP DBNODE（查询CSDB节点信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DBNODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 节点管理
status: active
---

# DSP DBNODE（查询CSDB节点信息）

## 功能

该命令用于查询CSDB的节点信息，包括节点位置信息、状态信息、负载信息等。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLUSTERID | 子集群标识 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定特定子集群，可以通过<br>**[DSP DBCLUSTER](../集群管理/查询CSDB子集群信息（DSP DBCLUSTER）_29626985.md)**<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：1～10。<br>默认值：无。 |
| RUNAME | 资源单元名称 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定服务端进程所在的资源单元名称，可以通过<br>**[LST SERVICERUSTATE](../../../单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，长度为1～63。<br>默认值：无。 |
| NODETYPE | 节点类型 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定服务端进程的类型。<br>数据来源：本端规划<br>取值范围：<br>- “CONTROL”：查询控制节点（PRP进程）的信息。<br>- “STORAGE”：查询存储节点（DNP进程）的信息。<br>默认值：无。 |
| NODENO | 同类进程实例号 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定同类型进程在资源单元内的排序序号，从0开始排序。<br>数据来源：本端规划<br>取值范围：0～63。<br>默认值：无。<br>配置原则：<br>- 如果节点类型是“CONTROL”，本参数的值应为“0”。<br>- 如果节点类型是“STORAGE”，本参数的值必须小于STORAGE节点数的最大值。<br>- 不输入该参数可对指定类型的所有节点生效。 |
| NODESTATE | 节点状态 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定服务端进程的状态。<br>数据来源：本端规划<br>取值范围：<br>- “NORMAL”<br>- “FAULT”<br>默认值：无。<br>配置原则：如果不指定节点状态，显示所有节点状态的节点信息。 |

## 操作的配置对象

- [CSDB节点信息（DBNODE）](configobject/UNC/20.15.2/DBNODE.md)

## 使用实例

查询 “子集群标识” 为 “1” 、 “节点类型” 为 “STORAGE” 的节点信息：

DSP DBNODE: CLUSTERID=1, NODETYPE=STORAGE;

```
%%DSP DBNODE: CLUSTERID=1, NODETYPE=STORAGE;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
子集群标识  资源单元名称     节点类型  同类进程实例号  节点通信信息           节点状态  节点主备状态  内存大小(M)  内存使用率(%)  CPU占用率(%)  队列使用率(%)  持久化状态      Worker个数  表空间计算方法  性能权重  

1           CSDB_SD_RU_0064  存储节点  0               nlsId = 2, nodeId = 4  正常      主            18832        4              4             5              已经关闭持久化  3           原模型法        150       
1           CSDB_SD_RU_0065  存储节点  0               nlsId = 2, nodeId = 7  正常      主            18832        4              3             3              已经关闭持久化  3           原模型法        150       
(结果个数 = 2)

---    END
```

查询 “子集群标识” 为 “1” 、 “节点类型” 为 “CONTROL” 的节点信息：

DSP DBNODE: CLUSTERID=1, NODETYPE=CONTROL;

```
%%DSP DBNODE: CLUSTERID=1, NODETYPE=CONTROL;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
子集群标识  资源单元名称     节点类型  同类进程实例号  节点通信信息           节点状态  节点主备状态  内存大小(M)  内存使用率(%)  持久化状态      

1           CSDB_SD_RU_0065  控制节点  0               nlsId = 2, nodeId = 8  正常      备            1611         23             已经关闭持久化  
1           CSDB_SD_RU_0064  控制节点  0               nlsId = 2, nodeId = 5  正常      主            1611         23             已经关闭持久化  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CSDB节点信息（DSP-DBNODE）_29626990.md`
