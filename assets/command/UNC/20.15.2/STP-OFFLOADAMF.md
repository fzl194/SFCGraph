---
id: UNC@20.15.2@MMLCommand@STP OFFLOADAMF
type: MMLCommand
name: STP OFFLOADAMF（停止AMF迁移任务）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: OFFLOADAMF
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF Pool 迁移控制
status: active
---

# STP OFFLOADAMF（停止AMF迁移任务）

## 功能

**适用NF：AMF**

此命令用于停止当前正在进行的迁移任务。

当需要发起新的迁移任务，执行“DSP OFFLOADAMF”命令查询是否有正在迁移的任务，如果有正在迁移的任务，执行此命令停止当前正在进行的迁移任务，再执行“STR OFFLOADAMF”发起新任务。

## 注意事项

- 该命令执行后立即生效。

- 此命令对类型为“IMSI(指定IMSI)”的迁移任务不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/OFFLOADAMF]] · AMF迁移任务（OFFLOADAMF）

## 使用实例

停止AMF迁移任务，执行如下命令：

```
STP OFFLOADAMF:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/停止AMF迁移任务（STP-OFFLOADAMF）_17555437.md`
