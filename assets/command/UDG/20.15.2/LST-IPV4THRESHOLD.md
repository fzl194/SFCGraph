---
id: UDG@20.15.2@MMLCommand@LST IPV4THRESHOLD
type: MMLCommand
name: LST IPV4THRESHOLD（查询IPv4阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPV4THRESHOLD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由基础
- IPv4阈值
status: active
---

# LST IPV4THRESHOLD（查询IPv4阈值）

## 功能

该命令用于查询IPv4阈值，在整机路由前缀数量超过阈值时，上报告警，提示用户检查是否存在异常，提前干预。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPV4THRESHOLD]] · IPv4阈值（IPV4THRESHOLD）

## 使用实例

查询IPv4阈值：

```
LST IPV4THRESHOLD:;
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

- 原始手册：`evidence/UDG/20.15.2/查询IPv4阈值（LST-IPV4THRESHOLD）_50121214.md`
