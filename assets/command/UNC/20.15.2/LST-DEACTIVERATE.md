---
id: UNC@20.15.2@MMLCommand@LST DEACTIVERATE
type: MMLCommand
name: LST DEACTIVERATE（查询去激活用户承载的速率）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DEACTIVERATE
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 去活PDP速率
status: active
---

# LST DEACTIVERATE（查询去激活用户承载的速率）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用来查询去激活用户承载的速率。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DEACTIVERATE]] · 去激活用户承载的速率（DEACTIVERATE）

## 使用实例

运营商配置了去活用户承载的速率，可以使用该命令来查询已配置的去活用户承载速率：

```
%%LST DEACTIVERATE:;%%
RETCODE = 0  操作成功

结果如下
--------
去活速率(个/秒)  =  1000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询去激活用户承载的速率（LST-DEACTIVERATE）_09652350.md`
