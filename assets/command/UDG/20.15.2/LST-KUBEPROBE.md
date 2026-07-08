---
id: UDG@20.15.2@MMLCommand@LST KUBEPROBE
type: MMLCommand
name: LST KUBEPROBE（查询是否放通就绪状态检测）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: KUBEPROBE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST KUBEPROBE（查询是否放通就绪状态检测）

## 功能

该命令用于查询是否放通就绪状态检测。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/KUBEPROBE]] · 是否放通就绪状态检测（KUBEPROBE）

## 使用实例

查询是否放通就绪状态检测。

```
%%LST KUBEPROBE:;%%
RETCODE = 0  操作成功

结果如下
--------
                  是否检测就绪状态 = 开启
        特定网元下是否检测就绪状态 = 开启
 PSP平台大颗粒服务是否检测就绪状态 = 开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询是否放通就绪状态检测（LST-KUBEPROBE）_61502717.md`
