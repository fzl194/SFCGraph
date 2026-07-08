---
id: UNC@20.15.2@MMLCommand@LST NGM2MPLCY
type: MMLCommand
name: LST NGM2MPLCY（查询5G M2M策略参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGM2MPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G M2M管理
- 5G M2M策略参数配置
status: active
---

# LST NGM2MPLCY（查询5G M2M策略参数）

## 功能

**适用NF：AMF**

该命令用于查询5G M2M策略参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定M2M策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户。<br>- “HOME_USER（本网用户）”：本网用户。<br>- “FOREIGN_USER（外网用户）”：外网用户。<br>- “IMSI_PREFIX（IMSI前缀）”：IMSI前缀。<br>- “SPECIFIC_IMSI（指定IMSI）”：指定IMSI。<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定M2M策略用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~14。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_IMSI"时为条件可选参数。<br>参数含义：该参数用于指定M2M策略用户的IMSI（完整IMSI）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGM2MPLCY]] · 5G M2M策略参数（NGM2MPLCY）

## 使用实例

- 查询所有记录，执行如下命令：
  ```
  %%LST NGM2MPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                     用户范围  =  本网用户
                     IMSI前缀  =  12345
                         IMSI  =  NULL
                 特征条件组合  =  不指定特征条件
                 数据网络名称  =  NULL
                     eDRX开关  =  OFF
   NR模式EDRX寻呼周期签约优先  =  No
               NR模式寻呼周期  =  使用UE请求值
       NR模式寻呼时间窗口时长  =  使用UE请求值
  (结果个数 = 1)

  ---    END
  ```
- 查询指定IMSI前缀的记录，执行如下命令：
  ```
  %%LST NGM2MPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="12345";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                     用户范围  =  本网用户
                     IMSI前缀  =  12345
                         IMSI  =  NULL
                 特征条件组合  =  不指定特征条件
                 数据网络名称  =  NULL
                     eDRX开关  =  OFF
   NR模式EDRX寻呼周期签约优先  =  No
               NR模式寻呼周期  =  使用UE请求值
       NR模式寻呼时间窗口时长  =  使用UE请求值
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGM2MPLCY.md`
