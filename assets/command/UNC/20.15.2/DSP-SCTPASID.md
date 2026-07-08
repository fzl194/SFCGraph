---
id: UNC@20.15.2@MMLCommand@DSP SCTPASID
type: MMLCommand
name: DSP SCTPASID（显示SCTP偶联ID）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SCTPASID
command_category: 查询类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# DSP SCTPASID（显示SCTP偶联ID）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于查看SCTP(Stream Control Transmission Protocol)偶联ID及相关信息。偶联就是两个SCTP端点通过SCTP协议规定的4步握手机制建立起来的进行数据传递的逻辑联系或者通道。

## 注意事项

- 该命令为内部调试命令。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：整网规划。<br>取值范围：0~63 位字符串<br>默认值：无 |
| PN | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程号。<br>取值范围：0~20<br>默认值：无 |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待查询SCTP偶联的IP类型。取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| LOCIPV4 | 本地IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待查询SCTP偶联的本地IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>配置为<br>“IPV4(IPv4)”<br>后生效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| LOCIPV6 | 本地IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待查询SCTP偶联的本地IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>配置为<br>“IPV6(IPv6)”<br>后生效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>说明：目前暂不支持IPv6。 |
| LOCPORT | 本地端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待查询SCTP偶联的本地端口号。<br>取值范围：1024~65534<br>默认值：无 |
| PEERIPV4 | 对端IP地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待查询SCTP偶联的对端IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>配置为<br>“IPV4(IPv4)”<br>后生效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| PEERIPV6 | 对端IP地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待查询SCTP偶联的对端IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>配置为<br>“IPV6(IPv6)”<br>后生效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| PEERPORT | 对端端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待查询SCTP偶联的对端端口号。<br>取值范围：0~65535<br>默认值：无 |
| LNKTYPE | 链路类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定使用SCTP协议的链路类型。取值范围：<br>- “M3UALNK(M3UALNK)”<br>- “DMLNK(DMLNK)”<br>- “LCSLNK(LCSLNK)”<br>- “SGSLNK(SGSLNK)”<br>- “S1APLNK(S1APLNK)”<br>- “SBCLNK(SBCLNK)”<br>- NGAPLNK(NGAPLNK)<br>默认值：无 |

## 操作的配置对象

- [SCTP偶联ID（SCTPASID）](configobject/UNC/20.15.2/SCTPASID.md)

## 使用实例

本地IP地址为10.100.43.70，端口号为36412，对端IP地址为10.100.42.70，对端端口号为20045，链路类型为S1APLNK，查询SCTP偶联ID：

DSP SCTPASID: IPT=IPV4, LOCIPV4="10.100.43.70", LOCPORT=36412, PEERIPV4="10.100.42.70", PEERPORT=20045, LNKTYPE=S1APLNK;

```
%%DSP SCTPASID: IPT=IPV4, LOCIPV4="10.100.43.70", LOCPORT=36412, PEERIPV4="10.100.42.70", PEERPORT=20045, LNKTYPE=S1APLNK;%%
RETCODE = 0  操作成功。

查询SCTP偶联ID
--------------
                偶联ID  =  882
        主用本端IP地址  =  10.100.43.70
        主用对端IP地址  =  10.100.42.70
           对端IP地址1  =  10.100.42.70
           对端IP地址2  =  10.100.42.71
       对端IP地址1状态  =  可达
       对端IP地址2状态  =  可达
       对端IP1拥塞窗口  =  6
     对端IP1慢启动门限  =  4
 对端IP1拥塞窗口增长率  =  1
 对端IP1连续未确认包数  =  0
   对端IP1连续确认包数  =  0
   对端IP1最大拥塞窗口  =  2
            对端IP1K值  =  0
       对端IP1最小时延  =  10
对端IP1CUBIC算法WMAX值  =  101
       对端IP2拥塞窗口  =  2
     对端IP2慢启动门限  =  2
 对端IP2拥塞窗口增长率  =  145
 对端IP2连续未确认包数  =  0
   对端IP2连续确认包数  =  0
   对端IP2最大拥塞窗口  =  3
            对端IP2K值  =  0
       对端IP2最小时延  =  10
对端IP2CUBIC算法WMAX值  =  3
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示SCTP偶联ID(DSP-SCTPASID)_72226017.md`
