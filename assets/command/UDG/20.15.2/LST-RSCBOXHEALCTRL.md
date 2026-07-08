---
id: UDG@20.15.2@MMLCommand@LST RSCBOXHEALCTRL
type: MMLCommand
name: LST RSCBOXHEALCTRL（查询ResourceBox自愈策略控制参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RSCBOXHEALCTRL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST RSCBOXHEALCTRL（查询ResourceBox自愈策略控制参数）

## 功能

该命令用于查询ResourceBox自愈策略控制参数。

> **说明**
> 该命令只适用于裸机容器云场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/RSCBOXHEALCTRL]] · ResourceBox自愈策略控制参数（RSCBOXHEALCTRL）

## 使用实例

查询ResourceBox自愈策略控制参数:

```
LST RSCBOXHEALCTRL:;
RETCODE = 0  操作成功

结果如下
--------
  ResourceBox全故障Node故障升级自愈控制 = 使能
  ResourceBox全故障Node正常升级自愈控制 = 使能
ResourceBox部分故障Node正常升级自愈控制 = 去使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ResourceBox自愈策略控制参数（LST-RSCBOXHEALCTRL）_50921273.md`
