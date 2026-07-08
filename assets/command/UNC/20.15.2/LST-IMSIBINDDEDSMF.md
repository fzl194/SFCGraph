---
id: UNC@20.15.2@MMLCommand@LST IMSIBINDDEDSMF
type: MMLCommand
name: LST IMSIBINDDEDSMF（查询拨测用户和专网SMF的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSIBINDDEDSMF
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 本地分流管理
- 专网SMF拨测管理
status: active
---

# LST IMSIBINDDEDSMF（查询拨测用户和专网SMF的绑定关系）

## 功能

**适用NF：SMF、PGW-C**

该命令用于查询拨测用户和专网SMF的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：本参数用于指定用户IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是6~15。每个字符只能是十进制数字。<br>默认值：无<br>配置原则：<br>该参数不支持号段前缀匹配。 |
| DEDDNN | 专用DNN | 可选必选说明：可选参数<br>参数含义：该参数指定专用DNN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| DEDSMFINSTID | 专网SMF实例标识 | 可选必选说明：可选参数<br>参数含义：本参数用于指定专网SMF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，大小写敏感。<br>默认值：无<br>配置原则：<br>该参数来源于对端设备LST NFUUID查询结果中的NF Instance ID。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSIBINDDEDSMF]] · 拨测用户和专网SMF的绑定关系（IMSIBINDDEDSMF）

## 使用实例

查询IMSI是"123456789012345"，DEDDNN是"testDNN"的用户激活到DEDSMFINSTID是“testSmfInstanceId”的SMF的配置

```
LST IMSIBINDDEDSMF:IMSI="123456789012345",DEDDNN="testDNN";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IMSIBINDDEDSMF.md`
