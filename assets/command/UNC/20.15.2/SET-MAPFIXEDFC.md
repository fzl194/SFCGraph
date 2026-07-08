---
id: UNC@20.15.2@MMLCommand@SET MAPFIXEDFC
type: MMLCommand
name: SET MAPFIXEDFC（设置SMS的MAP接口固定速率流控）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MAPFIXEDFC
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 接口流控
- MAP接口流控
status: active
---

# SET MAPFIXEDFC（设置SMS的MAP接口固定速率流控）

## 功能

**适用NF：SMSF**

该命令用于表示设置SMS的MAP接口固定速率流控。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| FCSWITCH | MTFCTHD | FLCTL | CAUSE | RATELEVEL |
| --- | --- | --- | --- | --- |
| ON | 10000 | FAILRSP | RESOURCELIMITATION | WholeSystem |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCSWITCH | 流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否开启SMS的MAP接口固定速率流控。<br>数据来源：本端规划<br>取值范围：<br>- ON（开启）<br>- OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MAPFIXEDFC查询当前参数配置值。<br>配置原则：无 |
| MTFCTHD | MT消息流控速率(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于表示MT消息流控速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1000000，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MAPFIXEDFC查询当前参数配置值。<br>配置原则：无 |
| FLCTL | 流控处理方式 | 可选必选说明：可选参数<br>参数含义：该参数用于表示对SMS的MAP接口固定速率流控的方式。<br>数据来源：本端规划<br>取值范围：<br>- “FAILRSP（失败响应）”：根据流控响应原因值，返回失败响应码。<br>- “DISCARD（直接丢弃）”：不返回响应码。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MAPFIXEDFC查询当前参数配置值。<br>配置原则：无 |
| CAUSE | 流控响应原因值 | 可选必选说明：该参数在"FLCTL"配置为"FAILRSP"时为条件可选参数。<br>参数含义：该参数用于表示流控响应原因值。<br>数据来源：本端规划<br>取值范围：<br>- “RESOURCELIMITATION（资源限制）”：29002协议原因值Resource Limitation(51)<br>- “SYSTEMFAILURE（系统错误）”：29002协议原因值System Failure(34)<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MAPFIXEDFC查询当前参数配置值。<br>配置原则：无 |
| RATELEVEL | 阈值计算策略 | 可选必选说明：可选参数<br>参数含义：该参数用于控制“MT消息流控速率(个/秒)”的计算策略。<br>数据来源：本端规划<br>取值范围：<br>- WholeSystem（整系统）<br>- Process（进程）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MAPFIXEDFC查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MAPFIXEDFC]] · SMS的MAP接口固定速率流控（MAPFIXEDFC）

## 使用实例

运营商想要将SMS的MAP接口固定速率流控开关打开，MT消息流控速率设置为10001个/秒，流控处理方式设置为失败响应，流控响应原因值设置为资源限制，阈值计算策略设置为整系统时，执行如下命令：

```
SET MAPFIXEDFC: FCSWITCH=ON, MTFCTHD=10001, FLCTL=FAILRSP, CAUSE=RESOURCELIMITATION, RATELEVEL=WholeSystem;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-MAPFIXEDFC.md`
