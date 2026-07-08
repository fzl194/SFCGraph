---
id: UNC@20.15.2@MMLCommand@MOD BACKUPGUAMI
type: MMLCommand
name: MOD BACKUPGUAMI（修改供备GUAMI信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: BACKUPGUAMI
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- AMF
- 备用GUAMI列表管理
status: active
---

# MOD BACKUPGUAMI（修改供备GUAMI信息）

## 功能

![](修改供备GUAMI信息（MOD BACKUPGUAMI）_09653090.assets/notice_3.0-zh-cn_2.png)

执行该命令前，需要确认将本AMF用作备用AMF的GUAMI标识配置是否已同步修改，否则会导致AMF用户上下文备份失败。

**适用NF：AMF**

该命令用于修改将本AMF用作备用AMF的GUAMI信息。

## 注意事项

- 该命令执行后立即生效。

- 增加、删除或者修改本AMF提供备用功能的GUAMI信息，都会引起本AMF到NRF的注册更新。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | GUAMI索引 | 可选必选说明：必选参数<br>参数含义：该参数是将本AMF作为备用AMF的GUAMI的配置记录索引信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| BACKUPTYPE | 备用类型 | 可选必选说明：可选参数<br>参数含义：该参数表示本AMF提供备用功能的应用类型，分故障和计划性退服两种。<br>数据来源：全网规划<br>取值范围：<br>- “FAILURE（故障）”：主用AMF故障<br>- “PLANNED_REMOVAL（计划性退服）”：主用AMF从网络中计划性退服<br>默认值：无<br>配置原则：无 |
| PLMNIDX | PLMN索引 | 可选必选说明：可选参数<br>参数含义：该参数是将本AMF作为备用AMF的GUAMI的PLMN信息的索引，PLMN索引通过ADD NGSRVPLMN命令配置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |
| AMFREGIONID | AMF区域标识 | 可选必选说明：可选参数<br>参数含义：该参数是将本AMF作为备用AMF的GUAMI的区域标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| AMFSETID | AMF集合标识 | 可选必选说明：可选参数<br>参数含义：该参数是将本AMF作为备用AMF的GUAMI的集合标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成，且第一个字符只能是数字0-3。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| AMFPOINTER | AMF集合内指示符 | 可选必选说明：可选参数<br>参数含义：该参数是将本AMF作为备用AMF的GUAMI的集合内指示符。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成，且第一个字符只能是数字0-3。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数是对将本AMF作为备用AMF的GUAMI的描述信息，在运维过程中起到助记的作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [供备GUAMI信息（BACKUPGUAMI）](configobject/UNC/20.15.2/BACKUPGUAMI.md)

## 使用实例

将本AMF用作备用AMF的某个GUAMI标识做了修改，本AMF的供备GUAMI也需要同步修改，执行如下命令：

```
MOD BACKUPGUAMI: INDEX=2, BACKUPTYPE=FAILURE, PLMNIDX=0, AMFREGIONID="01", AMFSETID="322", AMFPOINTER="0a", DESC="for Shanghai AMF11";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改供备GUAMI信息（MOD-BACKUPGUAMI）_09653090.md`
