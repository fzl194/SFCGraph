---
id: UDG@20.15.2@MMLCommand@LST IPSAGING
type: MMLCommand
name: LST IPSAGING（查询IPS老化配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPSAGING
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IP管理
- IP维护
status: active
---

# LST IPSAGING（查询IPS老化配置）

## 功能

该命令用于查询老化配置。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPSAGING]] · IPS老化配置（IPSAGING）

## 使用实例

查询IPS Aging配置：

```
LST IPSAGING:;

RETCODE = 0  操作成功

结果如下
-------------------------
              开启老化功能 =  TRUE
                老化阈值  =  5
              同步打包包数  =  10
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IPS老化配置（LST-IPSAGING）_14954720.md`
