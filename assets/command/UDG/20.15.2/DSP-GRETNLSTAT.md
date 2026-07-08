---
id: UDG@20.15.2@MMLCommand@DSP GRETNLSTAT
type: MMLCommand
name: DSP GRETNLSTAT（查询GRE隧道数目）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: GRETNLSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- GRE调测
status: active
---

# DSP GRETNLSTAT（查询GRE隧道数目）

## 功能

该命令用于查询GRE隧道数目。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [GRE隧道数目（GRETNLSTAT）](configobject/UDG/20.15.2/GRETNLSTAT.md)

## 使用实例

查询GRE隧道数目：

```
DSP GRETNLSTAT:;
```

```

        RETCODE = 0  操作成功。

        结果如下
        --------
        IPv4 GRE隧道个数 = 1
        IPv6 GRE隧道个数 = 1

        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询GRE隧道数目（DSP-GRETNLSTAT）_00600385.md`
