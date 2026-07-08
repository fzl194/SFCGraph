---
id: UNC@20.15.2@MMLCommand@LST SMCAUSEMAP
type: MMLCommand
name: LST SMCAUSEMAP（查询SM原因值映射配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMCAUSEMAP
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- SM原因值管理
- 原因值映射管理
status: active
---

# LST SMCAUSEMAP（查询SM原因值映射配置）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

此命令用于查询原因值映射配置记录。原因值映射就是将某些原因值映射成目标原因值，通过接口消息中下发给其他NF。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CAUSEGRPID | 原因值组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定表示一个原因值映射规则集合的唯一数字ID。如果不输入此参数，系统会查询所有配置记录。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~127。<br>默认值：无<br>配置原则：<br>该参数必须通过命令ADD SMCAUSEGRP配置。 |
| CAUSERANGE | 原因值范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定原因值范围。<br>数据来源：全网规划<br>取值范围：<br>- “DEFAULT（缺省）”：表示无需指定某一特定接口的起始和终止原始原因值。<br>- “SPECIAL（特定）”：表示需指定某一特定接口的起始原始原因值。<br>- “SPECIAL_APP_ERR（特定应用层错误）”：表示需指定某一特定接口的起始http层状态码以及应用层错误<br>默认值：无<br>配置原则：<br>- 一个“CAUSEGRPID(原因值组标识)”只能对应一个“DEFAULT(缺省)”配置。“SPECIAL(特定)”可以配置多个。“SPECIAL_APP_ERR(特定应用层错误)”针对服务化接口触发的NAS原因值，可以配置多个。<br>- 在实际使用时，CAUSERANGE下各个枚举的优先级顺序： SPECIAL_APP_ERR > SPECIAL > DEFAULT。如果同时配置了“DEFAULT(缺省)”、“SPECIAL(特定)”和“SPECIAL_APP_ERR(特定应用层错误)”的记录，则优先使用“SPECIAL_APP_ERR(特定应用层错误)”记录。如果同时配置了“DEFAULT(缺省)”和“SPECIAL(特定)”的记录，则优先使用“SPECIAL(特定)”记录。<br>- 同一原因值组标识下，原因值范围为SPECIAL时，输入的原始原因值范围不允许相互交叉、包含或重合。同一原因值组标识下，原因值范围为SPECIAL_APP_ERR时，若APPERROR相同，输入的原始原因值范围不允许相互交叉、包含或重合。 |
| BGCAUSE | 起始原始原因值 | 可选必选说明：该参数在"CAUSERANGE"配置为"SPECIAL"、"SPECIAL_APP_ERR"时为条件可选参数。<br>参数含义：该参数用于指定某一特定接口的起始原始原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：<br>“BGCAUSE(起始原始原因值)”小于等于“EDCAUSE(终止原始原因值)”。 |
| APPERROR | 应用层错误 | 可选必选说明：该参数在"CAUSERANGE"配置为"SPECIAL_APP_ERR"时为条件可选参数。<br>参数含义：该参数表示服务化接口下对端网元返回的应用层错误，与BGCAUSE以及EDCAUSE参数一起进行原因值映射。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMCAUSEMAP]] · SM原因值映射配置（SMCAUSEMAP）

## 使用实例

查询原因值组标识为126，原因值范围设置为特定应用层错误的原因值映射配置。

```
%%LST SMCAUSEMAP: CAUSEGRPID=126, CAUSERANGE=SPECIAL_APP_ERR;%%
RETCODE = 0  操作成功

结果如下
--------
  原因值组标识  =  126
    原因值范围  =  特定应用层错误
起始原始原因值  =  1
终止原始原因值  =  1
    应用层错误  =  1
    目标原因值  =  27
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMCAUSEMAP.md`
