---
id: UDG@20.15.2@MMLCommand@LST GYONESHOT
type: MMLCommand
name: LST GYONESHOT（查询Gy一次重定向参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GYONESHOT
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- Gy接口一次重定向控制
- Gy接口一次重定向
status: active
---

# LST GYONESHOT（查询Gy一次重定向参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示配置的Gy接口一次重定向相关参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/GYONESHOT]] · Gy一次重定向参数（GYONESHOT）

## 使用实例

查询一次重定向的配置信息：

```
LST GYONESHOT:;
```

```

RETCODE = 0  操作成功。

Gy一次重定向参数信息
--------------------
       扩展过滤器名字 = test
  重定向完成时间（秒）= 15
   重定向携带信息名称 = test
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Gy一次重定向参数（LST-GYONESHOT）_86528909.md`
