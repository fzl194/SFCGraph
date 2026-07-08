---
id: UDG@20.15.2@MMLCommand@LST VOLTEMOSEVAL
type: MMLCommand
name: LST VOLTEMOSEVAL（查询VoLTE AMR编解码的语音质量采用的评估方式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VOLTEMOSEVAL
command_category: 查询类
applicable_nf:
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- Volte MOS 评估方式
status: active
---

# LST VOLTEMOSEVAL（查询VoLTE AMR编解码的语音质量采用的评估方式）

## 功能

**适用NF：PGW-U**

该命令用于查询VoLTE AMR编解码的语音质量采用的评估方式。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [VoLTE AMR编解码的语音质量采用的评估方式（VOLTEMOSEVAL）](configobject/UDG/20.15.2/VOLTEMOSEVAL.md)

## 使用实例

查询VoLTE AMR编解码的语音质量采用的评估方式：

```
LST VOLTEMOSEVAL:;
```

```

RETCODE = 0 操作成功

显示Mos评估方式
---------------
评估方式 = POLQA_SWB_AMR
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询VoLTE-AMR编解码的语音质量采用的评估方式（LST-VOLTEMOSEVAL）_63753119.md`
