---
id: UNC@20.15.2@MMLCommand@ADD AMFRESELPLCY
type: MMLCommand
name: ADD AMFRESELPLCY（增加AMF重选控制策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: AMFRESELPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF区域重选功能管理
- AMF重选控制策略
status: active
---

# ADD AMFRESELPLCY（增加AMF重选控制策略）

## 功能

**适用NF：AMF**

该命令用于增加AMF重选功能控制策略。AMF可基于用户的号段，控制在用户新接入AMF时，是否需要将用户通过重定向方式重选至指定的AMF。

在特性新开通等场景，只在特定AMF试开通，Pool内其他AMF可通过本命令将指定的开通用户重选到特性AMF上。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 最多可输入16条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBGRPID | 用户群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用AMF重选功能的用户群组。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。该用户群组标识通过ADD NGUSRGRP进行添加。<br>默认值：无<br>配置原则：无 |
| AMFINSTANCEID | AMF实例标识 | 可选必选说明：必选参数<br>参数含义：本参数用于指定重定向目标AMF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：<br>该参数来源于重定向目标AMF配置的NF实例标识。华为AMF可以通过LST NFUUID命令查询NF实例标识参数的取值。 |

## 操作的配置对象

- [AMF重选控制策略（AMFRESELPLCY）](configobject/UNC/20.15.2/AMFRESELPLCY.md)

## 使用实例

指定用户群组1的用户接入时，重定向到AMF（AMF实例标识为“AMF-INSTANCEID-1”），执行命令如下：

```
ADD AMFRESELPLCY: SUBGRPID=1, AMFINSTANCEID="AMF-INSTANCEID-1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加AMF重选控制策略（ADD-AMFRESELPLCY）_98333328.md`
