---
id: UNC@20.15.2@MMLCommand@LST PCSCFIMSISDNSEG
type: MMLCommand
name: LST PCSCFIMSISDNSEG（查询IMSI和MSISDN号段）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCSCFIMSISDNSEG
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- IMS管理
- P-CSCF管理
- P-CSCF选择的IMSI和MSISDN号段
status: active
---

# LST PCSCFIMSISDNSEG（查询IMSI和MSISDN号段）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询IMSI/MSISDN号码段。

## 注意事项

当需要输入的通配号段字符串带有？时需要用%3f转义，为防止导出后再导入失败，LST IMSIMSISDNSEG显示时会显示成%3f而不是？。ADD的参数IMSIWILDCARD允许输入？，所以在LST时要求显示为%3f。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCSCFIMSISDNSEG]] · IMSI和MSISDN号段（PCSCFIMSISDNSEG）

## 使用实例

查询所有IMSI和MSISDN号段：

```
LST PCSCFIMSISDNSEG:;
RETCODE = 0  操作成功

结果如下
--------------------
IMSI/MSISDN号段名称 IMSI/MSISDN号段类型 号段起始字符串 号段结束字符串 通配号段字符串 锁定IMSIMSISDN号段

huawei              IMSI                1              2              NULL           不使能
huawei1             IMSI                10             20             NULL           不使能
(结果个数 = 2)

--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PCSCFIMSISDNSEG.md`
