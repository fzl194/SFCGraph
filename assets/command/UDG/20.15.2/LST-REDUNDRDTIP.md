---
id: UDG@20.15.2@MMLCommand@LST REDUNDRDTIP
type: MMLCommand
name: LST REDUNDRDTIP（查询冗余备份重定向IP）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: REDUNDRDTIP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 静态地址用户路由冗余
- 冗余备份重定向IP
status: active
---

# LST REDUNDRDTIP（查询冗余备份重定向IP）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询全局的冗余备份隧道虚拟重定向IP。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/REDUNDRDTIP]] · 冗余备份重定向IP（REDUNDRDTIP）

## 使用实例

查询冗余备份隧道虚拟重定向地址：

```
LST REDUNDRDTIP:;
```

```

RETCODE = 0 操作成功。

冗余备份重定向IP
----------------
IP版本 = IPv4
IPV4地址 = 192.168.0.1
IPV6地址 = ::
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-REDUNDRDTIP.md`
