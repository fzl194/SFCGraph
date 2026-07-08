---
id: UDG@20.15.2@MMLCommand@DSP SFETUNNEL
type: MMLCommand
name: DSP SFETUNNEL（显示Tunnel表项）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFETUNNEL
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

# DSP SFETUNNEL（显示Tunnel表项）

## 功能

该命令用于根据隧道类型、目的IP、源IP、VPN ID、KEY-USED、GRE-KEY、RUNAME显示Tunnel表项。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRETUNNELTYPE | GRE隧道类型 | 可选必选说明：必选参数<br>参数含义：GRE隧道类型。该参数用于控制输入参数中的目的IP、源IP地址的协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GRE4Tunnel：IPv4 GRE隧道。<br>- GRE6Tunnel：IPv6 GRE隧道。<br>默认值：无 |
| DESTINATION | 目的IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GRETUNNELTYPE”配置为“GRE4Tunnel”时为必选参数。<br>参数含义：该参数用于指定目的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| SOURCE | 源IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GRETUNNELTYPE”配置为“GRE4Tunnel”时为必选参数。<br>参数含义：该参数用于指定源IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DESTINATION6 | 目的IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GRETUNNELTYPE”配置为“GRE6Tunnel”时为必选参数。<br>参数含义：目的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| SOURCE6 | 目的IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“GRETUNNELTYPE”配置为“GRE6Tunnel”时为必选参数。<br>参数含义：源IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| VPN | VPN编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| KEYUSED | Key标志 | 可选必选说明：必选参数<br>参数含义：该参数用于表示Key值配置标志。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1。<br>默认值：无 |
| GREKEY | Key | 可选必选说明：必选参数<br>参数含义：该参数用于表示配置的Key值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SFETUNNEL]] · Tunnel表项（SFETUNNEL）

## 使用实例

显示指定资源单元的Tunnel表项：

```
DSP SFETUNNEL: GRETUNNELTYPE=GRE4Tunnel, DESTINATION="192.168.1.1", SOURCE="192.168.1.2", VPN=0, RUNAME="VNODE_VNRS_VNFC_IPU_0064", KEYUSED=1, GREKEY=10;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
 结果                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
TableName    : IPV4 TUNNEL
TotalRecords : 1
(*):  Key of the table
---------------------------------------------------------------------------------------
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
           *TunnelId : 00000003                        TnlValid : 01                  
             KeyUsed : 01                              Checksum : 00                  
           TnlStatus : 01                           KeepAliveEn : 00                  
             IfCntEn : 00                              IfStatEn : 01                  
        RedundancyEn : 00                          ProtocolType : 00   
                McEn : 01                                IGMPEn : 00                
          ReasmBoard : 0041                              TnlMTU : 000005dc            
          TnlMTUIPv6 : 00000000                       SrcIPAddr : 192.168.1.2         
           DstIPAddr : 192.168.1.1                     VrfIndex : 0000                
        BindVrfIndex : 0000                      IfStatIndexIng : 00000014            
       IfStatIndexEg : 00000015                         IfIndex : 0000001b            

(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SFETUNNEL.md`
