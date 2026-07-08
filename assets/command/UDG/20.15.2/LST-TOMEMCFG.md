---
id: UDG@20.15.2@MMLCommand@LST TOMEMCFG
type: MMLCommand
name: LST TOMEMCFG（查询TCP Socket缓存配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOMEMCFG
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP Socket缓存配置
status: active
---

# LST TOMEMCFG（查询TCP Socket缓存配置）

## 功能

**适用NF：UPF**

该命令用于查询TCP socket配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOMEMCFG]] · TCP Socket缓存配置（TOMEMCFG）

## 使用实例

查询TCP Socket配置信息：

```
LST TOMEMCFG:;
```

```

RETCODE = 0  操作成功

TCP Socket配置
--------------
为TCP socket预留的接收缓存大小的最小值（字节） =  1310720
为TCP socket预留的接收缓存大小的默认值（字节） =  10485760
为TCP socket预留的发送缓存大小的最大值（字节） =  20971520
为TCP socket预留的发送缓存大小的最小值（字节） =  1310720
为TCP socket预留的发送缓存大小的默认值（字节） =  10485760
为TCP socket预留的发送缓存的大小最大值（字节） =  20971520    
应用层缓存开销的计算因子  =  5

(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TOMEMCFG.md`
