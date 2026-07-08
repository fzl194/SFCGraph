---
id: UDG@20.15.2@MMLCommand@ADD VXLANBINDRULE
type: MMLCommand
name: ADD VXLANBINDRULE（新增VXLAN隧道组绑定Rule）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: VXLANBINDRULE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 8000
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VXLAN隧道绑定Rule
status: active
---

# ADD VXLANBINDRULE（新增VXLAN隧道组绑定Rule）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置VXLAN隧道组与Rule的绑定关系。

## 注意事项

- 该命令最大记录数为8000。
- 执行该命令时，新增Rule绑定的Vxlan组会改变业务流的转发流程,匹配到该rule的数据报文会转发到MEP。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数必须已经通过ADD RULE命令配置。<br>- ADD RULE命令中POLICYTYPE为WORKER，WORKERNAME为traffic-fd。其他类型的规则不能绑定VXLAN组。 |
| VXLANGRPNAME | VXLAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数配置Vxlan组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数必须已经通过ADD VXLANGRP命令配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VXLANBINDRULE]] · VXLAN隧道组绑定Rule（VXLANBINDRULE）

## 使用实例

配置VXLAN隧道组与Rule的绑定关系，执行如下命令：

```
ADD VXLANBINDRULE: RULENAME="rule", VXLANGRPNAME="vxlangrp";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-VXLANBINDRULE.md`
