---
id: UDG@20.15.2@MMLCommand@DSP SFELINEARTABLE
type: MMLCommand
name: DSP SFELINEARTABLE（显示指定的线性表记录）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFELINEARTABLE
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

# DSP SFELINEARTABLE（显示指定的线性表记录）

## 功能

该命令用于根据索引显示指定的线性表记录。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STRINDEX | 字符串型索引 | 可选必选说明：必选参数<br>参数含义：显示指定线性表项字符串型索引值：十进制（0-4294967295）或者十六进制（0x0-0xFFFFFFFF）。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～10。<br>默认值：无 |
| TABLETYPE | 表类型 | 可选必选说明：必选参数<br>参数含义：表示表编号： [1]vpn：显示VPN表； [2]re：显示IP路由信息表； [3]nhp：显示IPV4转发下一跳表； [4]nst：显示下一跳分离表； [5]ba：显示外部优先级到内部优先级的映射表； [6]phb：显示内部优先级到外部优先级的映射表； [7]bfd_isend：显示BFD入方向发送表； [8]bfd_pkt：显示BFD报文模板表； [9]mplsarp：显示MPLSARP表； [10]nhlfe：显示NHLFE表； [11]nhp6：显示IPv6下一跳表； [12]trunk：显示trunk表； [13]ipsec_tunnel：显示IPsec tunnel表； [14]aib：显示AIB表； [15]at：显示AT表； [16]gphb：显示差分服务代码点到VLAN优先级映射表； [17]nd：显示指定的IPv6 ND表； [18]nst6：显示IPv6下一跳分离表； [19]re6：显示指定的IPv6 RE表； [20]mre：显示指定的MRE表； [21]tb_mask：显示指定的TB-MASK表； [22]mrt：显示指定的MRT表； [23]mib：显示指定的MIB表； [31]fabric_tunnel：显示指定的FABRIC_TUNNEL表； [36]pst: 显示指定的pst表。 [37]bfd_glbmap：显示指定的BFD全局映射表，该表维护BFD所绑定的端口信息。 [48]board-cfg：显示BOARD-CFG表； [49]global-action：显示指定的GLOBAL-ACTION表。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- VPN：VPN表。<br>- RE：路由信息表。<br>- NHP：NHP表。<br>- NST：NST表。<br>- BA：BA表。<br>- PHB：PHB表。<br>- BFD_ISEND：BFD报文发送表。<br>- BFD_PKT：BFD报文模板表。<br>- MPLSARP：MPLS-ARP表项。<br>- NHLFE：NHLFE表项。<br>- NHP6：IPv6-NHP表项。<br>- TRUNK：Trunk表。<br>- IPSEC_TUNNEL：IPsec Tunnel表。<br>- AIB：AIB表。<br>- AT：AT表。<br>- GPHB：GPHB表。<br>- ND：ND表。<br>- NST6：IPV6-NST表。<br>- RE6：RE6表。<br>- MRE：MRE表。<br>- TB_MASK：TB_MASK表。<br>- MRT：MRT表。<br>- MIB：MIB表。<br>- FABRIC_TUNNEL：FABRIC_TUNNEL表。<br>- PST：端口状态表。<br>- BFD_GLBMAP：BFD全局映射表，该表用于维护BFD所绑定的端口信息。<br>- BOARD_CFG：BOARD_CFG表。<br>- GLOBAL_ACTION：全局动作表。<br>默认值：无 |
| RUNAME | 资源单元名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFELINEARTABLE]] · 指定的线性表记录（SFELINEARTABLE）

## 使用实例

显示指定资源单元、指定索引号的线性表：

```
DSP SFELINEARTABLE:STRINDEX="1",TABLETYPE=VPN,RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```

RETCODE = 0  操作成功                                             
                                                                                
结果如下                                                       
-------------------------                                                       
资源单元编号  =  66 
      表名称  =  vpn 
        索引  =  1                                                                 
资源单元名称  =  VNODE_VNRS_VNFC_IPU_0066 
        结果  =
                 *VpnIndex : 00000001  Valid : 01
                   FwdType : 00        VrfId : 0000
                                                                 
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SFELINEARTABLE.md`
