---
id: UNC@20.15.2@MMLCommand@LST PDPCAR
type: MMLCommand
name: LST PDPCAR（查询PDP流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PDPCAR
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 数据转发管理
- 转发资源管理
- PDP资源管理
- PDP流控参数管理
status: active
---

# LST PDPCAR（查询PDP流控参数）

## 功能

**适用网元：SGSN**

该命令用于查询PDP流控参数配置表。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/PDPCAR]] · PDP流控参数（PDPCAR）

## 使用实例

查询PDP流量控制参数：

LST PDPCAR:;

```
%%LST PDPCAR:;%%
RETCODE = 0  操作成功。
输出结果如下
-------------------------
PDP流控开关  =  开
PDP流控倍数  =  1
PDP突发系数  =  9
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PDPCAR.md`
