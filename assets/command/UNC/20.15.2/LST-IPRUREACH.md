---
id: UNC@20.15.2@MMLCommand@LST IPRUREACH
type: MMLCommand
name: LST IPRUREACH（查询RU到网关的可达性检测配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPRUREACH
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 无线路由管理
- RU到网关的可达性
status: active
---

# LST IPRUREACH（查询RU到网关的可达性检测配置）

## 功能

该命令用于查询RU到网关可达性的检测配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| IPVERSION | IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用来表示网关地址的IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| SOURCERU | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～49。<br>默认值：无 |

## 操作的配置对象

- [RU到网关的可达性检测配置（IPRUREACH）](configobject/UNC/20.15.2/IPRUREACH.md)

## 使用实例

查询RU到网关可达性检测的配置：

```
LST IPRUREACH:VPNNAME="vrf";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
      VPN实例名称  =  vrf
           地址族  =  IPv4单播
         目的地址  =  10.1.1.1
           RU名称  =  VNODE_VNRS_VNFC_IPU_0066
      BFD会话名称  =  test
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RU到网关的可达性检测配置（LST-IPRUREACH）_00440741.md`
