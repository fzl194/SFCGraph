---
id: UDG@20.15.2@MMLCommand@DSP PLYTRACE
type: MMLCommand
name: DSP PLYTRACE（查询策略跟踪）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PLYTRACE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 系统调测
- 策略调测
- 策略跟踪
status: active
---

# DSP PLYTRACE（查询策略跟踪）

## 功能

此命令用于运维人员判断在CSLB转发路径上是否有完整的转发策略。转发路径分为上行和下行，其中上行指数据流从VNRS发往CSLB方向，下行指数据流从服务侧发往CSLB方向。

## 注意事项

- 该命令执行后立即生效。
- 该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPVNFCID | 服务VNFC ID | 可选必选说明：必选参数<br>参数含义：CSLB服务的VNFC ID，可通过<br>**[DSP SRVIP](../../../../业务管理/路由管理/服务实例地址/查询服务IP（DSP SRVIP）_29627067.md)**<br>查询。<br>取值范围：0~4294967294<br>默认值：无 |
| APPINSTID | 服务实例ID | 可选必选说明：必选参数<br>参数含义：服务实例ID，通过<br>**[DSP SRVIP](../../../../业务管理/路由管理/服务实例地址/查询服务IP（DSP SRVIP）_29627067.md)**<br>：查询Instance ID。<br>取值范围：0~4294967294<br>默认值：无 |
| DIRECTION | 报文方向 | 可选必选说明：必选参数<br>参数含义：数据报文发送的方向。<br>取值范围：<br>- “E_FLOW_FRIP(从VNRS发往CSLB) ”<br>- “E_FLOW_FRAPP(从服务侧发往CSLB) ”<br>默认值：无 |
| IPTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：IP地址类型<br>取值范围：<br>- “IPV4(IPV4) ”<br>- “IPV6(IPV6) ”<br>默认值：无 |
| SRCIPV4 | 源IPv4 | 可选必选说明：可选参数<br>参数含义：源IPv4地址<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| SRCIPV6 | 源IPv6 | 可选必选说明：可选参数<br>参数含义：源IPv6地址<br>取值范围：0:0:0:0:0:0:0:0~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| SRCPORT | 源端口 | 可选必选说明：可选参数<br>参数含义：源端口<br>默认值：无 |
| DSTIPV4 | 目的IPv4 | 可选必选说明：可选参数<br>参数含义：目的IPv4地址<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| DSTIPV6 | 目的IPv6 | 可选必选说明：可选参数<br>参数含义：目的IPv6地址<br>取值范围：0~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| DSTPORT | 目的端口 | 可选必选说明：可选参数<br>参数含义：目的端口<br>默认值：无 |
| PROTTYPE | 协议类型 | 可选必选说明：可选参数<br>参数含义：协议类型<br>取值范围：<br>- “PE_PROT_ICMP(Icmp) ”<br>- “PE_PROT_TCP(Tcp) ”<br>- “PE_PROT_UDP(Udp) ”<br>- “PE_PROT_SCTP(Sctp) ”<br>默认值：无 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：VPN名称<br>取值范围：0~31<br>默认值：无 |
| LBINDEX | LB索引 | 可选必选说明：可选参数<br>参数含义：CSLB的索引号。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PLYTRACE]] · 策略跟踪（PLYTRACE）

## 使用实例

- 查询VNRS发往CSLB的转发策略。
  DSP PLYTRACE:APPVNFCID=4,APPINSTID=91,DIRECTION=E_FLOW_FRIP,DSTIPV4="10.255.255.255",DSTPORT=12033,PROTTYPE=PE_PROT_UDP,VPNNAME="test1",LBINDEX=2;

  ```
  %%DSP PLYTRACE: APPVNFCID=4,APPINSTID=91,DIRECTION=E_FLOW_FRIP,DSTIPV4="10.255.255.255",DSTPORT=12033,PROTTYPE=PE_PROT_UDP,VPNNAME="test1",LBINDEX=2;%%
  RETCODE = 0  操作成功。
  结果如下:
  -------------------------
  服务VNFC ID  =  4
   服务实例ID  =  91
     报文方向  =  从VNRS发往CSLB
       IP类型  =  IPV4
       源IPv4  =  10.0.0.0
       源IPv6  =  2001:0db8::
       源端口  =  0
     目的IPv4  =  10.255.255.255
     目的IPv6  =  2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
   目的端口号  =  12033
     协议类型  =  Udp
      VPN名称  =  test1
       LB索引  =  2
   结果字符串  =  
  LBSRV:
  Match = Success;usInstIdx = 4;FPlyID = 8192;FIdentID = 4096;
  VPNEXCH:
  Match = Success;udwMpfVpnIdx = 0;
  LBSRV:
  Match = Success;FPlyID = 8192;FIdentID = 4096;CoDeploy = True
  IT'S NOT RESERVED BY CSDB
  LBSRV:
  Match = Success;VpnFlag = 0;FPlyID = 8192;FIdentID = 4096
  POLICY:
  Match= Success;Type = 4;ID = 8192;Key1 = 1426846570;Key2 = 17;Key3 = 12033;Key4 = 0;ActionID = 4;NextHopID = 1;NextHopIndex = 16553
  NEXTHOP:
  Match= Success;ID= 1;Idx = 16553;Tp = 2416521521;Tb = 2;Qos = 1
  RESULT:
  Success
  (结果个数 = 1)
  ---    END
  ```
- 查询服务侧发往CSLB的转发策略。
  DSP PLYTRACE:APPVNFCID=4,APPINSTID=91,DIRECTION=E_FLOW_FRAPP,SRCIPV4="10.0.0.0",SRCPORT=12033,VPNNAME="SADF",LBINDEX=1;

  ```
  %%DSP PLYTRACE: APPVNFCID=4,APPINSTID=91,DIRECTION=E_FLOW_FRAPP,SRCIPV4="10.0.0.0",SRCPORT=12033,VPNNAME="SADF",LBINDEX=1;%%
  RETCODE = 0  操作成功。
  结果如下:
  -------------------------
   服务VNFC ID  =  4
    服务实例ID  =  91
      报文方向  =  从服务VNFC发往CSLB
        IP类型  =  IPV4
        源IPv4  =  10.0.0.0
        源IPv6  =  2001:0db8::
        源端口  =  12033
      目的IPv4  =  10.255.255.255
      目的IPv6  =  2001:0db8:ffff:ffff:ffff:ffff:ffff:ffff
    目的端口号  =  0
      协议类型  =  Icmp
       VPN名称  =  SADF
        LB索引  =  1
    结果字符串  =  
  VPNCFG:
  Match = Success;AppIdx = 0;LocalIdx = 0
  LBSRV:
  Match = Success; FPlyID = 8192; FIdentID = 4096;CoDeploy=True
  VPNRT:
  Match = Success;VpnIdx = 4;Tp = 0;Tb = 0
  RESULT:
  Success
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询策略跟踪（DSP-PLYTRACE）_29627121.md`
