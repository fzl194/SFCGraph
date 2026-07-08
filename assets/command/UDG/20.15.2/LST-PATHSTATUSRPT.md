---
id: UDG@20.15.2@MMLCommand@LST PATHSTATUSRPT
type: MMLCommand
name: LST PATHSTATUSRPT（查询用户面路径状态上报功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PATHSTATUSRPT
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- GTP路径管理
- GTP协议参数管理
- 用户面路径状态上报开关
status: active
---

# LST PATHSTATUSRPT（查询用户面路径状态上报功能）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询用户面路径故障/路径恢复上报开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [用户面路径状态上报功能（PATHSTATUSRPT）](configobject/UDG/20.15.2/PATHSTATUSRPT.md)

## 使用实例

查询用户面路径故障/路径恢复上报开关：

```
LST PATHSTATUSRPT:;
```

```

RETCODE = 0  操作成功

用户面路径状态上报功能
------------------
路径状态上报开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询用户面路径状态上报功能（LST-PATHSTATUSRPT）_19905872.md`
