---
id: UNC@20.15.2@MMLCommand@ADD LOCALAPNNIGP
type: MMLCommand
name: ADD LOCALAPNNIGP（增加本地APNNI组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LOCALAPNNIGP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 本地APNNI组管理
status: active
---

# ADD LOCALAPNNIGP（增加本地APNNI组）

## 功能

**适用网元：SGSN**

该命令用于增加本地APNNI组信息。定制APN纠正功能会引用该配置参数APNNIGRPID，可参考 **[ADD SMACTCTRL](../激活过程管理/增加激活过程控制参数（ADD SMACTCTRL）_26305472.md)** 命令的APNNIGRPID参数说明。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为128。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNIGRPID | 本地APNNI组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本地APNNI组号。<br>数据来源：本端规划取值范围：0～127<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用来指定APNNI信息。<br>数据来源：本端规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。<br>- 同一组内APNNI不能相同。 |
| PRI | APNNI优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用一个组内APNNI的优先级。<br>数据来源：本端规划<br>取值范围：0～127<br>默认值：无<br>配置原则：<br>- 数值越小，优先级越高。<br>- 同一组内APNNI的优先级值不能相同。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LOCALAPNNIGP]] · 本地APNNI组（LOCALAPNNIGP）

## 使用实例

运营商希望部署定制APN纠正功能时，配置一个本地APNNI组，组号为“1”，组内包含的APNNI按照优先级从高到低顺序依次为"HUAWEI1.COM"，"HUAWEI2.COM"，"HUAWEI3.COM"。

```
ADD LOCALAPNNIGP: APNNIGRPID=1, APNNI="HUAWEI1.COM",PRI=0;
ADD LOCALAPNNIGP: APNNIGRPID=1, APNNI="HUAWEI2.COM",PRI=1;
ADD LOCALAPNNIGP: APNNIGRPID=1, APNNI="HUAWEI3.COM",PRI=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-LOCALAPNNIGP.md`
