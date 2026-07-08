---
id: UNC@20.15.2@MMLCommand@LST NGCONNECTPLMN
type: MMLCommand
name: LST NGCONNECTPLMN（查询5G Connect PLMN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGCONNECTPLMN
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- 互联PLMN管理
status: active
---

# LST NGCONNECTPLMN（查询5G Connect PLMN）

## 功能

**适用NF：AMF**

该命令用于查询可接入到本运营商的Connect PLMN。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在UNC系统中唯一标识某个运营商。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成Connect PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成Connect PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用5G Connect PLMN的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “SPECIFIED_IMSI_RANGE（指定IMSI范围）”：指定IMSI范围<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIED_IMSI_RANGE"时为条件可选参数。<br>参数含义：该参数用于指定应用5G Connect PLMN的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGCONNECTPLMN]] · 5G Connect PLMN（NGCONNECTPLMN）

## 使用实例

- 查询系统中“运营商标识”为“0”的NG模式互联PLMN信息，执行如下命令：
  ```
  %%LST NGCONNECTPLMN: NOID=0;%%
  RETCODE = 0  操作成功

  结果如下
  --------
             运营商标识  =  0
             移动国家码  =  123
               移动网号  =  45
               用户范围  =  所有用户
               IMSI前缀  =  NULL
   是否允许紧急呼叫业务  =  NR接入的紧急呼叫回落
       紧急号码下发开关  =  是
               漫游模式  =  异网漫游
   隐藏用户位置信息开关  =  是
               跟踪区域  =  410020
               小区标识  =  123456789
         gNodeB标识长度  =  22
             gNodeB标识  =  4294967295
               描述信息  =  for MNO A
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中当前配置的NG模式互联PLMN信息，执行如下命令：
  ```
  %%LST NGCONNECTPLMN:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
             运营商标识  =  0
             移动国家码  =  460
               移动网号  =  03
               用户范围  =  所有用户
               IMSI前缀  =  NULL
   是否允许紧急呼叫业务  =  NR接入的紧急呼叫回落
       紧急号码下发开关  =  是
               漫游模式  =  异网漫游
   隐藏用户位置信息开关  =  是
               跟踪区域  =  410020
               小区标识  =  123456789
         gNodeB标识长度  =  22
             gNodeB标识  =  4294967295
               描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G-Connect-PLMN（LST-NGCONNECTPLMN）_09653790.md`
