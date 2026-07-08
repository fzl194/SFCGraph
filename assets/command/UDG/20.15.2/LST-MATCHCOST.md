---
id: UDG@20.15.2@MMLCommand@LST MATCHCOST
type: MMLCommand
name: LST MATCHCOST（查询Cost匹配路由策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MATCHCOST
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 匹配路由开销
status: active
---

# LST MATCHCOST（查询Cost匹配路由策略）

## 功能

该命令用于查询匹配路由开销值的配置结果。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MATCHCOST]] · Cost匹配路由策略（MATCHCOST）

## 使用实例

查询匹配路由开销值配置信息：

```
LST MATCHCOST:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
  路由策略名字  =  a
路由策略节点号  =  19
       Cost值   =  19
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-MATCHCOST.md`
