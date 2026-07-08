---
id: UDG@20.15.2@MMLCommand@LST ECHOIPLIST
type: MMLCommand
name: LST ECHOIPLIST（查询GTP路径管理IP地址）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ECHOIPLIST
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- GTP路径管理
- GTP协议参数管理
- 路径地址列表
status: active
---

# LST ECHOIPLIST（查询GTP路径管理IP地址）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询GTP路径管理的黑白名单控制的IP地址段。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [GTP路径管理IP地址（ECHOIPLIST）](configobject/UDG/20.15.2/ECHOIPLIST.md)

## 使用实例

查询GTP路径管理的黑白名单控制的IP地址段信息：

```
LST ECHOIPLIST:;
```

```

RETCODE = 0  操作成功。

Echo List
---------
IP地址版本类型  =  IPV4
IP地址段的地址  =  10.36.0.2
      掩码长度  =  27
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询GTP路径管理IP地址（LST-ECHOIPLIST）_82837221.md`
