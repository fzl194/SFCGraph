---
id: UNC@20.15.2@MMLCommand@LST UFCSFB
type: MMLCommand
name: LST UFCSFB（查询预留功能策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UFCSFB
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- 预留功能策略管理
status: active
---

# LST UFCSFB（查询预留功能策略）

## 功能

**适用网元：MME**

该命令用于查询预留功能策略。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “HOME_USER(本网用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无<br>说明：如果不输入该参数，系统会查询所有配置记录。 |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>说明：- 如果不输入该参数，系统会查询所有的“SUBRANGE（用户范围）”配置为“FOREIGN_USER（外网用户）”或“HOME_USER（本网用户）”记录。<br>- NOID未配置时，显示为255 |
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于系统对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：此参数在<br>“SUBRANGE（用户范围）”<br>设置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无<br>说明：如果不输入该参数，系统会查询所有“SUBRANGE（用户范围）”配置为“IMSI_PREFIX（指定IMSI前缀）”的配置记录。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UFCSFB]] · 预留功能策略（UFCSFB）

## 使用实例

查询本网用户的预留功能策略：

LST UFCSFB: SUBRANGE=HOME_USER;

```
%%LST UFCSFB: SUBRANGE=HOME_USER;%%
RETCODE = 0  操作成功。

操作结果如下：
--------------
    用户范围  =  本网用户
  运营商标识  =  0
    IMSI前缀  =  NULL
    预留功能  =  是
基于IMEI控制  =  白名单
IMEI群组标识  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UFCSFB.md`
