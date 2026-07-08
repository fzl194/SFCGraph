---
id: UDG@20.15.2@MMLCommand@SYNC FILE
type: MMLCommand
name: SYNC FILE（多节点文件同步）
nf: UDG
version: 20.15.2
verb: SYNC
object_keyword: FILE
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 文件传输
status: active
---

# SYNC FILE（多节点文件同步）

## 功能

将多个节点的文件进行同步，使得整个文件系统的数据保持一致。

> **说明**
> 无。

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FILE]] · 文件传输（FILE）

## 使用实例

同步文件系统的异常文件：

```
%%SYNC FILE:;%%
RETCODE = 0  操作成功

进度报告
--------
已完成 = 0%
(结果个数 = 1)

---    END

%%SYNC FILE:;%%
RETCODE = 0  操作成功

进度报告
--------
已完成 = 100%
(结果个数 = 1)

---    END

%%SYNC FILE:;%%
RETCODE = 0  操作成功

同步结果
--------
删除文件  =  0
同步文件  =  0
(结果个数 = 1)

共有3个报告
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SYNC-FILE.md`
