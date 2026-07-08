---
id: UDG@20.15.2@MMLCommand@ADD FWRULE
type: MMLCommand
name: ADD FWRULE（增加转发规则）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: FWRULE
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 代理管理
status: active
---

# ADD FWRULE（增加转发规则）

## 功能

![](增加转发规则（ADD FWRULE）_01524840.assets/notice_3.0-zh-cn.png)

该命令执行后可能会影响到目的IP的转发，请谨慎操作。

此命令用于增加指定IP的原端口到目的端口的转发规则，可用于SFTP端口的转换。

> **说明**
> - 该命令仅限角色为Administrators的用户执行。
>
> - 同一目的IP和端口只能配置一条规则，若需修改，请先使用**[RMV FWRULE](删除转发规则（RMV FWRULE）_01844648.md)**命令删除该规则后使用本命令重新配置。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| IPTYPE | IP版本 | 可选必选说明：必选参数。<br>参数含义：IP类型。<br>取值范围：<br>- IPV4(IPv4类型)<br>- IPV6(IPv6类型)<br>默认值：IPV4(IPv4类型)。<br>配置原则：无。 |
| TGTIPV4 | 目的IPV4地址 | 可选必选说明：当<br>“IP版本”<br>为<br>“IPV4(IPv4类型)”<br>时为必选参数。<br>参数含义：目的IPV4地址。<br>取值范围：有效的IPv4地址。<br>默认值：无。<br>配置原则：无。 |
| TGTIPV6 | 目的IPV6地址 | 可选必选说明：当<br>“IP版本”<br>为<br>“IPV6(IPv6类型)”<br>时为必选参数。<br>参数含义：目的IPV6地址。<br>取值范围：有效的IPv6地址。<br>默认值：无。<br>配置原则：无。 |
| PORT | 端口 | 可选必选说明：必选参数。<br>参数含义：目的IP地址的原端口。<br>取值范围：1~65535<br>默认值：无。<br>配置原则：无。 |
| TGTPORT | 目的端口 | 可选必选说明：必选参数。<br>参数含义：目的IP地址的目的端口。<br>取值范围：1~65535<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FWRULE]] · 转发规则（FWRULE）

## 使用实例

假如运营商希望将发往192.168.1.1:22的请求转发到192.168.1.1:25，需要执行如下命令增加转发规则。

```
%%ADD FWRULE: IPTYPE=IPV4, TGTIPV4="192.168.1.1", PORT=22, TGTPORT=25;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-FWRULE.md`
