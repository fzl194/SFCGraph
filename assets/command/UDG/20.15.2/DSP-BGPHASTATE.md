---
id: UDG@20.15.2@MMLCommand@DSP BGPHASTATE
type: MMLCommand
name: DSP BGPHASTATE（查询BGP HA状态信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: BGPHASTATE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP HA状态信息
status: active
---

# DSP BGPHASTATE（查询BGP HA状态信息）

## 功能

该命令用于查询BGP HA状态信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFTYPE | BGP地址族类型 | 可选必选说明：可选参数<br>参数含义：BGP地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@BGPHASTATE]] · BGP HA状态信息（BGPHASTATE）

## 使用实例

查询BGP HA状态信息：

```
DSP BGPHASTATE:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
BGP HA状态信息  =
BRM : HA Mode      : BRM_HA_SUPPORT_NSR
      HA COMP State: BRM_HAS_PROTECT

                     CROSSATTR State   : BRM_HA_DATA_REALTIME_BACKUP
                     CROSSIID  State   : BRM_HA_DATA_REALTIME_BACKUP
                     MVRFPRIATTR  State: BRM_HA_DATA_REALTIME_BACKUP
      IPv4 Unicast : BRM_HAS_INSTANCE_PROTECT

                     ATTRID State   : BRM_HA_DATA_REALTIME_BACKUP
                     NEXTHOP State  : BRM_HA_DATA_REALTIME_BACKUP
                     IID State      : BRM_HA_DATA_REALTIME_BACKUP
                     IMPRT State    : BRM_HA_DATA_REALTIME_BACKUP
                     NTKRT State    : BRM_HA_DATA_REALTIME_BACKUP
                     AGGRRT State   : BRM_HA_DATA_REALTIME_BACKUP
                     AUTOSUM State  : BRM_HA_DATA_REALTIME_BACKUP
                     UPG State      : BRM_HA_DATA_REALTIME_BACKUP
                     RIBIN State    : BRM_HA_DATA_BOUNDARY_DECISION_OVER
                     RIBOUT State   : BRM_HA_DATA_BOUNDARY_DECISION_OVER
                     LABEL State    : BRM_HA_DATA_REALTIME_BACKUP
                     XCID State     : BRM_HA_DATA_REALTIME_BACKUP
                     LIFN State     : BRM_HA_DATA_REALTIME_BACKUP
                     VDCFG State    : BRM_HA_DATA_NO_BACKUP
                     VDRT State     : BRM_HA_DATA_NO_BACKUP
                     CROSSRT State  : BRM_HA_DATA_NO_BACKUP
                     FLOW RT  State : BRM_HA_DATA_NO_BACKUP
                     RULE State     : BRM_HA_DATA_NO_BACKUP
                     REMOTEIID State: BRM_HA_DATA_NO_BACKUP
                     INSIMPRT State : BRM_HA_DATA_REALTIME_BACKUP

BNM: HA Mode      : BNM_HA_SUPPORT_NSR
     HA COMP State: BNM_HAS_PROTECT

     _public_     : BNM_HAS_VRF_PROTECT

                     PEERINFO State : BNM_HA_DATA_BOUNDARY_DECISION_OVER
                     IPv4 Unicast   : BNM_HA_VRF_AF_REALTIME_BACKUP
                     UPG State      : BNM_HA_DATA_REALTIME_BACKUP
                     AGENTPEER State: BNM_HA_DATA_REALTIME_BACKUP
                     Router Id State: BNM_HA_DATA_REALTIME_BACKUP

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-BGPHASTATE.md`
