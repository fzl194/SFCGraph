---
id: UDG@20.15.2@MMLCommand@DSP CONNDOWN
type: MMLCommand
name: DSP CONNDOWN（显示连接中断信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CONNDOWN
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Diameter管理
- 连接Down记录
status: active
---

# DSP CONNDOWN（显示连接中断信息）

## 功能

该命令用于显示Diameter连接中断信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CONNDOWN]] · 连接中断信息（CONNDOWN）

## 使用实例

显示Diameter连接中断信息：

```
DSP CONNDOWN:;
```

```

RETCODE = 0 操作成功

结果如下
------------------------
本地角色  本端地址         远端地址          连接ID          断连原因            断连时间               创建时间

服务端    10.1.1.10        10.1.1.9          3               客户端删除          2017-01-24 03:00:56    2017-01-24 02:55:50
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-CONNDOWN.md`
