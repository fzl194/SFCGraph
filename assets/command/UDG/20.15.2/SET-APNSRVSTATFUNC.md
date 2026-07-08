---
id: UDG@20.15.2@MMLCommand@SET APNSRVSTATFUNC
type: MMLCommand
name: SET APNSRVSTATFUNC（设置APN业务统计开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNSRVSTATFUNC
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- APN的业务统计开关设置
status: active
---

# SET APNSRVSTATFUNC（设置APN业务统计开关）

## 功能

**适用NF：PGW-U、UPF**

![](设置APN业务统计开关（SET APNSRVSTATFUNC）_82837848.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。

该命令用于配置指定APN是否启用ServiceStatistic检测功能。当需要配置指定该APN开启或关闭基于业务的性能统计功能的时候使用此命令。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条。
- 每个APN实例下可以配置一条ServiceStatistic检测功能，该记录随APN建立时有初始值DISABLE。
- 重复配置本命令，表示对已有配置数据修改。配置修改，仅对之后发生承载更新的用户或者新激活用户生效。
- APN开启基于业务的性能统计功能后，需要对业务流进行复杂的协议识别处理，可能到导致业务处理能力下降。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH |
| --- | --- |
| 初始值 | DISABLE |

- 该命令误配后会影响系统性能。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SWITCH | 开关标识 | 可选必选说明：必选参数<br>参数含义：该参数用于在指定APN下配置是否启用service-statistic功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：业务统计功能关闭。<br>- ENABLE：业务统计功能打开。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN业务统计开关（APNSRVSTATFUNC）](configobject/UDG/20.15.2/APNSRVSTATFUNC.md)

## 使用实例

假如运营商需要开启指定APN的ServiceStatistic检测功能，则配置命令如下：

```
SET APNSRVSTATFUNC:APN="apntest",SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置APN业务统计开关（SET-APNSRVSTATFUNC）_82837848.md`
