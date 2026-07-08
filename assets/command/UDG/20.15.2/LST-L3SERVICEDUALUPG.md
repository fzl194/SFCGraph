---
id: UDG@20.15.2@MMLCommand@LST L3SERVICEDUALUPG
type: MMLCommand
name: LST L3SERVICEDUALUPG（查询微服务迁移过程）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: L3SERVICEDUALUPG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 灰度升级管理
- 微服务迁移过程
status: active
---

# LST L3SERVICEDUALUPG（查询微服务迁移过程）

## 功能

灰度升级中，执行此命令，用于查询微服务迁移过程。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@L3SERVICEDUALUPG]] · 一个微服务迁移流程（L3SERVICEDUALUPG）

## 使用实例

查询服务名为AM的微服务迁移流程信息：

```
%%LST L3SERVICEDUALUPG:;%%
RETCODE = 0  操作成功

结果如下
--------
 L3Service  =  AM
OldVersion  =  21.1
NewVersion  =  21.5
 OldPODNum  =  5
 NewPODNum  =  7
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-L3SERVICEDUALUPG.md`
