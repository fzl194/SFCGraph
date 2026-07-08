---
id: UNC@20.15.2@MMLCommand@LST GTPCLE
type: MMLCommand
name: LST GTPCLE（查询GTP-C本地实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPCLE
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- Gtpc本端实体管理
status: active
---

# LST GTPCLE（查询GTP-C本地实体）

## 功能

**适用网元：SGSN、MME、AMF**

该命令用于查询GTPC本地实体。

## 注意事项

- 本命令执行后立即生效。
- 所有参数不输入，表示查询所有已存在的GTPC本端实体记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | 组号 | 可选必选说明：可选参数<br>参数含义：本参数用于指定GTPC本端实体对应的组号。组号用于组网规划时不同接口，或者不同用户范围使用独立的GTPC本端实体。<br>数据来源：本端规划<br>取值范围：0~32<br>默认值：无 |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定GTPC本端实体的IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- “TPTADDR_TYPE_IPV4(IPv4)”<br>- “TPTADDR_TYPE_IPV6(IPv6)”<br>默认值：无 |
| LEIPV4 | IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：本参数用于指定GTPC本端实体的IPV4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV4(IPv4)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| LEIPV6 | IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：本参数用于指定GTPC本端实体的IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV6(IPv6)”<br>后生效。<br>数据来源：本端规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |

## 操作的配置对象

- [GTP-C本地实体（GTPCLE）](configobject/UNC/20.15.2/GTPCLE.md)

## 使用实例

1. 查询GTPC本地实体
  LST GTPCLE:;
  ```
  %%LST GTPCLE:;%%
  RETCODE = 0  执行成功。
  操作结果如下
  -------------------------
  组号     IP地址类型  IPv4地址          VPN名称   GTP-C本端实体标识   描述信息   资源标识

  11       IPv4        192.168.3.4       _abc_      0                  NULL       0
  3        IPv4        192.168.3.5       _abc_      1                  Gtpule     1
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTP-C本地实体(LST-GTPCLE)_72345567.md`
