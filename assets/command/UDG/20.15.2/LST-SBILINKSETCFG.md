---
id: UDG@20.15.2@MMLCommand@LST SBILINKSETCFG
type: MMLCommand
name: LST SBILINKSETCFG（查询服务化接口链路集属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SBILINKSETCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口链路集管理
status: active
---

# LST SBILINKSETCFG（查询服务化接口链路集属性）

## 功能

该命令用于查询服务化接口链路集的属性配置信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/SBILINKSETCFG]] · 服务化接口链路集属性（SBILINKSETCFG）

## 使用实例

查询服务化接口链路集的属性配置，可以用如下命令：

```
%%LST SBILINKSETCFG:;%%
RETCODE = 0  操作成功

结果如下
--------
链路集老化时间(小时) = 10
FQDN周期性检查开关 = ON
进程内链路集故障阈值 = 50
系统内链路集故障阈值 = 20
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询服务化接口链路集属性（LST-SBILINKSETCFG）_83653660.md`
