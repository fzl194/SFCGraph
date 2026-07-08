---
id: UNC@20.15.2@MMLCommand@LST PGWESTNSR
type: MMLCommand
name: LST PGWESTNSR（查询E-STN-SR和PGW关系配置表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PGWESTNSR
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 紧急呼叫配置
- E-STN-SR和PGW关系配置表
status: active
---

# LST PGWESTNSR（查询E-STN-SR和PGW关系配置表）

## 功能

**适用网元：MME**

该命令用于查询SRVCC的紧急会话转移号码和P-GW关系配置表。 UNC 通过本命令查询出来的PGW IP来找到P-GW对应的“SRVCC的紧急会话转移号码”。与华为MSC设备对接需要配置本命令。

## 注意事项

1. 如果不输入任何参数，输出所有的记录。
2. 如果输入IPT参数，则输出指定IP地址类型的记录。
3. 如果输入了指定的IP地址和IP地址掩码，输出指定的记录。
4. IP地址和IP地址掩码必须成对输入，不允许只输入IP地址而不输入掩码。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | PGW的IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定P-GW的IP地址类型。<br>数据来源：运营商规划<br>取值范围：<br>- IPV4(IPV4)<br>- IPV6(IPV6)<br>默认值：无 |
| PGWIPV4 | PGW的IPV4地址 | 可选必选说明：可选参数<br>参数含义：该参数用于设置P-GW的IPv4地址。<br>前提条件：该参数在<br>“PGW的IP地址类型”<br>配置为<br>“IPV4(IPV4)”<br>后生效。<br>数据来源：运营商规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| IPV4MSK | PGW的IPV4地址掩码 | 可选必选说明：可选参数<br>参数含义：该参数用于设置P-GW的IPv4类型的GTPC地址掩码。<br>前提条件：该参数在<br>“PGW的IP地址类型”<br>配置为<br>“IPV4(IPV4)”<br>后生效。<br>数据来源：运营商规划<br>取值范围： 0.0.0.0～255.255.255.255<br>默认值：无 |
| PGWIPV6 | PGW的IPV6地址 | 可选必选说明：可选参数<br>参数含义：该参数用于设置P-GW的IPv6地址。<br>前提条件：该参数在<br>“PGW的IP地址类型”<br>配置为<br>“IPV6(IPV6)”<br>后生效。<br>数据来源：运营商规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| IPV6MSK | IPV6地址前缀长度 | 可选必选说明：可选参数<br>参数含义：该参数用于设置P-GW的IPv6地址的前缀的长度。<br>前提条件：该参数在<br>“PGW的IP地址类型”<br>配置为<br>“IPV6(IPV6)”<br>后生效。<br>数据来源：运营商规划<br>取值范围：1～128<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PGWESTNSR]] · E-STN-SR和PGW关系配置表（PGWESTNSR）

## 使用实例

1. 不输入查询条件，查询全部SRVCC的紧急会话转移号码和P-GW关系配置表：
  LST PGWESTNSR:;
  ```
  %%LST PGWESTNSR:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  ------------
  PGW的IP地址类型    PGW的IPV4地址    PGW的IPV4地址掩码    PGW的IPV6地址                  IPV6地址前缀长度    SRVCC的紧急会话转移号码

  IPV4               192.168.111.0    255.255.255.255      2001:db8:10:19:44:55:10:12     0                   12345678               
  IPV4               192.168.111.1    255.255.255.255      2001:db8:10:19:44:55:10:13     0                   12345678               
  (结果个数 = 2)
  ---    END
  ```
2. 查询 “PGW的IP地址类型” 为 “IPV4” ， “PGWIPV4” 为 “192.168.111.111” ， “IPV4MSK” 为 “255.255.0.0” 的E-STN-SR和P-GW关系配置表。
  LST PGWESTNSR: IPT=IPV4, PGWIPV4="192.168.111.0", IPV4MSK="255.255.255.255";
  ```
  %%LST PGWESTNSR: IPT=IPV4, PGWIPV4="192.168.111.0", IPV4MSK="255.255.255.255";%%
  RETCODE = 0  操作成功。

  输出结果如下
  ------------
          PGW的IP地址类型  =  IPV4
            PGW的IPV4地址  =  192.168.111.0
        PGW的IPV4地址掩码  =  255.255.255.255
            PGW的IPV6地址  =  2001:db8:10:19:44:55:10:12
         IPV6地址前缀长度  =  0
  SRVCC的紧急会话转移号码  =  12345678
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PGWESTNSR.md`
