---
id: UNC@20.15.2@MMLCommand@LST SMSFSELPLCY
type: MMLCommand
name: LST SMSFSELPLCY（查询SMSF选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSFSELPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- SMSF选择策略管理
status: active
---

# LST SMSFSELPLCY（查询SMSF选择策略）

## 功能

**适用NF：AMF**

该命令用于查询SMSF的选择策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用SMSF选择策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（ 所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_RANGE（IMSI范围）”：IMSI范围<br>- “MSISDN_RANGE（MSISDN范围）”：MSISDN范围<br>默认值：无<br>配置原则：<br>对于指定的用户（群），SMSF选择策略的匹配优先级从高到低依次为：“IMSI_RANGE(IMSI范围)”，“MSISDN_RANGE(。<br>MSISDN范围)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| STARTIMSI | 起始IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_RANGE"时为条件可选参数。<br>参数含义：该参数用于表示起始IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| STARTMSISDN | 起始MSISDN | 可选必选说明：该参数在"SUBRANGE"配置为"MSISDN_RANGE"时为条件可选参数。<br>参数含义：该参数用于表示起始MSISDN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSFSELPLCY]] · SMSF选择策略（SMSFSELPLCY）

## 使用实例

- 查询当前配置的SMSF选择策略，执行如下命令：
  ```
  %%LST SMSFSELPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  用户范围       起始IMSI  结束IMSI  起始MSISDN  结束MSISDN  是否使用SUPI  是否使用GPSI  

  本网用户       NULL      NULL      NULL        NULL        关闭          开启                   
  IMSI范围       123450    123459    NULL        NULL        关闭          开启                   
  IMSI范围       1234500   1234509   NULL        NULL        关闭          开启                   
  (结果个数 = 3)

  ---    END
  ```
- 查询当前配置“用户范围”为“本网用户”的SMSF选择策略，执行如下命令：
  ```
  %%LST SMSFSELPLCY:SUBRANGE=HOME_USER;%%
  RETCODE = 0  操作成功

  结果如下
  --------
         用户范围  =  本网用户
         起始IMSI  =  NULL
         结束IMSI  =  NULL
       起始MSISDN  =  NULL
       结束MSISDN  =  NULL
     是否使用SUPI  =  关闭
     是否使用GPSI  =  开启
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMSF选择策略（LST-SMSFSELPLCY）_91579981.md`
