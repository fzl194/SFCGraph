---
id: UNC@20.15.2@MMLCommand@LST N26MMECHAR
type: MMLCommand
name: LST N26MMECHAR（查询N26接口MME属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N26MMECHAR
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- N26接口管理
- MME属性
status: active
---

# LST N26MMECHAR（查询N26接口MME属性）

## 功能

**适用NF：AMF**

该命令用于查询N26接口对端MME的属性信息。

## 注意事项

网段完全重叠的记录不能重复下发，网段有包含关系的记录可以同时下发。如果对端MME的IP与多个记录的网段都匹配，产品选择掩码最长的记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 对端设备范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指示对端MME设备范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_MME（所有MME）”：所有MME<br>- “SPECIAL_MME（指定MME）”：指定MME<br>默认值：无<br>配置原则：<br>系统开工时缺省增加了“所有MME”的记录，ADD命令中就不需要增加“所有MME”的记录。 |
| IPTYPE | IP地址类型 | 可选必选说明：该参数在"RANGE"配置为"SPECIAL_MME"时为条件可选参数。<br>参数含义：该参数用于指定对端MME的信令面IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPv4）”：IPv4<br>- “IPV6（IPv6）”：IPv6<br>默认值：无<br>配置原则：无 |
| IPV4 | MME IPv4信令面地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于指定对端MME的信令面IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>有效的IPv4地址必须是A、B或者C类地址，且不能为环回地址（127.x.y.z）。 |
| MASKV4 | IPv4掩码 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于指定对端MME的信令面IPv4地址的掩码。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |
| IPV6 | MME IPv6信令面地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于指定对端MME的信令面IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）和组播地址（FF00::/8）。 |
| MASKV6 | IPv6子网前缀长度 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于指定子网前缀的长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N26MMECHAR]] · N26接口MME属性（N26MMECHAR）

## 使用实例

- 查询IP地址为2001:db8:0:0:0:0:0:0的MME的属性信息，执行如下命令：
  ```
  %%LST N26MMECHAR: RANGE=SPECIAL_MME, IPTYPE=IPV6, IPV6="2001:db8:0:0:0:0:0:0", MASKV6=126;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
             对端设备范围  =  指定MME
               IP地址类型  =  IPv6
       MME IPv4信令面地址  =  255.255.255.255
                 IPv4掩码  =  0.0.0.0
       MME IPv6信令面地址  =  2001:db8::
         IPv6子网前缀长度  =  126
                  MME能力  =  NULL
   是否传递AM-PCF签约RFSP  =  否
     是否传递AM-PCF签约NI  =  否
                 接口类型  =  S10/N26 MME
  (结果个数 = 1)
  ```
- 查询全量MME的属性信息，执行如下命令：
  ```
  %%LST N26MMECHAR:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  对端设备范围  IP地址类型  MME IPv4信令面地址  IPv4掩码   MME IPv6信令面地址  IPv6子网前缀长度  MME能力               是否传递AM-PCF签约RFSP   是否传递AM-PCF签约NI      接口类型

  所有MME       INVALID     255.255.255.255     0.0.0.0    ::                  0                 支持non-IP类型的PDN   否                       否                        S10/N26 MME
  指定MME       IPv4        10.10.10.10         128.0.0.0  ::                  0                 NULL                  否                       否                        S10/N26 MME
  指定MME       IPv6        255.255.255.255     0.0.0.0    2001:db8::          126               NULL                  否                       否                        S10/N26 MME
  (结果个数 = 3)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-N26MMECHAR.md`
