---
id: UNC@20.15.2@MMLCommand@LST NGPEIPLCY
type: MMLCommand
name: LST NGPEIPLCY（查询5G PEI策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGPEIPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 业务安全管理
- PEI策略管理
status: active
---

# LST NGPEIPLCY（查询5G PEI策略）

## 功能

**适用NF：AMF**

该命令用于查询系统内当前配置的PEI控制策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “IMSI_PREFIX（指定IMSI前缀）”：指定IMSI前缀<br>- “IMSI（指定IMSI）”：IMSI<br>默认值：无<br>配置原则：<br>当SUBRANGE取值为“IMSI(指定IMSI)”时，匹配用户的方式为全匹配。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定IMSI前缀，取值5～15位十进制数字。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定IMSI，取值14~15位十进制数字。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGPEIPLCY]] · 5G PEI策略（NGPEIPLCY）

## 使用实例

- 查询系统内当前配置的PEI控制策略：
  ```
  %%LST NGPEIPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                   用户范围  =  所有用户
                   IMSI前缀  =  NULL
                       IMSI  =  NULL
                PEI获取策略  =  不获取
                PEI检查策略  =  不检查
                   流程类型  =  初始注册
    PEI获取失败是否允许接入  =  是
    PEI检查超时是否允许接入  =  是
     是否允许黑名单用户接入  =  是
     是否允许灰名单用户接入  =  是
   是否允许紧急注册用户接入  =  是
  是否允许EIR发现失败时接入  =  是
  是否允许EIR返回失败时接入  =  是
                PEI检查上限  =  0
                是否重选EIR  =  是
          是否支持EIR重定向  =  是
                   描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询系统内当前配置“用户范围”为“指定IMSI前缀”且“IMSI前缀”为“123456”的PEI控制策略：
  ```
  %%LST NGPEIPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456";%%
  RETCODE = 0  操作成功

  结果如下
  --------
                   用户范围  =  指定IMSI前缀
                   IMSI前缀  =  123456
                       IMSI  =  NULL
                PEI获取策略  =  获取IMEI
                PEI检查策略  =  检查IMEI
                   流程类型  =  周期性注册
    PEI获取失败是否允许接入  =  否
    PEI检查超时是否允许接入  =  是
     是否允许黑名单用户接入  =  是
     是否允许灰名单用户接入  =  是
   是否允许紧急注册用户接入  =  是
  是否允许EIR发现失败时接入  =  是
  是否允许EIR返回失败时接入  =  是
                PEI检查上限  =  0
                是否重选EIR  =  是
          是否支持EIR重定向  =  是
                   描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGPEIPLCY.md`
