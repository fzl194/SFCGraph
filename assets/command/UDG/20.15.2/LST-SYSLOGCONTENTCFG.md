---
id: UDG@20.15.2@MMLCommand@LST SYSLOGCONTENTCFG
type: MMLCommand
name: LST SYSLOGCONTENTCFG（查询日志内容配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SYSLOGCONTENTCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# LST SYSLOGCONTENTCFG（查询日志内容配置）

## 功能

本命令用于查询系统上报给第三方Syslog服务器的日志内容配置。

日志内容配置可通过执行 [**SET SYSLOGCONTENTCFG**](设置日志内容配置（SET SYSLOGCONTENTCFG）_24521974.md) 命令进行操作。

> **说明**
> 无。

## 参数

无。

## 操作的配置对象

- [日志内容配置（SYSLOGCONTENTCFG）](configobject/UDG/20.15.2/SYSLOGCONTENTCFG.md)

## 使用实例

```
%%LST SYSLOGCONTENTCFG:;%%
RETCODE = 0  操作成功

操作结果如下
------------
报文头APP-NAME  =  日志类型
      报文头IP  =  -
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询日志内容配置（LST-SYSLOGCONTENTCFG）_51800805.md`
