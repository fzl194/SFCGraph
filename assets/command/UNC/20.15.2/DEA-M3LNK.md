---
id: UNC@20.15.2@MMLCommand@DEA M3LNK
type: MMLCommand
name: DEA M3LNK（去活M3UA信令链路）
nf: UNC
version: 20.15.2
verb: DEA
object_keyword: M3LNK
command_category: 动作类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- M3UA管理
- M3UA链路
status: active
---

# DEA M3LNK（去活M3UA信令链路）

## 功能

![](去活M3UA信令链路(DEA M3LNK)_26306118.assets/notice_3.0-zh-cn_2.png)

去激活链路将会导致该链路无法进行业务。

**适用网元：SGSN、MME、SMSF**

该命令用于去活M3UA信令链路。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后，链路进入“非激活”状态。
- 去激活后的链路不能进行业务，业务会倒换到其他链路上进行。这样就会导致其他链路的负荷增大，因此需要在业务量比较少的时候进行该命令。
- 进行链路去激活操作，会产生链路故障告警。如果到一个目的信令点只有一条路由，则会产生目的信令点不可达告警和路由不可用告警(目的信令点不可达告警的ID为10337，路由不可用告警的ID为10336) 。
- 该命令只能在AS端或者IPSP的客户端操作。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNK | 链路号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示M3UA链路号。<br>取值范围：0~1279<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@M3LNK]] · M3UA信令链路（M3LNK）

## 使用实例

去活链路号为1的M3UA链路：

DEA M3LNK: LNK=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/DEA-M3LNK.md`
