---
id: UDG@20.15.2@MMLCommand@DSP SFETABLEVERBOSE
type: MMLCommand
name: DSP SFETABLEVERBOSE（按摘要和详情两种方式显示SFE表项信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFETABLEVERBOSE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE表项统计
status: active
---

# DSP SFETABLEVERBOSE（按摘要和详情两种方式显示SFE表项信息）

## 功能

按摘要和详情两种方式显示SFE的表项信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FENODEID | FE节点编号 | 可选必选说明：可选参数<br>参数含义：表示FE节点编号值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| TABLETYPE | 表类型 | 可选必选说明：必选参数<br>参数含义：表示表编号： [1]arp：显示ARP表； [2]arpreply：显示ARP REPLY表； [3]vpn：显示VPN表； [4]re：显示IP路由信息表； [5]nhp：显示IPV4转发下一跳表； [6]nst：显示下一跳分离表； [7]ba：显示外部优先级到内部优先级的映射表； [8]phb：显示内部优先级到外部优先级的映射表； [9]bfd_isend：显示BFD入方向发送表； [10]bfd_erecv：显示BFD出方向接收表； [11]bfd_pkt：显示BFD报文模板表； [12]bfd_irecv：显示BFD入方向接收表； [13]ipat：显示上行端口属性表； [14]epat：显示下行端口属性表； [15]icib：显示基于port+vlan的上行业务属性表； [16]ecib：显示基于port+vlan的下行业务属性表； [17]fib4：显示FIBv4表； [18]tunnel：显示tunnel表； [19]at：显示AT表； [20]iqvct：显示IQVCT表； [21]eqvct：显示EQVCT表； [22]port：显示PORT表； [23]ctrlvid：显示CTRLVID表； [24]vrrp：显示VRRP表； [25]vxlan-otnlv4：显示VXLAN OTNLV4表； [26]vxlan-aib：显示VXLAN AIB表； [27]vni：显示VNI表； [28]vniencap：显示VNIENCAP表； [29]vlanif bd：显示VLANIF BD表； [30]aib：显示AIB表； [31]fid：显示FID表； [32]mac-limit：显示MAC-Limit表； [33]elb：显示ELB表； [34]mrt：显示组播复制表项； [35]be：显示BE表项； [46]fib6：显示指定IPv6 FIB的表； [47]re6：显示指定IPv6 RE的表； [48]nd：显示指定IPv6 ND的表； [49]ndh：显示指定IPv6 NDH的表； [50]nst6：显示IPv6下一跳分离表； [51]mplsarp：显示MPLSARP表； [52]nhlfe：显示Nhlfe表； [53]nhp6：显示IPv6下一跳表； [54]gphb：显示差分服务代码点到VLAN优先级映射表； [55]trunk：显示trunk表； [56]localip：显示LOCALIP表； [57]mfib4：显示MFIB4表； [58]mre：显示MRE表； [59]tb_mask：显示TB_MASK表； [60]mib：显示MIB表； [63]pst: 显示pst表； [64]bfd_glbmap: 显示BFD全局映射表，该表维护BFD所绑定的端口信息； [65]portmac: 显示端口MAC表； [82]board-cfg: 显示BOARD-CFG表； [84]global-action：显示GLOBAL-ACTION表； [87]nd-fast-reply：显示ND FAST REPLY表； [100]Dynamic Host Configuration Protocol bind table：显示DHCP绑定表。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ARP：ARP表。<br>- ARPREPLY：ARP-REPLY表。<br>- VPN：VPN表。<br>- RE：路由信息表。<br>- NHP：NHP表。<br>- NST：NST表。<br>- BA：BA表。<br>- PHB：PHB表。<br>- BFD_ISEND：BFD报文发送表。<br>- BFD_ERECV：BFD报文出方向接收表。<br>- BFD_PKT：BFD报文模板表。<br>- BFD_IRECV：BFD报文入方向接收表。<br>- IPAT：上行入方向主端口表。<br>- EPAT：下行出方向主端口表。<br>- ICIB：上行入方向子端口表。<br>- ECIB：下行出方向子端口表。<br>- FIB4：FIB4表。<br>- TUNNEL：遂道表。<br>- AT：AT表。<br>- IQVCT：IQVCT表。<br>- EQVCT：EQVCT表。<br>- PORT：PORT表。<br>- CTRLVID：CTRLVID控制表。<br>- VRRP：VRRP表。<br>- VXLAN_OTNLV4：VXLAN-OTNLV4表。<br>- VXLAN_AIB：VXLAN-AIB表。<br>- YNI：YNI表。<br>- VNIENCAP：VNIENCAP表。<br>- VLANIF_BD：VLANIFBD表。<br>- AIB：AIB表。<br>- FID：FID表。<br>- MAC_LIMIT：MAC_LIMIT表。<br>- ELB：ELB表。<br>- MRT：MRT表。<br>- BE：BE表。<br>- FIB6：FIB6表。<br>- RE6：RE6表。<br>- ND：ND表。<br>- NDH：NDH表。<br>- NST6：IPV6-NST表。<br>- MPLSARP：MPLS-ARP表项。<br>- NHLFE：NHLFE表项。<br>- NHP6：IPv6-NHP表项。<br>- GPHB：GPHB表。<br>- TRUNK：TRUNK表。<br>- LOCALIP：LOCALIP表。<br>- MFIB4：MFIB4表。<br>- MRE：MRE表。<br>- TB_MASK：TB_MASK表。<br>- MIB：MIB表。<br>- PST：端口状态表。<br>- BFD_GLBMAP：BFD全局映射表，该表用于维护BFD所绑定的端口信息。<br>- PORT_MAC：端口MAC表。<br>- MIIF：MIIF表。<br>- PATHMTU：PATHMTU表。<br>- BOARD_CFG：BOARD_CFG表。<br>- GLOBAL_ACTION：全局动作表。<br>- ND_FAST_REPLY：ND快回表。<br>- DHCP_BIND：DHCP-BIND表。<br>默认值：无 |
| RUNAME | 资源单元名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| VERBOSE | 详细信息 | 可选必选说明：必选参数<br>参数含义：显示详细信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFETABLEVERBOSE]] · 按摘要和详情两种方式显示SFE表项信息（SFETABLEVERBOSE）

## 使用实例

显示指定资源单元的SFE表详细信息：

```
DSP SFETABLEVERBOSE:RUNAME="VNODE_VNRS_VNFC_IPU_0066", TABLETYPE=VPN, VERBOSE=1;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
资源单元编号 = 66   
FE节点编号   = 4259585
    表类型   = vpn
资源单元名称 = VNODE_VNRS_VNFC_IPU_0066
  详细信息   = 1  
      结果   = *VpnIndex : 00000001 
               VrfId : 0001           
               Valid : 0000                                                                                                                                                                                                
               FwdType : 00                                           
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SFETABLEVERBOSE.md`
