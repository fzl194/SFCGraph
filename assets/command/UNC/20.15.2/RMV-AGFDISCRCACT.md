---
id: UNC@20.15.2@MMLCommand@RMV AGFDISCRCACT
type: MMLCommand
name: RMV AGFDISCRCACT（删除AGF基于TOPO异常响应处理动作）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AGFDISCRCACT
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- AGF基于TOPO异常响应处理动作
status: active
---

# RMV AGFDISCRCACT（删除AGF基于TOPO异常响应处理动作）

## 功能

**适用NF：NCG**

该命令用于删除AGF基于TOPO异常响应处理动作。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RCTYPE | RC类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RC的类型。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（针对未指定的异常返回码设置处理动作）<br>- VALUE（针对指定异常返回码设置处理动作）<br>- TIMEOUT（等待响应超时）<br>默认值：无<br>配置原则：无 |
| CODETYPE | 指定异常返回码类型 | 可选必选说明：该参数在"RCTYPE"配置为"VALUE"时为条件必选参数。<br>参数含义：该参数用于指定异常返回码的类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是300~999，0~10。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AGFDISCRCACT]] · AGF基于TOPO异常响应处理动作（AGFDISCRCACT）

## 使用实例

删除指定异常返回码类型为“900”的结果码处理动作：

```
RMV AGFDISCRCACT: RCTYPE=VALUE, CODETYPE=900;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-AGFDISCRCACT.md`
