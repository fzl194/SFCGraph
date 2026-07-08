---
id: UDG@20.15.2@MMLCommand@MOD ACLBINDAPN
type: MMLCommand
name: MOD ACLBINDAPN（修改Acl绑定关系）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: ACLBINDAPN
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户ACL管理
- ACL绑定APN
status: active
---

# MOD ACLBINDAPN（修改Acl绑定关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于修改APN下配置的ACL绑定。当需要改变APN下数据流的某个方向上绑定的ACL规则、或者改变改APN下ACL规则的生效时间时，可以使用此命令。

## 注意事项

- 生效方式：若配置时指定一个时间段，以此来指示ACL生效时间；如果没有指定时间段，则表示ACL是立即生效的。
- 区分down-link in-bound、down-link out-bound、up-link in-bound、up-link out-bound四个方向的绑定。gate和remark在in-bound使用，redirect在out-bound使用。如果ACL下绑定的节点中动作不符合要求，则返回失败；如果ACL下未绑定ACL节点，则不做检查。（由于系统对生效的ACL需要建立快速搜索表，建议配置时1秒不超过1个）。
- 命令SET SGWACLFUNC用来控制入口APN ACL功能对SGW是否生效，默认生效。
- SGW作为一个透传设备，不进行remark功能。
- ACL绑定到APN中或从APN中解绑时，需要等待30s后生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DIRECTION | 方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN绑定ACL的down-link in-bound、down-link out-bound、up-link in-bound、up-link out-bound四个方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UPIN：APN绑定ACL的方向为上行进系统。<br>- UPOUT：APN绑定ACL的方向为上行出系统。<br>- DOWNIN：APN绑定ACL的方向为下行进系统。<br>- DOWNOUT：APN绑定ACL的方向为下行出系统。<br>默认值：无<br>配置原则：按实际需要控制的方向来置值。 |
| ACLNAME | ACL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 当参数Direction配置为UPIN、DOWNIN时，该参数只能配置ACL节点的动作为gate、remark的ACL名称。<br>- 当参数Direction配置为UPOUT、DOWNOUT时，该参数只能配置ACL节点的动作为redirect的ACL名称。 |
| TIMERANGENAME | 时间段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置绑定关系生效时间。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写，以字母开头。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD TIMERANGE命令配置生成。<br>- 输入单空格将删除该参数已有配置项。<br>- 如果期望APN下绑定的ACL规则在指定的时间段生效则需要设置此参数；不配置此参数时，APN下绑定的ACL规则立即生效。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ACLBINDAPN]] · Acl绑定关系（ACLBINDAPN）

## 使用实例

假如运营商需要修改APN上行、进系统方向下绑定的ACL规则，由重定向动作的ACL规则改为门控动作的ACL规则：

```
MOD ACLBINDAPN:APN="testapn",DIRECTION=UPIN,ACLNAME="testacl2";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改Acl绑定关系（MOD-ACLBINDAPN）_82837725.md`
