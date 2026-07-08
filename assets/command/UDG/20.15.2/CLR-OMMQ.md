---
id: UDG@20.15.2@MMLCommand@CLR OMMQ
type: MMLCommand
name: CLR OMMQ（清理OMMQ数据）
nf: UDG
version: 20.15.2
verb: CLR
object_keyword: OMMQ
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- OMMQ管理
status: active
---

# CLR OMMQ（清理OMMQ数据）

## 功能

![](清理OMMQ数据（CLR OMMQ）_00669142.assets/notice_3.0-zh-cn.png)

该命令执行可能会导致OMMQ数据丢失，在业务运行正常情况下请勿执行。

该命令用于OMMQ数据损坏后，恢复系统正常运行。

> **说明**
> 该命令执行时间较长，请耐心等待操作结果，请勿重复执行此命令。等待时间最长为180s。

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/OMMQ]] · 清理OMMQ数据（OMMQ）

## 使用实例

当OMMQ数据损坏时，清除OMMQ数据。

```
%%CLR OMMQ:;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清理OMMQ数据（CLR-OMMQ）_00669142.md`
