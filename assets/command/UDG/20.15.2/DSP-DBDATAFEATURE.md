---
id: UDG@20.15.2@MMLCommand@DSP DBDATAFEATURE
type: MMLCommand
name: DSP DBDATAFEATURE（查询CSDB数据特征）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DBDATAFEATURE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 数据特征管理
status: active
---

# DSP DBDATAFEATURE（查询CSDB数据特征）

## 功能

该命令用于查询CSDB的数据特征信息，包括数据特征值、数据特征在记录的偏移和数据特征的角色。

## 注意事项

针对参数"CSTYPE" （客户端服务端类型）取值为“CLIENT”的查询，存在如下约束：

- 通过命令**[DSP DBINSTANCE](../实例管理/查询CSDB子实例信息（DSP DBINSTANCE）_29626987.md)**查询CSDB子实例信息时， 返回信息中初始容量和总容量为0的不支持查询。
- 通过命令**[DSP DBINSTANCE](../实例管理/查询CSDB子实例信息（DSP DBINSTANCE）_29626987.md)**查询CSDB子实例信息时， 返回信息中初始容量和总容量不为0，但是通过命令**[DSP DBPLUGIN](../插件管理/查询CSDB插件信息（DSP DBPLUGIN）_29626994.md)**查询CSDB插件信息时，返回信息为“NLS或插件不存在”的不支持查询。
- 通过命令**[DSP DBINSTANCE](../实例管理/查询CSDB子实例信息（DSP DBINSTANCE）_29626987.md)**查询CSDB子实例信息时， 返回信息中初始容量和总容量不为0，且通过命令**[DSP DBPLUGIN](../插件管理/查询CSDB插件信息（DSP DBPLUGIN）_29626994.md)**能成功查询到CSDB插件信息时，支持查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | 子实例标识 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定唯一一个子实例，可以通过<br>**[DSP DBINSTANCE](../实例管理/查询CSDB子实例信息（DSP DBINSTANCE）_29626987.md)**<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：1～100。<br>默认值：无。 |
| CSTYPE | 客户端服务端类型 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定客户端还是服务端。<br>数据来源：本端规划<br>取值范围：<br>- “CLIENT”：显示客户端的数据特征。<br>- “SERVER”：显示服务端的数据特征。<br>默认值：无。 |
| TBLID | 数据表标识 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定唯一一张数据表，可以通过<br>**[DSP DBTBL](../数据表管理/查询CSDB数据表信息（DSP DBTBL）_29626992.md)**<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：0～1023。<br>默认值：无。 |
| DATAFEATUREOPT | 数据特征选项 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定数据特征选项。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_FEATURE”：显示所有数据特征。<br>- “SPEC_PLUGINID”：显示指定插件的数据特征。<br>- “SPEC_FEATURE”：显示指定的数据特征。<br>默认值：ALL_FEATURE。 |
| PLUGINID | 插件标识 | 可选必选说明：条件必选参数。<br>参数含义：该参数用于指定插件标识，可以通过<br>**[DSP DBPLUGIN](../插件管理/查询CSDB插件信息（DSP DBPLUGIN）_29626994.md)**<br>命令查询获取。<br>前提条件：该参数在<br>“DATAFEATUREOPT”<br>参数设置为<br>“SPEC_PLUGINID”<br>后生效。<br>数据来源：本端规划<br>取值范围：0～4294967295。<br>默认值：无。 |
| DATAFEATURE | 数据特征 | 可选必选说明：条件必选参数。<br>参数含义：该参数用于指定数据特征。<br>数据来源：本端规划<br>前提条件：该参数在<br>“DATAFEATUREOPT”<br>参数设置为<br>“SPEC_FEATURE”<br>后生效。<br>取值范围：0～4294967295。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DBDATAFEATURE]] · CSDB数据特征（DBDATAFEATURE）

## 使用实例

查询 “子实例标识” 为 “1” 、 “客户端服务端类型” 为 “SERVER” 、 “数据表标识” 为 “11” 、 “插件标识” 为 “50000022” 的数据特征信息：

DSP DBDATAFEATURE: INSTANCEID=1, CSTYPE=SERVER, TBLID=11, DATAFEATUREOPT=SPEC_PLUGINID, PLUGINID=50000022;

```
%%DSP DBDATAFEATURE: INSTANCEID=1, CSTYPE=SERVER, TBLID=11, DATAFEATUREOPT=SPEC_PLUGINID, PLUGINID=50000022;%%
RETCODE = 0  执行成功

操作结果如下：
--------------
子实例标识    数据表标识    数据特征    数据特征偏移    虚拟化网络功能组件标识    插件标识   
1             11            300         0               5               50000022 
1             11            319         0               5               50000022 
1             11            318         0               5               50000022 
1             11            317         0               5               50000022 
1             11            316         0               5               50000022 
1             11            315         0               5               50000022 
1             11            314         0               5               50000022 
1             11            313         0               5               50000022 
1             11            312         0               5               50000022 
1             11            311         0               5               50000022 
1             11            310         0               5               50000022 
1             11            309         0               5               50000022 
1             11            308         0               5               50000022 
1             11            307         0               5               50000022 
1             11            306         0               5               50000022 
1             11            305         0               5               50000022 
1             11            304         0               5               50000022 
1             11            303         0               5               50000022 
1             11            302         0               5               50000022 
1             11            301         0               5               50000022 
(结果个数 = 20)
---    END
```

查询 “子实例标识” 为 “1” 、 “客户端服务端类型” 为 “CLIENT” 、 “数据表标识” 为 “11” 、 “插件标识” 为 “50000022” 的数据特征信息：

DSP DBDATAFEATURE: INSTANCEID=1, CSTYPE=CLIENT, TBLID=11, DATAFEATUREOPT=SPEC_PLUGINID, PLUGINID=50000022;

```
%%DSP DBDATAFEATURE: INSTANCEID=1, CSTYPE=CLIENT, TBLID=11, DATAFEATUREOPT=SPEC_PLUGINID, PLUGINID=50000022;%%
RETCODE = 0  执行成功

操作结果如下
-------------------------
子实例标识    数据表标识    数据特征    数据特征偏移    数据特征角色    虚拟化网络功能组件标识    插件标识    

1             11            300         0               生产者          5              50000022  
1             11            301         0               生产者          5              50000022  
1             11            302         0               生产者          5              50000022  
1             11            303         0               生产者          5              50000022  
1             11            304         0               生产者          5              50000022  
1             11            305         0               生产者          5              50000022  
1             11            306         0               生产者          5              50000022  
1             11            307         0               生产者          5              50000022  
1             11            308         0               生产者          5              50000022  
1             11            309         0               生产者          5              50000022  
1             11            310         0               生产者          5              50000022  
1             11            311         0               生产者          5              50000022  
1             11            312         0               生产者          5              50000022  
1             11            313         0               生产者          5              50000022  
1             11            314         0               生产者          5              50000022  
1             11            315         0               生产者          5              50000022  
1             11            316         0               生产者          5              50000022  
1             11            317         0               生产者          5              50000022  
1             11            318         0               生产者          5              50000022  
1             11            319         0               生产者          5              50000022  
(结果个数 = 20)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CSDB数据特征（DSP-DBDATAFEATURE）_29626996.md`
