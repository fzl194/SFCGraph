---
id: UNC@20.15.2@MMLCommand@LST ANONYMOUSAPN
type: MMLCommand
name: LST ANONYMOUSAPN（查询匿名APN配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ANONYMOUSAPN
command_category: 查询类
applicable_nf:
- SMF
- GGSN
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- 匿名APN
status: active
---

# LST ANONYMOUSAPN（查询匿名APN配置）

## 功能

**适用NF：SMF、GGSN、PGW-C**

该命令用来查询匿名APN接入功能的相关配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ANONYMOUSAPN]] · 匿名APN配置（ANONYMOUSAPN）

## 使用实例

查询匿名APN接入功能的相关配置。

```
%%LST ANONYMOUSAPN:;%%
RETCODE = 0  操作成功
结果如下
--------
     本地用户开关 = 不使能
     拜访用户开关 = 不使能
     漫游用户开关 = 使能
本地用户纠错后APN = NULL
漫游用户纠错后APN = isp
拜访用户纠错后APN = NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ANONYMOUSAPN.md`
