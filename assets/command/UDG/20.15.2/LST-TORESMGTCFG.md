---
id: UDG@20.15.2@MMLCommand@LST TORESMGTCFG
type: MMLCommand
name: LST TORESMGTCFG（查询TCP资源管理配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TORESMGTCFG
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP资源管理配置
status: active
---

# LST TORESMGTCFG（查询TCP资源管理配置）

## 功能

**适用NF：UPF**

该命令用于查询TCP资源管理配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TORESMGTCFG]] · TCP资源管理配置（TORESMGTCFG）

## 使用实例

查询TCP资源管理配置信息：

```
LST TORESMGTCFG:;
```

```

RETCODE = 0  操作成功

TCP资源管理配置
---------------
重用处于time_wait的socket  =  ENABLE
TCP在FIN_WAIT_2状态的时间  =  3
应用层控制的FIN_WAIT_2状态存活时间的计算因子  =  3
TCP代理允许处于TIME_WAIT状态的socket个数的上限值  =  5000
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TORESMGTCFG.md`
