---
id: UDG@20.15.2@MMLCommand@LST ADDRESSATTR
type: MMLCommand
name: LST ADDRESSATTR（查询AddressAttr配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ADDRESSATTR
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
- 全局地址分配属性配置
status: active
---

# LST ADDRESSATTR（查询AddressAttr配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询全局地址分配属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/ADDRESSATTR]] · AddressAttr配置（ADDRESSATTR）

## 使用实例

查询全局地址分配属性：

```
LST ADDRESSATTR:;
```

```

返回值 = 0  操作成功

全局地址分配属性
-----------------------------------
IPv4地址池通配功能开关  =  ENABLE
IPv6地址池通配功能开关  =  DISABLE
         地址租期（秒） =  30
  IPv4主机路由发布开关  =  ENABLE
  IPv6主机路由发布开关  =  ENABLE
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询AddressAttr配置（LST-ADDRESSATTR）_05977154.md`
