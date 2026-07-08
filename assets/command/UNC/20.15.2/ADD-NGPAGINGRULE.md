---
id: UNC@20.15.2@MMLCommand@ADD NGPAGINGRULE
type: MMLCommand
name: ADD NGPAGINGRULE（增加5G寻呼规则）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NGPAGINGRULE
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP接口寻呼管理
- NG寻呼规则管理
status: active
---

# ADD NGPAGINGRULE（增加5G寻呼规则）

## 功能

**适用NF：AMF**

此命令用于增加5G寻呼规则。通过此命令配置AMF精准寻呼的规则集，比如指定使用精准寻呼的用户群、业务类型、使用的寻呼动作组合等。通过部署精准寻呼，缩小寻呼范围，减少RAN的寻呼负荷，节省网络资源。

## 注意事项

- 该命令执行后立即生效。

- 不能为同一个用户（群）的同一种业务类型配置多条寻呼规则。

- 最多可输入1000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULEIDX | 规则索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G寻呼规则的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000。<br>默认值：无<br>配置原则：无 |
| GRPTYPE | 用户群类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用5G精准寻呼的用户的标识类型。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>- “MSISDN_PREFIX（MSISDN前缀）”：指定MSISDN前缀<br>- “IMEI_TAC（IMEI_TAC）”：指定IMEI_TAC<br>默认值：无<br>配置原则：<br>对于指定的用户，精准寻呼规则的匹配优先级从高到低依次为："IMSI_PREFIX(IMSI前缀)"或"MSISDN_PREFIX(MSISDN前缀)"或"IMEI_TAC(IMEI_TAC)"、"ALL_USER(所有用户)"。 |
| IMEITAC | IMEI TAC | 可选必选说明：该参数在"GRPTYPE"配置为"IMEI_TAC"时为条件必选参数。<br>参数含义：该参数用于指定应用5G精准寻呼的用户的IMEI TAC。TAC（Type Allocation Code）是组成IMEI的前8个数字。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是8。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：该参数在"GRPTYPE"配置为"MSISDN_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定应用5G精准寻呼的用户的MSISDN前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"GRPTYPE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定应用5G精准寻呼的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| SVRTYPE | 业务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用5G精准寻呼的业务类型。<br>数据来源：本端规划<br>取值范围：<br>- “SMF_N1N2（N1N2TRANS消息）”：N1N2TRANS消息<br>- “UDM_SDM（UDM SDM消息）”：UDM SDM消息<br>- “OTHER（OTHER消息）”：OTHER消息<br>默认值：无<br>配置原则：无 |
| DNNIND | DNN指示 | 可选必选说明：该参数在"SVRTYPE"配置为"SMF_N1N2"时为条件必选参数。<br>参数含义：该参数用于指定应用5G精准寻呼的DNN范围，即所有DNN，或者指定的单个DNN。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_DNN（所有DNN）”：所有DNN<br>- “SPEC_DNN（指定DNN）”：指定DNN<br>默认值：无<br>配置原则：无 |
| DNN | 数据网络名称 | 可选必选说明：该参数在"DNNIND"配置为"SPEC_DNN"时为条件必选参数。<br>参数含义：该参数用于指定应用5G精准寻呼的数据网络名称（DNN）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| FQI | 5G QoS标识 | 可选必选说明：该参数在"SVRTYPE"配置为"SMF_N1N2"时为条件可选参数。<br>参数含义：该参数用于指定SMF通过N1N2MsgTransfer（非PCF释放会话）触发寻呼场景下，使用5G精准寻呼功能的5QI匹配值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| ARPPL | ARP优先级别 | 可选必选说明：该参数在"SVRTYPE"配置为"SMF_N1N2"时为条件可选参数。<br>参数含义：该参数用于指定SMF通过N1N2MsgTransfer（非PCF释放会话）触发寻呼场景下，使用5G精准寻呼功能的ARP优先级匹配值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| PPI | 寻呼策略指示 | 可选必选说明：该参数在"SVRTYPE"配置为"SMF_N1N2"时为条件可选参数。<br>参数含义：该参数用于指定SMF通过N1N2MsgTransfer（非PCF释放会话）触发寻呼场景下，使用5G精准寻呼功能的寻呼策略指示。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~7。<br>默认值：无<br>配置原则：<br>系统初始值为“255”，有效的PPI取值范围是0-7。 |
| PRIORITY | 匹配优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本寻呼规则的匹配优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：200<br>配置原则：<br>优先级数值越小，代表优先级越高。<br>在业务匹配多条寻呼规则的场景下，优先级高的寻呼规则优先匹配。 |
| ACTGRP | 寻呼动作组合 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本寻呼规则使用的寻呼动作组合。<br>数据来源：本端规划<br>取值范围：<br>- “LAST_GNB（最近访问GNB）”：最近访问GNB<br>- “NEIGH_GNB（邻接GNB）”：邻接GNB<br>- “LAST_TA（最近访问TA）”：最近访问TA<br>- “NEIGH_TA（邻接TA ）”：邻接TA<br>默认值：无<br>配置原则：无 |
| DESC | 规则描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定寻呼规则的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [5G寻呼规则（NGPAGINGRULE）](configobject/UNC/20.15.2/NGPAGINGRULE.md)

## 使用实例

增加一条5G寻呼规则， “用户群类型”为“ALL_USER(所有用户)”，“业务类型”为“SMF_N1N2(N1N2TRANS消息)”，“DDN指示”为“ALL_DNN(所有DNN)”，设置该规则的“匹配优先级”为“50”，“寻呼动作组合”为“LAST_GNB”，执行如下命令：

```
ADD NGPAGINGRULE: GRPTYPE=ALL_USER, SVRTYPE=SMF_N1N2, DNNIND=ALL_DNN, PRIORITY=50, ACTGRP=LAST_GNB-1,RULEIDX=6;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加5G寻呼规则（ADD-NGPAGINGRULE）_09652969.md`
