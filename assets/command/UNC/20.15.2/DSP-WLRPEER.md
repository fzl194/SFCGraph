---
id: UNC@20.15.2@MMLCommand@DSP WLRPEER
type: MMLCommand
name: DSP WLRPEER（显示无线路由对端状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: WLRPEER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示无线路由相关信息
status: active
---

# DSP WLRPEER（显示无线路由对端状态）

## 功能

该命令用于显示无线路由对端状态。

## 注意事项

只有建立无线路由对端peer后才能使用该命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示路由的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |

## 操作的配置对象

- [无线路由对端状态（WLRPEER）](configobject/UNC/20.15.2/WLRPEER.md)

## 使用实例

显示无线路由对端状态：

```
DSP WLRPEER:AFTYPE=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
                 地址族  =  IPv4单播
                对端地址 =  10.1.1.10
               对端状态  =  UP
              对端状态机 =  NORMAL
                   标识  =  NULL
             批量版本号  =  1
                  事务号 =  0
                GR定时器 =  NOT RUN
        GR剩余时间（ms） =  0
              限制定时器 =  NOT RUN
      限制剩余时间（ms） =  0
                 前缀Job =  NOT RUN
                PAE组Job =  NOT RUN
                  用户ID =  0
              上次UP时间 =  2017-11-21 21:36:57
            上次DOWN时间 =  NULL
      上次老化路由的数量 =  0
      上次老化PAEG的数量 =  0
    上次老化引流表的数量 =  0
上次老化接口引流表的数量 =  0
                注册状态 =  REGISTED
 (结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示无线路由对端状态（DSP-WLRPEER）_00866097.md`
