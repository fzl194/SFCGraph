---
id: UNC@20.15.2@MMLCommand@MOD OCSGRPBINDING
type: MMLCommand
name: MOD OCSGRPBINDING（修改OCS组绑定关系）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: OCSGRPBINDING
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- OCS Diameter连接
- 绑定OCS Group到DCC模板
status: active
---

# MOD OCSGRPBINDING（修改OCS组绑定关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用来修改OCS组绑定关系。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 修改绑定关系，可能导致在线计费用户查找不到OCS，在线计费用户可能激活失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCCTMPLTNAME | DCC模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定操作的DCC在线计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：该参数使用ADD DCCTEMPLATE命令配置生成。 |
| PRIORSEC | 主备用标记 | 可选必选说明：必选参数<br>参数含义：该参数用于指定OCS组的主备标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PRIMARY：表示该服务器是主用服务器。<br>- SECONDARY：表示该服务器是备用服务器。<br>默认值：无<br>配置原则：无 |
| OCSGRPNAME | OCS组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定OCS组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD OCSGROUP命令配置生成。 |
| SEGGROUPNAME | IMSI/MSISDN号码段组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户号段组。如果同一个DCC模板配置了多个用户号段组，则根据优先级来选择OCS组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：无 |
| IMSIPRIORITY | IMSI/MSISDN号码段组优先级 | 可选必选说明：可选参数<br>参数含义：指定IMSI/MSISDN号码段组优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。值越小优先级越高，取值优先级唯一。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OCSGRPBINDING]] · OCS组绑定关系（OCSGRPBINDING）

## 使用实例

修改OCS组绑定关系（DCC模板为dcc1，OCS组为ocsgroup1，号段组为“seggroup1”）的优先级为2，命令为：

```
MOD OCSGRPBINDING: DCCTMPLTNAME="dcc1", PRIORSEC=PRIMARY, OCSGRPNAME="ocsgroup1", SEGGROUPNAME="seggroup1", IMSIPRIORITY=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改OCS组绑定关系（MOD-OCSGRPBINDING）_09896976.md`
