---
id: UNC@20.15.2@MMLCommand@CLR BACKUPAMFCACHE
type: MMLCommand
name: CLR BACKUPAMFCACHE（清除备用AMF缓存信息）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: BACKUPAMFCACHE
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- 备用AMF缓存策略管理
status: active
---

# CLR BACKUPAMFCACHE（清除备用AMF缓存信息）

## 功能

**适用NF：AMF**

该命令用于清除AMF本地缓存的备用AMF信息，清除的方式为设置老化标记位。设置老化标记位后，在下一次移动性流程中AMF会强制重新发现备用AMF信息，未服务发现之前AMF会惯性继续使用老化状态缓存的备用AMF信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLRTYPE | 清除类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定清除备用AMF缓存信息的清除类型。<br>数据来源：本端规划<br>取值范围：<br>- “CLRALL（清除所有）”：清除所有GUAMI的备用AMF缓存信息。<br>- “SPECIFIC_GUAMI（指定GUAMI）”：清除指定GUAMI的备用AMF缓存信息。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：该参数在"CLRTYPE"配置为"SPECIFIC_GUAMI"时为条件必选参数。<br>参数含义：该参数用于指定GUAMI中的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：该参数在"CLRTYPE"配置为"SPECIFIC_GUAMI"时为条件必选参数。<br>参数含义：该参数用于指定GUAMI中的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| AMFREGIONID | AMF区域标识 | 可选必选说明：该参数在"CLRTYPE"配置为"SPECIFIC_GUAMI"时为条件必选参数。<br>参数含义：该参数用于指定GUAMI中的AMF所在区域的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| AMFSETID | AMF集合标识 | 可选必选说明：该参数在"CLRTYPE"配置为"SPECIFIC_GUAMI"时为条件必选参数。<br>参数含义：该参数用于指定GUAMI中的AMF所在集合（即Pool）的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成，且第一个字符只能是数字0-3。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| AMFPOINTER | AMF指示符 | 可选必选说明：该参数在"CLRTYPE"配置为"SPECIFIC_GUAMI"时为条件必选参数。<br>参数含义：该参数用于指定GUAMI中的AMF指示符信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成，且第一个字符只能是数字0-3。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BACKUPAMFCACHE]] · 缓存的备用AMF信息（BACKUPAMFCACHE）

## 使用实例

清除本地所有GUAMI缓存的备用AMF信息，执行如下命令：

```
CLR BACKUPAMFCACHE: CLRTYPE=CLRALL;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-BACKUPAMFCACHE.md`
