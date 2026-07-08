---
id: UNC@20.15.2@MMLCommand@MOD PCRFGRPBNDAPN
type: MMLCommand
name: MOD PCRFGRPBNDAPN（修改APN和Pcrf组关联关系）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PCRFGRPBNDAPN
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- PCRF组绑定APN
status: active
---

# MOD PCRFGRPBNDAPN（修改APN和Pcrf组关联关系）

## 功能

**适用NF：PGW-C、GGSN**

此命令用来修改APN和Pcrf组关联关系。当修改APN与PCRF组的绑定关系时，已经建立的IP-CAN Session状态不受影响，但新建立的IP-CAN Session会按更新后的绑定关系进行关联PCRF的选取。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| DEFAULTFLAG | 缺省标记 | 可选必选说明：必选参数<br>参数含义：该参数用于指定缺省标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DEFAULT<br>- IMSI_MSISDN_SEG<br>默认值：无<br>配置原则：<br>- DEFAULT：表示配置缺省号段。<br>- IMSI_MSISDN_SEG：表示配置有IMSI/MSISDN号段。 |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DEFAULTFLAG”配置为“IMSI_MSISDN_SEG”时为必选参数。<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD IMSIMSISDNSEG命令配置生成。 |
| PRIORITY | 优先级 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DEFAULTFLAG”配置为“IMSI_MSISDN_SEG”时为必选参数。<br>参数含义：该参数用于指定优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。优先级唯一。<br>默认值：无<br>配置原则：无 |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD PCRFGROUP命令配置生成。 |
| DESCRIPTION | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于配置号段绑定PCRF组的描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN和Pcrf组关联关系（PCRFGRPBNDAPN）](configobject/UNC/20.15.2/PCRFGRPBNDAPN.md)

## 使用实例

修改APN和Pcrf组关联关系，APN为“aaa”，缺省标记为DEFAULT，PCRFGRPNAME为“aaa”，命令为：

```
MOD PCRFGRPBNDAPN:APN="aaa",DEFAULTFLAG=DEFAULT,PCRFGRPNAME="aaa";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN和Pcrf组关联关系（MOD-PCRFGRPBNDAPN）_09897107.md`
