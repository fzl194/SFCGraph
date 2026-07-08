---
id: UNC@20.15.2@MMLCommand@RMV PERFDNN
type: MMLCommand
name: RMV PERFDNN（删除DNN性能统计对象）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFDNN
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# RMV PERFDNN（删除DNN性能统计对象）

## 功能

**适用NF：SMF**

该命令用于删除DNN性能统计对象。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示指定的网络切片支持的数据网络名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>确保DNN性能统计对象支持的DNN在LST APN中能够查询到。 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数表示组成Serving PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>本参数需要在ADD NGSRVPLMN中已配置。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数表示组成Serving PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>本参数需要在ADD NGSRVPLMN中已配置。 |
| SNSSAI | 网络切片 | 可选必选说明：必选参数<br>参数含义：该参数标识切片信息，由切片业务类型和切片细分标识组成。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是8~10。网络切片输入格式为SST-SD。SST输入长度范围是1~3，只允许输入十进制数字（0-9），除0之外不能以0开头，对应十进制数取值范围是0~255；SD输入长度为6，采用十六进制表示，只能由数字（0-9），字母（A-F、a-f）组成，字母大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数需要在ADD PLMNNS中已配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PERFDNN]] · DNN性能统计对象（PERFDNN）

## 使用实例

当运营商希望删除一个PERFDNN配置记录，其中DNN为"huawei.com"，PLMN为12303，网络切片为“1-010101”作为性能指标对象时，执行如下命令：

```
RMV PERFDNN: DNN="huawei.com", MCC="123", MNC="03", SNSSAI="1-010101";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PERFDNN.md`
