---
id: UDG@20.15.2@MMLCommand@LST NGLANFUNC
type: MMLCommand
name: LST NGLANFUNC（查询5G LAN功能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NGLANFUNC
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN基础配置
- 5G LAN功能开关
status: active
---

# LST NGLANFUNC（查询5G LAN功能配置）

## 功能

**适用NF：UPF**

该命令用于查询5G LAN功能开关状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/NGLANFUNC]] · 5G LAN功能配置（NGLANFUNC）

## 使用实例

查询5G LAN功能开关：

```
LST NGLANFUNC:;
```

```

返回值 = 0  操作成功

5G LAN 功能配置
-----------------------------
5G LAN 功能开关  =  开启
N19数据转发开关  =  开启
(结果数= 1)

---    结束
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询5G-LAN功能配置（LST-NGLANFUNC）_20154433.md`
