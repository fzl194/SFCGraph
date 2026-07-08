---
id: UNC@20.15.2@MMLCommand@LST DHCP6CLIENT
type: MMLCommand
name: LST DHCP6CLIENT（查询DHCPv6客户端配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DHCP6CLIENT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- DHCP管理
- DHCPv6客户端配置
status: active
---

# LST DHCP6CLIENT（查询DHCPv6客户端配置）

## 功能

该命令用于查询DHCPv6客户端的配置信息。

## 注意事项

该命令在Ethernet接口上配置执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [DHCPv6客户端（DHCP6CLIENT）](configobject/UNC/20.15.2/DHCP6CLIENT.md)

## 使用实例

查询当前DHCPv6客户端的配置：

```
LST DHCP6CLIENT: IFNAME="Ethernet64/0/4";
```

```

RETCODE = 0  操作成功

结果如下
--------
                接口名称  =  Ethernet64/0/4
        DHCPv6客户端使能  =  TRUE
                地址模式  =  主机地址模式
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DHCPv6客户端配置（LST-DHCP6CLIENT）_00866313.md`
