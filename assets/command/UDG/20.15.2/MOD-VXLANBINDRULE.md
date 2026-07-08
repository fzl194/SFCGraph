---
id: UDG@20.15.2@MMLCommand@MOD VXLANBINDRULE
type: MMLCommand
name: MOD VXLANBINDRULE（修改VXLAN隧道组绑定Rule）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: VXLANBINDRULE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VXLAN隧道绑定Rule
status: active
---

# MOD VXLANBINDRULE（修改VXLAN隧道组绑定Rule）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改VXLAN隧道组与Rule的绑定关系。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令时，修改Rule绑定的Vxlan组会改变业务流的转发流程,匹配到该rule的数据报文会转发到新的MEP。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数必须已经通过ADD RULE命令配置。<br>- ADD RULE命令中POLICYTYPE为WORKER，WORKERNAME为traffic-fd。其他类型的规则不能绑定VXLAN组。 |
| VXLANGRPNAME | VXLAN组名称 | 可选必选说明：可选参数<br>参数含义：该参数配置Vxlan组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：输入空格提示操作异常。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VXLANBINDRULE]] · VXLAN隧道组绑定Rule（VXLANBINDRULE）

## 使用实例

修改与testrule绑定的VXLAN隧道组为vxlangrp2：

```
MOD VXLANBINDRULE: RULENAME="rule", VXLANGRPNAME="vxlangrp2";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-VXLANBINDRULE.md`
