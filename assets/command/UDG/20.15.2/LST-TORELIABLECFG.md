---
id: UDG@20.15.2@MMLCommand@LST TORELIABLECFG
type: MMLCommand
name: LST TORELIABLECFG（查询TCP可靠性配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TORELIABLECFG
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP可靠性配置
status: active
---

# LST TORELIABLECFG（查询TCP可靠性配置）

## 功能

**适用NF：UPF**

该命令用于查询TCP可靠性配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TORELIABLECFG]] · TCP可靠性配置（TORELIABLECFG）

## 使用实例

查询TCP可靠性配置信息：

```
LST TORELIABLECFG:;
```

```

RETCODE = 0  操作成功

TCP可靠性配置
-------------
TCP重试次数1  =  3
TCP重试次数2  =  5
TCP保活探测时间  =  480
TCP流中重排序的数据报最大数量  =  3
TCP的MTU探测功能  =  ENABLE
TCP流控策略  =  DISABLE
是否启动ER和TLP算法  =  3

(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询TCP可靠性配置（LST-TORELIABLECFG）_31379109.md`
