---
id: UNC@20.15.2@MMLCommand@CLR NSSFIPSTAT
type: MMLCommand
name: CLR NSSFIPSTAT（清除NSSF局向内统概要数据）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: NSSFIPSTAT
command_category: 动作类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF维测管理
status: active
---

# CLR NSSFIPSTAT（清除NSSF局向内统概要数据）

## 功能

**适用NF：NSSF**

该命令用于清除NSSF局向内统概要数据。

## 注意事项

- 该命令执行后立即生效。

- 如果只清理特定IP的局向内统数据，必须指定IP，如果不指定，则会清理所有局向内统数据。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPADDRESSTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需清除的局向内统对应对端NF的客户端IP类型。不指定该参数时表示清除所有局向内统数据。<br>数据来源：本端规划<br>取值范围：<br>- IPTypeV4（IPV4类型）<br>- IPTypeV6（IPV6类型）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPV4地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定对端NF的客户端IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPV6地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定对端NF的客户端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NSSF的局向内统概要数据（NSSFIPSTAT）](configobject/UNC/20.15.2/NSSFIPSTAT.md)

## 使用实例

- 将IP为10.10.10.10的NF对应的局向内统数据清零：
  ```
  CLR NSSFIPSTAT:IPADDRESSTYPE=IPTypeV4,IPV4ADDRESS="10.10.10.10";
  ```
- 将所有局向内统数据清零：
  ```
  CLR NSSFIPSTAT:;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除NSSF局向内统概要数据（CLR-NSSFIPSTAT）_22556855.md`
