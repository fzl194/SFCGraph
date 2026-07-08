---
id: UDG@20.15.2@MMLCommand@LST DBTHRESHOLD
type: MMLCommand
name: LST DBTHRESHOLD（查询CSDB配置过载门限）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DBTHRESHOLD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 门限管理
status: active
---

# LST DBTHRESHOLD（查询CSDB配置过载门限）

## 功能

该命令用于查询CSDB门限参数，包括CPU过载门限、存储过载门限以及队列过载门限。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLUSTERID | 子集群标识 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定唯一一个子集群，可以通过<br>**[DSP DBCLUSTER](../集群管理/查询CSDB子集群信息（DSP DBCLUSTER）_29626985.md)**<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：1～10。<br>默认值：无。 |

## 操作的配置对象

- [CSDB配置过载门限（DBTHRESHOLD）](configobject/UDG/20.15.2/DBTHRESHOLD.md)

## 使用实例

查询所有子集群的过载门限参数：

```
LST DBTHRESHOLD:;
%%LST DBTHRESHOLD:;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
子集群标识  门限类型     1级过载下门限  1级过载上门限  2级过载下门限  2级过载上门限  3级过载下门限  3级过载上门限  

1           CPU过载门限   75             80             80             85             85             90             
1           存储过载门限  70             80             80             90             90             95             
1           队列过载门限  50             55             55             60             60             65             
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CSDB配置过载门限(LST-DBTHRESHOLD)_78080691.md`
