---
id: UNC@20.15.2@MMLCommand@LST NRFPATUPDIDXSW
type: MMLCommand
name: LST NRFPATUPDIDXSW（查询PATCH更新携带下标处理开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFPATUPDIDXSW
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- PATCH更新携带下标处理开关
status: active
---

# LST NRFPATUPDIDXSW（查询PATCH更新携带下标处理开关）

## 功能

**适用NF：NRF**

该命令用于查询NF PATCH更新，更新的信元路径是否可以携带下标。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFPATUPDIDXSW]] · PATCH更新携带下标处理开关（NRFPATUPDIDXSW）

## 使用实例

NF PATCH更新时，查询更新的信元路径是否可以携带下标，若开关打开，则更新的信元路径禁止携带下标；若开关关闭，则更新的信元路径允许携带下标。

```
LST NRFPATUPDIDXSW:;
%%LST NRFPATUPDIDXSW:;%%
RETCODE = 0  操作成功

结果如下
------------------------
禁止PATCH更新携带下标开关  =  关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PATCH更新携带下标处理开关（LST-NRFPATUPDIDXSW）_88377442.md`
