---
id: UNC@20.15.2@MMLCommand@ADD PERFNSADDRPOOL
type: MMLCommand
name: ADD PERFNSADDRPOOL（增加切片地址池性能统计对象）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PERFNSADDRPOOL
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

# ADD PERFNSADDRPOOL（增加切片地址池性能统计对象）

## 功能

**适用NF：SMF**

该命令用于增加切片地址池性能统计对象，主要用于基于网络切片粒度的UE地址相关性能统计。

## 注意事项

- 该命令执行后立即生效。

- 该命令当前版本不支持。

- 最多可输入500条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定切片地址池性能统计对象的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~499。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成PLMN的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>该参数的取值必须和LST NGSRVPLMN命令查询到的MCC相同。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成PLMN的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>该参数的取值必须和LST NGSRVPLMN命令查询到的MNC相同。 |
| SST | 切片业务类型 | 可选必选说明：必选参数<br>参数含义：该参数表示切片的业务类型，如eMBB（1）、URLLC（2）、MIoT（3）等协议定义的标准SST，或者运营商自定义的SST。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~3。只允许输入十进制数字（0-9），除0之外不能以0开头。对应十进制数取值范围是0~255。<br>默认值：无<br>配置原则：<br>该参数的取值必须和LST PLMNNS命令查询到的SST相同。 |
| SD | 切片细分标识 | 可选必选说明：可选参数<br>参数含义：该参数表示根据服务群体，对某类网络业务切片的进一步细分。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>该参数的取值必须和LST PLMNNS命令查询到的SD相同。 |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定已配置的地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数的取值必须和ADD ADDRPOOL命令的POOLNAME参数相同。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFNSADDRPOOL]] · 切片地址池性能统计对象（PERFNSADDRPOOL）

## 使用实例

增加PLMN为12368，切片业务类型为eMBB，地址池为pool1的性能统计对象：

```
ADD PERFNSADDRPOOL: IDX=1, MCC="123", MNC="68", SST="1", SD="010101", POOLNAME="pool1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PERFNSADDRPOOL.md`
