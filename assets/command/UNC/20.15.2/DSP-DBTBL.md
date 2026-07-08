---
id: UNC@20.15.2@MMLCommand@DSP DBTBL
type: MMLCommand
name: DSP DBTBL（查询CSDB数据表信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DBTBL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 数据表管理
status: active
---

# DSP DBTBL（查询CSDB数据表信息）

## 功能

该命令用于查询CSDB指定实例的数据表的信息，包括数据表名称、数据表记录个数、数据表的节点分布信息。

## 注意事项

针对参数"CSTYPE" （客户端服务端类型）取值为“CLIENT”的查询，存在如下约束：

- 通过命令**[DSP DBINSTANCE](../实例管理/查询CSDB子实例信息（DSP DBINSTANCE）_29626987.md)**查询CSDB子实例信息时， 返回信息中初始容量和总容量为0的不支持查询。
- 通过命令**[DSP DBINSTANCE](../实例管理/查询CSDB子实例信息（DSP DBINSTANCE）_29626987.md)**查询CSDB子实例信息时， 返回信息中初始容量和总容量不为0，但是通过命令**[DSP DBPLUGIN](../插件管理/查询CSDB插件信息（DSP DBPLUGIN）_29626994.md)**查询CSDB插件信息时，返回信息为“NLS或插件不存在”的不支持查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | 子实例标识 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定唯一一个子实例，可以通过<br>**[DSP DBINSTANCE](../实例管理/查询CSDB子实例信息（DSP DBINSTANCE）_29626987.md)**<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：1～100。<br>默认值：无。 |
| TBLID | 数据表标识 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定唯一一张数据表。<br>数据来源：本端规划<br>取值范围：0～4095。<br>默认值：无。<br>配置原则：如果不指定数据表标识，则显示所有数据表的信息。 |
| CSTYPE | 客户端服务端类型 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定是客户端还是服务端。<br>数据来源：本端规划<br>取值范围：<br>- “CLIENT”：显示客户端的数据表信息。<br>- “SERVER”：显示服务端的数据表信息。<br>默认值：无。 |
| VNFCID | 虚拟化网络功能组件标识 | 可选必选说明：条件可选参数。<br>参数含义：该参数用于指定客户端进程所在的VNFC标识，可以通过<br>**[DSP DBINSTANCE](../实例管理/查询CSDB子实例信息（DSP DBINSTANCE）_29626987.md)**<br>命令查询获取。<br>前提条件：该参数在<br>“CSTYPE”<br>参数设置为<br>“CLIENT”<br>后生效。<br>数据来源：本端规划<br>取值范围：0～4294967295。<br>默认值：无。 |
| RUNAME | 资源单元名称 | 可选必选说明：条件可选参数。<br>参数含义：该参数用于指定服务端进程所在的资源单元名称，可以通过<br>**[LST SERVICERUSTATE](../../../单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>命令查询获取。<br>前提条件：该参数在<br>“CSTYPE”<br>参数设置为<br>“SERVER”<br>后生效。<br>数据来源：本端规划<br>取值范围：不超过63个英文字符。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DBTBL]] · CSDB数据表信息（DBTBL）

## 使用实例

查询 “子实例标识” 为 “2” 、 “数据表标识” 为 “11” 在服务端的分布信息：

DSP DBTBL: INSTANCEID=2, TBLID=11, CSTYPE=SERVER;

```
%%DSP DBTBL: INSTANCEID=2, TBLID=11, CSTYPE=SERVER;%%
RETCODE = 0  执行成功
操作结果如下
-------------------------
数据表标识    数据表名称    资源单元名称      节点类型    同类进程实例号    数据表的实际记录个数    数据表的最大记录个数    表空间使用率(%)    主副本记录个数    备副本记录个数    当前版本号    目标版本号     定义压缩字段
11            MM SM ROOT    SDB_SD_RU_0064    存储节点    1                 0                       NULL                    0                  0                 0                 4294967295    4294967295     定义
11            MM SM ROOT    SDB_SD_RU_0064    存储节点    0                 0                       NULL                    0                  0                 0                 4294967295    4294967295     定义     
11            MM SM ROOT    SDB_SD_RU_0065    存储节点    0                 0                       NULL                    0                  0                 0                 4294967295    4294967295     定义
11            MM SM ROOT    SDB_SD_RU_0065    存储节点    1                 0                       NULL                    0                  0                 0                 4294967295    4294967295     定义
11            MM SM ROOT    ALL               存储节点    NULL              0                       NULL                    0                  0                 0                 4294967295    4294967295     NULL
(结果个数 = 5)
---    END
```

查询 “子实例标识” 为 “2” 、 “数据表标识” 为 “11” 在客户端的分布信息：

DSP DBTBL: INSTANCEID=2, TBLID=11, CSTYPE=CLIENT;

```
%%DSP DBTBL: INSTANCEID=2, TBLID=11, CSTYPE=CLIENT;%%
RETCODE = 0  执行成功

操作结果如下
-------------------------
数据表标识    数据表名称    网络功能组件标识    插件标识    数据表的实际记录个数    数据表的最大记录个数    表空间使用率(%)    当前版本号       定义压缩字段      使能压缩

11            MM SM ROOT    5                   50000025    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000010    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000004    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000026    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000007    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000021    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000005    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000023    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000018    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000019    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000024    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000011    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000006    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000008    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000012    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000022    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000020    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    5                   50000009    0                       79333                   0                  4294967295       定义              使能
11            MM SM ROOT    NULL                NULL        0                       1427994                 0                  4294967295       NULL              NULL
(结果个数 = 19)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CSDB数据表信息（DSP-DBTBL）_29626992.md`
