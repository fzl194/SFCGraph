---
id: UNC@20.15.2@MMLCommand@ADD MSCOPC
type: MMLCommand
name: ADD MSCOPC（增加MSC信令点）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MSCOPC
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
max_records: 2
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- MSC管理
status: active
---

# ADD MSCOPC（增加MSC信令点）

## 功能

**适用NF：SMSF**

该命令用于增加MSC信令点配置。

## 注意事项

此命令的最大记录数为2。

## 权限

manage-ug；system-ug;
G_1，管理员级别命令组；G_2，操作员级别命令组;

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPX | MSC信令点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MSC本局信令点索引。<br>数据来源：本端规划<br>取值范围：1~2。<br>默认值：无<br>配置原则：无 |
| NI | 网络指示语 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络指示语，区分不同的网络。<br>数据来源：整网规划<br>取值范围：<br>- “INT（国际网）”<br>- “INTB（国际备用网）”<br>- “NAT（国内网）”<br>- “NATB（国内备用网）”<br>默认值：无<br>配置原则：<br>该命令中的NI+OPC+MSCN需要先通过ADD SCCPOPC创建。<br>说明：配置的网络指示语在信令属性表中应该配置为有效（<br>[**SET SIGATTR**](../信令网属性管理/设置信令网属性(SET SIGATTR)_72226021.md)<br>）。 |
| OPC | 本局信令点编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本局信令点编码，可以采用24位信令点编码或14位信令编码。本局信令点编码在同一网络中唯一。<br>数据来源：整网规划<br>取值范围：字符串类型，输入长度范围为1~8<br>默认值：无<br>配置原则：<br>- 配置的信令点编码结构需要和信令属性表中对应的信令网络的网络结构保持一致。<br>- 取值为0x1~0x3FFF（对应14位编码）或0x1~0xFFFFFF（对应24位编码），不输入0x也取输入为十六进制值，即输入123等价于0x123。<br>- 该命令中的NI+OPC+MSCN需要先通过ADD SCCPOPC创建。 |
| MSCN | 本局MSC号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本局MSC号。该字段需要和SMSC协商，不能和ADD SMSFOPC的SMSFN重复，可以和ADD VLROPC的VLRN重复。<br>数据来源：整网规划<br>取值范围：长度不超过16的十进制数字<br>默认值：无<br>配置原则：<br>该命令中的NI+OPC+MSCN需要先通过ADD SCCPOPC创建。 |
| MASTER | 主用信令点 | 可选必选说明：可选参数<br>参数含义：该参数用于是否为主用MSC，有且只能有一个MSC为主。<br>数据来源：本端规划<br>取值范围：<br>- “NO”<br>- “YES”<br>默认值：NO |

## 操作的配置对象

- [MSC信令点（MSCOPC）](configobject/UNC/20.15.2/MSCOPC.md)

## 使用实例

增加MSC信令点，MSC信令点索引为1，网络指示语为NAT，本局信令点编码为“340012”，本局MSC号为" 861390340012 ",主用信令点为“NO”：

```
ADD MSCOPC: OPX=1, NI=NAT, OPC="340012", MSCN="861390340012", MASTER=NO;"
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加MSC信令点(ADD-MSCOPC)_77595448.md`
