---
id: UDG@20.15.2@MMLCommand@DSP WLRATTRINFO
type: MMLCommand
name: DSP WLRATTRINFO（查询无线路由属性信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: WLRATTRINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示无线路由属性信息
status: active
---

# DSP WLRATTRINFO（查询无线路由属性信息）

## 功能

该命令用来查询无线路由属性信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用来指定VPN实例的地址族信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| VRFNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定VPN实例的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| ATTRID | 属性ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示路由的属性ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/WLRATTRINFO]] · 无线路由属性信息（WLRATTRINFO）

## 使用实例

查询无线路由属性信息：

```
DSP WLRATTRINFO: AFTYPE = ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
        地址族  =  IPv4单播
       VPN名称  =  _public_
        属性ID  =  1
        服务ID  =  1
负载分担策略ID  =  1
        元数据  =  1,0,0
      引用计数  =  1
      策略组标识 = 2
        团体属性 = 10 20 40 50
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询无线路由属性信息（DSP-WLRATTRINFO）_49802018.md`
