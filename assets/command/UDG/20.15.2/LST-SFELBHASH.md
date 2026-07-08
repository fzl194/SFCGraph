---
id: UDG@20.15.2@MMLCommand@LST SFELBHASH
type: MMLCommand
name: LST SFELBHASH（查询IP转发负载分担hash计算模式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SFELBHASH
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP性能配置
- IP转发负载分担hash模式配置
status: active
---

# LST SFELBHASH（查询IP转发负载分担hash计算模式）

## 功能

该命令用于查询IP转发负载分担hash计算模式。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。
- 该命令仅支持发往Fabric口方向的报文做负载分担hash。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFELBHASH]] · IP转发负载分担hash计算模式（SFELBHASH）

## 使用实例

查询负载分担hash计算模式：

```
LST SFELBHASH:;
```

```

RETCODE = 0 操作成功。

结果如下
-------------------------
  报文类型  = IP报文
  hash类型  = 三元组
(结果个数 = 1)
--- 结束
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IP转发负载分担hash计算模式（LST-SFELBHASH）_00866021.md`
