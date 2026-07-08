---
id: UNC@20.15.2@MMLCommand@ADD FLOWFILTER
type: MMLCommand
name: ADD FLOWFILTER（增加流过滤器）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: FLOWFILTER
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 100000
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务过滤器
- 流过滤器
status: active
---

# ADD FLOWFILTER（增加流过滤器）

## 功能

**适用NF：PGW-C、SMF**

该命令用于添加流过滤器。主要有两个用途：

UL CL分流场景下，在会话相关流程中，SMF会将流过滤器下发给UPF，UPF基于流过滤器执行相应的数据转发动作。ADC场景下，用于匹配PCF下发的ADC规则中的AppId，若匹配成功则将该ADC规则下发给UPF，指示UPF进行应用检测（详情参见WSFD-109102 ADC基本功能）。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100000。当配置记录数大于规格的98%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格95%时，恢复“ALM-135602215 配置数量超阈值”告警。阈值可以通过MOD CFGTHRESHOLD命令修改。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置“流过滤器名称”， 该参数可供RULE命令中的“流过滤器名称”参数引用。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：此配置参数对应UPF上配置的ADD FLOWFILTERGRP命令里的参数“流过滤器组名称”或ADD FLOWFILTER命令里的参数“流过滤器名称”，SMF和UPF上配置的此参数需要协商保持一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FLOWFILTER]] · 流过滤器（FLOWFILTER）

## 使用实例

假设运营商需要增加流过滤器，指定流过滤器名称：“FLOWFILTERNAME”为“testflowfiltername”：

```
ADD FLOWFILTER:FLOWFILTERNAME="testflowfiltername";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-FLOWFILTER.md`
