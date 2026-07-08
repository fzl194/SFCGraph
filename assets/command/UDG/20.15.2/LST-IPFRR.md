---
id: UDG@20.15.2@MMLCommand@LST IPFRR
type: MMLCommand
name: LST IPFRR（查询IP FRR）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPFRR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由基础
- 路由管控功能列表
status: active
---

# LST IPFRR（查询IP FRR）

## 功能

该命令用来查看当前设置的IP FRR功能情况。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：如果不配置此参数，则查询所有VPN的IP FRR功能情况。 |
| AFTYPE | 地址族 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址族类型。支持IPv4和IPv6单播地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无<br>配置原则：如果不配置此参数，则查询IPv4和IPv6单播地址族下的IP FRR功能情况。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPFRR]] · IP FRR（IPFRR）

## 使用实例

查询IPv4 FRR配置情况：

```
LST IPFRR:AFTYPE=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
地址族      VPN实例名称       是否使能FRR
IPv4单播    _public_          FALSE
IPv4单播    __mpp_vpn_inner__ TRUE
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IP-FRR（LST-IPFRR）_49960910.md`
