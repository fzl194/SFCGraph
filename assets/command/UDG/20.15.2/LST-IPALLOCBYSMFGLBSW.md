---
id: UDG@20.15.2@MMLCommand@LST IPALLOCBYSMFGLBSW
type: MMLCommand
name: LST IPALLOCBYSMFGLBSW（显示基于SMF分配地址的全局开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPALLOCBYSMFGLBSW
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
- 基于SMF分配地址开关
status: active
---

# LST IPALLOCBYSMFGLBSW（显示基于SMF分配地址的全局开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示基于SMF分配地址的全局开关。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPALLOCBYSMFGLBSW]] · 基于SMF分配地址的全局开关（IPALLOCBYSMFGLBSW）

## 使用实例

查询基于SMF分配地址的全局开关：

```
LST IPALLOCBYSMFGLBSW:;
```

```

RETCODE = 0 操作成功。

基于SMF分配地址全局开关
-----------------------------------------------
IPv4开关 = 使能
IPv6开关 = 使能
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示基于SMF分配地址的全局开关（LST-IPALLOCBYSMFGLBSW）_82837158.md`
