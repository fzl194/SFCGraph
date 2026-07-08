---
id: UNC@20.15.2@MMLCommand@RMV LADN
type: MMLCommand
name: RMV LADN（删除本地数据网络）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LADN
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- AMF
- 本地数据网络管理
status: active
---

# RMV LADN（删除本地数据网络）

## 功能

**适用NF：AMF**

该命令用于删除本地数据网络，或者本地数据网络的某部分区域。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本地数据网络。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| BGNTAI | 跟踪区标识起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本地数据网络（LADN）的生效区域范围。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~12。TAI由MCC、MNC和TAC组成。MCC为3位数字，MNC为2个或者3位数字，填写时请遵循实际长度。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LADN]] · 本地数据网络（LADN）

## 使用实例

删除一个DNN为huawei.com，BGNTAI为12303121201的LADN信息：

```
RMV LADN: DNN="huawei.com", BGNTAI="12303121201";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-LADN.md`
