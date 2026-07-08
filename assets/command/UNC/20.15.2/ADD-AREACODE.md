---
id: UNC@20.15.2@MMLCommand@ADD AREACODE
type: MMLCommand
name: ADD AREACODE（增加区域编码）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: AREACODE
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- 通用区域编码管理
status: active
---

# ADD AREACODE（增加区域编码）

## 功能

**适用NF：AMF**

AMF可基于运营商规划的区域做差异化控制（比如用户接入控制）。AMF配置上述“区域”分为两个步骤，首先是定义区域编码（AreaCode），其次是为已定义的区域编码添加位置成员。本命令用于在AMF上增加区域编码。

## 注意事项

- 该命令执行后立即生效。

- 本命令可用于配置与UDM对齐的全网规划的AreaCode，也可用于配置仅在AMF系统内使用的一般区域编码。如果AreaCode是全网规划的，那么AreaCode以及AreaCode内的跟踪区列表应该与周边NF（如UDM）的配置数据保持一致。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREACODE | 区域编码 | 可选必选说明：必选参数<br>参数含义：该参数用于唯一标识AMF服务的某个区域，该区域由一个或者若干个跟踪区组成。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数是对通用区域的描述信息，在运维中起到助记的作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AREACODE]] · 区域编码（AREACODE）

## 使用实例

UDM规划了一个区域，编码为“jq001.pd006.sh.mcc123.mnc45”，并用于签约数据；AMF也需要同步配置该区域，执行如下命令：

```
ADD AREACODE: AREACODE="jq001.pd006.sh.mcc123.mnc45", DESC="for zone1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加区域编码（ADD-AREACODE）_44006351.md`
