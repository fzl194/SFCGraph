---
id: UDG@20.15.2@MMLCommand@LST GIREDIRECTFUNC
type: MMLCommand
name: LST GIREDIRECTFUNC（查询全局Gi重定向信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GIREDIRECTFUNC
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- Gi重定向
- Gi重定向功能
status: active
---

# LST GIREDIRECTFUNC（查询全局Gi重定向信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询全局IPv4和IPv6 Gi重定向开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/GIREDIRECTFUNC]] · 全局Gi重定向信息（GIREDIRECTFUNC）

## 使用实例

查询IPv4和IPv6 Gi重定向全局开关：

```
LST GIREDIRECTFUNC:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
IPV4全局Gi重定向开关  =  使能
IPV6全局Gi重定向开关  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GIREDIRECTFUNC.md`
