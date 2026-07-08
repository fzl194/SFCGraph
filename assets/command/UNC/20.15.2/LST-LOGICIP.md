---
id: UNC@20.15.2@MMLCommand@LST LOGICIP
type: MMLCommand
name: LST LOGICIP（查询逻辑IP地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOGICIP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IP管理
- IP配置
status: active
---

# LST LOGICIP（查询逻辑IP地址）

## 功能

该命令用于查询已经配置的逻辑IP地址以及逻辑IP地址与VPN实例的所属关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | 逻辑IP地址版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定逻辑IP地址版本。<br>数据来源：全网规划<br>取值范围：<br>- “IPv4（IPv4）”：IPv4地址<br>- “IPv6（IPv6）”：IPv6地址<br>默认值：无<br>配置原则：无 |
| LOGICIPV4 | 逻辑IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件可选参数。<br>参数含义：该参数用于指定逻辑IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| LOGICIPV6 | 逻辑IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件可选参数。<br>参数含义：该参数用于指定逻辑IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LOGICIP]] · 逻辑IP地址信息（LOGICIP）

## 使用实例

- 查询逻辑IP地址为fc00:38:0:0:0:0:0:2的表信息。
  ```
  LST LOGICIP: IPVERSION=IPv6, LOGICIPV6="fc00:38:0:0:0:0:0:2";
  %%LST LOGICIP: IPVERSION=IPv6, LOGICIPV6="fc00:38:0:0:0:0:0:2";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  逻辑IP地址版本  =  IPv6
    逻辑IPv6地址  =  fc00:38::2
    IPv6 MTU大小  =  1500
     VPN实例名称  =  _public_
            描述  =  ipv6
  (结果个数 = 1)

  ---    END
  ```
- 查询逻辑IP表
  ```
  LST LOGICIP:;
  %%LST LOGICIP:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  逻辑IP地址版本  逻辑IPv4地址  逻辑IPv6地址  IPv4 MTU大小  IPv6 MTU大小  VPN实例名称  描述  

  IPv4            172.16.0.1    ::            1500          1500          _public_     NULL  
  IPv6            0.0.0.0       fc00:38::2    1500          1500          _public_     ipv6
         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LOGICIP.md`
