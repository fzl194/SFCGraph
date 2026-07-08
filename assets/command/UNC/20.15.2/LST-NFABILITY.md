---
id: UNC@20.15.2@MMLCommand@LST NFABILITY
type: MMLCommand
name: LST NFABILITY（查询配置NF的能力信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFABILITY
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF能力信息管理
status: active
---

# LST NFABILITY（查询配置NF的能力信息）

## 功能

**适用NF：NRF**

该命令用于查询配置NF的能力信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFIDTYPE | NF标识类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF标识类型。<br>数据来源：全网规划<br>取值范围：<br>- NF_ID（NF实例标识）<br>- NF_IP（NF IP地址）<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：该参数在"NFIDTYPE"配置为"NF_IP"时为条件可选参数。<br>参数含义：该参数用于指定NF的客户端地址的IP类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：该参数在"NFIDTYPE"配置为"NF_ID"时为条件可选参数。<br>参数含义：该参数用于表示NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于表示NF的客户端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于表示NF的客户端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFABILITY]] · 配置NF的能力信息（NFABILITY）

## 使用实例

- 查询全部配置NF的能力信息：
  ```
  LST NFABILITY:;
  %%LST NFABILITY:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  NF实例标识                       NF支持的能力                     IPV6地址  IPv4地址     IP类型       NF标识类型

  123e4567-e89b-12d3-a456-426655440000  无缓存                    ::    0.0.0.0  IPv4地址  NF实例标识
  223e4567-e89b-12d3-a456-426655440000  增量构建缓存&无缓存 ::    0.0.0.0  IPv4地址  NF实例标识
  (结果个数 = 2)
  ```
- 查询NF实例标识为123e4567-e89b-12d3-a456-426655440000的NF的能力信息：
  ```
  LST NFABILITY: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";
  %%LST NFABILITY: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
    NF实例标识  =  123e4567-e89b-12d3-a456-426655440000
  NF支持的能力  =  No Cache
      IPV6地址  =  ::
      IPv4地址  =  0.0.0.0
        IP类型  =  IPv4 address
    NF标识类型  =  NF ID
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询配置NF的能力信息（LST-NFABILITY）_44006965.md`
