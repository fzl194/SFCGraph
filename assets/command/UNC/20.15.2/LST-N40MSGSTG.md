---
id: UNC@20.15.2@MMLCommand@LST N40MSGSTG
type: MMLCommand
name: LST N40MSGSTG（查询缓存开关、回放间隔、回放速率）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N40MSGSTG
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 融合计费消息缓存
status: active
---

# LST N40MSGSTG（查询缓存开关、回放间隔、回放速率）

## 功能

**适用NF：SMF、PGW-C**

该命令用于查询缓存开关、回放间隔、回放速率。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/N40MSGSTG]] · 缓存开关、回放间隔、回放速率（N40MSGSTG）

## 使用实例

查询缓存开关、回放间隔、回放速率

```
%%LST N40MSGSTG:;%%
RETCODE = 0  操作成功

结果如下
--------
            融合计费消息缓存开关  =  不使能
融合计费消息回放的最小间隔(分钟)  =  30
   融合计费消息回放的速率(个/秒)  =  500
                        加密开关  =  不使能
             缓存Tx定时器时长(秒) = 15
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询缓存开关、回放间隔、回放速率（LST-N40MSGSTG）_34667402.md`
