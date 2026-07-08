---
id: UNC@20.15.2@MMLCommand@CLR DNSC
type: MMLCommand
name: CLR DNSC（清除DNS缓存）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: DNSC
command_category: 动作类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- DNS维护管理
- 清除DNS Cache
status: active
---

# CLR DNSC（清除DNS缓存）

## 功能

![](清除DNS缓存(CLR DNSC)_72345945.assets/notice_3.0-zh-cn_2.png)

在话务高峰时执行此命令可能导致DNS查询记录不全、话务呼损等问题，建议在凌晨话务低谷时执行。

**适用网元：SGSN、MME、AMF**

该命令用于清除DNS Cache。

DNS Cache是使用DNS服务器解析时查找到的域名和IP地址信息在系统中的缓存，用于快速解析域名。

DNS Cache分为一级Cache和二级Cache。一级Cache保存在SPP进程上，保存了每个SPP进程各自常用的域名记录；二级Cache保存在1号SGP进程上，保存的域名记录为每个SPP进程中域名记录的集合。当SPP进程需要获取域名记录时，首先在HOSTFILE中查询。如果HOSTFILE中查询不到需要的域名记录，则在一级Cache中进行查询。如果一级Cache中查询不到需要的域名记录，则在二级Cache上查询。如果二级Cache仍查询不到需要的域名记录，则向DNS服务器进行查询。

每条Cache的记录具有一定的生命周期，生命周期结束后，该记录失效。

DNS服务器上的数据修改后，可以使用该命令清除 UNC 整系统DNS Cache，即使用该命令依次清除二级Cache和一级Cache。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后，一级Cache或二级Cache被清空，可能会导致在短时间内向DNS服务器查询次数有所上升。
- 仅清除一级Cache或二级Cache主要用于调测验证DNS Cache功能的场景。现网操作需要清除DNS Cache时，可以通过软参BYTE_EX_B25 BIT1控制采用同时清除全部缓存或者先清除二级Cache，再清除一级Cache的方式清除DNS Cache，建议通过先清除二级Cache再清除一级Cache的方式清除UNC整系统的DNS Cache，否则有可能导致Cache有残留数据。
- 如需清除AMF侧DNS客户端缓存，请同时使用CLR DNSC命令和CLR NGDNSCACHE命令。
- 当“DWORD_EX_B83”BIT9软参值为“0”时，执行该命令后，可能会上报“ALM-80630 系统业务资源过载”告警。
- 离散清缓存期间，打开或关闭软参BYTE_EX_B25 BIT1、BYTE_EX_B25 BIT3~BIT4、BYTE_EX_B322 BIT1~BIT2或BYTE_EX_B332 BIT6，其对应的功能（UNC执行CLR DNSC清除缓存时的清除策略、执行CLR DNSC清除L1缓存的时间间隔、控制DNS一级缓存离散清除速率、执行CLR DNSC清除DNS缓存时的策略）均会在下一次离散清缓存时生效。
- 离散清缓存期间，不建议修改软参BYTE_EX_B25 BIT1、BYTE_EX_B25 BIT3~BIT4、BYTE_EX_B322 BIT1~BIT2或BYTE_EX_B332 BIT6。
- 离散清缓存期间，每次执行该命令时，均会判断与上一次执行该命令的时间间隔是否大于等于一次离散清缓存需要的时间，如果符合条件则可以继续执行命令，否则会认为上一次执行命令没有结束，提示操作冲突，命令执行失败。一次离散清缓存需要的时间由BYTE_EX_B25 BIT1、BYTE_EX_B25 BIT3~BIT4、BYTE_EX_B322 BIT1~BIT2和BYTE_EX_B332 BIT6这些软参的功能决定。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>SPU<br>资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：整网规划<br>取值范围：1~63 位字符串<br>默认值：无 |
| PROCESSNO | 进程号 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定SPP或SGP进程号。通过<br>**[DSP PROCESSINFO](../../../../../../平台服务管理/单体服务公共功能管理/操作维护/系统调测/进程和组件信息/显示进程信息（DSP PROCESSINFO）_59103523.md)**<br>获取。SGP进程号请输入1。<br>前提条件：该参数在<br>“Cache类型”<br>配置为<br>“L1CACHE(一级Cache)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0~20<br>默认值：无 |
| CACHETYPE | Cache类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要清除的DNS Cache类型。数据来源：整网规划<br>取值范围：<br>- “L1CACHE(一级Cache)”<br>- “L2CACHE(二级Cache)”<br>- “ALL(所有Cache)”<br>默认值：<br>“ALL(所有Cache)” |
| DNSQUERYMODE | DNS查询方式 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定DNS查询的类型。<br>前提条件：该参数在<br>“Cache类型”<br>配置为<br>“L1CACHE(一级Cache)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “AAAA/A(AAAA/A)”<br>- “NAPTR(NAPTR)”<br>默认值：无 |
| DOMAINNAME | DOMAINNAME域名 | 可选必选说明：可选参数<br>参数含义：该参数用于标识要删除的Cache的域名。<br>数据来源：整网规划<br>取值范围：0~255个字符<br>默认值：无 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：此参数用于指定待查询的服务名称，可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>配置原则：<br>- 如果“Cache类型”参数配置为“L1CACHE(一级Cache)”，则SERVICETYPE需要填写USN的VNFC类型名称。<br>- 如果“Cache类型”参数配置为“L2CACHE(二级Cache)”，则SERVICETYPE需要填写LINK的VNFC类型名称。<br>- 如果“Cache类型”参数配置为“ALL(所有Cache)”，则SERVICETYPE需要填写LINK的VNFC类型名称。 |

## 操作的配置对象

- [DNS缓存（DNSC）](configobject/UNC/20.15.2/DNSC.md)

## 使用实例

DNS服务器上的数据修改，通过该命令清除SPU整系统DNS Cache。

CLR DNSC: CACHETYPE=L2CACHE, SERVICETYPE="LINK_VNFC";

CLR DNSC: CACHETYPE=L1CACHE, SERVICETYPE="USN_VNFC";

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除DNS缓存(CLR-DNSC)_72345945.md`
