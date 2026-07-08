---
id: UDG@20.15.2@MMLCommand@DSP WLRGLOBALINFO
type: MMLCommand
name: DSP WLRGLOBALINFO（查询无线路由全局信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: WLRGLOBALINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示无线路由全局信息
status: active
---

# DSP WLRGLOBALINFO（查询无线路由全局信息）

## 功能

该命令用于显示无线路由全局信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |

## 操作的配置对象

- [无线路由全局信息（WLRGLOBALINFO）](configobject/UDG/20.15.2/WLRGLOBALINFO.md)

## 使用实例

显示无线路由全局信息：

```
DSP WLRGLOBALINFO: AFTYPE=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
             组件PID    =  0x1da4653
             组件CID    =  0x81da4653
        逻辑路由器ID    =  0x0
        虚拟路由器ID    =  0x0
            组件状态    =  SMOOTH
          负载均衡数    =  1
            调试开关    =  OFF
       GR定时器（ms）   =  300000
  PAE延时定时器（ms）   =  30000
            前缀总数    =  0
    前缀超限告警上限    =  1000000
    前缀超限告警下限    =  950000
    前缀阈值告警上限    =  800000
    前缀阈值告警下限    =  700000
        性能打点开关    =  OFF
             PAE状态    =  Enabled
        最大流控数量    =  0
        当前流控数量    =  0
        升级引流状态    =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询无线路由全局信息（DSP-WLRGLOBALINFO）_00866353.md`
