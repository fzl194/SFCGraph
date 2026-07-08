---
id: UDG@20.15.2@MMLCommand@LST UEINJECTLIST
type: MMLCommand
name: LST UEINJECTLIST（查询UE灌包白名单）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UEINJECTLIST
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- UE侧连通性检测
- UE灌包白名单
status: active
---

# LST UEINJECTLIST（查询UE灌包白名单）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询白名单中的UE信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UEINJECTLIST]] · UE灌包白名单（UEINJECTLIST）

## 使用实例

查询UE下行灌包功能的白名单：

```
LST UEINJECTLIST:;
```

```

RETCODE = 0  操作成功。

UE 下行灌包白名单
-----------------
  用户标识  =  IMSI
用户ID信息  =  12345678901234
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询UE灌包白名单（LST-UEINJECTLIST）_82837104.md`
