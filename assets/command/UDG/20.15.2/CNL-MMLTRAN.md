---
id: UDG@20.15.2@MMLCommand@CNL MMLTRAN
type: MMLCommand
name: CNL MMLTRAN（取消配置）
nf: UDG
version: 20.15.2
verb: CNL
object_keyword: MMLTRAN
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 事务管理
status: active
---

# CNL MMLTRAN（取消配置）

## 功能

在启动事务模式后，期间下发的配置命令，如果需要取消配置，可以执行该命令进行配置回退。

> **说明**
> 无。

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/MMLTRAN]] · 取消配置（MMLTRAN）

## 使用实例

```
%%CNL MMLTRAN:;%%
RETCODE = 0  操作成功  

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/取消配置（CNL-MMLTRAN）_00282056.md`
