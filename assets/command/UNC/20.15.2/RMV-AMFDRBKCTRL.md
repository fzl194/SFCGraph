---
id: UNC@20.15.2@MMLCommand@RMV AMFDRBKCTRL
type: MMLCommand
name: RMV AMFDRBKCTRL（删除AMF热备容灾的控制参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AMFDRBKCTRL
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF热备容灾管理
status: active
---

# RMV AMFDRBKCTRL（删除AMF热备容灾的控制参数）

## 功能

**适用NF：AMF**

该命令用于删除AMF热备容灾的控制参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定热备容灾的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：IMSI前缀<br>- “MSISDN_PREFIX（MSISDN前缀）”：MSISDN前缀<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定热备容灾用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"MSISDN_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定热备容灾用户的MSISDN前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| FEATURECOND | 特征条件组合 | 可选必选说明：必选参数<br>参数含义：该参数用于指示特征条件的组合。<br>数据来源：本端规划<br>取值范围：<br>- “NONE（不指定特征条件）”：不指定特征条件。<br>- “DNN（仅指定DNN条件）”：仅指定DNN条件。<br>- “NSSAI（仅指定切片条件）”：仅指定切片条件。<br>- “DNN_NSSAI（仅指定DNN和切片条件）”：仅指定DNN和切片条件。<br>默认值：无<br>配置原则：无 |
| DNN | 数据网络名称 | 可选必选说明：该参数在"FEATURECOND"配置为"DNN"、"DNN_NSSAI"时为条件必选参数。<br>参数含义：该参数用于指定热备容灾用户的DNN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数来源于用户签约数据。 |
| SST | 切片业务类型 | 可选必选说明：该参数在"FEATURECOND"配置为"NSSAI"、"DNN_NSSAI"时为条件必选参数。<br>参数含义：该参数用于指定应用热备容灾功能的切片业务类型特征。如eMBB（1）、URLLC（2）、MIoT（3）等协议定义的标准SST，或者运营商自定义的SST。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。只允许输入十进制数字（0-9），除0之外不能以0开头。对应十进制数取值范围是0~255。<br>默认值：无<br>配置原则：<br>该参数来源于用户签约数据。 |
| SD | 切片细分标识 | 可选必选说明：该参数在"FEATURECOND"配置为"NSSAI"、"DNN_NSSAI"时为条件必选参数。<br>参数含义：该参数用于指定应用热备容灾功能的切片细分标识特征。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~6。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>该参数在"FEATURECOND"配置为"NONE"、"DNN"时，值为"FFFFFF"。 |

## 操作的配置对象

- [AMF热备容灾控制参数（AMFDRBKCTRL）](configobject/UNC/20.15.2/AMFDRBKCTRL.md)

## 使用实例

删除AMF热备容灾控制参数，执行如下命令：

```
RMV AMFDRBKCTRL: SUBRANGE=ALL_USER, FEATURECOND=DNN_NSSAI, DNN="huawei.com", SST=0, SD="010101";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除AMF热备容灾的控制参数（RMV-AMFDRBKCTRL）_61467250.md`
