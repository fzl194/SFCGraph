---
id: UNC@20.15.2@MMLCommand@LST GTPULE
type: MMLCommand
name: LST GTPULE（查询GTP-U本地实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPULE
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-U接口管理
- Gtpu本端实体管理
status: active
---

# LST GTPULE（查询GTP-U本地实体）

## 功能

**适用网元：SGSN、MME**

该命令用于查询GTPU本地实体。

## 注意事项

本命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | 组号 | 可选必选说明：可选参数<br>参数含义：本参数用于指定GTPU本端实体对应的组号。组号用于组网规划时不同接口，或者不同用户范围使用独立的GTPU本端实体。<br>数据来源：本端规划<br>取值范围：0~32<br>默认值：无 |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定GTPU本端实体的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “TPTADDR_TYPE_IPV4(IPV4)”<br>- “TPTADDR_TYPE_IPV6(IPV6)”<br>默认值：无 |
| LEIPV4 | IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：本参数用于指定GTPU本端实体的IPv4地址<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV4(IPV4)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| LEIPV6 | IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：本参数用于指定GTPU本端实体的IPv6地址<br>前提条件：该参数在<br>“IP类型”<br>参数配置为<br>“TPTADDR_TYPE_IPV6(IPV6)”<br>后生效。<br>数据来源：本端规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPULE]] · GTP-U本地实体（GTPULE）

## 使用实例

查询GTPU本地实体：

LST GTPULE:;

```
%%LST GTPULE:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
组号    IP地址类型    IPv4地址          VPN名称    记录索引    描述信息    资源标识

0       IPV4          10.141.149.100    abc        2           NULL        2       
0       IPV4          10.141.149.101    abc        3           NULL        3       
仍有后续报告输出
---    END

%%LST GTPULE:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
组号    IP地址类型    IPv6地址                          VPN名称    记录索引    描述信息    资源标识

0       IPV6          2001:db8:10:19:44:55:10:12        abc        0           NULL        0       
0       IPV6          2001:db8:10:19:44:55:10:13        abc        1           NULL        1       
(结果个数 = 4)
共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTP-U本地实体(LST-GTPULE)_26305792.md`
