---
id: UNC@20.15.2@MMLCommand@RES USRCTLGGSN
type: MMLCommand
name: RES USRCTLGGSN（恢复可用的GGSN地址）
nf: UNC
version: 20.15.2
verb: RES
object_keyword: USRCTLGGSN
command_category: 调测类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GGSN容灾功能
status: active
---

# RES USRCTLGGSN（恢复可用的GGSN地址）

## 功能

**适用网元：SGSN**

此命令用于手工启用从故障变为正常的GGSN，恢复与对应GGSN的业务通信。

如果由于网络等原因导致到某个GGSN的通信经常中断，为了避免业务的频繁切换，可以通过 [**ADD USRCTLGGSN**](增加手工恢复GGSN地址(ADD USRCTLGGSN)_72345505.md) 命令屏蔽该GGSN，在确认故障完全排除后，再恢复到该GGSN的业务。

当 UNC 检测到本表中配置的GGSN故障恢复后，产生 “ALM-12605 GTPC路径恢复正常需手工启动新业务接入” 告警。只有在经过操作员人工确认（ [**RES USRCTLGGSN**](恢复可用的GGSN地址(RES USRCTLGGSN)_72345507.md) ）后，才选择故障恢复后的GGSN业务，执行该命令后告警恢复。

## 注意事项

可以通过 [**DSP USRCTLGGSN**](显示手工恢复GGSN地址状态(DSP USRCTLGGSN)_26305716.md) 命令查询需要手工恢复的GGSN列表。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：此参数用于指定IP地址的IP类型。<br>数据来源：与对端协商<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| LOCIPV4 | 本端IP地址 | 可选必选说明：条件可选参数<br>参数含义：此参数用于指定与GGSN网元通信的本端网元的IPV4地址。<br>数据来源：通过<br>[**LST GTPCLE**](../../Gtpc本端实体管理/查询GTP-C本地实体(LST GTPCLE)_72345567.md)<br>命令来查询本端IP。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则: 如果指定本端IP，则只恢复该IP与对端GGSN之间的路径；如果不指定本端IP，则恢复所有本端IP与对端GGSN之间的路径。<br>说明：指定恢复对端地址相关的所有路径时，不能恢复路径故障的路径。 |
| PEERIPV4 | 对端IP地址 | 可选必选说明：条件必选参数<br>参数含义：此参数用于指定GGSN网元的IPv4地址。<br>数据来源：与对端协商<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则：<br>- 对端IP地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 对端IP地址必须是A、B或者C类地址。 |
| LOCIPV6 | 本端IP地址 | 可选必选说明：条件可选参数<br>参数含义：此参数用于指定与GGSN通信的本端网元的IPV6地址。<br>数据来源：通过<br>[**LST GTPCLE**](../../Gtpc本端实体管理/查询GTP-C本地实体(LST GTPCLE)_72345567.md)<br>命令来查询本端IP。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| PEERIPV6 | 对端IP地址 | 可选必选说明：条件必选参数<br>参数含义：此参数用于指定对端GGSN的IPV6地址。<br>数据来源：与对端协商<br>取值范围： ::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USRCTLGGSN]] · 手工恢复GGSN地址（USRCTLGGSN）

## 使用实例

1. 恢复指定的路径：
  RES USRCTLGGSN: IPT=IPV4, LOCIPV4="192.168.14.20", PEERIPV4="192.168.45.20";
  ```
  %%RES USRCTLGGSN: IPT=IPV4, LOCIPV4="192.168.14.20", PEERIPV4="192.168.45.20";%%
  RETCODE = 0  操作成功。

  操作结果如下
  -------------------------
               本端IP地址 = 192.168.14.20
               对端IP地址 = 192.168.45.20
             路径接口类型 = 2G或3G网络
                 路径版本 = V1
                 路径状态 = 正常
  (结果数目 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RES-USRCTLGGSN.md`
