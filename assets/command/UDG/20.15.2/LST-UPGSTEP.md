---
id: UDG@20.15.2@MMLCommand@LST UPGSTEP
type: MMLCommand
name: LST UPGSTEP（查询灰度升级Pod滚动步长）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPGSTEP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 灰度升级管理
- 灰度升级步长
status: active
---

# LST UPGSTEP（查询灰度升级Pod滚动步长）

## 功能

灰度升级阶段，执行此命令，用于显示灰度升级Pod滚动步长。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPGSTEP]] · 灰度升级Pod滚动步长（UPGSTEP）

## 使用实例

查询灰度升级各Pod类型的冗余资源比例：

```
%%LST UPGSTEP:;%%
RETCODE = 0  操作成功

结果如下
--------
升级POD类型  冗余资源比例  

业务服务     50            
链路类服务   25            
cslb+ip      25            
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询灰度升级Pod滚动步长（LST-UPGSTEP）_88662248.md`
