---
id: UNC@20.15.2@MMLCommand@LST DIAMETERPARA
type: MMLCommand
name: LST DIAMETERPARA（查询Diameter参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DIAMETERPARA
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- 路由控制
- Diameter路由控制
status: active
---

# LST DIAMETERPARA（查询Diameter参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [Diameter参数（DIAMETERPARA）](configobject/UNC/20.15.2/DIAMETERPARA.md)

## 使用实例

查询当前是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送功能的配置信息：

```
LST DIAMETERPARA:;
```

```

RETCODE = 0  操作成功。

Diameter参数信息
----------------
基于域名的路由功能开关  =  允许
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Diameter参数（LST-DIAMETERPARA）_09897316.md`
