---
id: UDG@20.15.2@MMLCommand@LST SRIPV6STATICSITE
type: MMLCommand
name: LST SRIPV6STATICSITE（查询IPv6静态路由全局属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SRIPV6STATICSITE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 静态路由管理
- IPv6静态路由全局属性管理
status: active
---

# LST SRIPV6STATICSITE（查询IPv6静态路由全局属性）

## 功能

该命令用来查询IPv6路由全局属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRIPV6STATICSITE]] · IPv6静态路由全局属性（SRIPV6STATICSITE）

## 使用实例

查询IPv6静态路由全局属性：

```
LST SRIPV6STATICSITE:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
      全局默认优先级  =  60
BFD最小接收间隔（ms） =  200
BFD最小传输间隔（ms） =  200
        本地检测倍数  =  3
      最大IPv6路由数  =  100000
      当前IPv6路由数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SRIPV6STATICSITE.md`
