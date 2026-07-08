---
id: UNC@20.15.2@MMLCommand@RMV SMFPDUREACT
type: MMLCommand
name: RMV SMFPDUREACT（删除跨区域PDU会话重建策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMFPDUREACT
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 跨区域PDU会话管理
- 跨区域PDU会话重建
status: active
---

# RMV SMFPDUREACT（删除跨区域PDU会话重建策略）

## 功能

**适用NF：SMF**

该命令用于删除一条跨区域PDU会话重建策略。

## 注意事项

- 该命令执行后立即生效。

- 执行删除命令不配置SD时，默认删除SD值为“FFFFFF”的记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | DNN | 可选必选说明：必选参数<br>参数含义：该参数用于指定跨区域PDU会话重建的DNN，即用户请求的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ISNSSAI | 是否匹配S-NSSAI | 可选必选说明：必选参数<br>参数含义：该参数用于表示跨区域PDU会话重建时是否匹配S-NSSAI。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无<br>配置原则：<br>如果运营商期望根据S-NSSAI和DNN的方式选择需要重建的PDU会话，则设置为“YES”；如果运营商期望仅根据DNN选择需要重建的PDU会话，则设置为“NO”。 |
| SST | 切片业务类型 | 可选必选说明：该参数在"ISNSSAI"配置为"YES"时为条件必选参数。<br>参数含义：该参数用于表示跨区域PDU会话重建时的网络切片业务类型。网络切片标识（S-NSSAI）由切片业务类型（SST）和切片细分标识（SD）两部分组成，其中切片细分标识是可选的。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：该参数在"ISNSSAI"配置为"YES"时为条件可选参数。<br>参数含义：该参数用于表示跨区域PDU会话重建时的网络切片细分标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFPDUREACT]] · 跨区域PDU会话重建策略（SMFPDUREACT）

## 使用实例

删除一条“DNN”为IMS的跨区域PDU会话重建策略：

```
RMV SMFPDUREACT: DNN="IMS",ISNSSAI=NO;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SMFPDUREACT.md`
