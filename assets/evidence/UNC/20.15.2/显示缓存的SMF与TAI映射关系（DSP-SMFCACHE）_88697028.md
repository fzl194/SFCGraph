# 显示缓存的SMF与TAI映射关系（DSP SMFCACHE）

- [命令功能](#ZH-CN_MMLREF_0000001088697028__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001088697028__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001088697028__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001088697028__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001088697028__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001088697028)

**适用NF：AMF**

该命令用于查询AMF缓存的SMF与POD名称、支持TAI列表的映射关系。

## [注意事项](#ZH-CN_MMLREF_0000001088697028)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001088697028)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001088697028)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的信息。<br>数据来源：本端规划<br>取值范围：<br>- “QUERYLOC（查询SMF实例ID和POD名称）”：查询AMF上缓存的SMF实例ID和所在的POD名称。<br>- “QUERYTAIS（查询指定TAI列表）”：查询AMF上指定POD名称和缓存的SMF实例ID对应的TAI列表。<br>- “QUERYTAILOC（查询指定SMF实例ID）”：查询AMF上指定POD名称和TAI所在SMF实例ID。<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：该参数在"QUERYTYPE"配置为"QUERYTAIS"、"QUERYTAILOC"时为条件必选参数。<br>参数含义：该参数表示AMF上缓存SMF与TAI映射关系的POD名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| INSTANCEID | SMF实例ID | 可选必选说明：该参数在"QUERYTYPE"配置为"QUERYTAIS"时为条件必选参数。<br>参数含义：该参数AMF上表示缓存的SMF实例ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~60。<br>默认值：无<br>配置原则：无 |
| SPECIFIEDTAI | 指定TAI | 可选必选说明：该参数在"QUERYTYPE"配置为"QUERYTAILOC"时为条件必选参数。<br>参数含义：该参数用于查询AMF缓存中的指定TAI所在的SMF实例ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是11~12。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001088697028)

- 查询AMF上缓存的SMF实例ID和所在的POD名称，执行如下命令：
  ```
  DSP SMFCACHE:QUERYTYPE=QUERYLOC;
  ```
- 根据步骤1获取的POD名称和缓存的SMF实例ID，查询对应POD名称和SMF实例ID下的SMF与TAI映射关系，执行如下命令：
  ```
  DSP SMFCACHE:QUERYTYPE=QUERYTAIS,PODNAME="pod-1",INSTANCEID="smfInstanceId-1";
  ```

## [输出结果说明](#ZH-CN_MMLREF_0000001088697028)

| 输出项名称 | 输出项解释 |
| --- | --- |
| SMF实例ID | 该参数AMF上表示缓存的SMF实例ID。 |
| POD名称 | 该参数表示AMF上缓存SMF与TAI映射关系的POD名称。 |
| SMF支持的TAI列表 | 该参数表示AMF缓存的SMF支持的TAI列表。 |
