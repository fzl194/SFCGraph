---
id: UDG@20.15.2@MMLCommand@LST PUBCFGDOMAIN
type: MMLCommand
name: LST PUBCFGDOMAIN（查询域配置信息表）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PUBCFGDOMAIN
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 集中配置管理
- 公共配置域管理
status: active
---

# LST PUBCFGDOMAIN（查询域配置信息表）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

本命令用于查询网元已加入的配置域的名称。配置域也称之为集中配置管理组。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [公共配置域名称（PUBCFGDOMAIN）](configobject/UDG/20.15.2/PUBCFGDOMAIN.md)

## 使用实例

显示网元已加入的所有域的域信息：

```
LST PUBCFGDOMAIN:;
```

```

RETCODE = 0  操作成功。

公共配置域信息
-------------------------
域名称  

aaa            
bbb            
ccc            
ddd            
sss            
(Number of results = 5)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询域配置信息表（LST-PUBCFGDOMAIN）_68186120.md`
