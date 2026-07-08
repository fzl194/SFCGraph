---
id: UNC@20.15.2@MMLCommand@MOD DSCPPRIMCR
type: MMLCommand
name: MOD DSCPPRIMCR（修改DSCP映射优先级配置表）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DSCPPRIMCR
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- 接口DSCP管理
- DSCP优先级映射管理
status: active
---

# MOD DSCPPRIMCR（修改DSCP映射优先级配置表）

## 功能

**适用网元：MME**

本命令用于修改DSCP映射优先级表，以及数据报文入发送队列的策略。DSCP映射优先级表是调度模块决定报文入队列的依据。USN网元将报文分为四个优先级，不同DSCP值的报文将按照DSCP映射优先级表入不同优先级的队列，找不到映射关系的报文将入“优先级4”的队列。

接收的报文(信令报文+数据报文)按照DSCP映射优先级表入接收队列。发送的信令报文按照DSCP映射优先级表入发送队列，发送的数据报文按照 “数据报文的映射队列策略” 入发送队列。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SLTPR | 选择操作类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指示修改DSCP映射优先级表以及数据报文的入队列策略的操作类型。<br>数据来源：全网规划<br>取值范围：<br>- “DSCP(DSCP映射关系)”：修改DSCP的映射关系。<br>默认值：无<br>配置原则：无 |
| DSCPV | DSCP值 | 可选必选说明：可选参数<br>参数含义：本参数用于指示修改DSCP映射优先级的DSCP值。<br>前提条件：该参数在<br>“选择操作类型”<br>设置为<br>“DSCP(DSCP映射关系)”<br>时生效。<br>数据来源：全网规划<br>取值范围：0~63<br>默认值：无<br>配置原则：无 |
| MAPPRI | 映射优先级 | 可选必选说明：可选参数<br>参数含义：本参数用于指示修改DSCP值的映射优先级。<br>前提条件：该参数在<br>“选择操作类型”<br>设置为<br>“DSCP(DSCP映射关系)”<br>时生效。<br>数据来源：全网规划<br>取值范围：PRI_1~PRI_4<br>默认值：无<br>配置原则：<br>- PRI_1~4分别表示4种处理优先级，1~4依次从高到低。<br>- 一般报文入队列类别关系为：DSCP为NC、INC的报文进入“优先级1”队列，DSCP为EF、AF4、AF3的报文进入“优先级2”队列，DSCP为AF2、AF1的报文进入“优先级3”队列，DSCP为BE的报文进入“优先级4”队列。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DSCPPRIMCR]] · DSCP映射优先级配置表（DSCPPRIMCR）

## 使用实例

修改DSCP为56的映射优先级为PRI_2：

MOD DSCPPRIMCR: SLTPR=DSCP, DSCPV=56, MAPPRI=PRI_2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-DSCPPRIMCR.md`
