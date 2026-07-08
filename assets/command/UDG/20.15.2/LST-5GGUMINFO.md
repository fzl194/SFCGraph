---
id: UDG@20.15.2@MMLCommand@LST 5GGUMINFO
type: MMLCommand
name: LST 5GGUMINFO（查询灰度升级所处于的阶段）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: 5GGUMINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 灰度升级管理
- 灰度升级批次
status: active
---

# LST 5GGUMINFO（查询灰度升级所处于的阶段）

## 功能

灰度升级阶段，执行此命令，用于显示灰度升级正在进行的阶段。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [灰度升级所处于的阶段（5GGUMINFO）](configobject/UDG/20.15.2/5GGUMINFO.md)

## 使用实例

显示灰度升级阶段：

```
%%LST 5GGUMINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
阶段  =  PreUpgrade
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询灰度升级所处于的阶段（LST-5GGUMINFO）_88343780.md`
