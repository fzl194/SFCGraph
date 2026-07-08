---
id: UDG@20.15.2@MMLCommand@LST TRUNKATTR
type: MMLCommand
name: LST TRUNKATTR（查询宽带集群属性配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TRUNKATTR
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- 宽带集群管理
- 宽带集群属性配置
status: active
---

# LST TRUNKATTR（查询宽带集群属性配置）

## 功能

**适用NF：SGW-U、PGW-U**

该命令用于查询控制长时间处于空闲状态的集群用户进行去活处理功能的开关状态，以及是否配置GTP-U消息头中携带Sequence Number字段。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TRUNKATTR]] · 宽带集群属性配置（TRUNKATTR）

## 使用实例

查询控制长时间处于空闲状态的集群用户进行去活处理功能的开关状态，以及是否配置GTP-U消息头中携带Sequence Number字段：

```
LST TRUNKATTR:;
```

```

RETCODE = 0  操作成功

宽带集群功能配置
----------------
       空闲去活开关  =  不使能
Sequence Number开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TRUNKATTR.md`
