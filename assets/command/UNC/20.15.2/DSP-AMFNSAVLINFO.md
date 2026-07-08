---
id: UNC@20.15.2@MMLCommand@DSP AMFNSAVLINFO
type: MMLCommand
name: DSP AMFNSAVLINFO（显示授权后的网络切片可用性信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: AMFNSAVLINFO
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 网络切片选择管理
- 网络切片可用性信息查询
status: active
---

# DSP AMFNSAVLINFO（显示授权后的网络切片可用性信息）

## 功能

**适用NF：AMF**

该命令用于查询AMF上授权后的网络切片可用性信息或无线侧单独上报的切片信息。所谓“授权后”的网络切片可用性信息即AMF通过NSSF获取的各跟踪区所支持网络切片信息。切片获取的数据源可以通过SET NSSELPARA命令中的CAMPUSNSSRC进行设置。

## 注意事项

本命令仅支持查询指定跟踪区（TA）的网络切片可用性信息，不支持一次性查询AMF整系统的TA的网络切片可用性信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAI | TAI | 可选必选说明：必选参数<br>参数含义：该参数用于指定待查询网络切片可用性信息的跟踪区标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是11~12。TAI由MCC、MNC和TAC组成。MCC为3位十进制数字，MNC为2位或者3位十进制数字，填写时请遵循实际长度。TAC编码为十六进制数，长度固定为6位；若不足则左起用0补足6位。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [授权后的网络切片可用性信息（AMFNSAVLINFO）](configobject/UNC/20.15.2/AMFNSAVLINFO.md)

## 使用实例

TAI1（460018A0001）和TAI2（460018A0002）配置在相同的TAList（ADD NGTALST）中，实测发现AMF给TAI1中的UE分配的TA List没有包含TAI2，执行如下命令检查TAI1和TAI2支持的网络切片是否存在差异：

```
DSP AMFNSAVLINFO: TAI="460018A0001";
2.DSP AMFNSAVLINFO: TAI="460018A0002";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示授权后的网络切片可用性信息（DSP-AMFNSAVLINFO）_28567623.md`
