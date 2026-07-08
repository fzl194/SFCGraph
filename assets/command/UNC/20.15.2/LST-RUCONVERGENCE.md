---
id: UNC@20.15.2@MMLCommand@LST RUCONVERGENCE
type: MMLCommand
name: LST RUCONVERGENCE（查询汇聚RU信息）
nf: UNC
version: 20.15.2
verb: LST
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

# LST RUCONVERGENCE（查询汇聚RU信息）

## 功能

**适用NF：NCG**

该命令用于查询RU分配信息。

## 注意事项

- 2345G混合部署的汇聚RU，不会分配业务RU。
- LST命令只会查出MOD命令设置的分配规则。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [汇聚RU信息（RUCONVERGENCE）](configobject/UNC/20.15.2/RUCONVERGENCE.md)

## 使用实例

查询汇聚RU信息：

```
LST RUCONVERGENCE:;
```

```
RETCODE = 0  操作成功。
结果如下:
---------
      RU的ID  =  65
      RU角色  =  业务RU
当前汇聚RUID  =  65
历史汇聚RUID  =  64
汇聚RUID状态  =  正常
    处理模式  =  设置规则
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询汇聚RU信息（LST-RUCONVERGENCE）_26952596.md`
