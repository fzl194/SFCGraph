---
id: UDG@20.15.2@MMLCommand@LST VPNAPPCFG
type: MMLCommand
name: LST VPNAPPCFG（查询下发的VPN的app类型信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VPNAPPCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# LST VPNAPPCFG（查询下发的VPN的app类型信息）

## 功能

查询下发的VPN的app类型信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VPNAPPCFG]] · 下发的VPN的app类型信息（VPNAPPCFG）

## 使用实例

使用如下命令查询下发的VPN的app类型信息：

```
%%LST VPNAPPCFG:;%%
RETCODE = 0  操作成功

结果如下
--------
VPN名称  =  vpna
App类型  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-VPNAPPCFG.md`
