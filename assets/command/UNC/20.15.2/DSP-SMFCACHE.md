---
id: UNC@20.15.2@MMLCommand@DSP SMFCACHE
type: MMLCommand
name: DSP SMFCACHE（显示缓存的SMF与TAI映射关系）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMFCACHE
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- SMF缓存策略管理
status: active
---

# DSP SMFCACHE（显示缓存的SMF与TAI映射关系）

## 功能

**适用NF：AMF**

该命令用于查询AMF缓存的SMF与POD名称、支持TAI列表的映射关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的信息。<br>数据来源：本端规划<br>取值范围：<br>- “QUERYLOC（查询SMF实例ID和POD名称）”：查询AMF上缓存的SMF实例ID和所在的POD名称。<br>- “QUERYTAIS（查询指定TAI列表）”：查询AMF上指定POD名称和缓存的SMF实例ID对应的TAI列表。<br>- “QUERYTAILOC（查询指定SMF实例ID）”：查询AMF上指定POD名称和TAI所在SMF实例ID。<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：该参数在"QUERYTYPE"配置为"QUERYTAIS"、"QUERYTAILOC"时为条件必选参数。<br>参数含义：该参数表示AMF上缓存SMF与TAI映射关系的POD名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| INSTANCEID | SMF实例ID | 可选必选说明：该参数在"QUERYTYPE"配置为"QUERYTAIS"时为条件必选参数。<br>参数含义：该参数AMF上表示缓存的SMF实例ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~60。<br>默认值：无<br>配置原则：无 |
| SPECIFIEDTAI | 指定TAI | 可选必选说明：该参数在"QUERYTYPE"配置为"QUERYTAILOC"时为条件必选参数。<br>参数含义：该参数用于查询AMF缓存中的指定TAI所在的SMF实例ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是11~12。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFCACHE]] · 缓存的SMF与TAI映射关系（SMFCACHE）

## 使用实例

- 查询AMF上缓存的SMF实例ID和所在的POD名称，执行如下命令：
  ```
  DSP SMFCACHE:QUERYTYPE=QUERYLOC;
  ```
- 根据步骤1获取的POD名称和缓存的SMF实例ID，查询对应POD名称和SMF实例ID下的SMF与TAI映射关系，执行如下命令：
  ```
  DSP SMFCACHE:QUERYTYPE=QUERYTAIS,PODNAME="pod-1",INSTANCEID="smfInstanceId-1";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SMFCACHE.md`
