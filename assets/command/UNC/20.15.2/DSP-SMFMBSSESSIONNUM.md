---
id: UNC@20.15.2@MMLCommand@DSP SMFMBSSESSIONNUM
type: MMLCommand
name: DSP SMFMBSSESSIONNUM（显示MB-SMF组播广播会话数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMFMBSSESSIONNUM
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G组播广播管理
- MB-SMF组播广播管理
- 显示MB-SMF组播广播会话数
status: active
---

# DSP SMFMBSSESSIONNUM（显示MB-SMF组播广播会话数）

## 功能

**适用NF：SMF**

该命令用于显示MB-SMF组播广播会话数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYSCOPE | 查询范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询会话上下文的范围。<br>数据来源：本端规划<br>取值范围：<br>- “SUMMARY（汇总信息）”：查询汇总信息。以汇总方式呈现。<br>- “ALL_POD_INFO（所有POD信息）”：查询所有POD信息。以POD粒度呈现。<br>- “SPECIFIED_POD_INFO（指定POD信息）”：查询指定POD信息。<br>默认值：无<br>配置原则：无 |
| POD_ID | POD名称 | 可选必选说明：该参数在"QUERYSCOPE"配置为"SPECIFIED_POD_INFO"时为条件必选参数。<br>参数含义：该参数用于指定需要查询会话上下文数的POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFMBSSESSIONNUM]] · MB-SMF组播广播会话数（SMFMBSSESSIONNUM）

## 使用实例

当希望查询整系统的MBS组播广播会话数时，使用如下命令：

```
%%DSP SMFMBSSESSIONNUM: QUERYSCOPE=SUMMARY;%%
RETCODE = 0  操作成功

结果如下
--------
MBS会话数  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示MB-SMF组播广播会话数（DSP-SMFMBSSESSIONNUM）_32772569.md`
