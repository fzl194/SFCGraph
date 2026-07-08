---
id: UNC@20.15.2@MMLCommand@ADD SGSLKS
type: MMLCommand
name: ADD SGSLKS（增加SGs链路集）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SGSLKS
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 256
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- SGSAP
- SGsAP链路集管理
status: active
---

# ADD SGSLKS（增加SGs链路集）

## 功能

**适用网元：MME**

此命令用于增加SGs链路集。

当需要配置到一个MSC/VLR的链接时，首先通过执行此命令配置一个管理到MSC/VLR的所有链路的集合，然后通过 [**ADD SGSLNK**](../SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) 命令配置多条并行链路。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为256。
- 此配置涉及“基于CSFB的语音业务”特性（特性编号：WSFD-102301，License部件编码：LKV2CSFBGU02），执行命令请使用**DSP LICENSE**命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSX | 链路集索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定链路集的索引。<br>数据来源：本端规划<br>取值范围：0~255<br>默认值：无<br>配置原则：增加链路集时，链路集索引建议从小到大配置。 |
| VN | VLR号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端MSC/VLR提供的VLR号。<br>前提条件：该参数已增加，参见<br>[**ADD VLR**](../../VLR管理/增加VLR配置信息(ADD VLR)_26305254.md)<br>。<br>数据来源：与对端MSC/VLR协商<br>取值范围：1~15位十进制数字<br>默认值 ：无 |
| LSN | 链路集名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定链路集的名称。<br>数据来源：本端规划<br>取值范围：1~50位字符串<br>默认值：noname<br>说明：该参数用于区分不同的链路集，也可以直接使用MSC/VLR名来标识。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGSLKS]] · SGs链路集（SGSLKS）

## 使用实例

增加一个 “VLR号” 为 “11808” 的SGs链路集， “链路集索引” 为 “0” ， “链路集名 ” 为 “VLR8” ：

ADD SGSLKS: LSX=0, VN="11808", LSN="VLR8";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SGSLKS.md`
