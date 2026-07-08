---
id: UNC@20.15.2@MMLCommand@LST DDNFLOWCTRL
type: MMLCommand
name: LST DDNFLOWCTRL（查询DDN流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DDNFLOWCTRL
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- DDN流控参数
status: active
---

# LST DDNFLOWCTRL（查询DDN流控参数）

## 功能

**适用NF：SMF、SGW-C**

该命令用于查询DDN流控参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [DDN流控参数（DDNFLOWCTRL）](configobject/UNC/20.15.2/DDNFLOWCTRL.md)

## 使用实例

查询DDN流控参数信息，执行如下命令：

```
%%LST DDNFLOWCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
Wal值  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DDN流控参数（LST-DDNFLOWCTRL）_64343879.md`
