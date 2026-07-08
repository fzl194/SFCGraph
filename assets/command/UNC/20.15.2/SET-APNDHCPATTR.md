---
id: UNC@20.15.2@MMLCommand@SET APNDHCPATTR
type: MMLCommand
name: SET APNDHCPATTR（设置APN DHCP属性配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: APNDHCPATTR
command_category: 配置类
applicable_nf:
- GGSN
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- APN的DHCP属性
status: active
---

# SET APNDHCPATTR（设置APN DHCP属性配置）

## 功能

**适用NF：GGSN、PGW-C、SMF**

该命令用于设置APN的DHCP相关信息，当用户需要修改APN下配置的DHCP信息时，可以使用该命令。

## 注意事项

- 该命令执行后立即生效。

- APN的值是由ADD APN命令添加。
- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：DHCPV4DEFER：DISABLE，INFINITELEASE：DISABLE，LEASEDAY：1，LEASEHOUR：0，LEASEMINUTE：0，DHCPV6STATELESS：DISABLE。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无。<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| DHCPV4DEFER | DHCPv4延迟分配 | 可选必选说明：可选参数<br>参数含义：表明是否支持DHCPv4延迟分配。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNDHCPATTR查询当前参数配置值。<br>配置原则：<br>根据运营商需求设置。 |
| INFINITELEASE | 租约无限 | 可选必选说明：可选参数<br>参数含义：该参数指定租用有效期限为无限长。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNDHCPATTR查询当前参数配置值。<br>配置原则：无 |
| LEASEDAY | 租约天数(天) | 可选必选说明：该参数在"INFINITELEASE"配置为"DISABLE"时为条件必选参数。<br>参数含义：该参数指定租用有效期限的天数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~30，单位是天。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNDHCPATTR查询当前参数配置值。<br>配置原则：无 |
| LEASEHOUR | 租约小时数(小时) | 可选必选说明：该参数在"INFINITELEASE"配置为"DISABLE"时为条件必选参数。<br>参数含义：该参数指定租用有限期限的小时数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~23，单位是小时。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNDHCPATTR查询当前参数配置值。<br>配置原则：无 |
| LEASEMINUTE | 租约分钟数(分钟) | 可选必选说明：该参数在"INFINITELEASE"配置为"DISABLE"时为条件必选参数。<br>参数含义：该参数指定租用有效期限的分钟数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~59，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNDHCPATTR查询当前参数配置值。<br>配置原则：无 |
| DHCPV6STATELESS | DHCPv6无状态 | 可选必选说明：可选参数<br>参数含义：表明是否支持DHCPv6无状态流程。<br>注意：IPV6 PD功能也需要开启此开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNDHCPATTR查询当前参数配置值。<br>配置原则：<br>根据运营商需求设置。 |

## 操作的配置对象

- [APN DHCP属性配置（APNDHCPATTR）](configobject/UNC/20.15.2/APNDHCPATTR.md)

## 使用实例

假设用户在APN “huawei.com”接入，需要该APN支持DHCPv4延迟分配，并指定租用有效期限为无限长，使用该命令配置：

```
SET APNDHCPATTR: APN="huawei.com", DHCPV4DEFER=ENABLE, INFINITELEASE=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置APN-DHCP属性配置（SET-APNDHCPATTR）_96243072.md`
