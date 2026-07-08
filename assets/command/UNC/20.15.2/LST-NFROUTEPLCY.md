---
id: UNC@20.15.2@MMLCommand@LST NFROUTEPLCY
type: MMLCommand
name: LST NFROUTEPLCY（查询NF路由策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFROUTEPLCY
command_category: 查询类
applicable_nf:
- SMF
- AMF
- SMSF
- NCG
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- NF通信模式管理
- NF间接路由管理
status: active
---

# LST NFROUTEPLCY（查询NF路由策略）

## 功能

**适用NF：SMF、AMF、SMSF、NCG、NSSF**

该命令用于查询对端NF路由策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INFOTYPE | 信息类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定信息类型。<br>数据来源：全网规划<br>取值范围：<br>- “NFID（NFID）”：使用NF实例ID信息<br>- “IP（IP）”：使用IP信息<br>- “FQDN（FQDN）”：使用FQDN信息<br>默认值：无<br>配置原则：无 |
| IPADDRESSTYPE | IP地址类型 | 可选必选说明：该参数在"INFOTYPE"配置为"IP"时为条件必选参数。<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPTypeV4（IPTypeV4）<br>- IPTypeV6（IPTypeV6）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFROUTEPLCY]] · NF路由策略（NFROUTEPLCY）

## 使用实例

- 查询所有对端NF路由策略；
  ```
  %%LST NFROUTEPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  索引   信息类型         NF实例标识      IP地址类型      IPv4前缀     IPv6前缀  				IPv4掩码长度  IPv6掩码长度       FQDN后缀         路由策略             

  1      NFID             udm_instance_0  NULL            0.0.0.0      ::           			0          	  0          NULL             直连通信
  2      IP               NULL            IPTypeV4        192.168.0.0  ::           			24         	  0          NULL             通过SCP通信
  3      IP               NULL            IPTypeV6        0.0.0.0      2001:db8:1:1:1:1:1:0   0             120        NULL             通过SCP通信
  4      FQDN             NULL            NULL            0.0.0.0      ::           			0             0          udm1.huawei.com  通过SCP通信
  (结果个数 = 4)

  ---    END
  ```
- 查询所有按NF实例标识配置的路由策略；
  ```
  %%LST NFROUTEPLCY: INFOTYPE=NFID;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
        索引  =  1
  NF实例标识  =  udm_instance_0
    路由策略  =  直连通信
  (结果个数 = 1)

  ---    END
  ```
- 查询所有按IP配置的路由策略；
  ```
  %%LST NFROUTEPLCY: INFOTYPE=IP, IPADDRESSTYPE=IPTypeV4;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
      索引      =  2
  IPv4前缀      =  192.168.0.0
  IPv4掩码长度  =  24
  路由策略      =  通过SCP通信
  (结果个数 = 1)

  ---    END
  ```
- 查询所有按FQDN配置的路由策略。
  ```
  %%LST NFROUTEPLCY: INFOTYPE=FQDN;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
      索引  =  4
  FQDN后缀  =  udm1.huawei.com
  路由策略  =  通过SCP通信
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFROUTEPLCY.md`
