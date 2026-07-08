---
id: UNC@20.15.2@MMLCommand@MOD SGWSEGGCHGMETH
type: MMLCommand
name: MOD SGWSEGGCHGMETH（修改SGW IMSI/MSISDN Group Charge Method）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SGWSEGGCHGMETH
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- SGW计费控制
- SGW IMSI_MSISDN号段组计费方式
status: active
---

# MOD SGWSEGGCHGMETH（修改SGW IMSI/MSISDN Group Charge Method）

## 功能

**适用NF：SGW-C**

该命令用于修改SGW基于号段组的计费方式。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGGROUPNAME | IMSI/MSISDN号段组名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定用户号段组。如果配置了多个用户号段组，则根据优先级来选择。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：如果配置了多个用户号段组，则根据优先级来选择。 |
| PRIORITY | IMSI/MSISDN号段组优先级 | 可选必选说明：可选参数<br>参数含义：指定IMSI/MSISDN号段组优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。值越小优先级越高，优先级唯一。<br>默认值：无<br>配置原则：无 |
| OFFLINEFLAG | IMSI/MSISDN号段组离线计费开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IMSI/MSISDN号段组下的用户是否产生S-GW离线话单。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：禁止。<br>- ENABLE：允许。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：配置INHERIT表示继承基于APN的离线计费开关的配置。如果APN下离线计费开关配置为INHERIT或APN不存在，则继承基于计费属性的配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGWSEGGCHGMETH]] · SGW IMSI/MSISDN Group Charge Method（SGWSEGGCHGMETH）

## 使用实例

根据需求，将名称为“huawei”的号段组的离线计费开关修改为使能，优先级修改为5，命令为：

```
MOD SGWSEGGCHGMETH: SEGGROUPNAME="huawei", PRIORITY=5, OFFLINEFLAG=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SGWSEGGCHGMETH.md`
