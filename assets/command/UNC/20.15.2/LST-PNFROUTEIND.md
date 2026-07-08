---
id: UNC@20.15.2@MMLCommand@LST PNFROUTEIND
type: MMLCommand
name: LST PNFROUTEIND（查询对端NF的路由指示信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFROUTEIND
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF路由标识信息
status: active
---

# LST PNFROUTEIND（查询对端NF的路由指示信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询本地配置的远端NF实例支持的路由指示信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFROUTEIND]] · 对端NF的路由指示信息（PNFROUTEIND）

## 使用实例

查询对端NF路由指示信息。

```
%%LST PNFROUTEIND:;%%
RETCODE = 0 操作成功

结果如下
------------------------
  NF实例标识 = ausf_instance_0
    路由指示 = 0000
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询对端NF的路由指示信息（LST-PNFROUTEIND）_09653249.md`
