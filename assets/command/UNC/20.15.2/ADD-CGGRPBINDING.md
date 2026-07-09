---
id: UNC@20.15.2@MMLCommand@ADD CGGRPBINDING
type: MMLCommand
name: ADD CGGRPBINDING（增加CG组绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CGGRPBINDING
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 2000
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG组管理
- CG组绑定
status: active
---

# ADD CGGRPBINDING（增加CG组绑定关系）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来增加离线计费模板和CG组绑定关系。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为2000。
- 该命令引用了IMSI/MSISDN号段，可能导致匹配不到号段，在全局范围内选择CG发送话单。
- 一个离线模板下最大可配置32个CG组。
- 一个离线模板下未配置IMSI/MSISDN号段组的CG组最多只能配置一个。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCTEMPLATENAME | 离线计费模板名 | 可选必选说明：必选参数<br>参数含义：指定离线计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD OFCTEMPLATE命令配置生成。 |
| CGGRPID | CG组ID | 可选必选说明：必选参数<br>参数含义：指定CG组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32。<br>默认值：无<br>配置原则：该参数使用ADD CGGROUP命令配置生成。 |
| SEGGROUPNAME | Imsi/Msisdn号码段组名称 | 可选必选说明：可选参数<br>参数含义：使用用户号段组。如果命令中配置了多个用户号段组，则根据优先级来选择CG组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD SUBSCRIBERIDSEGGRP命令配置生成。 |
| IMSIPRIORITY | Imsi/Msisdn号码段组优先级 | 可选必选说明：可选参数<br>参数含义：指定Imsi/Msisdn号码段组优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。值越小优先级越高，优先级唯一。<br>默认值：无<br>配置原则：不配置此参数时值默认为0。 |

## 操作的配置对象

- [CG组绑定关系（CGGRPBINDING）](configobject/UNC/20.15.2/CGGRPBINDING.md)

## 关联任务

- [0-00013](task/UNC/20.15.2/0-00013.md)

## 使用实例

增加CG组绑定关系（离线计费模板为ofctemplate1，CG组ID为1，号段组为seggroup1，优先级为1），命令为：

```
ADD CGGRPBINDING: OFCTEMPLATENAME="ofctemplate1", CGGRPID=1, SEGGROUPNAME="seggroup1", IMSIPRIORITY=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加CG组绑定关系（ADD-CGGRPBINDING）_09896884.md`
