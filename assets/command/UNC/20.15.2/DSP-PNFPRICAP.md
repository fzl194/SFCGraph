---
id: UNC@20.15.2@MMLCommand@DSP PNFPRICAP
type: MMLCommand
name: DSP PNFPRICAP（显示UPF优先级和权重）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PNFPRICAP
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF实例优先级权重信息管理
status: active
---

# DSP PNFPRICAP（显示UPF优先级和权重）

## 功能

**适用NF：SMF**

该命令用于查询对端UPF实例优先级与权重。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询方式。<br>数据来源：本端规划<br>取值范围：<br>- TAI（TAI）<br>- SMFSERVINGAREA（SMFSERVINGAREA）<br>- DNNANDDNAI（DNNANDDNAI）<br>默认值：无<br>配置原则：无 |
| NS | 切片 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF的切片。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~10。输入sst和sd，以-作为连接符。sst范围为0~255，sd为六位十六进制数。<br>默认值：无<br>配置原则：无 |
| TAI | 跟踪区标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"TAI"时为条件必选参数。<br>参数含义：该参数用于指定跟踪区标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>5G TAI : 输入长度范围是11~12。后6位为16进制数，其余为10进制数。<br>4G TAI：输入长度范围是9~10。后4位为16进制数，其余为10进制数。 |
| SMFSERVINGAREA | SMF服务区域 | 可选必选说明：该参数在"QUERYTYPE"配置为"SMFSERVINGAREA"时为条件必选参数。<br>参数含义：该参数用于指定UPF为SMF提供的服务区域。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写。<br>默认值：无<br>配置原则：无 |
| DNN | 数据网络名称 | 可选必选说明：该参数在"QUERYTYPE"配置为"DNNANDDNAI"时为条件必选参数。<br>参数含义：该参数用于指定对端NF实例支持的数据网络名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~66。不区分大小写。<br>默认值：无<br>配置原则：无 |
| DNAI | 数据网络访问标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"DNNANDDNAI"时为条件可选参数。<br>参数含义：该参数用于指定对端NF实例支持的数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFPRICAP]] · UPF优先级和权重（PNFPRICAP）

## 使用实例

查询对端UPF实例优先级与权重。

```
DSP PNFPRICAP: QUERYTYPE=TAI, TAI="FFFFFF",NS="255-19CDE0"
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示UPF优先级和权重（DSP-PNFPRICAP）_71516429.md`
