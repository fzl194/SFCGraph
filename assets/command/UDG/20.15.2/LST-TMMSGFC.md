---
id: UDG@20.15.2@MMLCommand@LST TMMSGFC
type: MMLCommand
name: LST TMMSGFC（查询跟踪消息流控状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TMMSGFC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 消息跟踪
status: active
---

# LST TMMSGFC（查询跟踪消息流控状态）

## 功能

本命令用于查询跟踪消息流控状态。

> **说明**
> 无。

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TMMSGFC]] · 跟踪消息流控状态（TMMSGFC）

## 使用实例

查询跟踪消息流控状态：

```
%%LST TMMSGFC:;%%
RETCODE = 0  操作成功

跟踪消息流控状态
----------------
客户端启用流控  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TMMSGFC.md`
