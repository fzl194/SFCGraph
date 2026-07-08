---
id: UNC@20.15.2@MMLCommand@ADD DSCPPRI
type: MMLCommand
name: ADD DSCPPRI（增加DSCP映射优先级配置表）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DSCPPRI
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 64
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- DSCP
- DSCP优先级映射管理
status: active
---

# ADD DSCPPRI（增加DSCP映射优先级配置表）

## 功能

**适用网元：SGSN、MME**

本命令用于增加DSCP映射优先级表。DSCP映射优先级表是调度模块决定报文入队列的依据。 UNC 网元将报文映射为四个优先级，不同DSCP值的报文将按照DSCP映射优先级表入不同优先级的队列，找不到映射关系的报文将入“优先级4”的队列。

相关命令: [**SET IFDSCP**](../接口DSCP管理/设置接口DSCP配置(SET IFDSCP)_26306022.md)

## 注意事项

- 本表最大记录数为64条记录。
- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SLTPR | 选择操作类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指示增加DSCP映射优先级表的操作类型。<br>数据来源：全网规划<br>取值范围： DSCP(DSCP映射关系)<br>默认值：DSCP(DSCP映射关系)<br>配置原则：无 |
| DSCPV | DSCP值 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指示新增DSCP映射优先级的DSCP值。<br>数据来源：全网规划<br>取值范围：0~63<br>默认值：无<br>配置原则：不能添加已有的默认记录对应的DSCP映射关系，默认记录如<br>[**MOD DSCPPRI**](修改DSCP映射优先级配置表(MOD DSCPPRI)_26146208.md)<br>命令中表1所示。 |
| MAPPRI | 映射优先级 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指示新增DSCP值的映射优先级。数据来源：全网规划<br>取值范围：<br>- “PRI_1(优先级1)”<br>- “PRI_2(优先级2)”<br>- “PRI_3(优先级3)”<br>- “PRI_4(优先级4)”<br>默认值：无<br>配置原则：<br>- PRI_1~4分别表示4种处理优先级，1~4依次从高到低。<br>- 一般报文入队列类别关系为：DSCP为NC、INC的报文进入“优先级1”队列，DSCP为EF、AF4、AF3的报文进入“优先级2”队列，DSCP为AF2、AF1的报文进入“优先级3”队列，DSCP为BE的报文进入“优先级4”队列。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DSCPPRI]] · DSCP映射优先级配置表（DSCPPRI）

## 使用实例

增加DSCP为50的映射优先级为PRI_2：

ADD DSCPPRI: SLTPR=DSCP, DSCPV=50, MAPPRI=PRI_2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加DSCP映射优先级配置表(ADD-DSCPPRI)_26306018.md`
