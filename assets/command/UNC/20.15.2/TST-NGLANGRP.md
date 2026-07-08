---
id: UNC@20.15.2@MMLCommand@TST NGLANGRP
type: MMLCommand
name: TST NGLANGRP（测试5G LAN组会话状态）
nf: UNC
version: 20.15.2
verb: TST
object_keyword: NGLANGRP
command_category: 调测类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 5G LAN管理
- 5G LAN组会话核查
status: active
---

# TST NGLANGRP（测试5G LAN组会话状态）

## 功能

**适用NF：SMF**

该命令用于主动发起5G LAN组会话核查。命令执行后，SMF会主动给UPF发送一个PFCP Session Modification Request消息来核查SMF和UPF之间的组会话信息。核查结果可通过DSP NGLANUPINFO: NGLANUPINFOTYPE=ALL命令来查询。

## 注意事项

- 该命令执行后立即生效。

- 当SMF整系统复位或DS复位时，为了及时获取组会话状态，可在DS重新拉起的一段时间之后，手动执行该命令来发起5G LAN组会话核查。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGLANGROUPID | 5G LAN组ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN群组的ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是18~37。字母大小写不敏感且全局唯一。<br>默认值：无<br>配置原则：<br>NGLANGROUPID以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A-F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A-F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGLANGRP]] · 测试5G LAN组会话状态（NGLANGRP）

## 使用实例

- 如果想对所有5G LAN组会话发起核查，执行如下命令：
  ```
  TST NGLANGRP;
  RETCODE = 0  操作成功。
  ```
- 如果想对指定组ID的5G LAN组会话核查，执行如下命令：
  ```
  TST NGLANGRP:NGLANGROUPID="A0000001-460-003-01";
  RETCODE = 0  操作成功。
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/TST-NGLANGRP.md`
