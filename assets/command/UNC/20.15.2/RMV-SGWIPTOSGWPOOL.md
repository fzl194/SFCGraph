---
id: UNC@20.15.2@MMLCommand@RMV SGWIPTOSGWPOOL
type: MMLCommand
name: RMV SGWIPTOSGWPOOL（删除SGW IP）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SGWIPTOSGWPOOL
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 网络管理
- 业务快速恢复
- SGW IP
status: active
---

# RMV SGWIPTOSGWPOOL（删除SGW IP）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用于删除SGW POOL下绑定的SGW IP。假设运营商需要重新规划网络或者不再使用某个SGW IP时，使用该命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SGWPOOLNAME | SGW POOL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SGW POOL名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>该参数使用ADD SGWPOOL命令配置生成。 |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SGW POOL的地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | SGW的IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数在“IPVERSION”配置为“IPv4”时为必选参数。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>有效的IPv4地址不能为环回地址(127.x.y.z)。<br>有效的IPv4地址必须是A、B或者C类地址。 |
| IPV6ADDRESS | SGW的IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数在“IPVERSION”配置为“IPv6”时为必选参数。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGWIPTOSGWPOOL]] · SGW IP（SGWIPTOSGWPOOL）

## 使用实例

- 假设用户需要删除已绑定“10.1.1.1”的IPv4地址的SGW POOL，其名为“sgwpool1”：
  ```
  RMV SGWIPTOSGWPOOL:SGWPOOLNAME="sgwpool1",IPVERSION=IPV4,IPV4ADDRESS="10.1.1.1";
  ```
- 假设用户需要删除已绑定“2001:DB8::/32”的IPv6地址的SGW POOL，其名为“sgwpool1”：
  ```
  RMV SGWIPTOSGWPOOL:SGWPOOLNAME="sgwpool1",IPVERSION=IPV6,IPV6ADDRESS="2001:DB8::/32";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SGWIPTOSGWPOOL.md`
