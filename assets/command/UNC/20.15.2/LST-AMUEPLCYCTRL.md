---
id: UNC@20.15.2@MMLCommand@LST AMUEPLCYCTRL
type: MMLCommand
name: LST AMUEPLCYCTRL（查询AM策略和UE策略控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMUEPLCYCTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AM策略和UE策略管理
- AM策略和UE策略控制参数
status: active
---

# LST AMUEPLCYCTRL（查询AM策略和UE策略控制参数）

## 功能

**适用NF：AMF**

该命令用于查询系统中当前配置的AM策略和UE策略的控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于表示AMF上配置AM策略和UE策略控制参数的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：IMSI前缀<br>- “MSISDN_PREFIX（MSISDN前缀）”：MSISDN前缀<br>默认值：无<br>配置原则：<br>对于指定的用户（群），策略匹配的优先级从高到低依次为：“MSISDN_PREFIX(MSISDN前缀)”、“IMSI_PREFIX(IMSI前缀)”、“HOME_USER(本网用户)”或“FOREIGN_USER(外网用户)”、“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定应用AM策略和UE策略的用户的IMSI前缀。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"MSISDN_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定应用AM策略和UE策略的用户的MSISDN前缀。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| NSGRPID | 网络切片群组标识 | 可选必选说明：该参数在"SUBRANGE"配置为"ALL_USER"时为条件可选参数。<br>参数含义：该参数用于表示AMF上配置的AM策略和UE策略控制参数应用的网络切片列表。该网络切片列表通过ADD PLCYNSGRP命令进行配置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~16。0用于表示无效的网络切片群组，即不按照网络切片对AM策略或者UE策略进行控制。<br>默认值：无<br>配置原则：<br>当运营商希望基于网络切片控制AMF是否需要向PCF建立AM、UE策略偶联时，可通过本参数关联指定的网络切片列表。 |

## 操作的配置对象

- [AM策略和UE策略控制参数（AMUEPLCYCTRL）](configobject/UNC/20.15.2/AMUEPLCYCTRL.md)

## 使用实例

- 查询系统中“用户范围”为“本网用户”的AM策略和UE策略的控制参数，执行如下命令：
  ```
  %%LST AMUEPLCYCTRL: SUBRANGE=HOME_USER;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                       用户范围  =  本网用户
                       IMSI前缀  =  NULL
                     MSISDN前缀  =  NULL
               网络切片群组标识  =  0
             是否建立AM策略偶联  =  否
             是否建立UE策略偶联  =  是
    AM策略建立/更新失败处理策略  =  去注册用户
    UE策略建立/更新失败处理策略  =  不处理异常
             AM策略终止处理策略  =  使用本地配置或签约的AM策略
             UE策略终止处理策略  =  不处理异常
              是否支持MECToMall  =  否
               是否支持就近接入  =  否
                 就近接入关键字  =  NULL
          就近接入是否发现H-PCF  =  否
    基于DNN的创建AM策略偶联开关  =  否
                      DNN关键字  =  NULL
   INTER注册场景PDU会话重建开关  =  否
  跨省漫游用户是否支持MECToMall  =  否
    基于DNN的创建UE策略偶联开关  =  是
              UE策略的DNN关键字  =  HUAWEI.COM
                       描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中当前配置的AM策略和UE策略的控制参数，执行如下命令：
  ```
  %%LST AMUEPLCYCTRL:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                       用户范围  =  所有用户
                       IMSI前缀  =  NULL
                     MSISDN前缀  =  NULL
               网络切片群组标识  =  0
             是否建立AM策略偶联  =  是
             是否建立UE策略偶联  =  否
    AM策略建立/更新失败处理策略  =  去注册用户
    UE策略建立/更新失败处理策略  =  不处理异常
             AM策略终止处理策略  =  使用本地配置或签约的AM策略
             UE策略终止处理策略  =  不处理异常
              是否支持MECToMall  =  否
               是否支持就近接入  =  否
                 就近接入关键字  =  NULL
          就近接入是否发现H-PCF  =  否
    基于DNN的创建AM策略偶联开关  =  否
                      DNN关键字  =  NULL
   INTER注册场景PDU会话重建开关  =  否
  跨省漫游用户是否支持MECToMall  =  否
    基于DNN的创建UE策略偶联开关  =  是
              UE策略的DNN关键字  =  HUAWEI.COM
                       描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AM策略和UE策略控制参数（LST-AMUEPLCYCTRL）_09653095.md`
