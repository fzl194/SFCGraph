---
id: UNC@20.15.2@MMLCommand@DSP IPINFOMCR
type: MMLCommand
name: DSP IPINFOMCR（显示IP相关信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: IPINFOMCR
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- 扩展调测
- 平台调测
- IP特性调测
status: active
---

# DSP IPINFOMCR（显示IP相关信息）

## 功能

**适用网元：MME**

该命令查询IP信息，包括转发、统计等信息。

## 注意事项

该命令暂不支持。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1~63位字符串<br>默认值：无 |
| PROCTYPE | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于要查询的进程类型。<br>取值范围：<br>- “SRP(SRP)”<br>默认值：无 |
| PROCNO | 进程序列号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询的进程序号。<br>取值范围：0~20<br>默认值：无 |
| TT | 表类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示要查询的表类型。<br>取值范围：<br>- “DATA(DATA)”<br>- “HASH(HASH)”<br>- “STAT(STAT)”<br>- “OTHER(OTHER)”<br>默认值：无<br>说明：该参数无效。 |
| MT | 模块类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定模块类型。<br>取值范围：<br>- “STAT(STAT)”<br>默认值：无 |
| MODULT | PFPModule | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定PFPModule表类型。<br>前提条件：该参数在<br>“模块类型”<br>设置为<br>“STAT(STAT)”<br>时有效。<br>取值范围：<br>- “RXM(RX 模块)”<br>- “TXM(TX 模块)”<br>- “GTPM(GTP模块)”<br>- “TIMEM(TIMER模块)”<br>- “INTERRXM(板间接收模块)”<br>- “INTRARXM(板内接收模块)”<br>- “INTERTXM(板间发送模块)”<br>- “INTRATXM(板内发送模块)”<br>- “X3M(X3模块)”<br>- “VPM(VP模块)”<br>- “ALL5M(ALL5模块)”<br>- “OAMM(OAM模块)”<br>- “LBM(LB模块)”<br>- “QUEM(QUE模块)”<br>- “XOIPM(XOIP模块)”<br>- “TRCM(TRC模块)”<br>- “IP(IP模块)”<br>- “TCP(TCP模块)”<br>- “BFD(BFD模块)”<br>- “ACL(ACL模块)”<br>- “ICMP(ICMP模块)”<br>- “UDP(UDP模块)”<br>- “BUFFM(BUFF模块)”<br>默认值：无 |
| BEXC | 起始偏移 | 可选必选说明：可选参数<br>参数含义：该参数用于查询的起始偏移。<br>取值范围：0~4294967295<br>默认值：0 |
| EEXC | 结束偏移 | 可选必选说明：可选参数<br>参数含义：该参数用于查询的结束偏移。<br>取值范围：0~4294967295<br>默认值：40 |
| APP1 | 模块附加过滤条件1 | 可选必选说明：可选参数<br>参数含义：该参数用于查询的模块附加过滤条件1。<br>取值范围：0~4294967295<br>默认值：无 |
| APP2 | 模块附加过滤条件2 | 可选必选说明：可选参数<br>参数含义：该参数用于查询的模块附加过滤条件2。<br>取值范围：0~4294967295<br>默认值：无 |
| APP3 | 模块附加过滤条件3 | 可选必选说明：可选参数<br>参数含义：该参数用于查询的模块附加过滤条件3。<br>取值范围：0~4294967295<br>默认值：无 |
| APP4 | 模块附加过滤条件4 | 可选必选说明：可选参数<br>参数含义：该参数用于查询的模块附加过滤条件4。<br>取值范围：0~4294967295<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPINFOMCR]] · IP相关信息（IPINFOMCR）

## 使用实例

查询IP信息。

1. 查询MCR_SP_RU_0064的IP统计信息：
  DSP IPINFOMCR: RUNAME="MCR_SP_RU_0064", PROCTYPE=SRP, PROCNO=0, MT=STAT, MODULT=IP;
  ```
  %%DSP IPINFOMCR: RUNAME="MCR_SP_RU_0064", PROCTYPE=SRP, PROCNO=0, MT=STAT, MODULT=IP;%%
  RETCODE = 0  操作成功。

  IP信息
  ------------------------
  字符串                                                      

  E_PFP_IP_RCV_TOTAL_IP_PKT                   (0x401): 25
  E_PFP_IP_RCV_IP_PKT                         (0x423): 25
  E_PFP_IP_OUTPUT_TOTAL_PKT_STAT              (0x425): 25
  E_PFP_IP_SND_TO_MPF_SUCC                    (0x442): 25

  (结果个数 = 4)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示IP相关信息(DSP-IPINFOMCR)_25291196.md`
