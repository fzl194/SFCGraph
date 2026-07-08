---
id: UDG@20.15.2@MMLCommand@LST UPETHSRVPARA
type: MMLCommand
name: LST UPETHSRVPARA（查询用户面以太业务参数配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPETHSRVPARA
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 用户面以太业务参数配置
status: active
---

# LST UPETHSRVPARA（查询用户面以太业务参数配置）

## 功能

**适用NF：UPF**

该命令用于查询用户面以太业务相关参数配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPETHSRVPARA]] · 用户面以太业务参数配置（UPETHSRVPARA）

## 使用实例

查询用户面以太业务相关参数配置：

```
LST UPETHSRVPARA:;
```

```

RETCODE = 0 操作成功。

用户面以太业务参数配置
-----------------
用户面以太业务开关  =  ENABLE          
用户面以太业务MAC地址  =  10-11-11-11-11-11
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询用户面以太业务参数配置（LST-UPETHSRVPARA）_75556851.md`
