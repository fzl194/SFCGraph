# 查询IP与NF区域映射关系配置（LST NRFNFREGIONIP）

- [命令功能](#ZH-CN_MMLREF_0000001171436541__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001171436541__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001171436541__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001171436541__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001171436541__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001171436541)

**适用NF：NRF**

该命令用于查询IP与NF区域的映射关系。

## [注意事项](#ZH-CN_MMLREF_0000001171436541)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001171436541)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001171436541)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF客户端地址的IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于表示NF的客户端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于表示NF客户端的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| NFREGION | NF归属区域 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF归属区域。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~36。该字段大小写不敏感 。<br>默认值：无<br>配置原则：<br>NF归属区域由运营商规划。 |

## [使用实例](#ZH-CN_MMLREF_0000001171436541)

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

## [输出结果说明](#ZH-CN_MMLREF_0000001171436541)

| 输出项名称 | 输出项解释 |
| --- | --- |
| IP类型 | 该参数用于指定NF客户端地址的IP类型。 |
| IPv6地址 | 该参数用于表示NF的客户端IPv6地址。 |
| IPv4地址 | 该参数用于表示NF客户端的IPv4地址。 |
| NF归属区域 | 该参数用于表示NF归属区域。 |
