---
id: UDG@20.15.2@MMLCommand@LST EPRPDYN
type: MMLCommand
name: LST EPRPDYN（查询EPRPDYN对象）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: EPRPDYN
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- EPRPDYN性能统计对象
status: active
---

# LST EPRPDYN（查询EPRPDYN对象）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询EPRPDYN对象。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACETYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：接口类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- S5S8PGW：接口类型为S5S8PGW，最大配置规格为12。<br>- S5S8SGW：接口类型为S5S8SGW，最大配置规格为12。<br>- N3UPF：接口类型为N3，最大配置规格为12。<br>- N9UPF：接口类型为N9，最大配置规格为12。<br>- S1USGW：接口类型为S1U，最大配置规格为12。<br>- S11USGW：接口类型为S11U，最大配置规格为12。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EPRPDYN]] · EPRPDYN对象（EPRPDYN）

## 使用实例

查询接口类型为S5S8PGW的EPRPDYN对象：

```
LST EPRPDYN: INTERFACETYPE=S5S8PGW;
```

```

RETCODE = 0  操作成功。

结果如下
--------
接口类型  =  S5S8PGW
对象名称  =  pgw1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询EPRPDYN对象（LST-EPRPDYN）_82837837.md`
