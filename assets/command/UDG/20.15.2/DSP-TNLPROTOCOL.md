---
id: UDG@20.15.2@MMLCommand@DSP TNLPROTOCOL
type: MMLCommand
name: DSP TNLPROTOCOL（显示隧道协议）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TNLPROTOCOL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- VPN隧道管理
- 隧道协议
status: active
---

# DSP TNLPROTOCOL（显示隧道协议）

## 功能

该命令用于显示隧道协议。

## 注意事项

只有配置隧道才能使用该命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TNLPROTOCOL]] · 隧道协议（TNLPROTOCOL）

## 使用实例

显示隧道协议：

```
DSP TNLPROTOCOL:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
接口名字    隧道类型
Tunnel0     Gre
Tunnel1     Gre
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-TNLPROTOCOL.md`
