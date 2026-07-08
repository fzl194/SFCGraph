---
id: UNC@20.15.2@MMLCommand@ADD NGLANGROUP
type: MMLCommand
name: ADD NGLANGROUP（增加5G LAN群组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NGLANGROUP
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 5G LAN管理
- 5G LAN组管理
status: active
---

# ADD NGLANGROUP（增加5G LAN群组）

## 功能

**适用NF：SMF**

该命令用于增加5G LAN群组。在PDU激活流程中，SMF会根据DNN、切片和PDUSessionType等信息，判断该会话是否属于一个5G LAN群组。如果是，按5G LAN PDU激活流程进行处理；如果否，按正常PDU会话流程进行处理。

## 注意事项

- 该命令执行后立即生效。

- 未规划SD时，可将SD设置为“FFFFFF”。
- 该命令仅用于内部测试，不对外使用。即该命令提供的5G LAN GroupID仅用于测试，正式商用时，请采用UDM下发GroupID的方式。若UDM下发和本地配置的场景同时发生，仅生效UDM下发的5G LAN GroupID。

- 最多可输入512条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN群组支持的DNN，即用户请求的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SST | 切片业务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN群组支持的网络切片业务类型。网络切片标识（S-NSSAI）由切片业务类型（SST）和切片细分标识（SD）两部分组成。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN群组支持的网络切片细分标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| PDUSESSIONTYPE | PDU会话类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN群组支持的PDU会话类型。<br>数据来源：全网规划<br>取值范围：<br>- Ethernet（以太类型会话）<br>- IPv4（IPv4类型会话）<br>- IPv6（IPv6类型会话）<br>- IPv4v6（IPv4v6类型会话）<br>默认值：无<br>配置原则：无 |
| GROUPID | 5G LAN组ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN群组的ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是18~37。字母大小写不敏感且全局唯一。<br>默认值：无<br>配置原则：<br>GROUPID以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A-F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A-F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGLANGROUP]] · 5G LAN群组（NGLANGROUP）

## 使用实例

新增一条群组编号为“A0000001-460-003-01”，DNN为“huawei.com”，SST为1，SD为“010101”，PDU会话类型为Ethernet的5G LAN群组，执行如下命令:

```
ADD NGLANGROUP: GROUPID="A0000001-460-003-01", DNN="huawei.com", SST=1, SD="010101", PDUSESSIONTYPE=Ethernet;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NGLANGROUP.md`
