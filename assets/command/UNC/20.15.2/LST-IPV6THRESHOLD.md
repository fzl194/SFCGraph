---
id: UNC@20.15.2@MMLCommand@LST IPV6THRESHOLD
type: MMLCommand
name: LST IPV6THRESHOLD（查询IPv6阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPV6THRESHOLD
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由基础
- IPv6阈值
status: active
---

# LST IPV6THRESHOLD（查询IPv6阈值）

## 功能

该命令用来查询IPv6整机路由前缀阈值告警的阈值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPV6THRESHOLD]] · IPv6阈值（IPV6THRESHOLD）

## 使用实例

查询IPv6整机路由前缀阈值告警的阈值：

```
LST IPV6THRESHOLD:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
最大百分比（%） =  80
最小百分比（%） =  70
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IPv6阈值（LST-IPV6THRESHOLD）_50281398.md`
