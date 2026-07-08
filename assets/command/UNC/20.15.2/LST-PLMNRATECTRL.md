---
id: UNC@20.15.2@MMLCommand@LST PLMNRATECTRL
type: MMLCommand
name: LST PLMNRATECTRL（查询Serving PLMN速率控制配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PLMNRATECTRL
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 速率控制
- PLMN速率控制
- Serving PLMN速率控制配置
status: active
---

# LST PLMNRATECTRL（查询Serving PLMN速率控制配置）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于Serving PLMN速率控制开关的查询。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLMNRATECTRL]] · Serving PLMN速率控制配置（PLMNRATECTRL）

## 使用实例

Serving PLMN速率控制开关查询：

```
%%LST PLMNRATECTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
Serving PLMN速率控制开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Serving-PLMN速率控制配置（LST-PLMNRATECTRL）_64343890.md`
