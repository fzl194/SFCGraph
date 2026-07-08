---
id: UNC@20.15.2@MMLCommand@MOD USRBLACKLST
type: MMLCommand
name: MOD USRBLACKLST（修改用户黑名单限制列表）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: USRBLACKLST
command_category: 配置类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 接入限制
- 黑名单接入限制
status: active
---

# MOD USRBLACKLST（修改用户黑名单限制列表）

## 功能

**适用NF：SGSN、MME、AMF**

该命令用于修改用户黑名单限制的限制模式。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定限制用户黑名单接入的IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是15。<br>默认值：无<br>配置原则：无 |
| RESTRICTMODE | 限制模式 | 可选必选说明：可选参数<br>参数含义：该参数用于控制限制用户黑名单接入的系统模式。<br>数据来源：全网规划<br>取值范围：<br>- N2_MODE（N2模式）<br>- S1_MODE（S1模式）<br>- Iu_MODE（Iu模式）<br>- Gb_MODE（Gb模式）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用户黑名单限制列表（USRBLACKLST）](configobject/UNC/20.15.2/USRBLACKLST.md)

## 使用实例

修改一条黑名单限制列表记录，用户为123456789012345，限制用户通过N2模式接入，执行如下命令：

```
MOD USRBLACKLST: IMSI="123456789012345", RESTRICTMODE=N2_MODE-1&S1_MODE-0&Iu_MODE-0&Gb_MODE-0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改用户黑名单限制列表（MOD-USRBLACKLST）_15633693.md`
