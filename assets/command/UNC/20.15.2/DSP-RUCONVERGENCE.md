---
id: UNC@20.15.2@MMLCommand@DSP RUCONVERGENCE
type: MMLCommand
name: DSP RUCONVERGENCE（显示汇聚RU信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RUCONVERGENCE
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 汇聚RU
status: active
---

# DSP RUCONVERGENCE（显示汇聚RU信息）

## 功能

**适用NF：NCG**

该命令用于显示RU分配信息。

## 注意事项

2345G混合部署的汇聚RU，不会分配业务RU。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [汇聚RU信息（RUCONVERGENCE）](configobject/UNC/20.15.2/RUCONVERGENCE.md)

## 使用实例

显示汇聚RU信息：

```
DSP RUCONVERGENCE:;
```

```
RETCODE = 0  操作成功。
结果如下:
---------
RU的ID  操作类型  RU角色  客户端数量  当前汇聚RUID  历史汇聚RUID  汇聚RUID状态  汇聚RU的TB值  当前RU的TB值  

64      注册      汇聚RU  30          0             0             正常          0             1033          
65      注册      业务RU  30          64            0             正常          1033          1036          
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示汇聚RU信息（DSP-RUCONVERGENCE）_83976188.md`
