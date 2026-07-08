---
id: UDG@20.15.2@MMLCommand@LST MATCHPROTOCOL
type: MMLCommand
name: LST MATCHPROTOCOL（查询路由协议匹配路由策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MATCHPROTOCOL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 匹配路由协议
status: active
---

# LST MATCHPROTOCOL（查询路由协议匹配路由策略）

## 功能

该命令用于查询路由协议匹配路由策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：可选参数<br>参数含义：该参数用来表示路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MATCHPROTOCOL]] · 路由协议匹配路由策略（MATCHPROTOCOL）

## 使用实例

查询路由策略节点下的协议匹配路由策略：

```
LST MATCHPROTOCOL:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
路由策略名字    路由策略节点号    协议类型
policy          10                OSPF路由
policy1         9                 OSPF路由
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询路由协议匹配路由策略（LST-MATCHPROTOCOL）_00841217.md`
