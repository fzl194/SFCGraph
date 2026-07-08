# 查询字段映射关系（LST CDRFIELDTYPE）

- [命令功能](#ZH-CN_MMLREF_0245110920__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0245110920__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0245110920__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0245110920__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0245110920__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0245110920)

**适用NF：NCG**

该命令用于查询字段映射关系。

## [注意事项](#ZH-CN_MMLREF_0245110920)

无

#### [操作用户权限](#ZH-CN_MMLREF_0245110920)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0245110920)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FIELDNAME | 字段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定字段名称。<br>数据来源：本端规划<br>取值范围：<br>- RATTYPE（RAT类型）<br>- SSCMODE（SSC模式）<br>- PDUSESSIONTYPE（PDU会话类型）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0245110920)

查询字段映射关系：

```
%%LST CDRFIELDTYPE:;%%
RETCODE = 0  操作成功

结果如下
--------
字段名称     RAT类型名称                                 SSC类型名称  PDU类型名称   类型取值  

RAT类型      New Radio                                   SSCMode 1    IPv4          51        
RAT类型      Evolved Universal Terrestrial Radio Access  SSCMode 1    IPv4          6         
RAT类型      Wireless LAN                                SSCMode 1    IPv4          3         
RAT类型      Virtual                                     SSCMode 1    IPv4          7         
RAT类型      GERA                                        SSCMode 1    IPv4          2         
RAT类型      NB IoT                                      SSCMode 1    IPv4          8         
RAT类型      LTE-M                                       SSCMode 1    IPv4          9         
RAT类型      UTRA                                        SSCMode 1    IPv4          1         
SSC模式      New Radio                                   SSCMode 1    IPv4          1         
SSC模式      New Radio                                   SSCMode 2    IPv4          2         
SSC模式      New Radio                                   SSCMode 3    IPv4          3         
PDU会话类型  New Radio                                   SSCMode 1    IPv4          1         
PDU会话类型  New Radio                                   SSCMode 1    IPv6          2         
PDU会话类型  New Radio                                   SSCMode 1    IPv4v6        0         
PDU会话类型  New Radio                                   SSCMode 1    Unstructured  3         
PDU会话类型  New Radio                                   SSCMode 1    Ethernet      4         
PDU会话类型  New Radio                                   SSCMode 1    Non-IP        50
RAT类型      NR_REDCAP                                   SSCMode 1    IPv4          58
(结果个数 = 18)
```

## [输出结果说明](#ZH-CN_MMLREF_0245110920)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 字段名称 | 该参数用于指定字段名称。 |
| RAT类型名称 | 该参数用于指定RAT类型名称。 |
| SSC类型名称 | 该参数用于指定SSC类型名称。 |
| PDU类型名称 | 该参数用于指定PDU类型名称。 |
| 类型取值 | 该参数用于指定类型取值。 |
