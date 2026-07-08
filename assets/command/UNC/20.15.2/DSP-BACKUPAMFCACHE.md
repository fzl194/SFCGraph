---
id: UNC@20.15.2@MMLCommand@DSP BACKUPAMFCACHE
type: MMLCommand
name: DSP BACKUPAMFCACHE（显示缓存的备用AMF信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BACKUPAMFCACHE
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- 备用AMF缓存策略管理
status: active
---

# DSP BACKUPAMFCACHE（显示缓存的备用AMF信息）

## 功能

**适用NF：AMF**

该命令用于查询AMF缓存的备用AMF信息。

当AMF热备功能开启且AMF以3gpp-Sbi-Binding头域的形式向周边NF携带备用AMF信息时（通过SET AMFRESTOFUNC命令开启），AMF才会服务发现并缓存备用AMF的信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定备用AMF缓存信息的查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “QUERYALL（查询所有GUAMI）”：查询所有GUAMI的备用AMF缓存信息。<br>- “SPECIFIC_GUAMI（指定GUAMI）”：查询指定GUAMI的备用AMF缓存信息。<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定AMF上缓存备用AMF信息的POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：<br>该参数可通过执行DSP POD命令指定POD类型（usn-pod）获取POD名称。 |
| MCC | 移动国家码 | 可选必选说明：该参数在"QUERYTYPE"配置为"SPECIFIC_GUAMI"时为条件必选参数。<br>参数含义：该参数用于指定GUAMI中的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：该参数在"QUERYTYPE"配置为"SPECIFIC_GUAMI"时为条件必选参数。<br>参数含义：该参数用于指定GUAMI中的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| AMFREGIONID | AMF区域标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"SPECIFIC_GUAMI"时为条件必选参数。<br>参数含义：该参数用于指定GUAMI中的AMF所在区域的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| AMFSETID | AMF集合标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"SPECIFIC_GUAMI"时为条件必选参数。<br>参数含义：该参数用于指定GUAMI中的AMF所在集合（即Pool）的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成，且第一个字符只能是数字0-3。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| AMFPOINTER | AMF指示符 | 可选必选说明：该参数在"QUERYTYPE"配置为"SPECIFIC_GUAMI"时为条件必选参数。<br>参数含义：该参数用于指定GUAMI中的AMF指示符信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成，且第一个字符只能是数字0-3。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [缓存的备用AMF信息（BACKUPAMFCACHE）](configobject/UNC/20.15.2/BACKUPAMFCACHE.md)

## 使用实例

查询AMF上缓存的所有备用AMF信息：

```
%%DSP BACKUPAMFCACHE:QUERYTYPE=QUERYALL;%%
RETCODE = 0  操作成功

结果如下
------------------------
      POD名称  =  usn-pod-0
备份AMF实例ID  =  00000000-0000-0000-0000-000000000021
   移动国家码  =  460
     移动网号  =  03
  AMF区域标识  =  10
  AMF集合标识  =  280
    AMF指示符  =  01
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示缓存的备用AMF信息（DSP-BACKUPAMFCACHE）_83021417.md`
