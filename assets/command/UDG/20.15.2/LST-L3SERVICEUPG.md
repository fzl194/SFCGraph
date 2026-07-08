---
id: UDG@20.15.2@MMLCommand@LST L3SERVICEUPG
type: MMLCommand
name: LST L3SERVICEUPG（查询服务升级进度）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: L3SERVICEUPG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 灰度升级管理
- 服务升级进度
status: active
---

# LST L3SERVICEUPG（查询服务升级进度）

## 功能

灰度升级中，执行此命令，用于查询服务升级进度。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@L3SERVICEUPG]] · 服务升级进度（L3SERVICEUPG）

## 使用实例

查询服务AM的升级进度：

```
%%LST L3SERVICEUPG:;%%
RETCODE = 0  操作成功

结果如下
--------
L3Service  =  AM
 Position  =  Service
     Mode  =  Gray
   Status  =  InUpgrade
 Progress  =  20
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-L3SERVICEUPG.md`
