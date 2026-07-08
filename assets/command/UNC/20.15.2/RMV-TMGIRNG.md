---
id: UNC@20.15.2@MMLCommand@RMV TMGIRNG
type: MMLCommand
name: RMV TMGIRNG（删除TMGI号段）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TMGIRNG
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G组播广播管理
- MB-SMF组播广播管理
- MB-SMF TMGI配置管理
status: active
---

# RMV TMGIRNG（删除TMGI号段）

## 功能

**适用NF：SMF**

该命令用来删除TMGI号段。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。仅支持0-9的数字，所有配置下仅支持同一个MCC、MNC组合。<br>默认值：无<br>配置原则：<br>配置时应与基站支持的MCC保持一致。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。仅支持0-9的数字，所有配置下仅支持同一个MCC、MNC组合。<br>默认值：无<br>配置原则：<br>配置时应与基站支持的MNC保持一致。 |
| MBSIDRNGSTART | MBS Service ID区域起点值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定组播广播服务标识区域起点值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是8。字符串类型，长度为8位。 必须是0x/X开头的十六进制数，仅支持输入0x/X、0-9、a-f/A-F，字母不区分大小写，取值范围0x000000~0xFFFFFF。<br>默认值：无<br>配置原则：<br>MBSIDRNGSTART一定要小于等于MBSIDRNGEND。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TMGIRNG]] · TMGI号段（TMGIRNG）

## 使用实例

当需要删除MCC为460，MNC为03，MBSSERVICEIDSTART为0x000001的TMGI段时，执行如下命令：

```
RMV TMGIRNG: MCC="460", MNC="03", MBSIDRNGSTART="0x000001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-TMGIRNG.md`
