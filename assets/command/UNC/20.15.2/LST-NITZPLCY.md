---
id: UNC@20.15.2@MMLCommand@LST NITZPLCY
type: MMLCommand
name: LST NITZPLCY（查询NITZ策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NITZPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NITZ管理
- NITZ策略管理
status: active
---

# LST NITZPLCY（查询NITZ策略）

## 功能

**适用NF：AMF**

该命令用于查询当前配置的NITZ策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREARANGE | 区域范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定AMF服务的某些区域范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_AREA（所有区域）”：所有区域<br>- “AREA_CODE（指定区域编码）”：指定区域编码<br>默认值：无<br>配置原则：无 |
| AREACODE | 区域编码 | 可选必选说明：该参数在"AREARANGE"配置为"AREA_CODE"时为条件可选参数。<br>参数含义：该参数用于唯一标识AMF服务的某个区域，该区域由一个或者若干个跟踪区组成。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。该区域编码必须已经通过ADD AREACODE命令添加成功，可执行LST AREACODE进行查看，区域编码中的成员由ADD AREAMEM添加。<br>默认值：无<br>配置原则：无 |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于表示应用NITZ策略的用户群标识。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “USER_GROUP（用户群）”：用户群<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定应用NITZ策略的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| USRGRPID | 用户群组标识 | 可选必选说明：该参数在"SUBRANGE"配置为"USER_GROUP"时为条件可选参数。<br>参数含义：该参数用于指定应用NITZ策略的用户群标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。该用户群标识必须已经通过ADD NGUSRGRP命令添加成功，可执行LST NGUSRGRP进行查看，用户群中的用户可通过ADD NGUSRGRPMEM添加。<br>默认值：无<br>配置原则：<br>当USRGRPID未输入取值时，系统会为此参数赋无效值4294967295(0xFFFFFFFF)。 |

## 操作的配置对象

- [NITZ策略（NITZPLCY）](configobject/UNC/20.15.2/NITZPLCY.md)

## 使用实例

- 查询系统中当前配置的NITZ策略，执行如下命令：
  ```
  %%LST NITZPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
           区域范围  =  指定区域编码
           区域编码  =  SomeCity
           用户范围  =  所有用户
           IMSI前缀  =  NULL
       用户群组标识  =  4294967295
         运营商全称  =  ABC
         运营商简称  =  abc
           描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中当前配置“区域范围”为“指定区域编码”且“区域编码”为“Jinqiao_Industrial_Park”的NITZ策略，执行如下命令：
  ```
  %%LST NITZPLCY: AREARANGE=AREA_CODE, AREACODE="Jinqiao_Industrial_Park";%%
  RETCODE = 0  操作成功

  结果如下
  --------
           区域范围  =  指定区域编码
           区域编码  =  Jinqiao_Industrial_Park
           用户范围  =  所有用户
           IMSI前缀  =  NULL
       用户群组标识  =  4294967295
         运营商全称  =  ABC
         运营商简称  =  abc
           描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NITZ策略（LST-NITZPLCY）_09653785.md`
