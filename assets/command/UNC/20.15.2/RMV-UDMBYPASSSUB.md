---
id: UNC@20.15.2@MMLCommand@RMV UDMBYPASSSUB
type: MMLCommand
name: RMV UDMBYPASSSUB（删除UDM Bypass最小签约数据配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UDMBYPASSSUB
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- UDM故障BYPASS最小签约数据配置管理
status: active
---

# RMV UDMBYPASSSUB（删除UDM Bypass最小签约数据配置）

## 功能

**适用NF：AMF**

该命令用于对指定的用户（群）删除UDM Bypass最小签约数据配置。

## 注意事项

执行本命令后，仅针对用户新流程生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置UDM Bypass最小签约数据集的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：<br>对于指定的用户（群），UDM Bypass最小签约数据集的匹配优先级从高到低依次为：“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于系统根据指定用户的IMSI前缀进行匹配，从而区分不同的用户群。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UDM Bypass最小签约数据配置（UDMBYPASSSUB）](configobject/UNC/20.15.2/UDMBYPASSSUB.md)

## 使用实例

对全网用户，删除UDM Bypass最小签约数据配置，执行如下命令：

```
RMV UDMBYPASSSUB: SUBRANGE=ALL_USER;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UDM-Bypass最小签约数据配置（RMV-UDMBYPASSSUB）_32335887.md`
