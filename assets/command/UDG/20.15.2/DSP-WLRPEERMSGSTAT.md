---
id: UDG@20.15.2@MMLCommand@DSP WLRPEERMSGSTAT
type: MMLCommand
name: DSP WLRPEERMSGSTAT（查询PEER有关消息的统计计数）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: WLRPEERMSGSTAT
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

# DSP WLRPEERMSGSTAT（查询PEER有关消息的统计计数）

## 功能

该命令用于查询PEER有关消息的统计计数。

## 注意事项

只有建立无线路由对端PEER后才能使用该命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：可选参数<br>参数含义：该参数用于表示地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无<br>配置原则：不输入的时候表示查询IPv4和IPv6地址族相关消息的总和。 |
| ISVERBOSE | 是否详细输出 | 可选必选说明：必选参数<br>参数含义：该参数用于表示是否详细输出。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [PEER有关消息的统计计数（WLRPEERMSGSTAT）](configobject/UDG/20.15.2/WLRPEERMSGSTAT.md)

## 使用实例

查询PEER有关消息的统计计数：

```
DSP WLRPEERMSGSTAT:ADDRESSFAMILY=ipv4unicast,ISVERBOSE=TRUE;
```

```

RETCODE = 0  操作成功

结果如下
--------
Peer地址    消息类型            接收的数目    接收失败的数目    发送的数目    发送失败的数目    重传的数目

10.1.1.1    REGISTER            3             0                 3             0                 0
10.1.1.1    BATCHBEGIN          3             0                 3             0                 0
10.1.1.1    BATCHEND            3             0                 3             0                 0
10.1.1.1    UPDATE              3             0                 3             0                 0
10.1.1.1    NOTIFY              0             0                 0             0                 0
10.1.1.1    SUBSCRIBE           4             0                 4             0                 0
10.1.1.1    SUBUPDATE           0             0                 0             0                 0
10.1.1.1    QUERYBGP            0             0                 0             0                 0
10.1.1.1    SMOOTHREQUEST       0             0                 0             0                 0
10.1.1.1    FLOWRULE            2             0                 2             0                 0
10.1.1.1    SERVICEADDRESS      2             0                 2             0                 0
10.1.1.1    FORWARDINGADDRESS   2             0                 2             0                 0
(结果个数 = 12)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询PEER有关消息的统计计数（DSP-WLRPEERMSGSTAT）_00441021.md`
