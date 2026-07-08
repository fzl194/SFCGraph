---
id: UDG@20.15.2@MMLCommand@LST IPALLOCRULE
type: MMLCommand
name: LST IPALLOCRULE（显示地址分配规则）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPALLOCRULE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 地址分配规则
status: active
---

# LST IPALLOCRULE（显示地址分配规则）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示全局地址分配规则。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPALLOCRULE]] · 地址分配规则（IPALLOCRULE）

## 使用实例

查询全局地址分配规则：

```
LST IPALLOCRULE:;
```

```

RETCODE = 0 操作成功。

地址分配规则
---------------------
IPv4第一级规则开关 = 使能
IPv4第一级规则 = APN & SMF
IPv4第二级规则开关 = 使能
IPv4第二级规则 = SMF
IPv4第三级规则开关 = 不使能
IPv4第三级规则 = NULL
IPv6第一级规则开关 = 使能
IPv6第一级规则 = APN & SMF
IPv6第二级规则开关 = 使能
IPv6第二级规则 = SMF
IPv6第三级规则开关 = 不使能
IPv6第三级规则 = NULL
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IPALLOCRULE.md`
