---
id: UNC@20.15.2@MMLCommand@ADD SELECTRULEINFO
type: MMLCommand
name: ADD SELECTRULEINFO（增加UPF选择规则信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SELECTRULEINFO
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF选择规则信息
status: active
---

# ADD SELECTRULEINFO（增加UPF选择规则信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于增加UPF选择规则信息。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 配置高通量业务规则时，其优先级需低于重点业务保障和用户体验规则的优先级。
- 当前版本不支持RULERANGE配置为“ALL”。
- 配置媒体中继业务规则时，其优先级低于高通量业务。

- 最多可输入5000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCF下发的规则名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD UPFBINDSELRULE命令中的“规则名称”参数取值保持一致时，该规则的参数功能生效。 |
| RULEFUNC | 规则功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCF下发的规则绑定的功能。<br>数据来源：全网规划<br>取值范围：<br>- QOSANA（重点业务保障）<br>- QOSEXP（用户体验）<br>- QOSCCC（高通量业务）<br>- RELAY（媒体中继业务）<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于标识规则的优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。值越小优先级越高。<br>默认值：无<br>配置原则：无 |
| DELIVERSW | 是否下发给UPF | 可选必选说明：可选参数<br>参数含义：该参数用于标识规则是否下发给UPF。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |
| RULERANGE | 下发范围 | 可选必选说明：该参数在"DELIVERSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于标识规则的下发范围。<br>数据来源：全网规划<br>取值范围：<br>- CENTRAL（仅对中心UPF(主锚点UPF)生效）<br>- ALL（对所有UPF均生效）<br>默认值：无<br>配置原则：<br>该参数仅在DELIVERSW配置为“ENABLE”时生效。 |

## 操作的配置对象

- [UPF选择规则信息（SELECTRULEINFO）](configobject/UNC/20.15.2/SELECTRULEINFO.md)

## 使用实例

增加UPF选择规则信息，规则名称为"rulename1"，规则功能为重点业务保障：

```
ADD SELECTRULEINFO: RULENAME="rulename1", RULEFUNC=QOSANA-1&QOSEXP-0&QOSCCC-0&RELAY-0, PRIORITY=0,  DELIVERSW=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加UPF选择规则信息（ADD-SELECTRULEINFO）_44232737.md`
