---
id: UDG@20.15.2@MMLCommand@SET CSLOGLEVEL
type: MMLCommand
name: SET CSLOGLEVEL（设置日志输出级别）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: CSLOGLEVEL
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# SET CSLOGLEVEL（设置日志输出级别）

## 功能

![](设置日志输出级别（SET CSLOGLEVEL）_09587910.assets/notice_3.0-zh-cn.png)

调低日志级别，可能造成CPU升高、业务呼损等严重后果，不建议操作。

此命令用于设置日志输出级别，设置的是整系统的日志输出级别。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | LEVEL |
> | --- |
> | ERR |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LEVEL | 日志级别 | 可选必选说明：必选参数<br>参数含义：该参数用于表示日志级别。<br>数据来源：本端规划<br>取值范围：<br>- “DEBUGGING（调试级别）”：调试级别<br>- “INFORMATIONAL（信息级别）”：信息级别<br>- “WARNING（警告级别）”：警告级别<br>- “ERR（错误级别）”：错误级别<br>- “CRITICAL（严重级别）”：严重级别<br>默认值：无。<br>配置原则：<br>日志级别的取值范围包括：<br>DEBUGGING(调试级别) ：输出调试信息，比如运行中比较重要的变量值等，用于开发人员定位较复杂的问题。<br>INFORMATIONAL(信息级别) ：重要流程、重要系统状态变迁，如当前数据库容量、占用多少等信息。<br>WARNING(警告级别) ：表明系统出现潜在风险，但不影响现有业务正常运行，比如用户手工停止某个服务，比如统计任务上报了数据而对应的话统未确认并丢弃数据。<br>ERR(错误级别) ：一般错误，数据或者事件是非预期的，影响面较大且模块内部能够处理掉，错误限制在模块内或者对其他模块有轻微影响的事件，用于记录引起调用失败的错误，可用于异常路径或者业务逻辑错误的情况下记录错误状态信息，以及造成错误的可能原因，如配置查询出的数据不能入库、统计任务创建失败等。<br>CRITICAL(严重级别) ：严重错误，用于系统运行环境严重受损，甚至丧失部分功能，无法继续的情况下记录错误状态信息，如网元创建失败等。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CSLOGLEVEL]] · 更新日志输出级别（CSLOGLEVEL）

## 使用实例

设置日志输出级别为调试级别：

```
SET CSLOGLEVEL: LEVEL=DEBUGGING;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置日志输出级别（SET-CSLOGLEVEL）_09587910.md`
