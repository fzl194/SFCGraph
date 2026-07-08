---
id: UNC@20.15.2@MMLCommand@DSP CHARGECONFLICT
type: MMLCommand
name: DSP CHARGECONFLICT（查询计费配置冲突）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CHARGECONFLICT
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
- 离线计费
- 离线计费维护
- 查看冲突配置
status: active
---

# DSP CHARGECONFLICT（查询计费配置冲突）

## 功能

**适用NF：PGW-C、SMF**

命令用来查询当前系统中是否存在与业务有冲突的配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [计费配置冲突（CHARGECONFLICT）](configobject/UNC/20.15.2/CHARGECONFLICT.md)

## 使用实例

查询系统中的计费配置冲突：

```
DSP CHARGECONFLICT:;
```

```

结果如下
------------------------
计费属性 = 0x0800
用户模板名称 = up1
APN名称 = apn2
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询计费配置冲突（DSP-CHARGECONFLICT）_09897020.md`
