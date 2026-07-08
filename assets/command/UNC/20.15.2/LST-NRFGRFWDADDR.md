---
id: UNC@20.15.2@MMLCommand@LST NRFGRFWDADDR
type: MMLCommand
name: LST NRFGRFWDADDR（查询备份NRF地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFGRFWDADDR
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF主备容灾参数
status: active
---

# LST NRFGRFWDADDR（查询备份NRF地址）

## 功能

**适用NF：NRF**

查询备份NRF地址。

## 注意事项

仅供调测使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERNRFNAME | 备份NRF名称 | 可选必选说明：可选参数<br>参数含义：该参数表示对端NRF名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数表示对端NRF地址的IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| IPV4 | IPV4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数表示对端NRF的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPV6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数表示对端NRF的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PORT | 端口 | 可选必选说明：可选参数<br>参数含义：该参数表示对端NRF地址所对应的端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| PEERNRFINSTID | 备份NRF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数表示备份NRF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~40。<br>默认值：无<br>配置原则：无 |
| TLS | 是否支持TLS | 可选必选说明：可选参数<br>参数含义：该参数用于指定NRF是否支持TLS。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFGRFWDADDR]] · 备份NRF地址（NRFGRFWDADDR）

## 使用实例

- 查询备份NRF名称peernrfname01，IPTYPE为IPV4的NRF备份地址信息。
  ```
  LST NRFGRFWDADDR:PEERNRFNAME="peernrfname01", IPTYPE=IPV4;
  %%LST NRFGRFWDADDR:PEERNRFNAME="peernrfname01", IPTYPE=IPV4;%%
  RETCODE = 0  执行成功

  结果如下
  ------------------------
      对端NRF名称  =  peernrfname01
           IP类型  =  IPv4地址
         IPV4地址  =  192.168.16.2
         IPV6地址  =  ::
  对端NRF实例标识  =  123e4567-e89b-12d3-a456-426655440000
             端口  =  12345
      是否支持TLS  =  TRUE
  (结果个数 = 1)
  ```
- 查询所有的NRF备份地址信息。
  ```
  LST NRFGRFWDADDR:;
  %%LST NRFGRFWDADDR:;%%
  RETCODE = 0  执行成功

  结果如下
  ------------------------ 
  对端NRF名称    IP类型        IPV4地址       IPV6地址      端口         对端NRF实例标识                       是否支持TLS
  peernrfname01  IPv4地址      192.168.16.2   ::            12345        123e4567-e89b-12d3-a456-426655440000  FALSE
  peernrfname02  IPv4地址      192.168.16.11  ::            23456        123e4567-e89b-12d3-a456-426655440011  TRUE
  peernrfname02  IPv6地址      0.0.0.0        fc00::0001    12345        123e4567-e89b-12d3-a456-426655660000  TRUE
  (结果个数 = 3)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询备份NRF地址（LST-NRFGRFWDADDR）_09653271.md`
