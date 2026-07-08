---
id: UNC@20.15.2@MMLCommand@LST NWNAMEBYHSS
type: MMLCommand
name: LST NWNAMEBYHSS（查询不发送运营商名称的HSS）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NWNAMEBYHSS
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- 不发送运营商名称的HSS
status: active
---

# LST NWNAMEBYHSS（查询不发送运营商名称的HSS）

## 功能

**适用网元：MME**

该命令用于查询不发送运营商名称的HSS。该命令对应的业务功能暂未实现。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置记录的索引。<br>数据来源：本端规划<br>取值范围：整数范围1~1000<br>默认值： 无<br>配置原则：无 |
| SELMODE | 匹配模式 | 可选必选说明：可选参数<br>参数含义：该参数用于表示选择不发送运营商名称的HSS的匹配模式。<br>数据来源：全网规划<br>取值范围：<br>- “LABEL(标识)”：匹配HSS主机名标识的用户<br>- “HOST(主机名)”：匹配HSS主机名的用户<br>- “REALM(域名)”：匹配HSS域名的用户<br>默认值：无<br>配置原则：无。 |
| LABEL | 标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定匹配用户的HSS网元标识的字符串。<br>前提条件：该参数在<br>“匹配模式”<br>设置为<br>“LABEL(标识)”<br>后生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。<br>默认值：无<br>配置原则：<br>- 输入字符串中不能含有非法字符，只允许输入字母，数字和“-”，不区分大小写。例如：UDMm、MHSS。<br>- 不允许配置以“null”开头的字符串。 |
| HOST | 主机名 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定用户的HSS的主机名。<br>前提条件：该参数在<br>“匹配模式”<br>设置为<br>“HOST(主机名)”<br>后生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”。例如：hss.epc.mnc123.mcc123.3gppnetwork.org<br>- 不允许配置以“null”开头的字符串。 |
| REALM | 域名 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定用户的HSS的域名。<br>前提条件：该参数在<br>“匹配模式”<br>设置为<br>“REALM(域名)”<br>后生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”。例如：epc.mnc123.mcc123.3gppnetwork.org<br>- 不允许配置以“null”开头的字符串。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NWNAMEBYHSS]] · 不发送运营商名称的HSS（NWNAMEBYHSS）

## 使用实例

1. 查询所有记录：
  LST NWNAMEBYHSS:;
2. 查询索引为1的记录：
  LST NWNAMEBYHSS: INDEX=1;
3. 查询“匹配模式”为“LABEL(标识)”的记录：
  LST NWNAMEBYHSS: SELMODE=LABEL;
4. 查询HSS主机名为“hss.epc.mnc123.mcc123.3gppnetwork.org”的记录：
  LST NWNAMEBYHSS: SELMODE=HOST, HOST="hss.epc.mnc123.mcc123.3gppnetwork.org";

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NWNAMEBYHSS.md`
