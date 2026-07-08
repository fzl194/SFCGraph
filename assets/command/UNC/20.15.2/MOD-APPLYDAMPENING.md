---
id: UNC@20.15.2@MMLCommand@MOD APPLYDAMPENING
type: MMLCommand
name: MOD APPLYDAMPENING（修改Dampening设置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APPLYDAMPENING
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 应用Dampening
status: active
---

# MOD APPLYDAMPENING（修改Dampening设置）

## 功能

该命令用于修改应用Dampening。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：区分大小写。 |
| NODESEQUENCE | 路由策略节点ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| HALFLIFEVALUE | 路由半生命时期（分钟） | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由半生命时期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～45。<br>默认值：无<br>配置原则：单位为分钟。 |
| REUSEVALUE | 路由再生极限 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由再生极限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20000。<br>默认值：无 |
| SUPPRESSVALUE | 路由抑制极限 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由抑制极限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20000。<br>默认值：无<br>配置原则：实际配置的值必须大于REUSEVALUE的值。 |
| CEILINGVALUE | 路由极限 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由极限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1001～20000。<br>默认值：无<br>配置原则：实际配置的值必须大于SUPPRESSVALUE。 |

## 操作的配置对象

- [Dampening设置（APPLYDAMPENING）](configobject/UNC/20.15.2/APPLYDAMPENING.md)

## 使用实例

修改EBGP路由的衰减参数的设置：

```
MOD APPLYDAMPENING:POLICYNAME="a",NODESEQUENCE=10,SUPPRESSVALUE=4000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Dampening设置（MOD-APPLYDAMPENING）_50121498.md`
