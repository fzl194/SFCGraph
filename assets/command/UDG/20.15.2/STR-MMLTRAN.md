---
id: UDG@20.15.2@MMLCommand@STR MMLTRAN
type: MMLCommand
name: STR MMLTRAN（启动事务模式）
nf: UDG
version: 20.15.2
verb: STR
object_keyword: MMLTRAN
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 事务管理
status: active
---

# STR MMLTRAN（启动事务模式）

## 功能

执行该命令后，会启动事务模式，在该模式下，下发给管道的配置类命令只有在执行提交配置命令 **CMT MMLTRAN** 后才会真正生效。

> **说明**
> - 如果已经开始事务模式，再次下发该命令**STR MMLTRAN**，按照操作成功处理。
> - 如果在事务模式下，已经下发过配置命令，再次下发该命令**STR MMLTRAN**对已经下发的配置命令无影响。

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MMLTRAN]] · 取消配置（MMLTRAN）

## 使用实例

```
%%STR MMLTRAN:;%% 
RETCODE = 0  操作成功  

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/STR-MMLTRAN.md`
