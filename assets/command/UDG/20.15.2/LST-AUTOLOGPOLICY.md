---
id: UDG@20.15.2@MMLCommand@LST AUTOLOGPOLICY
type: MMLCommand
name: LST AUTOLOGPOLICY（查询日志自动备份策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AUTOLOGPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# LST AUTOLOGPOLICY（查询日志自动备份策略）

## 功能

本命令用于请求系统显示已创建的日志自动备份策略。

> **说明**
> 无。

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/AUTOLOGPOLICY]] · 日志自动备份策略（AUTOLOGPOLICY）

## 使用实例

查询系统当前的日志自动备份策略信息：

```
%%LST AUTOLOGPOLICY:;%%
RETCODE = 0  操作成功
 
操作结果如下
------------
    备份周期(分)  =  30
SFTP服务器IP类型  =  IPV4
SFTP服务器IP地址  =  10.0.0.0
      SFTP用户名  =  root
        目标目录  =  /opt/test
        日志类型  =  操作日志&安全日志&系统日志
(结果个数 = 1)
 
---    END
```

```
%%LST AUTOLOGPOLICY:;%%
RETCODE = 0  操作成功

没有查到相应结果
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询日志自动备份策略（LST-AUTOLOGPOLICY）_89951696.md`
