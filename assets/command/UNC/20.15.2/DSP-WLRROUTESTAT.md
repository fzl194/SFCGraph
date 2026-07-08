---
id: UNC@20.15.2@MMLCommand@DSP WLRROUTESTAT
type: MMLCommand
name: DSP WLRROUTESTAT（查询无线路由的路由统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: WLRROUTESTAT
command_category: 查询类
effect_mode: 立即生效
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

# DSP WLRROUTESTAT（查询无线路由的路由统计信息）

## 功能

该命令用于查询无线路由的路由统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/WLRROUTESTAT]] · 无线路由的路由统计信息（WLRROUTESTAT）

## 使用实例

查询无线路由的路由统计信息：

```
DSP WLRROUTESTAT: AFTYPE=ipv4unicast;
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
VPN实例名称          路由类型    路由总数    活跃路由数

_public_             WLR_UD       4           4
_public_             WLR_BH       4           4
_public_             WLR_SP       1           1
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询无线路由的路由统计信息（DSP-WLRROUTESTAT）_50281410.md`
