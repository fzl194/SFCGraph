---
id: UNC@20.15.2@MMLCommand@LST NRFNFREGIONIP
type: MMLCommand
name: LST NRFNFREGIONIP（查询IP与NF区域映射关系配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFNFREGIONIP
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF区域与IP映射关系配置管理
status: active
---

# LST NRFNFREGIONIP（查询IP与NF区域映射关系配置）

## 功能

**适用NF：NRF**

该命令用于查询IP与NF区域的映射关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF客户端地址的IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于表示NF的客户端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于表示NF客户端的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| NFREGION | NF归属区域 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF归属区域。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~36。该字段大小写不敏感 。<br>默认值：无<br>配置原则：<br>NF归属区域由运营商规划。 |

## 操作的配置对象

- [IP与NF区域映射关系配置（NRFNFREGIONIP）](configobject/UNC/20.15.2/NRFNFREGIONIP.md)

## 使用实例

- 查询IPv4类型的IP与NF区域的映射关系；
  ```
  LST NRFNFREGIONIP:;
  %%LST NRFNFREGIONIP: IPTYPE=IPV4;%%
  RETCODE = 0  Operation succeeded

  The result is as follows
  ------------------------
  IP类型        IPv4地址     IPv6地址  NF归属区域 

  IPv4 address  10.10.10.10  ::        ff
  IPv4 address  10.10.10.11  ::        ff
  (Number of results = 2)

  ---    END
  ```
- 查询指定IP与NF区域的映射关系。
  ```
  %%LST NRFNFREGIONIP: IPTYPE=IPV4, IPV4="10.10.10.10";%%
  RETCODE = 0  Operation succeeded

  The result is as follows
  ------------------------
  IP类型     =  IPv4 address
  IPv4地址   =  10.10.10.10
  IPv6地址   =  ::
  NF归属区域 = ff
  (Number of results = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IP与NF区域映射关系配置（LST-NRFNFREGIONIP）_71436541.md`
