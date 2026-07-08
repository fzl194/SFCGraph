---
id: UDG@20.15.2@MMLCommand@SET DHCP6CLIENTDUID
type: MMLCommand
name: SET DHCP6CLIENTDUID（设置DHCPv6客户端DUID生成方式）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: DHCP6CLIENTDUID
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- DHCP管理
- DHCPv6客户端DUID生成模式
status: active
---

# SET DHCP6CLIENTDUID（设置DHCPv6客户端DUID生成方式）

## 功能

该命令用于设置DHCPv6客户端的DHCPv6唯一标识符DUID（DHCPv6 unique identifier）的生成方式。配置该命令后，设备上新增的DHCPv6客户端将按设置的方式生成DUID。

## 注意事项

- 该命令执行后立即生效。
- 更改DUID生成方式后，只有新增DHCPv6客户端才会按新方式生成DUID，已存在DHCPv6客户端的DUID不发生变化。
- 当指定DUID的生成方式为链路地址加虚拟局域网标识号时，如果删除接口下的虚拟局域网标识号配置时，接口下DHCPv6客户端的相关配置会关联删除。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| DUIDTYPE |
| --- |
| MAC_PLUS_VLAN |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DUIDTYPE | DUID生成方式 | 可选必选说明：必选参数<br>参数含义：该参数用于标识DUID的生成方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MAC_PLUS_INTERFACE：链路地址加接口名模式。<br>- MAC_PLUS_VLAN：链路地址加虚拟局域网标识号模式。<br>默认值：无 |

## 操作的配置对象

- [DHCPv6客户端DUID生成方式（DHCP6CLIENTDUID）](configobject/UDG/20.15.2/DHCP6CLIENTDUID.md)

## 使用实例

配置DUID生成方式为MAC_PLUS_VLAN：

```
SET DHCP6CLIENTDUID: DUIDTYPE=MAC_PLUS_VLAN;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置DHCPv6客户端DUID生成方式（SET-DHCP6CLIENTDUID）_66567276.md`
