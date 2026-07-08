---
id: UNC@20.15.2@MMLCommand@DSP WLRSMOOTHSTAT
type: MMLCommand
name: DSP WLRSMOOTHSTAT（查询无线路由与对端平滑状态机状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: WLRSMOOTHSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示无线路由平滑状态机信息
status: active
---

# DSP WLRSMOOTHSTAT（查询无线路由与对端平滑状态机状态）

## 功能

该命令用于查询无线路由与对端平滑开始、结束时间以及平滑状态机类型和状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| PEERIP | 对端地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示对端地址。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～64。IP地址。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/WLRSMOOTHSTAT]] · 无线路由与对端平滑状态机状态（WLRSMOOTHSTAT）

## 使用实例

显示无线路由平滑状态机的状态：

```
DSP WLRSMOOTHSTAT:AFTYPE=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
地址族         对端地址      状态机类型    状态机状态    上次开始时间           上次结束时间
IPv4单播       10.1.1.100    ROUTE         NORMAL        2017-11-21 21:37:22    2017-11-21 21:37:52
IPv4单播       10.1.1.100    PAEG          NORMAL        2017-11-21 21:37:02    2017-11-21 21:37:42
IPv4单播       10.1.1.100    FLOWRULE      NORMAL        2017-11-21 21:37:21    2017-11-21 21:37:36
 (结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询无线路由与对端平滑状态机状态（DSP-WLRSMOOTHSTAT）_49801426.md`
