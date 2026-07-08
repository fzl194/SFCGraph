---
id: UDG@20.15.2@MMLCommand@LST SECND
type: MMLCommand
name: LST SECND（查询ND快回）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SECND
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略ND
status: active
---

# LST SECND（查询ND快回）

## 功能

该命令用来查询ND快回使能配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [ND快回（SECND）](configobject/UDG/20.15.2/SECND.md)

## 使用实例

查询ND快回使能配置：

```
LST SECND:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
使能标记    是
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ND快回（LST-SECND）_00441197.md`
