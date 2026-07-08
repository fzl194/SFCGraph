---
id: UDG@20.15.2@MMLCommand@LST DNSLITEPARA
type: MMLCommand
name: LST DNSLITEPARA（显示轻量DNS参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DNSLITEPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务公共参数管理
- 轻量DNS参数
status: active
---

# LST DNSLITEPARA（显示轻量DNS参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示轻量DNS参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DNSLITEPARA]] · 轻量DNS参数（DNSLITEPARA）

## 使用实例

查询轻量DNS参数：

```
LST DNSLITEPARA:;
```

```

RETCODE = 0  操作成功。

轻量DNS参数
------------------------
轻量DNS规则匹配开关  =  使能
轻量DNS策略执行开关  =  使能
DNS规则状态控制开关  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-DNSLITEPARA.md`
