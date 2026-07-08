---
id: UDG@20.15.2@MMLCommand@ADD MULTICASTSOURCE
type: MMLCommand
name: ADD MULTICASTSOURCE（增加IGMP Snooping组播源配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: MULTICASTSOURCE
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- IGMP Snooping配置
- 组播源配置
status: active
---

# ADD MULTICASTSOURCE（增加IGMP Snooping组播源配置）

## 功能

**适用NF：UPF**

该命令用于增加IGMP Snooping组播源配置。

## 注意事项

- 该命令执行后立即生效。
- 如果此IMSI配置成了结对成员，那么此IMSI就只能以结对方式配置为组播源。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD NGVNINSTANCE命令配置生成。 |
| MCSOURCETYPE | 组播源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置组播源类型。<br>数据来源：全网规划<br>取值范围：<br>- IMSI：IMSI。<br>- DFSRPAIR：双发选收结对。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“MCSOURCETYPE”配置为“IMSI”时为必选参数。<br>参数含义：组播源IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15，每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| DFSRPAIRID | 双发选收结对ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“MCSOURCETYPE”配置为“DFSRPAIR”时为必选参数。<br>参数含义：该参数用于配置双发选收结对ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1-2048。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MULTICASTSOURCE]] · IGMP Snooping组播源配置（MULTICASTSOURCE）

## 使用实例

设置配置5G LAN组的N3侧的组播源：

```
ADD MULTICASTSOURCE: VNINSTANCE="a0000001-460-003-01", MCSOURCETYPE=IMSI, IMSI="217456789012353";

%%ADD MULTICASTSOURCE: VNINSTANCE="a0000001-460-003-01", MCSOURCETYPE=IMSI, IMSI="217456789012353";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-MULTICASTSOURCE.md`
