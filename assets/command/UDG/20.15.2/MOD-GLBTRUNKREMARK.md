---
id: UDG@20.15.2@MMLCommand@MOD GLBTRUNKREMARK
type: MMLCommand
name: MOD GLBTRUNKREMARK（修改整机Trunk Remark配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: GLBTRUNKREMARK
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 宽带集群流量管理
- 全局宽带集群QoS到DSCP或TOS映射
status: active
---

# MOD GLBTRUNKREMARK（修改整机Trunk Remark配置）

## 功能

**适用NF：SGW-U、PGW-U**

该命令用于修改已有的整机Trunk Remark配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QCI | QCI | 可选必选说明：必选参数<br>参数含义：该参数表示QoS流量级别。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~9，65~66，69~70。<br>默认值：无<br>配置原则：无 |
| ARPPL | ARP的优先级别 | 可选必选说明：必选参数<br>参数含义：该参数表示ARP的优先级别。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～15。<br>默认值：无<br>配置原则：无 |
| REMARKTYPE | 标记类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示映射到DSCP或者TOS。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DSCP：映射到DSCP。<br>- TOS：映射到TOS。<br>默认值：无<br>配置原则：无 |
| DSCP | DSCP | 可选必选说明：条件必选参数<br>前提条件：该参数在“REMARKTYPE”配置为“DSCP”时为必选参数。<br>参数含义：该参数用于表示DSCP。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- EF：对应的DSCP的值为101110。<br>- AF：对应的DSCP的值由参数AfClass和AfDropPrec界定。<br>- BE：对应的DSCP的值为000000。<br>- CS6：对应的DSCP的值为110000。<br>- CS7：对应的DSCP的值为111000。<br>- DSCP_VALUE：映射的DSCP值。<br>默认值：无<br>配置原则：无 |
| AFCLASS | AF级别 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DSCP”配置为“AF”时为必选参数。<br>参数含义：该参数用于表示AF队列序号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4。<br>默认值：无<br>配置原则：无 |
| AFDROPPREC | AF丢弃优先级 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DSCP”配置为“AF”时为必选参数。<br>参数含义：该参数表示AF丢弃优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～3。<br>默认值：无<br>配置原则：无 |
| TOSVALUE | TOS值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“REMARKTYPE”配置为“TOS”时为必选参数。<br>参数含义：该参数表示映射到TOS的值，分别对应IP优先级的8个队列ID，优先值高的报文先于优先值低的报文发送。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～7。<br>默认值：无<br>配置原则：无 |
| DSCPVALUE | DSCP值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DSCP”配置为“DSCP_VALUE”时为必选参数。<br>参数含义：该参数用于表示映射的DSCP值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLBTRUNKREMARK]] · 整机Trunk Remark配置（GLBTRUNKREMARK）

## 使用实例

将整机中Trunk Remark配置是QCI为1，ARP优先级为1，Remark类型为TOS，且TOS值为3的数据修改为TOS值为5：

```
MOD GLBTRUNKREMARK: QCI=1, ARPPL=1, REMARKTYPE=TOS, TOSVALUE=5;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-GLBTRUNKREMARK.md`
