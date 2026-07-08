---
id: UNC@20.15.2@MMLCommand@LST QOSCAPWHITEAPNS
type: MMLCommand
name: LST QOSCAPWHITEAPNS（查询不受SMFQOSCAP配置控制的APN白名单列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSCAPWHITEAPNS
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 基于IMSI号段的QoS管理
- 不受SMFQOSCAP配置控制的APN白名单列表
status: active
---

# LST QOSCAPWHITEAPNS（查询不受SMFQOSCAP配置控制的APN白名单列表）

## 功能

**适用NF：SMF**

该命令用于查询不受SMFQOSCAP配置控制的APN白名单列表。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待增加QoS限制配置的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- INVALIDSUBRANGE（无效的用户范围）<br>- IMSI_PREFIX（指定IMSI前缀的用户）<br>- VISITING（拜访用户）<br>- ROAMING（漫游用户）<br>- HOME_USER（本网用户）<br>- ALL_USER（所有用户）<br>- HOME_NOLOCAL_USER（本网非本省用户）<br>默认值：无<br>配置原则：<br>“SUBRANGE（用户范围）”的优先级从高到低为：“IMSI_PREFIX（指定IMSI前缀）”，"HOME_NOLOCAL_USER"（本网非本省用户），“HOME_USER（本网用户）”或“ROAMING（漫游用户）”或“VISITING（拜访用户）”，“ALL_USER（所有用户）”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于系统根据对用户的IMSI前缀进行匹配，从而区分不同的用户群。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>IMSI前缀取决于需要使用本条QoS限制的IMSI范围；<br>确定IMSI前缀时应遵循最大匹配原则。例如，对于IMSI号在308010700000000～308010700099999范围内的用户都需要将QoS信息限制为某一组数值，则应配置一条IMSI前缀为“3080107000”的记录；<br>当IMSI符合多条QoS限制配置的IMSI前缀时，采用匹配位数最多的记录。例如：用户IMSI号为308010700000001，有2条QoS限制配置的IMSI前缀分别为“30801”和“3080107”，则采用“3080107”的记录。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSCAPWHITEAPNS]] · 不受SMFQOSCAP配置控制的APN白名单列表。（QOSCAPWHITEAPNS）

## 使用实例

查询给定APN、用户范围和IMSI前缀对应的QOSCAPWHITEAPNS配置： 2.查询QOSCAPWHITEAPNS配置：

```
%%LST QOSCAPWHITEAPNS: APN="huawei.com",SUBRANGE=IMSI_PREFIX,IMSIPRE="3080107000";%%
            RETCODE = 0  操作成功

            操作结果如下
            ------------
            APN  =  huawei.com
            用户类型 = 指定IMSI前缀
            IMSI前缀  =  3080107000
            (结果个数 = 1)

            ---    END
            2.%%LST QOSCAPWHITEAPNS:;%%
            RETCODE = 0  操作成功

            操作结果如下
            ------------
            APN            用户范围             IMSI前缀

            huawei.com      指定IMSI前缀        3080107000
            123.com         所有用户            000000000000000

            (结果个数 = 2)

            ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询不受SMFQOSCAP配置控制的APN白名单列表（LST-QOSCAPWHITEAPNS）_75760456.md`
