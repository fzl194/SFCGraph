---
id: UDG@20.15.2@MMLCommand@LST CPACCESSLISTFUNC
type: MMLCommand
name: LST CPACCESSLISTFUNC（查询CP白名单开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CPACCESSLISTFUNC
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- CP节点管理
- CP白名单开关配置
status: active
---

# LST CPACCESSLISTFUNC（查询CP白名单开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

此命令用于查询CP白名单功能的开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/CPACCESSLISTFUNC]] · CP白名单开关（CPACCESSLISTFUNC）

## 使用实例

查询系统是否支持CP白名单功能：

```
LST CPACCESSLISTFUNC:;
```

```

RETCODE = 0 操作成功.

CP白名单开关配置
-----------
开关标识 = 不使能
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CP白名单开关（LST-CPACCESSLISTFUNC）_86530397.md`
