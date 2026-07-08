---
id: UDG@20.15.2@MMLCommand@SET NPSECPOLICYCAR
type: MMLCommand
name: SET NPSECPOLICYCAR（设置NP安全防攻击CAR规则）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NPSECPOLICYCAR
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP安全策略CAR
status: active
---

# SET NPSECPOLICYCAR（设置NP安全防攻击CAR规则）

## 功能

![](设置NP安全防攻击CAR规则(SET NPSECPOLICYCAR)_15401278.assets/notice_3.0-zh-cn.png)

修改CAR参数，影响系统功能和可靠性。参数配置不合理，会导致路由协议等相关报文丢弃，或导致控制面过载。

该命令用来设置IP的安全防攻击CAR规则。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CARTYPE | 安全协议类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定安全协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- OSPF：OSPF协议。<br>- LDP：LDP协议。<br>- IPV6_OSPF：IPV6_OSPF协议。<br>- IPV6_BGP：IPV6_BGP协议。<br>- IPV6_RA：IPV6_RA协议。<br>- IPV6_NS：IPV6_NS协议。<br>- GRE：GRE协议。<br>- IPV6_NA：IPV6_NA协议。<br>- BGP：BGP协议。<br>- IPV6_TOO_BIG：IPV6_TOO_BIG协议。<br>- Trace：IP Trace协议。<br>- UNKNOWN：未知协议。<br>- IPV6_RS：IPV6_RS协议。<br>- ARP_MISS：ARP_MISS协议。<br>- IPV4_MFIB_MISS：IPV4_MFIB_MISS协议。<br>- IPV6_ICMP：IPV6_ICMP协议。<br>- IGMP：IGMP协议。<br>- BFD_Trace：BFD_Trace协议。<br>- ARP：ARP协议。<br>- IPV6_DHCP：IPV6_DHCP协议。<br>- PIM：PIM协议。<br>- BFD：BFD协议。<br>- ICMP：ICMP协议。<br>- DHCP：DHCP协议。<br>- TOTAL_CAR：TOTAL_CAR。<br>默认值：无<br>配置原则：无 |
| CIR | 承诺信息速率（kbps） | 可选必选说明：必选参数<br>参数含义：该参数用于指定安全策略承诺信息速率。 该参数表示正常情况下允许发送的信息速率。即向漏桶发送令牌的速率，单位为kbps。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1000000。<br>默认值：无<br>配置原则：无 |
| CBS | 承诺突发尺寸（bytes） | 可选必选说明：可选参数<br>参数含义：该参数用于指定安全策略承诺突发尺寸。 此参数用于描述令牌桶C的容量，即在按CIR转发数据时允许转发的最大突发IP包尺寸。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～9000000。<br>默认值：无<br>配置原则：该参数建议大于或等于可能转发的最大IP包长度。如果不设置该参数，CBS的取值通过CIR*187计算得出。 |
| PIR | 峰值信息速率（kbps） | 可选必选说明：可选参数<br>参数含义：该参数用于指定安全策略峰值信息速率。该参数表示峰值流量速率，单位为kbps。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1000000。<br>默认值：无<br>配置原则：该参数值应大于或等于CIR。不设置该参数时，PIR默认为0。不配置时为单桶模式。 |
| PBS | 峰值突发尺寸（bytes） | 可选必选说明：可选参数<br>参数含义：该参数用于指定安全策略峰值突发尺寸。 此参数用于描述令牌桶P的容量，即在按PIR转发数据时允许转发的最大突发IP包尺寸。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～9000000。<br>默认值：无<br>配置原则：该参数建议大于或等于可能转发的最大IP包长度。不设置该参数时，PBS的取值通过PIR*187计算得出。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NPSECPOLICYCAR]] · NP安全防攻击CAR规则（NPSECPOLICYCAR）

## 使用实例

- 设置ARP协议的安全防攻击CAR规则：
  ```
  SET NPSECPOLICYCAR: CARTYPE=ARP, CIR=100, CBS=200, PIR=300, PBS=400;
  ```
  ```
  RETCODE = 0  操作成功。

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-NPSECPOLICYCAR.md`
