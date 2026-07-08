---
id: UNC@20.15.2@MMLCommand@RMV MMEIPTOMMEPOOL
type: MMLCommand
name: RMV MMEIPTOMMEPOOL（删除MME IP）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MMEIPTOMMEPOOL
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 网络管理
- 业务快速恢复
- MME IP
status: active
---

# RMV MMEIPTOMMEPOOL（删除MME IP）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于删除MME POOL绑定的地址。假设该MME IP不需要再使用，使用该命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEPOOLNAME | MME POOL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME POOL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD MMEPOOL命令配置生成。 |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME地址池的地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>- IPV4V6（IPV4V6）<br>默认值：无<br>配置原则：<br>仅当“BACKUP”参数配置为TRUE时，该参数可配置为IPV4V6。 |
| IPV4ADDRESS | MME的IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"、"IPV4V6"时为条件必选参数。<br>参数含义：该参数指定该地址类型为IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>有效的IPv4地址不能为环回地址(127.x.y.z)。<br>有效的IPv4地址必须是A、B或者C类地址。 |
| IPV6ADDRESS | MME的IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"、"IPV4V6"时为条件必选参数。<br>参数含义：该参数指定该地址类型为IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [MME IP（MMEIPTOMMEPOOL）](configobject/UNC/20.15.2/MMEIPTOMMEPOOL.md)

## 使用实例

假设用户需要删除“mmepool1”下绑定的IPv4地址“10.1.1.1”：

```
RMV MMEIPTOMMEPOOL:MMEPOOLNAME="mmepool1",IPVERSION=IPV4,IPV4ADDRESS="10.1.1.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MME-IP（RMV-MMEIPTOMMEPOOL）_31453521.md`
