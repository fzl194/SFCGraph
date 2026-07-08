---
id: UNC@20.15.2@MMLCommand@ADD MMEID
type: MMLCommand
name: ADD MMEID（增加MMEID配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MMEID
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME POOL区管理
- MMEID管理
status: active
---

# ADD MMEID（增加MMEID配置）

## 功能

![](增加MMEID配置(ADD MMEID)_26146088.assets/notice_3.0-zh-cn_2.png)

可能会造成IntraTAU成功率指标大幅下降。

**适用网元：MME**

此命令用于在MMEID表中增加一条记录，该记录在PLMN中唯一标识一个MME。在MME给用户分配GUTI时，系统会根据本命令中输入的 “MME编码（起始值）” 来生成GUTI。用户附着时，系统会将GUTI中的MCC、MNC、MMEGI及MMEC信息与MMEID中的信息比对，若不同则认为是Inter附着。

## 注意事项

- 此命令当前最大记录数为1。
- 此命令执行后立即生效。
- 可能会造成IntraTAU成功率指标大幅下降。
- 4G用户发起SGs接口更新时，会携带MMENAME信元给MSC，配置该命令将导致MMENAME信元改变，所以对端MSC需要同步修改相关配置，否则用户的SGs接口更新流程将会失败。
- 配置该命令时，需要同步修改DNS的相关域名，否则会导致相关的DNS查询失败。
- 配置该命令时，UNC会下发MME Configuration Update消息给eNodeB通知GUMMEI改变。
- 此命令配置的MMEID映射后对应的GUAMI不能和AMF中配置的GUAMI相同。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定由ITU-T统一分配的移动网络所在国家的标识符。<br>数据来源：整网规划<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个国家内的PLMN标识符。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数<br>默认值：无 |
| MMEGI | MME组识别码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME分组的编号。<br>数据来源：整网规划<br>取值范围：4位16进制编码<br>默认值：无<br>配置原则：<br>- MME组识别码在同一个PLMN下是唯一的。<br>- 可能会有多个PLMN同用一个MME组识别码。<br>- 同一个MME不能属于多个MME组。<br>- 按照协议需要设置MMEGI最高位为1。如果需要设置MMEGI最高位为0，则网元选择模式([**SET PESELPLCY**](../../../GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/SGSN MME选择/设置SGSN_MME选择策略（SET PESELPLCY）_72225643.md))推荐采用全网定制的识别模式。 |
| MMEC | MME编码（起始值） | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME组内的MME编码（起始值）。<br>数据来源：整网规划<br>取值范围：2位16进制编码<br>默认值：无<br>配置原则：<br>- 一个MME组内MME编码必须唯一。<br>- MME编码在互相覆盖的所有MME组中必须唯一。<br>- 在融合POOL组网场景下，本参数输入值应为：NRI起始值*2(8-NRI长度)，NRI起始值为[**ADD LOCALNRI**](../../SGSN POOL区管理/本局NRI配置/增加本局NRI配置信息(ADD LOCALNRI)_72345699.md)命令中输入的“NRI起始值”，NRI长度为[**ADD POOL**](../../SGSN POOL区管理/POOL区配置/增加POOL配置信息(ADD POOL)_72225781.md)命令中输入的“NRI长度”。如果不能满足上述规则，当进行GUL互操作时，可能导致IntraUNC流程变成InterUNC流程。 |
| MMECNUM | MME编码数目 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要配置的连续的MMEC的个数。<br>数据来源：整网规划<br>取值范围：1~32<br>默认值：1<br>配置原则：<br>- 在融合POOL组网场景下，本参数输入值应为：NRI个数*2(8-NRI长度)，NRI个数为[**ADD LOCALNRI**](../../SGSN POOL区管理/本局NRI配置/增加本局NRI配置信息(ADD LOCALNRI)_72345699.md)命令中输入的“NRI个数”，NRI长度为[**ADD POOL**](../../SGSN POOL区管理/POOL区配置/增加POOL配置信息(ADD POOL)_72225781.md)命令中输入的“NRI长度”。如果不能满足上述规则，当进行GUL互操作时，可能导致IntraUNC流程变成InterUNC流程。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMEID]] · MMEID配置（MMEID）

## 使用实例

增加一个 “移动国家码” 为 “123” 、 “移动网号” 为 “01” 、 “MME组识别码” 为 “8001” 、 “MME编码” 为 “01” 的MME节点：

ADD MMEID: MCC="123",MNC="01",MMEGI="8001",MMEC="01";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-MMEID.md`
