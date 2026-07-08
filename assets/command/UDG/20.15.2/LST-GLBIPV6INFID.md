---
id: UDG@20.15.2@MMLCommand@LST GLBIPV6INFID
type: MMLCommand
name: LST GLBIPV6INFID（查询整机IPv6接口ID配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBIPV6INFID
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- IPv6接口标识管理
- 全局IPv6接口标识管理
status: active
---

# LST GLBIPV6INFID（查询整机IPv6接口ID配置）

## 功能

**适用NF：PGW-U、UPF**

此命令用于整机查询IMSI作为用户的IPv6地址interface ID(IPv6地址的后64位)功能开关配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLBIPV6INFID]] · 整机IPv6接口ID配置（GLBIPV6INFID）

## 使用实例

查询IMSI作为用户的IPv6地址interface ID(IPv6地址的后64位)功能配置：

```
LST GLBIPV6INFID:;
```

```

RETCODE = 0 操作成功。

整机IPv6接口ID配置
--------------------
配置IMSI作为IPv6 Interface ID  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GLBIPV6INFID.md`
