# 显示专用DNN会话数（DSP MULDNNSESSNUM）

- [命令功能](#ZH-CN_MMLREF_0000001363370069__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001363370069__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001363370069__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001363370069__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001363370069__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001363370069)

**适用NF：PGW-C、SMF**

该命令用于查询N11SMF、N16aSMF、PGW-C和SPGW-C上通用DNN会话关联的专用DNN会话数。

## [注意事项](#ZH-CN_MMLREF_0000001363370069)

“查询分类”参数不输入时，表示查询汇总的信息。

#### [操作用户权限](#ZH-CN_MMLREF_0000001363370069)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001363370069)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QRY_SCOPE | 查询范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询会话上下文的范围。<br>数据来源：本端规划<br>取值范围：<br>- “SUMMARY（汇总信息）”：查询汇总信息。以汇总方式呈现。<br>- “ALL_POD_INFO（所有POD信息）”：查询所有POD信息。以POD粒度呈现。<br>- “SPECIFIED_POD_INFO（指定POD信息）”：查询指定POD信息。<br>默认值：SUMMARY<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定2B2C漫游双DNN特性的通用DNN会话的APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| POD_ID | POD名称 | 可选必选说明：该参数在"QRY_SCOPE"配置为"SPECIFIED_POD_INFO"时为条件必选参数。<br>参数含义：该参数用于指定需要查询会话上下文数的POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001363370069)

当希望查询UNC设备上各形态创建的专用DNN会话数量时，使用如下命令：

```
%%DSP MULDNNSESSNUM: QRY_SCOPE=SUMMARY, APN="huawei.com";%%
RETCODE = 0  操作成功

结果如下
------------------------
                            查询范围  =  汇总信息
                                 APN  =  huawei.com
      PGW-C上激活的专用DNN PDU会话数  =  0
    S/PGW-C上激活的专用DNN PDU会话数  =  0
N16a接口SMF上激活的专用DNN PDU会话数  =  0
 N11接口SMF上激活的专用DNN PDU会话数  =  0
                 专用DNN PDU会话总数  =  0
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001363370069)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 查询范围 | 该参数用于指定查询会话上下文的范围。<br>取值说明：<br>- “SUMMARY（汇总信息）”：查询汇总信息。以汇总方式呈现。<br>- “ALL_POD_INFO（所有POD信息）”：查询所有POD信息。以POD粒度呈现。<br>- “SPECIFIED_POD_INFO（指定POD信息）”：查询指定POD信息。 |
| APN名称 | 该参数用于指定2B2C漫游双DNN特性的通用DNN会话的APN实例名。 |
| PGW-C上激活的专用DNN PDU会话数 | 该参数表示PGW-C上激活的专用DNN PDU会话数。 |
| S/PGW-C上激活的专用DNN PDU会话数 | 该参数表示S/PGW-C上激活的专用DNN PDU会话数。 |
| N16A接口SMF上激活的专用DNN PDU会话数 | 该参数表示N16a接口SMF上激活的专用DNN PDU会话数。 |
| N11接口SMF上激活的专用DNN PDU会话数 | 该参数表示N11接口SMF上激活的专用DNN PDU会话数。 |
| 专用DNN PDU会话总数 | 该参数表示系统用户激活使用的专用DNN PDU总会话数，等于“PGW-C上激活的专用DNN PDU会话数”、“S/PGW-C上激活的专用DNN PDU会话数”、“N16a接口SMF上激活的专用DNN PDU会话数”、“N11接口SMF上激活的专用DNN PDU会话数”之和。 |
| POD名称 | 该参数用于指定需要查询会话上下文数的POD名称。 |
| POD版本号信息 | 该参数用于指定POD版本号。非灰度升级期间，该参数不显示。 |
