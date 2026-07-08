---
id: UDG@20.15.2@MMLCommand@RMV SSUPROTCOLGROUP
type: MMLCommand
name: RMV SSUPROTCOLGROUP（删除基于协议的质差检测策略）
nf: UDG
version: 20.15.2
verb: RMV
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

# RMV SSUPROTCOLGROUP（删除基于协议的质差检测策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除基于七层协议的质差判断策略。

## 注意事项

- 该命令执行后立即生效。
- DEFPRTGRPNAME如果在APPPOLICYCTRL中被绑定，需先解除绑定再删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEFPRTGRPNAME | 自定义协议组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定自定义的三级协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，不区分大小写，长度为1-63位。<br>默认值：无<br>配置原则：无 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定三级协议名称。<br>数据来源：本端规划<br>取值范围：参数来源于知识库中支持的三级协议名称。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SSUPROTCOLGROUP]] · 基于协议的质差检测策略（SSUPROTCOLGROUP）

## 使用实例

删除自定义协议组为testadc下协议为adc的基于协议的质差策略：

```
RMV SSUPROTCOLGROUP: DEFPRTGRPNAME="testadc", PROTOCOLNAME="adc";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除基于协议的质差检测策略（RMV-SSUPROTCOLGROUP）_09982392.md`
