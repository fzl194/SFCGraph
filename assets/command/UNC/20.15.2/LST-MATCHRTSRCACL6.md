---
id: UNC@20.15.2@MMLCommand@LST MATCHRTSRCACL6
type: MMLCommand
name: LST MATCHRTSRCACL6（查询匹配IPv6源路由地址ACL）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MATCHRTSRCACL6
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 匹配IPv6源路由地址ACL
status: active
---

# LST MATCHRTSRCACL6（查询匹配IPv6源路由地址ACL）

## 功能

该命令用于查询基于IPv6信息的ACL匹配源路由的配置结果。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置操作的路由策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MATCHRTSRCACL6]] · 匹配IPv6源路由地址ACL（MATCHRTSRCACL6）

## 使用实例

查询IPv6下Acl过滤器匹配源路由的配置信息：

```
LST MATCHRTSRCACL6:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
  路由策略名字  =  a
路由策略节点号  =  19
ACL名字或ACL号  =  a
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询匹配IPv6源路由地址ACL（LST-MATCHRTSRCACL6）_49961766.md`
