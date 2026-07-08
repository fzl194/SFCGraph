---
id: UDG@20.15.2@MMLCommand@LST GLBSMFATTR
type: MMLCommand
name: LST GLBSMFATTR（查询全局SMF属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBSMFATTR
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- 对端SMF属性
status: active
---

# LST GLBSMFATTR（查询全局SMF属性）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询UPF对接SMF是否为同一供应商提供的设备。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLBSMFATTR]] · 全局SMF属性（GLBSMFATTR）

## 使用实例

UPF对接SMF是否为同一供应商提供的设备：

```
LST GLBSMFATTR:;
```

```

RETCODE = 0  操作成功。

SMF属性
-------------
SMF是否为同一供应商  =  否
UPF去活会话  =  使能
N4计费上报消息冲突检查时长 = 0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GLBSMFATTR.md`
