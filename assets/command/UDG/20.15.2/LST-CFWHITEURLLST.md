---
id: UDG@20.15.2@MMLCommand@LST CFWHITEURLLST
type: MMLCommand
name: LST CFWHITEURLLST（查询URL过滤白名单列表）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CFWHITEURLLST
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- URL过滤白名单列表配置
status: active
---

# LST CFWHITEURLLST（查询URL过滤白名单列表）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询URL过滤白名单列表。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/CFWHITEURLLST]] · URL过滤白名单列表（CFWHITEURLLST）

## 使用实例

查询URL过滤白名单列表：

```
LST CFWHITEURLLST:;
```

```

RETCODE = 0  操作成功

URL过滤白名单列表信息
---------------------
URL过滤白名单名称  =  whitelist1
       配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询URL过滤白名单列表（LST-CFWHITEURLLST）_43518653.md`
