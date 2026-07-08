---
id: UDG@20.15.2@MMLCommand@LST UEINJECTSWITCH
type: MMLCommand
name: LST UEINJECTSWITCH（查询UE灌包开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UEINJECTSWITCH
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
- UE灌包功能
status: active
---

# LST UEINJECTSWITCH（查询UE灌包开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询UE下行灌包是否使能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UEINJECTSWITCH]] · UE灌包开关（UEINJECTSWITCH）

## 使用实例

查询UE下行灌包功能是否使能：

```
LST UEINJECTSWITCH:;
```

```

RETCODE = 0  操作成功。

UE下行灌包开关信息
------------------
开关标识  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UEINJECTSWITCH.md`
