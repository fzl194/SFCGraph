---
id: UDG@20.15.2@MMLCommand@LST UEPINGINF
type: MMLCommand
name: LST UEPINGINF（查询UE Ping逻辑接口开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UEPINGINF
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- UEPing逻辑接口控制
status: active
---

# LST UEPINGINF（查询UE Ping逻辑接口开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询UE ping逻辑口的开关状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UEPINGINF]] · UE Ping逻辑接口开关（UEPINGINF）

## 使用实例

查询UE ping逻辑口的开关状态：

```
LST UEPINGINF:;
```

```

RETCODE = 0  操作成功。

UE Ping逻辑接口开关
-------------------
Ping开关  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UEPINGINF.md`
