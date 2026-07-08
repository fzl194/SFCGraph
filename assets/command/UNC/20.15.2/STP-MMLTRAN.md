---
id: UNC@20.15.2@MMLCommand@STP MMLTRAN
type: MMLCommand
name: STP MMLTRAN（结束事务模式）
nf: UNC
version: 20.15.2
verb: STP
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

# STP MMLTRAN（结束事务模式）

## 功能

执行该命令后，会结束事务模式。

## 注意事项

- 未启动事务模式，执行该命令**STP MMLTRAN**，会执行失败。
- 如果在事务模式下，已经下发过配置命令，没有进行提交配置或者取消配置，该命令会执行失败。

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMLTRAN]] · 取消配置（MMLTRAN）

## 使用实例

```
%%STP MMLTRAN:;%% 
RETCODE = 0  操作成功  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/结束事务模式（STP-MMLTRAN）_47082049.md`
