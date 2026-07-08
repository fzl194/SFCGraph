---
id: UNC@20.15.2@MMLCommand@ADD SMSFOPC
type: MMLCommand
name: ADD SMSFOPC（增加SMSF本局信令点）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMSFOPC
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
max_records: 10
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- SMSFOPC本局信令点
status: active
---

# ADD SMSFOPC（增加SMSF本局信令点）

## 功能

**适用NF：SMSF**

该命令用于在5G短消息微服务SMSF对接短消息中心时，识别是否为5G短消息，用来区分传统2、3G网络业务和5G业务。

## 注意事项

- 此命令的最大记录数为10。
- 该命令中的NI+OPC+SMSFN需要先通过ADD SCCPOPC创建。

- 本局信令点只适用5G短消息使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPX | SMSF信令点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SMSF本局信令点索引。<br>数据来源：本端规划<br>取值范围：1～10。<br>默认值：无<br>配置原则：无 |
| NI | 网络指示语 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络指示语，区分不同的网络。<br>数据来源：整网规划<br>取值范围：<br>- “INT（国际网）”<br>- “INTB（国际备用网）”<br>- “NAT（国内网）”<br>- “NATB（国内备用网）”<br>默认值：无<br>配置原则：<br>- NI+OPC+SMSFN需要在SCCPOPC记录中存在。<br>说明：配置的网络指示语在信令属性表中应该配置为有效（<br>[**SET SIGATTR**](../../信令网属性管理/设置信令网属性(SET SIGATTR)_72226021.md)<br>）。 |
| OPC | 本局信令点编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本局信令点编码，可以采用24位信令点编码或14位信令编码。本局信令点编码在同一网络中唯一。<br>数据来源：整网规划<br>取值范围：长度不超过8的字符串<br>默认值：无<br>配置原则：<br>- 配置的信令点编码结构需要和信令属性表中对应的信令网络的网络结构保持一致。<br>- 取值为0x1~0x3FFF（对应14位编码）或0x1~0xFFFFFF（对应24位编码），不输入0x也取输入为十六进制值，即输入123等价于0x123。<br>- NI+OPC+SMSFN需要在SCCPOPC记录中存在。 |
| SMSFN | 本局SMSF号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本局SMSF号。<br>数据来源：整网规划<br>取值范围：长度不超过16的十进制数字<br>默认值：无<br>配置原则：<br>- NI+OPC+SMSFN需要在SCCPOPC记录中存在。 |
| OPN | 本局信令点名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本局信令点名。<br>数据来源：本端规划<br>取值范围：长度不超过32的字符串<br>默认值：noname<br>配置原则：无 |
| MASTER | 是否主用信令点 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SMSF本局信令点的主用信令点。<br>数据来源：本端规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>配置原则：无<br>说明：整系统中最多只支持1条为“YES”的记录。若无主用信令点（所有记录都为“NO”）发送短消息会失败。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSFOPC]] · SMSF本局信令点（SMSFOPC）

## 使用实例

增加SMSF本局信令点，本局信令点索引为1，网络指示语为INT，本局信令点编码为“0x55”，本局信令点名为“Peking”：

```
ADD SMSFOPC: OPX=1, NI=INT, OPC="0x55", SMSFN="8615654029",OPN="Peking", MASTER=YES
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SMSFOPC.md`
