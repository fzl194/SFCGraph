---
id: UNC@20.15.2@MMLCommand@LST CONFCTRL
type: MMLCommand
name: LST CONFCTRL（查看冲突控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CONFCTRL
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话流程控制管理
- 会话流程冲突控制
status: active
---

# LST CONFCTRL（查看冲突控制参数）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询低优先级流程消息的缓存重发次数和缓存重发时间间隔。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CONFCTRL]] · 查看冲突控制参数（CONFCTRL）

## 使用实例

查询缓存重发次数和缓存重发时间间隔：

```
%%LST CONFCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
       EPS消息缓存重发的次数  =  3
EPS消息缓存重发的时间间隔(s)  =  2
        NR消息缓存重发的次数  =  3
 NR消息缓存重发的时间间隔(s)  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CONFCTRL.md`
