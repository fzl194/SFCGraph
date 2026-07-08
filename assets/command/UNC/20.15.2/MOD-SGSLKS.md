---
id: UNC@20.15.2@MMLCommand@MOD SGSLKS
type: MMLCommand
name: MOD SGSLKS（修改SGs链路集）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SGSLKS
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- SGSAP
- SGsAP链路集管理
status: active
---

# MOD SGSLKS（修改SGs链路集）

## 功能

**适用网元：MME**

此命令用于修改SGs链路集名称。

## 注意事项

- 此命令执行后立即生效。
- 此配置涉及“基于CSFB的语音业务”特性（特性编号：WSFD-102301，License部件编码：LKV2CSFBGU02），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSX | 链路集索引 | 可选必选说明：必选参数<br>参数含义：待修改链路集的索引。<br>数据来源：本端规划<br>取值范围：0~255<br>默认值：无 |
| LSN | 链路集名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定链路集的名称。<br>数据来源：整网规划<br>取值范围：1~50位字符串<br>默认值：无<br>说明：- 该参数用于区分不同的链路集，也可以直接使用MSC/VLR名来标识。<br>- 如果不输入该参数，则表示不修改该链路集的名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGSLKS]] · SGs链路集（SGSLKS）

## 使用实例

修改一个链路集的 “链路集名” 为 “VLR808” ，该链路集的 “链路集索引” 为 “0” ：

MOD SGSLKS: LSX=0, LSN="VLR808";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SGSLKS.md`
