---
id: UDG@20.15.2@MMLCommand@DSP SFEFIB
type: MMLCommand
name: DSP SFEFIB（显示FIB表项信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFEFIB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- FIB表项统计
status: active
---

# DSP SFEFIB（显示FIB表项信息）

## 功能

该命令用于显示SFE FIB表项。

通过显示FIB表项，可以了解公网、私网路由信息等情况。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| DESTIP | 目的IP | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询表项中的目的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DESTIPMASKLEN | 目的IP掩码长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询表项中的IP地址掩码长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFEFIB]] · FIB表项信息（SFEFIB）

## 使用实例

显示指定资源单元的FIB表：

```
DSP SFEFIB:RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```

RETCODE = 0  操作成功。

结果如下
--------
目的IP             下一跳IP     BGP下一跳IP    VLAN编号    间接ID数量    FIB数量    其他FIB数量    时间戳        MPLS转发MTU值    原始AS域    Tunnel的ID值    内层标签    间接ID       标签    AT索引    路由标志    VPN名称     接口名称    选项标志    是否详细信息    目的IP掩码         目的IP掩码长度    备份间接ID    备份间接ID数量    备份下一跳IP    备份接口名称    备份上行标签    备份标签    VPN备份下一跳IP    VPN备份接口名称

10.25.255.255      10.0.0.1     0.0.0.0        0           1             4          0              1525818737    0                0           0x0             0x0         0x100000B    0x0     0x0       HU          _public_    InLoop0     0           0               255.255.255.255    32                0x0           0                 0.0.0.0         [No Intf]       0x0             0x0         0.0.0.0            [No Intf]      
10.25.25.25        10.0.0.1     0.0.0.0        0           1             4          0              1525818737    0                0           0x0             0x0         0x100000B    0x0     0x0       HU          _public_    InLoop0     0           0               255.255.255.255    32                0x0           0                 0.0.0.0         [No Intf]       0x0             0x0         0.0.0.0            [No Intf]      
172.31.0.1         172.31.1.1   0.0.0.0        0           1             4          0              1525818737    0                0           0x0             0x0         0x100000B    0x0     0x0       HU          _public_    InLoop0     0           0               255.255.255.255    32                0x0           0                 0.0.0.0         [No Intf]       0x0             0x0         0.0.0.0            [No Intf]      
172.16.0.1         172.31.1.1   0.0.0.0        0           1             4          0              1525818737    0                0           0x0             0x0         0x1000013    0x0     0x0       HU          _public_    InLoop0     0           0               255.0.0.0          8                 0x0           0                 0.0.0.0         [No Intf]       0x0             0x0         0.0.0.0            [No Intf]      
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示FIB表项信息（DSP-SFEFIB）_50280738.md`
