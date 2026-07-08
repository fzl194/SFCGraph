---
id: UDG@20.15.2@MMLCommand@STR NFDRSWOVER
type: MMLCommand
name: STR NFDRSWOVER（启动人工倒回命令）
nf: UDG
version: 20.15.2
verb: STR
object_keyword: NFDRSWOVER
command_category: 动作类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# STR NFDRSWOVER（启动人工倒回命令）

## 功能

![](启动人工倒回命令（STR NFDRSWOVER）_66924856.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当可能会导致用户接入异常网元影响业务，请谨慎使用并联系华为技术支持协助操作。

该命令用于启动基于业务KPI容灾倒换后的人工倒回操作。

> **说明**
> - 该命令执行后立即生效。
>
> - 执行该命令之前请先执行“[**DSP DBGHAFG**](显示HAFG相关信息（DSP DBGHAFG）_66924852.md): QUERYTYPE="APPID|DSP SELFSTATUS";”命令（其中APPID为可变内容，需要执行[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)查询获取执行倒回操作的网元的MEID），关注查询结果中“Status”是否为“normal”，如果是才可以执行本命令。若查询结果中“Status”不是为“normal”，还需通过本命令做强制倒回操作，则需联系华为技术支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数<br>参数含义：该参数用于设置执行倒回处理的网元ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：<br>可以通过MML命令<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。 |
| FORCE | 是否强制倒回 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否强制执行倒回。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NFDRSWOVER]] · 人工倒回命令（NFDRSWOVER）

## 使用实例

启动人工倒回操作。

```
%%STR NFDRSWOVER: MEID="0";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/STR-NFDRSWOVER.md`
