---
id: UNC@20.15.2@MMLCommand@DSP DBCLUSTER
type: MMLCommand
name: DSP DBCLUSTER（查询CSDB子集群信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DBCLUSTER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 集群管理
status: active
---

# DSP DBCLUSTER（查询CSDB子集群信息）

## 功能

该命令用于查询CSDB的子集群信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLUSTERID | 子集群标识 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定唯一一个子集群。<br>数据来源：本端规划<br>取值范围：1～10。<br>默认值：无。<br>配置原则：如果不指定子集群标识，则显示所有子集群的信息。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DBCLUSTER]] · CSDB子集群信息（DBCLUSTER）

## 使用实例

查询 “子集群标识” 为 “2” 的信息：

DSP DBCLUSTER: CLUSTERID=2;

```
%%DSP DBCLUSTER: CLUSTERID=2;%%
RETCODE = 0  操作成功。

操作结果如下：
--------------
    子集群标识  =  2
      VNFC名称  =  CSLB_VNFC
        DC名称  =  NULL
  资源单元个数  =  2
  控制节点状态  =  正常
  存储节点状态  =  正常
 内存使用率(%)  =  0
  CPU占用率(%)  =  0
 资源单元亲和性 = 强反亲和性
       副本模式 = 数据库级双副本
     持久化标识 = 开启持久化
     持久化状态 = 已经开启持久化
容灾子集群标识  =  2
 (结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DBCLUSTER.md`
