---
id: UDG@20.15.2@MMLCommand@LST NGLANCHGCTRL
type: MMLCommand
name: LST NGLANCHGCTRL（查询5G LAN计费控制相关参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NGLANCHGCTRL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN计费控制信息
status: active
---

# LST NGLANCHGCTRL（查询5G LAN计费控制相关参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询5G LAN计费控制相关参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NGLANCHGCTRL]] · 5G LAN计费控制相关参数（NGLANCHGCTRL）

## 使用实例

查询5G LAN计费控制相关参数：

```
LST NGLANCHGCTRL:;
```

```

RETCODE = 0  操作成功

5GLAN计费控制相关参数信息
----------------------
                    5GLAN 本地离线计费策略开关  =  是
(结果数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-NGLANCHGCTRL.md`
