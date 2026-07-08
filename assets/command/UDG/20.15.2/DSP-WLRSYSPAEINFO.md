---
id: UDG@20.15.2@MMLCommand@DSP WLRSYSPAEINFO
type: MMLCommand
name: DSP WLRSYSPAEINFO（显示系统PAE信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: WLRSYSPAEINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示APP订阅信息
status: active
---

# DSP WLRSYSPAEINFO（显示系统PAE信息）

## 功能

该命令用于显示系统PAE信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [系统PAE信息（WLRSYSPAEINFO）](configobject/UDG/20.15.2/WLRSYSPAEINFO.md)

## 使用实例

显示系统PAE信息：

```
DSP WLRSYSPAEINFO:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
FEI PID     Partner状态      TB high    TB low    TP      状态     剩余时间      PAE延时定时器

0x7f4661    Avail            0          64        4098    S        0              FALSE
0x7f4666    Avail            0          65        4098    S        0              FALSE
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示系统PAE信息（DSP-WLRSYSPAEINFO）_00440977.md`
