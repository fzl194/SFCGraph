---
id: UDG@20.15.2@MMLCommand@LST IMSBYPASS
type: MMLCommand
name: LST IMSBYPASS（显示IMS Bypass功能的相关参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IMSBYPASS
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- VOLTE管理
- IMS Bypass
status: active
---

# LST IMSBYPASS（显示IMS Bypass功能的相关参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询IMS Bypass功能的相关参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/IMSBYPASS]] · IMS Bypass功能的相关参数（IMSBYPASS）

## 使用实例

使用LST IMSBYPASS命令查询IMS Bypass功能的相关参数：

```
LST IMSBYPASS:;
```

```

RETCODE = 0  Operation succeeded

List IMS QoS URR reporting parameters
-------------------------------------
                        IMS Bypass switch  =  Disable
         URR-based QoS Flow Report Method  =  FLOW
Hysteresis Time for QoS type URR Stop (s)  =  0
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示IMS-Bypass功能的相关参数（LST-IMSBYPASS）_08806803.md`
