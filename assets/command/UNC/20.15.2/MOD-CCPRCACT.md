---
id: UNC@20.15.2@MMLCommand@MOD CCPRCACT
type: MMLCommand
name: MOD CCPRCACT（修改融合计费Proxy结果码处理动作）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CCPRCACT
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 融合计费Proxy结果码处理动作
status: active
---

# MOD CCPRCACT（修改融合计费Proxy结果码处理动作）

## 功能

**适用NF：NCG**

该命令用于修改融合计费Proxy结果码处理动作。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RCTYPE | RC类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RC的类型。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（针对未指定的异常返回码设置处理动作）<br>- VALUE（针对指定异常返回码设置处理动作）<br>- TIMEOUT（等待响应超时）<br>- LINKFAULT（链路不可达）<br>默认值：无<br>配置原则：无 |
| CODETYPE | 指定异常返回码类型 | 可选必选说明：该参数在"RCTYPE"配置为"VALUE"时为条件必选参数。<br>参数含义：该参数用于指定异常返回码的类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是300~999，65535，0。<br>默认值：无<br>配置原则：无 |
| FOTNM | Failover模板标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定融合计费Proxy Failover模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |
| PEERUNAVAILABLE | 代表对端不可用 | 可选必选说明：该参数在"RCTYPE"配置为"VALUE"时为条件可选参数。<br>参数含义：该参数用于标识该指定异常返回码是否代表对端不可用。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：<br>FALSE表示不代表对端不可用。<br>TRUE表示代表对端不可用。 |

## 操作的配置对象

- [融合计费Proxy结果码处理动作（CCPRCACT）](configobject/UNC/20.15.2/CCPRCACT.md)

## 使用实例

修改指定异常返回码类型为“900”的融合计费Proxy结果码处理动作，设置Failover模板标识为“ccpfot2”：

```
MOD CCPRCACT: RCTYPE=VALUE, CODETYPE=900, FOTNM="ccpfot2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改融合计费Proxy结果码处理动作（MOD-CCPRCACT）_45110926.md`
