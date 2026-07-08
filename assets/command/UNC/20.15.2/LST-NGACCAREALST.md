---
id: UNC@20.15.2@MMLCommand@LST NGACCAREALST
type: MMLCommand
name: LST NGACCAREALST（查询5G接入限制区域列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGACCAREALST
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 接入限制
- 5G接入限制区域管理
status: active
---

# LST NGACCAREALST（查询5G接入限制区域列表）

## 功能

**适用NF：AMF**

该命令用于查询5G接入限制区域信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREARANGE | 区域范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用接入限制的区域范围：所有区域或者指定区域。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_AREA（所有区域）”：所有区域<br>- “AREA_CODE（指定区域编码）”：指定区域编码<br>默认值：无<br>配置原则：无 |
| AREACODE | 区域编码 | 可选必选说明：该参数在"AREARANGE"配置为"AREA_CODE"时为条件可选参数。<br>参数含义：该参数用于指定应用接入限制的某个区域。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。该区域编码必须先通过ADD AREACODE进行添加；而区域内的跟踪区列表则通过ADD AREAMEM进行添加。<br>默认值：无<br>配置原则：无 |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用接入限制的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “USER_GROUP（用户群）”：用户群<br>- “SPECIAL_USER_RANGE（指定IMSI范围）”：指定IMSI范围。<br>- “MSISDN_PREFIX（MSISDN前缀）”：MSISDN前缀。<br>默认值：无<br>配置原则：无 |
| SUBGRPID | 用户群组标识 | 可选必选说明：该参数在"SUBRANGE"配置为"USER_GROUP"时为条件可选参数。<br>参数含义：该参数用于指定应用接入限制的用户群组。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。该用户群组标识通过ADD NGUSRGRP进行添加；群组内的用户标识列表通过ADD NGUSRGRPMEM进行添加。<br>默认值：无<br>配置原则：<br>当针对指定的区域，有多个用户（号段）需要做接入限制时，建议通过本参数指定用户范围。 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIAL_USER_RANGE"时为条件可选参数。<br>参数含义：该参数表示需要查询的IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"MSISDN_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定用户的MSISDN前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G接入限制区域列表（NGACCAREALST）](configobject/UNC/20.15.2/NGACCAREALST.md)

## 使用实例

- 查询系统中当前配置的5G接入限制区域信息，执行如下命令：
  ```
  %%LST NGACCAREALST:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
          区域范围  =  指定区域编码
          区域编码  =  SH_5G_TRIAL_NETWORK
          控制模式  =  白名单
        拒绝原因值  =  15
          用户范围  =  所有用户
      用户群组标识  =  4294967295
    添加IMSI的方式  =  添加IMSI
          起始IMSI  =  NULL
          终止IMSI  =  NULL
        MSISDN前缀  =  NULL
          描述信息  =  NULL
  (结果个数  = 1)

  ---    END
  ```
- 查询系统中当前配置“区域范围”为“指定区域编码”且“区域编码”为“Jinqiao_Industrial_Park”的5G接入限制区域信息，执行如下命令：
  ```
  %%LST NGACCAREALST: AREARANGE=AREA_CODE, AREACODE="Jinqiao_Industrial_Park";%%
  RETCODE = 0  操作成功

  结果如下
  --------
          区域范围  =  指定区域编码
          区域编码  =  Jinqiao_Industrial_Park
          控制模式  =  白名单
        拒绝原因值  =  15
          用户范围  =  用户群
      用户群组标识  =  888
    添加IMSI的方式  =  添加IMSI
          起始IMSI  =  NULL
          终止IMSI  =  NULL
        MSISDN前缀  =  NULL
          描述信息  =  for employees
  (结果个数  = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G接入限制区域列表（LST-NGACCAREALST）_44006984.md`
