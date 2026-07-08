---
id: UDG@20.15.2@MMLCommand@STR NFDREXE
type: MMLCommand
name: STR NFDREXE（启动人工执行容灾倒换）
nf: UDG
version: 20.15.2
verb: STR
object_keyword: NFDREXE
command_category: 动作类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# STR NFDREXE（启动人工执行容灾倒换）

## 功能

![](启动人工执行容灾倒换（STR NFDREXE）_02724853.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当可能会误倒换网元，影响现网业务，请谨慎使用并联系华为技术支持协助操作。

该命令用于启动基于业务KPI的容灾倒换。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数<br>参数含义：该参数用于设置执行容灾倒换处理的网元ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。<br>默认值：无<br>配置原则：<br>可以通过MML命令<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>获取。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NFDREXE]] · 人工执行容灾倒换（NFDREXE）

## 使用实例

人工执行容灾倒换。

```
%%STR NFDREXE: MEID="0";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/STR-NFDREXE.md`
