---
id: UDG@20.15.2@MMLCommand@DSP SECCARTAB
type: MMLCommand
name: DSP SECCARTAB（显示安全CAR表项）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SECCARTAB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略CAR
status: active
---

# DSP SECCARTAB（显示安全CAR表项）

## 功能

该命令用来显示安全CAR表项。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| POLICYTYPE | 策略类型 | 可选必选说明：必选参数<br>参数含义：表示安全策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Tcpip：TCP/IP策略。<br>- Urpf：URPF策略。<br>- WhiteList：白名单策略。<br>- BlackList：黑名单策略。<br>- Index：索引策略。<br>- UserFlow：用户自定义流策略。<br>- Protocol：协议策略。<br>- WhiteListV6：IPv6白名单。<br>默认值：无 |
| POLICYTYPEID | 安全策略类型索引 | 可选必选说明：条件必选参数<br>前提条件：该参数在“POLICYTYPE”配置为“Protocol”、“UserFlow”、“Tcpip” 或 “Index”时为必选参数。<br>参数含义：表示安全策略类型索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：<br>- 如果POLICYTYPE选择WhiteList/BlackList/WhiteListV6，则本参数不选，否则必选。如果POLICYTYPE选择Tcpip，则POLICYTYPEID仅可以为3=tcpsyn、4=fragment，如果POLICYTYPE选择Protocol，则POLICYTYPEID仅可以选择2=bfd、3=bgp、10=icmp、14=ldp、19=ospf、26=ssh-client、27=ssh-server、32=arp、43=arp-miss、46=bgpv6、47=ospfv3、51=icmpv6、69=ra、70=mld、71=rs、72=ns、73=na、74=gre、5=dhcp、68=dhcpv6，仅这些值可以查出数据。<br>- 如果SECPOLICYTYPE选择Index，需要根据DSP SECCARINFO查看安全CAR系统ID并在[35，1658]区间，[125，158]区间除外。如果SECPOLICYTYPE选择UserFlow，本参数在[1，32]之间。 |

## 操作的配置对象

- [安全CAR表项（SECCARTAB）](configobject/UDG/20.15.2/SECCARTAB.md)

## 使用实例

显示安全CAR表项：

```
DSP SECCARTAB: RUNAME="VNODE_VNRS_VNFC_IPU_0064", POLICYTYPE=BlackList;
```

```
RETCODE = 0  操作成功.                                                                                                     
结果如下 
------------------------
                     RU名称  =  VNODE_VNRS_VNFC_IPU_0064
                   策略类型  =  黑名单策略
                     原因ID  =  19
                   可用标记  =  1
        初始CIR参数（kbps）  =  0
       初始CBS参数（bytes）  =  0
                 初始优先级  =  低
        当前CIR参数（kbps）  =  0
       当前CBS参数（bytes）  =  0
                 当前优先级  =  低
        实际CIR参数（kbps）  =  0
       实际CBS参数（bytes）  =  0
                 最小包补偿  =  128
            CIR配置（kbps）  =  0
           CBS配置（bytes）  =  0
                 优先级配置  =  中
             最小包补偿配置  =  0
                   URPF类型  =  松散检查
               URPF默认类型  =  0
                   告警使能  =  1
                   存在告警  =  0
                   告警阈值  =  30000
             告警周期（秒）  =  600
                      计数   =  33
           当前丢弃报文总数  =  0
    当前丢弃报文速率（pps）  =  0
       最近一次丢弃报文总数  =  0
最近一次丢弃报文速率（pps）  =  0
       最近一次告警丢包计数  =  0
         历史丢弃的报文总数  =  0
               当前丢包总数  =  0
    历史丢包速率峰值（pps）  =  0
       历史丢包速率峰值时间  =  NULL
               最近丢包时间  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示安全CAR表项（DSP-SECCARTAB）_49962118.md`
