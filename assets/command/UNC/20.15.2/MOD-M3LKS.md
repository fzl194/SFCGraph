---
id: UNC@20.15.2@MMLCommand@MOD M3LKS
type: MMLCommand
name: MOD M3LKS（修改M3UA信令链路集）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: M3LKS
command_category: 配置类
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
- M3UA链路集
status: active
---

# MOD M3LKS（修改M3UA信令链路集）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于修改M3UA信令链路集配置数据。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSX | 链路集索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定准备修改的链路集的索引。<br>数据来源：本端规划<br>取值范围：0～1279<br>默认值：无 |
| SLSM | 链路选择掩码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在该链路集下的多条M3UA链路之间如何实现信令业务的负荷分担。<br>数据来源：整网规划<br>取值范围：<br>- “B0000(B0000)”<br>- “B0001(B0001)”<br>- “B0010(B0010)”<br>- “B0011(B0011)”<br>- “B0100(B0100)”<br>- “B0101(B0101)”<br>- “B0110(B0110)”<br>- “B0111(B0111)”<br>- “B1000(B1000)”<br>- “B1001(B1001)”<br>- “B1010(B1010)”<br>- “B1011(B1011)”<br>- “B1100(B1100)”<br>- “B1101(B1101)”<br>- “B1110(B1110)”<br>- “B1111(B1111)”<br>默认值：无<br>说明：一个链路集中的链路数目和链路选择掩码的关系：1条链路，设置为全0。<br>- 2条链路，设置1个BIT为1。<br>- 3-4条链路，设置2个BIT为1。<br>- 5-8条链路，设置3个BIT为1。<br>- 9-16条链路，设置4个BIT为1。<br>- 到同一个目的实体，链路选择掩码和链路集选择掩码（[**ADD M3DE**](../M3UA目的实体/增加M3UA目的实体(ADD M3DE)_72345901.md)）不能够有相同的BIT位设置成1； 如果该链路集的业务模式为“OVERRIDE”，该参数不起作用。 |
| LSN | 链路集名 | 可选必选说明：可选参数<br>参数含义：该参数用于表示链路集名称，标识链路集。<br>数据来源：本端规划<br>取值范围：1～32位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@M3LKS]] · M3UA信令链路集（M3LKS）

## 使用实例

将索引为1的M3UA链路集的链路选择掩码改为B0010，链路集名改为“lks1”：

MOD M3LKS: LSX=1, SLSM=B0010, LSN="lks1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-M3LKS.md`
