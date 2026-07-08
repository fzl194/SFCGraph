---
id: UNC@20.15.2@MMLCommand@LST AMFN8CMPTPLCY
type: MMLCommand
name: LST AMFN8CMPTPLCY（查询AMF N8接口兼容性策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFN8CMPTPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM协议参数管理
- AMF N8接口兼容性参数管理
status: active
---

# LST AMFN8CMPTPLCY（查询AMF N8接口兼容性策略）

## 功能

**适用NF：AMF**

该命令用于查询AMF N8接口兼容性策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用N8接口兼容性策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户。<br>- “HOME_USER（本网用户）”：本网用户。<br>- “FOREIGN_USER（外网用户）”：外网用户。<br>- “IMSI_PREFIX（IMSI前缀）”：IMSI前缀。<br>- “SPECIFIC_IMSI（指定IMSI）”：指定IMSI。<br>默认值：无<br>配置原则：<br>对于指定的用户（群），N8接口兼容性策略的匹配优先级从高到低依次为：“SPECIFIC_IMSI(指定IMSI)”，“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定应用N8接口兼容性策略的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~14。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_IMSI"时为条件可选参数。<br>参数含义：该参数用于指定应用N8接口兼容性策略的用户的IMSI（完整IMSI）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFN8CMPTPLCY]] · AMF N8接口兼容性策略（AMFN8CMPTPLCY）

## 使用实例

- 查询AMF N8接口兼容性策略，执行如下命令：
  ```
  %%LST AMFN8CMPTPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
            用户范围  =  所有用户
            IMSI前缀  =  NULL
                IMSI  =  NULL
  是否支持RedCap RAT  =  是
  是否携带V-GMLC地址  =  否
  (结果个数 = 1)

  ---    END
  ```
- 查询外网用户的AMF N8接口兼容性策略，执行如下命令：
  ```
  %%LST AMFN8CMPTPLCY:SUBRANGE=FOREIGN_USER;%%
  RETCODE = 0  操作成功

  结果如下
  --------
            用户范围  =  外网用户
            IMSI前缀  =  NULL
                IMSI  =  NULL
  是否支持RedCap RAT  =  是
  是否携带V-GMLC地址  =  否
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFN8CMPTPLCY.md`
