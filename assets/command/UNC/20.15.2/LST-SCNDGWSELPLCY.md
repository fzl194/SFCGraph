---
id: UNC@20.15.2@MMLCommand@LST SCNDGWSELPLCY
type: MMLCommand
name: LST SCNDGWSELPLCY（查询相同APN建立多个PDP/PDN连接的网关选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCNDGWSELPLCY
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- GGSN_P-GW选择
status: active
---

# LST SCNDGWSELPLCY（查询相同APN建立多个PDP/PDN连接的网关选择策略）

## 功能

**适用网元：SGSN、MME**

该命令用于查询用户使用相同APN建立多个PDP/PDN连接场景下，系统选择GGSN/P-GW的策略。

## 注意事项

- 无。

## 权限

manage-ug; system-ug; monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；G_4，来宾级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATTYPE | 接入类型 | 可选必选说明：可选参数<br>参数含义：该参数用以指定网关地址选择策略的适用用户的接入方式。<br>数据来源：整网规划<br>取值范围：<br>- “LTE(LTE)”：指定的接入类型是LTE。<br>- “GPRS_UMTS(GPRS&UMTS)”：指定的接入类型是GPRS或者UMTS。<br>默认值：无 |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用以指定网关地址选择策略的适用用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有指定接入类型的用户。<br>- “HOME_USER（本网用户）”：所有指定接入类型的本网用户。<br>- “FOREIGN_USER（外网用户）”：所有指定接入类型的外网用户。<br>- “IMSI_PREFIX（指定IMSI前缀）”：所有指定接入类型且指定IMSI前缀的用户。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用以指定网关地址选择策略的适用用户IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“指定IMSI前缀”<br>后生效。<br>数据来源：整网规划<br>取值范围：5~15位数字。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCNDGWSELPLCY]] · 相同APN建立多个PDP/PDN连接的网关选择策略（SCNDGWSELPLCY）

## 使用实例

不输入 “接入类型” 和 “用户范围” ，查询所有相同APN建立多个PDP/PDN连接的网关选择策略。

LST SCNDGWSELPLCY:;

```
%%LST SCNDGWSELPLCY:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
接入类型      用户范围        IMSI前缀     LTE模式相同APN网关选择策略     GU模式相同APN网关选择策略    描述信息

LTE           外网用户        NULL         使用接口IP                     NULL                         for 4g roaming user
LTE           指定IMSI前缀    123035       使用接口IP                     NULL                         for 4g imsipre 123035 user
GPRS&UMTS     指定IMSI前缀    123038       NULL                           使用接口IP                   for 23g imsipre 123038 user
(结果个数 = 3)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SCNDGWSELPLCY.md`
