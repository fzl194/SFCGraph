---
id: UDG@20.15.2@MMLCommand@SET POOLALMTHD
type: MMLCommand
name: SET POOLALMTHD（设置指定本地POOL占用率告警阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: POOLALMTHD
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 40000
category_path:
- 用户面服务管理
- 业务运维
- 业务告警管理
- 指定地址池占用率告警阈值
status: active
---

# SET POOLALMTHD（设置指定本地POOL占用率告警阈值）

## 功能

**适用NF：PGW-U、UPF**

此命令用于设置本地地址池使用率的告警阈值和告警恢复阈值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为40000。
- 修改告警阈值和告警恢复阈值后，如果之前上报了告警，则会先恢复之前的告警，然后根据新配置的告警阈值和告警恢复阈值判断是否上报新的告警。
- 若门限配置的不合理，配置过低，则可能会导致系统频繁告警；配置过高，则可能不能及时提醒地址可能即将用完，进而影响必要的扩容。
- 指定本地地址池告警恢复阈值时，告警恢复阈值必须小于告警阈值。
- 该命令最大记录数和ADD POOL的记录数保持一致。
- 该命令不存在系统初始值。当某个POOL不配置当前命令时，地址池的告警阈值使用全局的配置SET IPPOOLALMTHD。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：此参数必须是ADD POOL已配置的地址池名称。 |
| WARNTHRESH | 告警产生阈值（%） | 可选必选说明：必选参数<br>参数含义：本地地址池使用率的告警阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0 ~ 100，单位是百分比。<br>默认值：无<br>配置原则：无 |
| RECVTHRESH | 告警恢复阈值（%） | 可选必选说明：必选参数<br>参数含义：本地地址池使用率的告警恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0 ~ 100，单位是百分比。<br>默认值：无<br>配置原则：无 |
| SWITCH | 指定地址池告警阈值配置开关 | 可选必选说明：必选参数<br>参数含义：指定地址池告警阈值配置开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/POOLALMTHD]] · 本地指定地址池占用率告警阈值（POOLALMTHD）

## 使用实例

设置指定本地地址池使用率的告警阈值和告警恢复阈值：

```
SET POOLALMTHD: POOLNAME="pool1", WARNTHRESH=66, RECVTHRESH=55, SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置指定本地POOL占用率告警阈值（SET-POOLALMTHD）_37455140.md`
