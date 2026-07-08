---
id: UNC@20.15.2@MMLCommand@MOD SBIFQDNPORTPLCY
type: MMLCommand
name: MOD SBIFQDNPORTPLCY（修改FQDN端口策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SBIFQDNPORTPLCY
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- NF通信模式管理
- FQDN端口策略管理
status: active
---

# MOD SBIFQDNPORTPLCY（修改FQDN端口策略）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于修改FQDN使用端口号的策略。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCENE | 场景 | 可选必选说明：必选参数<br>参数含义：该参数用于指定端口策略适用的场景。<br>数据来源：全网规划<br>取值范围：<br>- “TARGETADDR（TARGETADDR）”：根据对端FQDN组装对端Uri<br>- “LOCALURI（LOCALURI）”：根据本端FQDN组装本端CallbackUri或Location等Uri<br>默认值：无<br>配置原则：无 |
| SCOPE | 范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定FQDN端口策略的适用范围。<br>数据来源：全网规划<br>取值范围：<br>- “INTERPLMNDEFAULT（INTERPLMNDEFAULT）”：PLMN间默认策略<br>- “BYPLMN（BYPLMN）”：指定PLMN的策略<br>默认值：无<br>配置原则：<br>如果同时有默认策略和基于PLMN的策略，优先使用基于PLMN的策略。 |
| PLMN | 对端PLMN | 可选必选说明：该参数在"SCOPE"配置为"BYPLMN"时为条件必选参数。<br>参数含义：该参数用于指定策略适用的对端PLMN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~6。<br>默认值：无<br>配置原则：<br>PLMN由MCC和MNC组成， MCC为3个十进制数字， MNC为2~3个十进制数字。例如PLMN=“12303”， 其中MCC=“123”， MNC=“03”。 |
| PORTPLCY | 端口策略 | 可选必选说明：必选参数<br>参数含义：该参数用于指定FQDN使用端口号的策略。<br>数据来源：全网规划<br>取值范围：<br>- “USEPORT（USEPORT）”：使用端口号<br>- “NOTUSEPORT（NOTUSEPORT）”：不使用端口号<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SBIFQDNPORTPLCY]] · FQDN端口策略（SBIFQDNPORTPLCY）

## 使用实例

- 修改根据对端FQDN组装对端Uri场景下，PLMN间默认策略为FQDN使用端口号。
  ```
  MOD SBIFQDNPORTPLCY:SCENE=TARGETADDR,SCOPE=INTERPLMNDEFAULT,PORTPLCY=USEPORT;
  ```
- 修改根据对端FQDN组装对端Uri场景下，对端PLMN为"12303"时，策略为FQDN不使用端口号。
  ```
  MOD SBIFQDNPORTPLCY:SCENE=TARGETADDR,SCOPE=BYPLMN,PLMN="12303",PORTPLCY=NOTUSEPORT;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SBIFQDNPORTPLCY.md`
