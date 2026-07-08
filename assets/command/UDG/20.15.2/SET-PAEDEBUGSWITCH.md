---
id: UDG@20.15.2@MMLCommand@SET PAEDEBUGSWITCH
type: MMLCommand
name: SET PAEDEBUGSWITCH（使能或去使能PAE转发日志）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PAEDEBUGSWITCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 系统资源
status: active
---

# SET PAEDEBUGSWITCH（使能或去使能PAE转发日志）

## 功能

![](使能或去使能PAE转发日志（SET PAEDEBUGSWITCH）_92520051.assets/notice_3.0-zh-cn.png)

本功能使能会降低性能，去使能之后性能恢复，使能后在120分钟后自动去使能。

该命令用来打开和关闭PAE转发流程记录日志的功能。

在PAE转发流程的异常分支中，由转发日志开关控制是否记录异常日志。

转发日志开关默认是关闭的。

## 注意事项

1. 该命令执行后立即生效。
2. 在需要定位转发异常时，打开该开关可以辅助定位，但打开开关后，对转发性能有一定的影响。建议保持该开关为默认的关闭状态。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |
| ENABLEFLAG | 使能标志 | 可选必选说明：必选参数<br>参数含义：该参数用于指定使能标志。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PAEDEBUGSWITCH]] · 使能或去使能PAE转发日志（PAEDEBUGSWITCH）

## 使用实例

使能微服务类型为“aa”微服务实例为“bb”内PAE转发日志开关：

```
SET PAEDEBUGSWITCH:CELLTYPE="aa", CELLINSTANCE="bb",ENABLEFLAG=TRUE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-PAEDEBUGSWITCH.md`
