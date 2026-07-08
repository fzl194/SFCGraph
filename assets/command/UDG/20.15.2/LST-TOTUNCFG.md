---
id: UDG@20.15.2@MMLCommand@LST TOTUNCFG
type: MMLCommand
name: LST TOTUNCFG（查询TCP Tun接口配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOTUNCFG
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP Tun接口配置
status: active
---

# LST TOTUNCFG（查询TCP Tun接口配置）

## 功能

**适用NF：UPF**

该命令用于查询TCP Tun接口配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TOTUNCFG]] · TCP Tun接口配置（TOTUNCFG）

## 使用实例

查询TCP Tun接口配置信息：

```
LST TOTUNCFG:;
```

```

RETCODE = 0  操作成功

TCP Tun接口配置
---------------
TUN_IN接口的GRO聚合功能开关  =  ENABLE
TUN_OUT接口的GSO聚合功能开关  =  ENABLE
休眠时间 =  10
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TOTUNCFG.md`
