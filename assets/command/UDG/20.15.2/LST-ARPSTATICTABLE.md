---
id: UDG@20.15.2@MMLCommand@LST ARPSTATICTABLE
type: MMLCommand
name: LST ARPSTATICTABLE（查询静态ARP表项）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ARPSTATICTABLE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP系统配置
status: active
---

# LST ARPSTATICTABLE（查询静态ARP表项）

## 功能

该命令用于查询ARP静态表项。

当设备上创建了ARP静态表项，可用该命令查询已创建的ARP静态表项信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP表项的VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，取值范围是1～31。<br>默认值：无 |
| IPADDR | IP地址 | 可选必选说明：可选参数<br>参数含义：该参数用于显示指定（目的）IPv4地址的ARP表项。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IP地址0.0.0.0～255.255.255.255。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ARPSTATICTABLE]] · 静态ARP表项（ARPSTATICTABLE）

## 使用实例

不指定参数时，查询VNFC上所有ARP静态表项：

```
LST ARPSTATICTABLE:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
     IP地址  =  10.1.1.2
  VLAN ID值  =  0
    MAC地址  =  00E0-FC12-3456
VPN实例名称  =  _public_
   接口名称  =  Ethernet64/0/3
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ARPSTATICTABLE.md`
