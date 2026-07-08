---
id: UNC@20.15.2@MMLCommand@LST CHGINITPRI
type: MMLCommand
name: LST CHGINITPRI（查询RADIUS计费和在线计费消息优先级）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGINITPRI
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 计费参数
status: active
---

# LST CHGINITPRI（查询RADIUS计费和在线计费消息优先级）

## 功能

**适用NF：PGW-C、SMF**

LST CHGINITPRI命令用来显示用户激活过程中RADIUS计费消息和在线计费消息交互优先级。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHGINITPRI]] · RADIUS计费和在线计费消息优先级（CHGINITPRI）

## 使用实例

查询RADIUS计费和在线计费消息优先级：

```
LST CHGINITPRI:;
```

```

RETCODE = 0  操作成功。

激活阶段计费模式优先
--------------------
RADIUS计费消息交互的优先级  =  1
  在线计费消息交互的优先级  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHGINITPRI.md`
