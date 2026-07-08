---
id: UDG@20.15.2@MMLCommand@DSP WLRPEERDATASTAT
type: MMLCommand
name: DSP WLRPEERDATASTAT（查询PEER相关数据的统计计数）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: WLRPEERDATASTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示无线路由统计信息
status: active
---

# DSP WLRPEERDATASTAT（查询PEER相关数据的统计计数）

## 功能

该命令用于查询PEER相关数据的统计计数。

## 注意事项

只有建立无线路由对端PEER后才能使用该命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/WLRPEERDATASTAT]] · PEER相关数据的统计计数（WLRPEERDATASTAT）

## 使用实例

查询PEER相关数据的统计计数：

```
DSP WLRPEERDATASTAT:ADDRESSFAMILY=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
--------
Peer地址    地址族      数据类型    新增的数目    删除的数目    修改的数目    老化的数目    失败的数目    缺失VPN的数目

10.1.1.1    IPv4单播    ROUTE       0             0             0             0             0             0
10.1.1.1    IPv4单播    PAEG        1             0             0             0             0             0
10.1.1.1    IPv4单播    FLOWRULE    1             0             1             0             0             0
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询PEER相关数据的统计计数（DSP-WLRPEERDATASTAT）_49801398.md`
