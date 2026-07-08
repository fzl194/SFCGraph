---
id: UDG@20.15.2@MMLCommand@LST TOPROXYCFG
type: MMLCommand
name: LST TOPROXYCFG（查询TCP代理配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOPROXYCFG
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP代理配置
status: active
---

# LST TOPROXYCFG（查询TCP代理配置）

## 功能

**适用NF：UPF**

该命令用于查询TCP代理配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TOPROXYCFG]] · TCP代理配置（TOPROXYCFG）

## 使用实例

查询TCP代理配置信息：

```
LST TOPROXYCFG:;
```

```

RETCODE = 0  操作成功

TCP代理配置
-----------
TCP并行建链模式开关  =  ENABLE
延时关闭链接开关  =  ENABLE
非正常链路核查功能开关  =  ENABLE
UE侧KEEPALIVE功能开关  =  ENABLE
TCP Pacing功能开关  =  ENABLE
参数自适应功能开关  =  ENABLE
快速ACK开关  =  ENABLE
单次从TCP socket读取的报文数目  =  8
TCP代理收到异常ACK后回复ACK的数量  =  2147483647
TCP时间戳选项  =  0
每条流的初始RTT  =  50
每条流的初始RTTVAR  =  50
是否开启syncookies功能  =  ENABLE
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TOPROXYCFG.md`
