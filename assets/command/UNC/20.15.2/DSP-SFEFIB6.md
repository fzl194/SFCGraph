---
id: UNC@20.15.2@MMLCommand@DSP SFEFIB6
type: MMLCommand
name: DSP SFEFIB6（查询IPv6的FIB表项信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SFEFIB6
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

# DSP SFEFIB6（查询IPv6的FIB表项信息）

## 功能

该命令用于查询IPv6的FIB表项信息。通过显示FIB表项，可以了解公网、私网路由信息等情况。FIB6用于保存报文转发信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称，可使用命令DSP RU查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| DESTIPV6 | 目的IP | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询表项中的目的地IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| DESTIPMASKLEN | 目的IP前缀长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询表项中的目的地IPv6地址前缀长度。该参数下发时必须带上参数DESTIPV6。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN名称。该参数下发时必须带上参数DESTIPV6。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFEFIB6]] · IPv6的FIB表项信息（SFEFIB6）

## 使用实例

查询IPv6的FIB表项信息：

```
DSP SFEFIB6 : RUNAME="VNODE_VNRS_VNFC_IPU_0067";
```

```

RETCODE = 0  操作成功。   

结果如下
--------
VLAN编号    目的IP      下一跳IP    BGP下一跳IP    间接ID数量    FIB数量    其他FIB数量    时间戳                 原始AS域    Tunnel的ID值    内层标签    间接ID       AT索引    路由标志    VPN名称     接口名称     目的IP前缀长度    备份间接ID    备份间接ID数量    备份下一跳IP    备份接口名称    备份内层标签    备份Tunnel的ID值    VPN FRR备份下一跳IP    VPN FRR备份接口名称

0          2001:db8::1    2001:db8::2    ::             1             3          0              2018-05-08 23:13:07    0           0x0             0x0         0x1000032    0x0       U           _public_    Eth67/0/8    100               0x0           0                 ::              [No Intf]       0x0             0x0                 ::                     [No Intf]          
0          2001:db8::3    2001:db8::4    ::             1             3          0              2018-05-08 23:13:07    0           0x0             0x0         0x100002a    0x0       HU          _public_    Eth67/0/8    128               0x0           0                 ::              [No Intf]       0x0             0x0                 ::                     [No Intf]          
0          2001:db8::5      ::          ::             1             3          0              2018-05-08 23:13:06    0           0x0             0x0         0x1000009    0x0       BU          _public_    NULL0        10                0x0           0                 ::              [No Intf]       0x0             0x0                 ::                     [No Intf]          
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SFEFIB6.md`
