---
id: UNC@20.15.2@MMLCommand@ADD UPLIST4RDS
type: MMLCommand
name: ADD UPLIST4RDS（向RADIUS服务器使用的UP列表中增加UP）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UPLIST4RDS
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 3200
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- UP列表
status: active
---

# ADD UPLIST4RDS（向RADIUS服务器使用的UP列表中增加UP）

## 功能

**适用NF：PGW-C、SMF**

该命令用来增加UP到RADIUS服务器使用的UP列表，该UP列表用于根据UP选择RADIUS服务器，并向其发送RADIUS消息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为3200。当配置记录数大于规格的98%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格95%时，恢复“ALM-135602215 配置数量超阈值”告警。阈值可以通过MOD CFGTHRESHOLD命令修改。
- 每个UP列表最多绑定64个UP。
- 该命令中的UPLISTNAME被UPFRDSCLIENTIP或UPFRDSSVR绑定时，不允许对绑定在此UPLISTNAME下的UPINSTANCEID做增加和删除操作。如必须修改，请先解除UPLISTNAME与UPFRDSCLIENTIP或UPFRDSSVR的绑定，增加/删除UPLIST4RDS后再与UPFRDSCLIENTIP或UPFRDSSVR绑定。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPLISTNAME | UP列表名称 | 可选必选说明：必选参数<br>参数含义：指定UP列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。长度1到63的非空格字符串。<br>默认值：无<br>配置原则：无 |
| UPINSTANCEID | UP实例标识 | 可选必选说明：必选参数<br>参数含义：指定UP实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～36。字符串类型，输入长度范围是1~36。UpfHostName参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：该参数使用ADD PNFPROFILE命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPLIST4RDS]] · 从RADIUS服务器使用的UP列表中删除UP（UPLIST4RDS）

## 使用实例

将主机名为"up1"的UP添加到名为"uplist1"的UP列表中：

```
ADD UPLIST4RDS: UPLISTNAME="uplist1", UPINSTANCEID="up1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-UPLIST4RDS.md`
