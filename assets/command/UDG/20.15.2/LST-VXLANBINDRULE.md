---
id: UDG@20.15.2@MMLCommand@LST VXLANBINDRULE
type: MMLCommand
name: LST VXLANBINDRULE（查询VXLAN隧道组绑定Rule）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VXLANBINDRULE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VXLAN隧道绑定Rule
status: active
---

# LST VXLANBINDRULE（查询VXLAN隧道组绑定Rule）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询VXLAN隧道组与Rule的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULENAME | 规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数必须已经通过ADD RULE命令配置。<br>- ADD RULE命令中POLICYTYPE为WORKER，WORKERNAME为traffic-fd。其他类型的规则不能绑定VXLAN组。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VXLANBINDRULE]] · VXLAN隧道组绑定Rule（VXLANBINDRULE）

## 使用实例

查询所有与Rule绑定的VXLAN隧道组：

```
LST VXLANBINDRULE:;
```

```

RETCODE = 0 操作成功。

VXLAN隧道绑定Rule信息
----------------------------------
规则名称 = rule
VXLAN组名称 = vxlangrp2
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-VXLANBINDRULE.md`
