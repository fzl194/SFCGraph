---
id: UDG@20.15.2@MMLCommand@LST TETHERDETGLBSW
type: MMLCommand
name: LST TETHERDETGLBSW（查询Tethering用户终端数量检测全局开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TETHERDETGLBSW
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- Tethering检测
- Tethering用户终端数量检测全局开关
status: active
---

# LST TETHERDETGLBSW（查询Tethering用户终端数量检测全局开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询Tethering用户终端数量检测全局开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [Tethering用户终端数量检测全局开关（TETHERDETGLBSW）](configobject/UDG/20.15.2/TETHERDETGLBSW.md)

## 使用实例

查询Tethering用户终端数量检测全局开关：

```
LST TETHERDETGLBSW:;
```

```

RETCODE = 0  操作成功。

Tethering 用户终端数量检测全局开关
-------------------------------------------------
开关表述  =  开启
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Tethering用户终端数量检测全局开关（LST-TETHERDETGLBSW）_82837449.md`
