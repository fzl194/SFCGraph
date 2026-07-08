---
id: UDG@20.15.2@MMLCommand@LST UPINITSETUP
type: MMLCommand
name: LST UPINITSETUP（显示主被动切换）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPINITSETUP
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
- UP信息管理
- UP主动被动建联开关
status: active
---

# LST UPINITSETUP（显示主被动切换）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询是否主动发起建立偶联的配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [主被动切换（UPINITSETUP）](configobject/UDG/20.15.2/UPINITSETUP.md)

## 使用实例

查询是否主动发起建立偶联的配置：

```
LST UPINITSETUP:;
```

```

RETCODE = 0  操作成功

主被动切换。
-----------------------------
UP 切换  =  ENABLE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示主被动切换（LST-UPINITSETUP）_82837254.md`
