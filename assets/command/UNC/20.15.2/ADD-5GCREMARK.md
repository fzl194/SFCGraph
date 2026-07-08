---
id: UNC@20.15.2@MMLCommand@ADD 5GCREMARK
type: MMLCommand
name: ADD 5GCREMARK（增加5GC QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: 5GCREMARK
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 5GC Qos映射ToS_DSCP
status: active
---

# ADD 5GCREMARK（增加5GC QoS到TOS/DSCP的映射规则）

## 功能

**适用NF：SMF**

该命令用来增加5G用户QoS参数到IP报头中的DSCP（区别服务编码点）/TOS（服务类型）的映射规则，用户的数据将根据映射得到的DSCP（区别服务编码点）/TOS（服务类型）中的参数值进行转发。

## 注意事项

- 命令执行后只对新接入用户生效。

- 最多可输入1000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：必选参数<br>参数含义：该参数指定QoS Profile的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |
| FIVEQI | 5QI | 可选必选说明：必选参数<br>参数含义：该参数表示5G QoS Identifier。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| ARPPL | ARP的优先级别 | 可选必选说明：必选参数<br>参数含义：该参数表示ARP的优先级别。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~15。<br>默认值：无<br>配置原则：<br>- 0：General，通用用户。如果某业务级别各个优先级的用户都没有配置DSCP，则用General配置的值。<br>- 1~15：用户的优先级，其中1的优先级最高。 |
| REMARKTYPE | 标记类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示映射到DSCP或者TOS。<br>数据来源：全网规划<br>取值范围：<br>- DSCP（映射到Dscp）<br>- TOS（映射到TOS）<br>默认值：无<br>配置原则：无 |
| DSCP | DSCP | 可选必选说明：该参数在"REMARKTYPE"配置为"DSCP"时为条件必选参数。<br>参数含义：该参数用于表示DSCP。<br>数据来源：全网规划<br>取值范围：<br>- EF（对应的DSCP的值为101110）<br>- AF（对应的DSCP的值由参数AfClass和AfDropPres界定）<br>- BE（对应的DSCP的值为000000）<br>- CS6（对应的DSCP的值为110000）<br>- CS7（对应的DSCP的值为111000）<br>- DSCP_VALUE（映射的DSCP值）<br>默认值：无<br>配置原则：无 |
| AFCLASS | AF级别 | 可选必选说明：该参数在"DSCP"配置为"AF"时为条件必选参数。<br>参数含义：该参数用于表示AF队列序号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~4。<br>默认值：无<br>配置原则：无 |
| AFDROPPREC | AF丢弃优先级 | 可选必选说明：该参数在"DSCP"配置为"AF"时为条件必选参数。<br>参数含义：该参数表示AF丢弃优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~3。<br>默认值：无<br>配置原则：无 |
| TOSVALUE | TOS值 | 可选必选说明：该参数在"REMARKTYPE"配置为"TOS"时为条件必选参数。<br>参数含义：该参数表示映射到TOS的值，分别对应IP优先级的8个队列ID，优先值高的报文先于优先值低的报文发送。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~7。<br>默认值：无<br>配置原则：无 |
| DSCPVALUE | DSCP值 | 可选必选说明：该参数在"DSCP"配置为"DSCP_VALUE"时为条件必选参数。<br>参数含义：该参数用于表示映射的DSCP值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：无 |
| N3DSCPSWITCH | N3 DSCP配置开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示N3接口DSCP配置开关。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（disable）”：不使能<br>- “ENABLE（ENABLE）”：使能<br>默认值：无<br>配置原则：无 |
| N3DSCP | N3 DSCP | 可选必选说明：该参数在"N3DSCPSWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于表示N3 DSCP。<br>数据来源：全网规划<br>取值范围：<br>- EF（对应的DSCP的值为101110）<br>- AF（对应的DSCP的值由参数AfClass和AfDropPres界定）<br>- BE（对应的DSCP的值为000000）<br>- CS6（对应的DSCP的值为110000）<br>- CS7（对应的DSCP的值为111000）<br>- DSCP_VALUE（映射的DSCP值）<br>默认值：无<br>配置原则：无 |
| N3AFCLASS | N3 AF级别 | 可选必选说明：该参数在"N3DSCP"配置为"AF"时为条件必选参数。<br>参数含义：该参数用于表示N3接口AF队列序号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~4。<br>默认值：无<br>配置原则：无 |
| N3AFDROPPREC | N3 AF丢弃优先级 | 可选必选说明：该参数在"N3DSCP"配置为"AF"时为条件必选参数。<br>参数含义：该参数表示N3接口AF丢弃优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~3。<br>默认值：无<br>配置原则：无 |
| N3DSCPVALUE | N3 DSCP值 | 可选必选说明：该参数在"N3DSCP"配置为"DSCP_VALUE"时为条件必选参数。<br>参数含义：该参数用于表示映射的N3接口DSCP值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：无 |
| N9DSCPSWITCH | N9 DSCP配置开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示N9接口DSCP配置开关。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（disable）”：不使能<br>- “ENABLE（ENABLE）”：使能<br>默认值：无<br>配置原则：无 |
| N9DSCP | N9 DSCP | 可选必选说明：该参数在"N9DSCPSWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于表示N9 DSCP。<br>数据来源：全网规划<br>取值范围：<br>- EF（对应的DSCP的值为101110）<br>- AF（对应的DSCP的值由参数AfClass和AfDropPres界定）<br>- BE（对应的DSCP的值为000000）<br>- CS6（对应的DSCP的值为110000）<br>- CS7（对应的DSCP的值为111000）<br>- DSCP_VALUE（映射的DSCP值）<br>默认值：无<br>配置原则：无 |
| N9AFCLASS | N9 AF级别 | 可选必选说明：该参数在"N9DSCP"配置为"AF"时为条件必选参数。<br>参数含义：N9 AF级别。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~4。<br>默认值：无<br>配置原则：无 |
| N9AFDROPPREC | N9 AF丢弃优先级 | 可选必选说明：该参数在"N9DSCP"配置为"AF"时为条件必选参数。<br>参数含义：N9 AF丢弃优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~3。<br>默认值：无<br>配置原则：无 |
| N9DSCPVALUE | N9 DSCP值 | 可选必选说明：该参数在"N9DSCP"配置为"DSCP_VALUE"时为条件必选参数。<br>参数含义：该参数用于表示映射的N9接口DSCP值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：无 |
| N6DSCPSWITCH | N6 DSCP配置开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示N6接口DSCP配置开关。<br>数据来源：全网规划<br>取值范围：<br>- “DISABLE（disable）”：不使能<br>- “ENABLE（ENABLE）”：使能<br>默认值：无<br>配置原则：无 |
| N6DSCP | N6 DSCP | 可选必选说明：该参数在"N6DSCPSWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于表示N6 DSCP。<br>数据来源：全网规划<br>取值范围：<br>- EF（对应的DSCP的值为101110）<br>- AF（对应的DSCP的值由参数AfClass和AfDropPres界定）<br>- BE（对应的DSCP的值为000000）<br>- CS6（对应的DSCP的值为110000）<br>- CS7（对应的DSCP的值为111000）<br>- DSCP_VALUE（映射的DSCP值）<br>默认值：无<br>配置原则：无 |
| N6AFCLASS | N6 AF级别 | 可选必选说明：该参数在"N6DSCP"配置为"AF"时为条件必选参数。<br>参数含义：N6 AF级别。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~4。<br>默认值：无<br>配置原则：无 |
| N6AFDROPPREC | N6 AF丢弃优先级 | 可选必选说明：该参数在"N6DSCP"配置为"AF"时为条件必选参数。<br>参数含义：N6 AF丢弃优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~3。<br>默认值：无<br>配置原则：无 |
| N6DSCPVALUE | N6 DSCP值 | 可选必选说明：该参数在"N6DSCP"配置为"DSCP_VALUE"时为条件必选参数。<br>参数含义：该参数用于表示映射的N6接口DSCP值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@5GCREMARK]] · 5GC QoS到TOS/DSCP的映射规则（5GCREMARK）

## 使用实例

添加QoS Profile名称为"profile"的5GC Remark配置，5QI值为5，ARP的优先级别为5，标记类型为“DSCP”，参数“DSCP”为EF：

```
ADD 5GCREMARK:QOSPROFILENAME="profile",FIVEQI=5,ARPPL=5,REMARKTYPE=DSCP,DSCP=EF; 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-5GCREMARK.md`
