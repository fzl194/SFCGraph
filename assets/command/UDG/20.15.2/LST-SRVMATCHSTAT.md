---
id: UDG@20.15.2@MMLCommand@LST SRVMATCHSTAT
type: MMLCommand
name: LST SRVMATCHSTAT（查询业务匹配统计参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SRVMATCHSTAT
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 业务匹配统计配置
status: active
---

# LST SRVMATCHSTAT（查询业务匹配统计参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询是否使能业务匹配的统计功能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRVMATCHSTAT]] · 业务匹配统计参数（SRVMATCHSTAT）

## 使用实例

查询是否使能业务匹配的统计功能：

```
LST SRVMATCHSTAT:;
```

```

RETCODE = 0  操作成功。

业务匹配统计功能信息
--------------------
开关  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SRVMATCHSTAT.md`
