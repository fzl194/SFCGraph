---
id: UNC@20.15.2@MMLCommand@DSP TALISTNGRANINFO
type: MMLCommand
name: DSP TALISTNGRANINFO（显示TALIST下5G基站接入数量信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TALISTNGRANINFO
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGRAN接入管理控制
status: active
---

# DSP TALISTNGRANINFO（显示TALIST下5G基站接入数量信息）

## 功能

**适用NF：AMF**

该命令用于查询TALIST下5G基站接入数量信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TALIST下基站信息查询的范围。<br>数据来源：本端规划<br>取值范围：<br>- “QUERYALL（全量查询）”：查询所有TALIST下接入的基站数量<br>- “OVERLOAD（过载查询）”：查询所有过载TALIST下接入的基站数量<br>- “SPECIFIEDTAI（指定TAI）”：查询指定TAI的基站接入数量<br>默认值：无<br>配置原则：无 |
| TAI | 跟踪区标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"SPECIFIEDTAI"时为条件必选参数。<br>参数含义：该参数表示NG-RAN基站支持的跟踪区信息。跟踪区标识由PLMN ID和TAC组成。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是11~12。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [TALIST下5G基站接入数量信息（TALISTNGRANINFO）](configobject/UNC/20.15.2/TALISTNGRANINFO.md)

## 使用实例

查询所有TALIST下5G基站接入数量信息，执行如下命令：

```
%%DSP TALISTNGRANINFO:;%%
RETCODE = 0  操作成功

操作结果如下
--------------
跟踪区列表标识 跟踪区标识       基站数目
1              total            200
1              46001000101      150
1              46001000102      50
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示TALIST下5G基站接入数量信息（DSP-TALISTNGRANINFO）_62657154.md`
