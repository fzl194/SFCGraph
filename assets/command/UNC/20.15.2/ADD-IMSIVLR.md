---
id: UNC@20.15.2@MMLCommand@ADD IMSIVLR
type: MMLCommand
name: ADD IMSIVLR（增加IMSI与VLR对应关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IMSIVLR
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
max_records: 1000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- IMSI与VLR对应关系
status: active
---

# ADD IMSIVLR（增加IMSI与VLR对应关系）

## 功能

![](增加IMSI与VLR对应关系(ADD IMSIVLR)_72225129.assets/notice_3.0-zh-cn_2.png)

该命令可能导致SGs接口MSC/VLR选择方式发生变化，只建议对拨测用户使用该命令，拨测完成后请删除。请确认是否要继续？

**适用网元：MME**

该命令用于增加IMSI与MSC/VLR对应关系。当用户接入时，通过SGs接口选择MSC/VLR发送Location Update Request消息时，会优先选择IMSI对应的MSC/VLR。 该命令仅用于拨测场景，在MSC/VLR新割接入网后，可通过指定用户接入该MSC/VLR，拨测设备是否工作正常。拨测完毕后，请删除该命令以免后续影响该拨测用户。

如果选择的MSC/VLR处于“自动迁移中”或者“手动迁移中”状态，或者与当前IMSI匹配的MSC/VLR的链路异常时，会按照原有MSC/VLR选择方式重新进行选择，原有选择方式参见“WSFD- 102301 基于CSFB的语音业务”中的描述。

## 注意事项

- 此命令最大记录数为1000。
- 该命令生效的前提条件是，“WSFD-102301基于CSFB的语音业务”和“WSFD-104408通过SGs接口实现短消息”两个特性license至少要开启一个。
- 该命令执行后，用户通过SGs接口选择MSC/VLR时生效。
- 使用本命令指定MSC/VLR后，组网上要求用户当前的LAI在指定的MSC/VLR配置的LAI范围内。若用户当前的LAI不在指定的MSC/VLR配置的LAI范围内，会造成指定用户的Location Update流程失败。
- 当部署了“WSFD-201007SRVCC的MSC拓扑选择”或“WSFD-102401基于CSFB的USSD业务”或“WSFD-102402基于CSFB的LCS业务”特性时，如果用户在SRVCC流程，按对应特性方式选择的MSC/VLR配置了主机名，而使用该命令选择的MSC/VLR在[**ADD VLR**](../VLR管理/增加VLR配置信息(ADD VLR)_26305254.md)命令中未配置主机名或与原有配置的不一致，可能导致SRVCC流程选择的MSC/VLR与SGs接口选择的MSC/VLR不合一。如果选择的MSC/VLR要求SGs与Sv口必须合一，则SRVCC流程会失败。
- 该命令对于DWORD_EX16 BIT12软参设置为1时控制的场景不生效。
- 当用户联合附着或联合TAU时注册的MSC发生故障，MME接收到MSC Pool内其他MSC的Paging请求，后续第一次Location Update流程不会重新选择MSC/VLR，直接向本地存储的MSC/VLR进行Location Update流程。对此该命令将不生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的IMSI。<br>数据来源：全网规划<br>取值范围：14~15位十进制数字<br>默认值：无 |
| VN | VLR号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端MSC/VLR提供的VLR号。<br>前提条件：该参数必须先在<br>[**ADD VLR**](../VLR管理/增加VLR配置信息(ADD VLR)_26305254.md)<br>中取值相同的“VN”参数。<br>数据来源：全网规划<br>取值范围：1~15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSIVLR]] · IMSI与VLR对应关系（IMSIVLR）

## 使用实例

增加IMSI与VLR对应关系，“IMSI”为“123030000000001”，“VLR号”为“86139027”:

ADD IMSIVLR: IMSI="123030000000001", VN="86139027";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-IMSIVLR.md`
