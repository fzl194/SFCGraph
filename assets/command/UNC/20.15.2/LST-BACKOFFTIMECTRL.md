---
id: UNC@20.15.2@MMLCommand@LST BACKOFFTIMECTRL
type: MMLCommand
name: LST BACKOFFTIMECTRL（查询异常场景的Back-off Time开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BACKOFFTIMECTRL
command_category: 查询类
applicable_nf:
- GGSN
- PGW-C
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- 异常场景的Back-off Time开关
status: active
---

# LST BACKOFFTIMECTRL（查询异常场景的Back-off Time开关）

## 功能

**适用NF：GGSN、PGW-C、SGW-C**

该命令用来查询异常场景下激活响应中携带Back-off Time开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/BACKOFFTIMECTRL]] · 异常场景的Back-off Time开关（BACKOFFTIMECTRL）

## 使用实例

查询异常场景的携带Back-off Time的开关：

```
%%LST BACKOFFTIMECTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
 控制APN锁定导致激活失败应答消息中携带Back-off Time字段的开关  =  不使能
           控制激活应答消息中携带GGSN Back-off Time字段的开关  =  不使能
控制承载受限导致激活失败应答消息中携带Back-off Time字段的开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询异常场景的Back-off-Time开关（LST-BACKOFFTIMECTRL）_96242091.md`
