---
id: UNC@20.15.2@MMLCommand@LST OVERLOADRC
type: MMLCommand
name: LST OVERLOADRC（查询判断对端过载的返回码）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OVERLOADRC
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
- 过载返回码
status: active
---

# LST OVERLOADRC（查询判断对端过载的返回码）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来查询各个接口配置的过载返回码列表。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/OVERLOADRC]] · 判断对端过载的返回码（OVERLOADRC）

## 使用实例

查询当前各个接口配置的过载返回码列表：

```
LST OVERLOADRC:;
```

```

RETCODE = 0  操作成功。

判断对端过载的返回码
--------------------
接口类型    返回码1    直连Peer标记1    返回码2    直连Peer标记2    返回码3    直连Peer标记3    返回码4    直连Peer标记4    返回码5    直连Peer标记5

Gx          3004       否               0          否               0          否               0          否               0          否           
Gy          3004       否               0          否               0          否               0          否               0          否           
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询判断对端过载的返回码（LST-OVERLOADRC）_09896712.md`
