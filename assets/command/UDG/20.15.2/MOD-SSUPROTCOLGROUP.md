---
id: UDG@20.15.2@MMLCommand@MOD SSUPROTCOLGROUP
type: MMLCommand
name: MOD SSUPROTCOLGROUP（修改基于协议的质差检测策略）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: SSUPROTCOLGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 智能板管理
- vvip
- 基于协议的质差策略
status: active
---

# MOD SSUPROTCOLGROUP（修改基于协议的质差检测策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改基于七层协议的质差判断策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEFPRTGRPNAME | 自定义协议组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定自定义的三级协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，不区分大小写，长度为1-63位。<br>默认值：无<br>配置原则：无 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定三级协议名称。<br>数据来源：本端规划<br>取值范围：参数来源于知识库中支持的三级协议名称。<br>默认值：无<br>配置原则：无 |
| POLICYCNDNAME | 策略参数名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要绑定的策略参数名。<br>数据来源：本端规划<br>取值范围：参数来源于ADD POLICYCONDITION中的POLICYCNDNAME。<br>默认值：无<br>配置原则：无 |
| QOEDETECTCOND | 业务流量特征 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进行质差判断的业务流量特征。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL_CHECK：均进行质差判断。<br>- UP_BIGFLOW_CHECK：只对上行速率大于下行速率的业务进行质差判断。<br>- DOWN_BIGFLOW_CHECK：只对下行速率大于上行速率的业务进行质差判断。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [基于协议的质差检测策略（SSUPROTCOLGROUP）](configobject/UDG/20.15.2/SSUPROTCOLGROUP.md)

## 使用实例

修改自定义协议组名称为ssuprotcolgroupname下协议名称为http的质差检测策略为policyname2：

```
MOD SSUPROTCOLGROUP: DEFPRTGRPNAME="ssuprotclogroupname", PROTOCOLNAME="http", POLICYCNDNAME="policyname2";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改基于协议的质差检测策略（MOD-SSUPROTCOLGROUP）_15739991.md`
