---
id: UNC@20.15.2@MMLCommand@LST PROXYSMFACCLIST
type: MMLCommand
name: LST PROXYSMFACCLIST（查询Proxy SMF接入控制列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PROXYSMFACCLIST
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- Proxy SGW_SMF管理
- Proxy SMF接入列表
status: active
---

# LST PROXYSMFACCLIST（查询Proxy SMF接入控制列表）

## 功能

**适用NF：SMF**

该命令用于Proxy SMF特性中查询接入控制列表记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGEALL | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接入控制的范围。<br>数据来源：本端规划<br>取值范围：<br>- ALL_USER（所有用户）<br>- IMSI_PRE（IMSI前缀）<br>- MSISDN_PRE（MSISDN前缀）<br>默认值：无<br>配置原则：<br>当存在多种用户范围的记录时，匹配的优先级由高到低为： IMSI_PRE/MSISDN_PRE，ALL_USER，如果某一用户同时匹配IMSI_PRE以及MSISDN_PRE记录时，最终是否允许接入受SET PROXYSMFFUNC命令中的CTRLTYPE参数控制。 |
| PREFIX | 前缀 | 可选必选说明：该参数在"SUBRANGEALL"配置为"IMSI_PRE"、"MSISDN_PRE"时为条件可选参数。<br>参数含义：该参数用于指定接入控制的号码前缀，当SUBRANGE为IMSI_PRE时表示IMSI号码前缀，当SUBRANGE为MSISDN_PRE时表示MSISDN号码前缀。使用时按照最长匹配进行查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：<br>取值范围为1~15位数字。 |
| CTRLTYPE | 控制类型 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否允许用户接入。<br>数据来源：本端规划<br>取值范围：<br>- ALLOW（允许）<br>- REJECT（拒绝）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PROXYSMFACCLIST]] · Proxy SMF接入控制列表（PROXYSMFACCLIST）

## 使用实例

查询所有Proxy SMF接入列表记录，执行如下命令：

```
%%LST PROXYSMFACCLIST:;%%
RETCODE = 0  操作成功

结果如下
--------
用户范围  =  所有用户
    前缀  =  *
控制类型  =  允许
描述信息  =  All User
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PROXYSMFACCLIST.md`
