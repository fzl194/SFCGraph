---
id: UNC@20.15.2@MMLCommand@LST SDAPLE
type: MMLCommand
name: LST SDAPLE（查询SDAP本地实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SDAPLE
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- Sdup接口管理
- Sdup接口业务地址管理
status: active
---

# LST SDAPLE（查询SDAP本地实体）

## 功能

**适用网元：MME**

本命令用于查询SDAP链路本地实体配置数据。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：本参数用于增加指定Sdup接口的业务IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “TPTADDR_TYPE_IPV4(IPV4)”<br>- “TPTADDR_TYPE_IPV6(IPV6)”<br>默认值： 无 |
| LEIPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于增加指定Sdup接口的业务IPv4地址。<br>前提条件：该参数在“IP地址类型”参数配置为“TPTADDR_TYPE_IPV4(IPV4)”后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>配置原则:<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。 |
| LEIPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：本参数用于增加指定Sdup接口的业务IPv6地址。<br>前提条件：该参数在“IP地址类型”参数配置为“TPTADDR_TYPE_IPV6(IPV6)”后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则:<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1/128)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SDAPLE]] · SDAP本地实体（SDAPLE）

## 使用实例

1. 查询SDAP链路本地实体的IPv4配置数据：
  LST SDAPLE: IPTYPE=TPTADDR_TYPE_IPV4;
  ```
  %%LST SDAPLE: IPTYPE=TPTADDR_TYPE_IPV4;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------------------
   IP地址类型  =  IPV4
     IPv4地址  =  192.168.15.10
      vpn名称  =  NULL
     记录索引  =  0
     描述信息  =  NULL
     资源索引  =  0
  (结果个数 = 1)
  ---    END
  ```
2. 查询SDAP链路本地实体的IPv6配置数据：
  LST SDAPLE: IPTYPE=TPTADDR_TYPE_IPV6;
  ```
  %%LST SDAPLE: IPTYPE=TPTADDR_TYPE_IPV6;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------------------
   IP地址类型  =  IPV6
     IPv6地址  =  2001:db8:10:19:44:55:10:12
      vpn名称  =  NULL
     记录索引  =  1
     描述信息  =  NULL
     资源索引  =  1
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SDAP本地实体(LST-SDAPLE)_72346893.md`
