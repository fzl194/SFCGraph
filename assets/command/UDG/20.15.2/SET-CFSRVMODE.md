---
id: UDG@20.15.2@MMLCommand@SET CFSRVMODE
type: MMLCommand
name: SET CFSRVMODE（配置 URL过滤业务模式）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: CFSRVMODE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- URL过滤业务模式配置
status: active
---

# SET CFSRVMODE（配置 URL过滤业务模式）

## 功能

**适用NF：PGW-U、UPF**

![](配置 URL过滤业务模式（SET CFSRVMODE）_19881182.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致URL过滤业务故障，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置URL过滤业务模式。

## 注意事项

- 该命令执行后立即生效。
- 如果DBMODE要设置为CUSTOMIZATION1，需要保证ADD CFPROFILE配置的CFPROFILENAME必须包含“&”且“&”不在字符串首尾，并且不同CFPROFILENAME“&”之前的字符串不一致。否则无法将DBMODE设置为CUSTOMIZATION1。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | DBMODE | ENCRYALGORI |
| --- | --- | --- |
| 初始值 | STANDARD | NONE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DBMODE | URL过滤策略库模式 | 可选必选说明：必选参数<br>参数含义：该命令用于配置URL过滤策略库模式。<br>数据来源：本端规划<br>取值范围：<br>- STANDARD：使用华为推荐模式。<br>- CUSTOMIZATION1：客户定制模式1，使用前请联系华为工程师。<br>- CUSTOMIZATION2：客户定制模式2，使用前请联系华为工程师。<br>默认值：无<br>配置原则：无 |
| ENCRYALGORI | 加密算法 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DBMODE”配置为“CUSTOMIZATION1”或“CUSTOMIZATION2”时为必选参数。<br>参数含义：该参数用于指定对携带的参数的加密方式。<br>数据来源：本端规划<br>取值范围：<br>- NONE：不进行加密，有安全风险，不建议使用。<br>- SHA256：加密类型为SHA256。<br>默认值：无<br>配置原则：ENCRYALGORI参数仅在DBMODE配置为CUSTOMIZATION1或CUSTOMIZATION2时生效。 |
| PSWDKEY | 加密算法密钥 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENCRYALGORI”配置为“SHA256”时为必选参数。<br>参数含义：该参数用于设置参数加密算法的密钥。<br>数据来源：本端规划<br>取值范围：输入长度范围为1~256.不支持空格。<br>默认值：无<br>配置原则：无 |
| PSWDKEYCONFIRM | 加密算法密钥确认 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENCRYALGORI”配置为“SHA256”时为必选参数。<br>参数含义：该参数用于确认加密算法的密钥。<br>数据来源：本端规划<br>取值范围：输入长度范围为1~256.不支持空格。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域参数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DBMODE”配置为“STANDARD”、“CUSTOMIZATION1” 或 “CUSTOMIZATION2”时为可选参数。<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~31.。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [URL过滤功能业务模式（CFSRVMODE）](configobject/UDG/20.15.2/CFSRVMODE.md)

## 使用实例

配置URL过滤策略库模式为STANDARD：

```
SET CFSRVMODE: DBMODE=STANDARD;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/配置-URL过滤业务模式（SET-CFSRVMODE）_19881182.md`
