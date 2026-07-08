---
id: UNC@20.15.2@MMLCommand@SET ROUTSMSCPARA
type: MMLCommand
name: SET ROUTSMSCPARA（设置SMSF/VLR选择SMSC的相关参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ROUTSMSCPARA
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- SMSC选择管理
status: active
---

# SET ROUTSMSCPARA（设置SMSF/VLR选择SMSC的相关参数）

## 功能

**适用NF：SMSF**

该命令用于设置SMSF/VLR选择SMSC的相关参数。

## 注意事项

- 该命令执行后立即生效。

- 双活组网的场景下，如果需要配置此命令，则两个VLR/SMSF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SMSCGT | ROUTBYIMSISW | VIRTUALGT | GPSITRUNCATLEN |
| --- | --- | --- | --- |
| 0 | FUNC_OFF | 0 | 4 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMSCGT | 本大区SMSC的虚拟GT | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMSF/VLR所在大区对应SMSC的虚拟GT。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。只允许输入十进制数字（0-9）。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ROUTSMSCPARA查询当前参数配置值。<br>配置原则：无 |
| ROUTBYIMSISW | 按号段选择SMSC开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示融合短消息在MO流程中是否按照ADD IMSIFORSMSC所配置的IMSI号段选择SMSC的功能开关。开关打开时，如果IMSI归属GT与当前大区SMSC GT相同，则用LST IMSIFORSMSC结果号段与该IMSI匹配，匹配成功则选同大区同DC SMSC，匹配失败则选同大区异DC SMSC。<br>开关关闭时，当SMSF为本大区用户选择SMSC时，截取配置的后N位MSISDN，与ADD SMSCGT配置的SMSC个数做模运算来选择SMSC。<br>数据来源：本端规划<br>取值范围：<br>- “FUNC_ON（打开）”：功能开关打开<br>- “FUNC_OFF（关闭）”：功能开关关闭<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ROUTSMSCPARA查询当前参数配置值。<br>配置原则：无 |
| VIRTUALGT | 本大区异DC部署的SMSC的真实GT | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMSF/VLR所在大区同DC部署的SMSC的真实GT。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。只允许输入十进制数字（0-9）。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ROUTSMSCPARA查询当前参数配置值。<br>配置原则：无 |
| GPSITRUNCATLEN | MSISDN匹配长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMSF选择SMSC时，匹配用于轮选计算的MSISDN长度。当SMSF为本大区用户选择SMSC时，截取配置的后N位MSISDN，与ADD SMSCGT配置的SMSC个数做模运算来选择SMSC。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15，单位是个。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ROUTSMSCPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [SMSF/VLR选择SMSC的相关参数（ROUTSMSCPARA）](configobject/UNC/20.15.2/ROUTSMSCPARA.md)

## 使用实例

运营商希望设置“本大区SMSC的虚拟GT”为“123456”，“按号段选择SMSC开关”为“打开”，“本大区异DC部署的SMSC的真实GT”为“1234567”，“MSISDN匹配长度”为“4”，执行如下命令：

```
SET ROUTSMSCPARA: SMSCGT="123456", ROUTBYIMSISW=FUNC_ON, VIRTUALGT="1234567", GPSITRUNCATLEN=4;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMSF_VLR选择SMSC的相关参数（SET-ROUTSMSCPARA）_03961141.md`
