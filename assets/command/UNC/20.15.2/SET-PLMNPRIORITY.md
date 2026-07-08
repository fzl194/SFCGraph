---
id: UNC@20.15.2@MMLCommand@SET PLMNPRIORITY
type: MMLCommand
name: SET PLMNPRIORITY（设置获取PLMN优先级）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PLMNPRIORITY
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 获取PLMN管理
- 获取PLMN方式的优先级
status: active
---

# SET PLMNPRIORITY（设置获取PLMN优先级）

## 功能

**适用NF：PGW-C、SGW-C、GGSN**

由于PGW一般是根据运营商的不同进行设置的，因此PGW的HPLMN可以直接通过ADD NGHPLMN进行设置。此时PGW只知道自身的PLMN还不足以判断用户是本地用户还是漫游用户，还需要知道SGW一侧的PLMN。由于SGW是根据用户的位置进行选择的，因此为适应位置上的变化，PGW要根据SGW具体的位置获知SGW一侧的PLMN。通过本指令可以更改PGW获取SGW一侧PLMN的方式的优先级。使用该命令配置获取SGSN/S-GW的PLMN信息的优先级。PGW根据优先级依次获取SGSN/S-GW的PLMN，直到获取成功为止。

## 注意事项

- 该命令执行后立即生效。

- 同一网元类型的优先级不能相同。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NODETYPE | PRIORITYMODE | GGSN1STPRIORITY | GGSN2NDPRIORITY | GGSN3RDPRIORITY | SGW1STPRIORITY | SGW2NDPRIORITY | PGW1STPRIORITY | PGW2NDPRIORITY | PGW3RDPRIORITY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GGSN | LOCAL | SGSN_IP | RAI | ULI | APN_OI | PGW_IP | SERVING_NETWORK | ULI | SGW_IP |
| SGWC | LOCAL | SGSN_IP | RAI | ULI | APN_OI | PGW_IP | SERVING_NETWORK | ULI | SGW_IP |
| PGWC | LOCAL | SGSN_IP | RAI | ULI | APN_OI | PGW_IP | SGW_IP | SERVING_NETWORK | ULI |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODETYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指示UNC的网元形态。<br>数据来源：本端规划<br>取值范围：<br>- GGSN（GGSN）<br>- SGWC（SGW-C）<br>- PGWC（PGW-C）<br>默认值：无。<br>配置原则：无 |
| PRIORITYMODE | 获取PLMN方法 | 可选必选说明：可选参数<br>参数含义：该参数用于两种获取PLMN方法。<br>数据来源：全网规划<br>取值范围：<br>- LOCAL（LOCAL）<br>- RADIUS（RADIUS）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PLMNPRIORITY查询当前参数配置值。<br>配置原则：无 |
| GGSN1STPRIORITY | GGSN第一优先级 | 可选必选说明：该参数在"NODETYPE"配置为"GGSN"时为条件必选参数。<br>参数含义：该参数用于指定GGSN第一优先级。<br>数据来源：本端规划<br>取值范围：<br>- SGSN_IP（SGSN_IP）<br>- RAI（RAI）<br>- ULI（ULI）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PLMNPRIORITY查询当前参数配置值。<br>配置原则：无 |
| GGSN2NDPRIORITY | GGSN第二优先级 | 可选必选说明：该参数在"NODETYPE"配置为"GGSN"时为条件必选参数。<br>参数含义：该参数用于指定GGSN第二优先级。<br>数据来源：本端规划<br>取值范围：<br>- SGSN_IP（SGSN_IP）<br>- RAI（RAI）<br>- ULI（ULI）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PLMNPRIORITY查询当前参数配置值。<br>配置原则：无 |
| GGSN3RDPRIORITY | GGSN第三优先级 | 可选必选说明：该参数在"NODETYPE"配置为"GGSN"时为条件必选参数。<br>参数含义：该参数用于指定GGSN第三优先级。<br>数据来源：本端规划<br>取值范围：<br>- SGSN_IP（SGSN_IP）<br>- RAI（RAI）<br>- ULI（ULI）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PLMNPRIORITY查询当前参数配置值。<br>配置原则：无 |
| SGW1STPRIORITY | SGW第一优先级 | 可选必选说明：该参数在"NODETYPE"配置为"SGWC"时为条件必选参数。<br>参数含义：该参数用于指定SGW-C第一优先级。<br>数据来源：本端规划<br>取值范围：<br>- APN_OI（APN_OI）<br>- PGW_IP（PGW_IP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PLMNPRIORITY查询当前参数配置值。<br>配置原则：无 |
| SGW2NDPRIORITY | SGW第二优先级 | 可选必选说明：该参数在"NODETYPE"配置为"SGWC"时为条件必选参数。<br>参数含义：该参数用于指定SGW-C第二优先级。<br>数据来源：本端规划<br>取值范围：<br>- APN_OI（APN_OI）<br>- PGW_IP（PGW_IP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PLMNPRIORITY查询当前参数配置值。<br>配置原则：无 |
| PGW1STPRIORITY | PGW第一优先级 | 可选必选说明：该参数在"NODETYPE"配置为"PGWC"时为条件必选参数。<br>参数含义：该参数用于指定PGW-C第一优先级。<br>数据来源：本端规划<br>取值范围：<br>- SERVING_NETWORK（SERVING_NETWORK）<br>- ULI（ULI）<br>- SGW_IP（SGW_IP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PLMNPRIORITY查询当前参数配置值。<br>配置原则：无 |
| PGW2NDPRIORITY | PGW第二优先级 | 可选必选说明：该参数在"NODETYPE"配置为"PGWC"时为条件必选参数。<br>参数含义：该参数用于指定PGW-C第二优先级。<br>数据来源：本端规划<br>取值范围：<br>- SERVING_NETWORK（SERVING_NETWORK）<br>- ULI（ULI）<br>- SGW_IP（SGW_IP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PLMNPRIORITY查询当前参数配置值。<br>配置原则：无 |
| PGW3RDPRIORITY | PGW第三优先级 | 可选必选说明：该参数在"NODETYPE"配置为"PGWC"时为条件必选参数。<br>参数含义：该参数用于指定PGW-C第三优先级。<br>数据来源：本端规划<br>取值范围：<br>- SERVING_NETWORK（SERVING_NETWORK）<br>- ULI（ULI）<br>- SGW_IP（SGW_IP）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PLMNPRIORITY查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLMNPRIORITY]] · 获取PLMN优先级（PLMNPRIORITY）

## 使用实例

用户在3G激活时，UNC作为GGSN，设置获取PLMN方法为本地获取，第一优先级为从消息中的RAI获取，第二优先级为消息发送方SGSN的IP，第三优先级为消息中的ULI。

```
SET PLMNPRIORITY:NODETYPE=GGSN,PRIORITYMODE=LOCAL,GGSN1STPRIORITY=RAI,GGSN2NDPRIORITY=SGSN_IP,GGSN3RDPRIORITY=ULI;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置获取PLMN优先级（SET-PLMNPRIORITY）_09653827.md`
