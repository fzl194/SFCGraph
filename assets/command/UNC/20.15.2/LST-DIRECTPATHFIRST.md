---
id: UNC@20.15.2@MMLCommand@LST DIRECTPATHFIRST
type: MMLCommand
name: LST DIRECTPATHFIRST（查询直连路径优先开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DIRECTPATHFIRST
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- 路由控制
- 路径选择控制
status: active
---

# LST DIRECTPATHFIRST（查询直连路径优先开关）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查询Diameter会话的CCR-U/T消息是否始终通过CCR-I的发送路径发送。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [直连路径优先开关（DIRECTPATHFIRST）](configobject/UNC/20.15.2/DIRECTPATHFIRST.md)

## 使用实例

查询直连路径优先开关参数：

```
LST DIRECTPATHFIRST:;
```

```

RETCODE = 0 操作成功

直连路径优先开关参数
--------------------
Gx接口直连路径优先开关 = 允许
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询直连路径优先开关（LST-DIRECTPATHFIRST）_61818782.md`
