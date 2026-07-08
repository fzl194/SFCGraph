---
id: UDG@20.15.2@MMLCommand@LST RESREC
type: MMLCommand
name: LST RESREC（查询资源记录）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RESREC
command_category: 查询类
applicable_nf:
- CloudEPSN
effect_mode: ''
is_dangerous: false
category_path:
- SFIP管理
- 第三方应用管理
- 资源记录管理
status: active
---

# LST RESREC（查询资源记录）

## 功能

**适用NF：CloudEPSN**

本命令实现查询A、AAAA、NS、SRV、NAPTR记录的功能。

## 注意事项

- （CloudDNS无需执行此步骤）在依次执行SET DNSINFO、GEN DNSTASKID、EXC DNSCFGTASK初始化执行机后，可以开始使用增加LST RESREC命令。
- 完整域名，即参数“域名”以“.”结尾。添加资源记录的“域名”参数时，可以是完整域名，也可以是部分域名，会自动将部分域名和区域名一起拼接成完整域名。例如：当参数“域名”不是以“.”结尾，是部分域名时：“区域名”为“ln.mnc000.mcc460.gprs”，“域名”为“cmnet”，完整域名为“cmnet.ln.mnc000.mcc460.gprs.”。
- （CloudDNS不支持此功能）域名输入为“@”，设定为与当前区域名称同名的域名。
- 若没有输入“域名”参数，则输出当前“区域名称”下“记录类型”选中类型的从初始记录号开始的count个数的记录内容。
- 若输入“域名”参数，参数start、count不生效。
- 当增加记录时，“TTL”参数不填写时，显示为NULL，代表与当前“区域名称”有相同的TTL值。
- “START”和“COUNT”参数若没有填写，则默认返回“记录类型”的前100条记录，若记录数量少于100条，则返回“记录类型”已有的全部记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 记录类型 | 可选必选说明：必选参数<br>参数含义：增加的记录类型。<br>数据来源：本端规划<br>取值范围：NA。<br>- A：A记录。<br>- AAAA：AAAA记录。<br>- NAPTR：NAPTR记录。<br>- SRV：SRV记录。<br>- NS：NS记录。<br>默认值：无<br>配置原则：<br>- A记录：由域名解析出IPV4地址的记录。<br>- AAAA记录：由域名解析出IPV6地址的记录。<br>- NS记录：配置区域所属的授权域名服务器的记录。<br>- SRV记录：根据某项服务的域名解析出主机名的记录。<br>- NAPTR记录：根据域名解析出替换域名的记录。 |
| VIEWNAME | 视图名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“A”、“AAAA”、“NAPTR”、“SRV” 或 “NS”时为可选参数。<br>参数含义：资源所属的域名解析视图名称。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 输入资源所属的域名解析视图名称。<br>- CloudDNS中视图默认值为"default"。<br>- CloudDNS当前支持视图最大规格为32字符。<br>- 视图最后一位不支持特殊字符。<br>- 执行命令时需要保证视图存在。 |
| ZONE | 区域名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“A”、“AAAA”、“NAPTR”、“SRV” 或 “NS”时为必选参数。<br>参数含义：资源记录的区域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），分隔符（.）构成的以字母和数字开头的字符串。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS当前支持域名最大长度为254，结尾必须以分隔符（.）结尾，且不能以xn--开头。 |
| DOMAIN | 域名 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“A”、“AAAA”、“NAPTR”、“SRV” 或 “NS”时为可选参数。<br>参数含义：资源记录的域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），分隔符（.）构成的以字母和数字开头的字符串。<br>- 域名可以是完整域名，此时以（.）作为结束符；也可以是部分域名，此时不能以点（.）作为结束符，系统会自动将部分域名和区域名一起拼接成完整域名。<br>- 只输入“@”字符表示用同名与区域名称的域名。<br>- 为了兼容DNS9816，在记录类型选择SRV、NAPTR、NS时候，支持输入下划线“_”。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS当前支持域名最大长度为254，结尾必须以分隔符（.）结尾，且不能以xn—开头。 |
| START | 起始记录号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“A”、“AAAA”、“NAPTR”、“SRV” 或 “NS”时为可选参数。<br>参数含义：资源记录起始记录号。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：0<br>配置原则：<br>- 若没有没配置domain参数，则输出当前zone下type类型选中的从初始记录号开始的count个数的记录内容。<br>- 若设置了domain参数，参数start不生效。 |
| COUNT | 记录个数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“A”、“AAAA”、“NAPTR”、“SRV” 或 “NS”时为可选参数。<br>参数含义：记录个数。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：100<br>配置原则：<br>- 若没有没配置domain参数，则输出当前zone下type类型选中的从初始记录号开始的count个数的记录内容。<br>- 若设置了domain参数，参数count不生效。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RESREC]] · DNS资源记录（RESREC）

## 使用实例

- 显示多条A记录，参数“记录类型”选择为“A”记录，参数“视图名称”填写为“default”，参数“区域名称”填写为“apn.epc.mncxxx.mccyyy.3gppnetwork.org”，不填写查询范围：
  ```
  LST RESREC: TYPE=A, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org";
  ```
  ```

  %%LST RESREC: TYPE=A, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org";%%
  RETCODE = 0    操作执行成功

      绝对域名                                             IP地址                         TTL

      test.apn.epc.mncxxx.mccyyy.3gppnetwork.org        10.161.251.123                     800
      test1.apn.epc.mncxxx.mccyyy.3gppnetwork.org       10.161.251.124                     NULL
      test2.apn.epc.mncxxx.mccyyy.3gppnetwork.org       10.161.251.126，10.161.251.127     800
   (结果个数 = 3)
  共有1个报告
  ---    END
  ```
- 显示一条AAAA记录，参数“记录类型”选择为“AAAA”记录，参数“视图名称”填写为“default”，参数“区域名称”填写为“apn.epc.mncxxx.mccyyy.3gppnetwork.org”，参数“域名”填写为“test”，不填写查询范围：
  ```
  LST RESREC: TYPE=AAAA, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";
  ```
  ```

  %%LST RESREC: TYPE=AAAA, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test ";%%
  RETCODE = 0    操作执行成功

    绝对域名  =  test.apn.epc.mncxxx.mccyyy.3gppnetwork.org 
       IP地址 =  2001:db8:85a3:8da:131b:8b2e:2590:6354 
          TTL =  800
  (结果个数 = 1)
  共有1个报告
  ---    END
  ```
- 显示一条NAPTR记录，参数“记录类型”选择为“NAPTR”记录，参数“视图名称”填写为“default”，参数“区域名称”填写为“apn.epc.mncxxx.mccyyy.3gppnetwork.org”，参数“域名”填写为“test”，不填写查询范围：
  ```
  LST RESREC: TYPE=NAPTR, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";
  ```
  ```

  %%LST RESREC: TYPE=NAPTR, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";%%
  RETCODE = 0    操作执行成功

        绝对域名 = test.apn.epc.mncxxx.mccyyy.3gppnetwork.org
            顺序 = 10
            偏好 = 10
            标志 = S
            服务 = x-3gpp-sgw:x-s5-gtp:x-s8-gtp:x-gn
      正则表达式 = NULL
        替换域名 = test1.cmnet.mnc000.mcc460.gprs.
  TTL  = 1
   (结果个数 = 1)
  共有1个报告
  ---    END
  ```
- 显示一条SRV记录，参数“记录类型”选择为“SRV”记录，参数“视图名称”填写为“default”，参数“区域名称”填写为“apn.epc.mncxxx.mccyyy.3gppnetwork.org”，参数“域名”填写为“test”，不填写查询范围：
  ```
  LST RESREC: TYPE=SRV, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";
  ```
  ```

  %%LST RESREC: TYPE=SRV, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";%%
  RETCODE = 0    操作执行成功

   绝对域名 = test.apn.epc.mncxxx.mccyyy.3gppnetwork.org
     优先级 = 10
       权重 = 10
     端口号 = 8080
       目标 = test1.cmnet.mnc000.mcc460.gprs
       TTL  = 1
   (结果个数 = 1)
  共有1个报告
  ---    END
  ```
- 显示一条NS记录，参数“记录类型”选择为“NS”记录，参数“视图名称”填写为“default”，参数“区域名称”填写为“apn.epc.mncxxx.mccyyy.3gppnetwork.org”，参数“域名”填写为“test”，不填写查询范围：
  ```
  LST RESREC: TYPE=NS, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";
  ```
  ```

  %%LST RESREC: TYPE=NS, VIEWNAME="default", ZONE="apn.epc.mncxxx.mccyyy.3gppnetwork.org", DOMAIN="test";%%
  RETCODE = 0    操作执行成功

       区域名称 = test.apn.epc.mncxxx.mccyyy.3gppnetwork.org
     域名服务器 = test1.apn.epc.mncxxx.mccyyy.3gppnetwork.org.
           TTL  = 1
   (结果个数 = 1)
  共有1个报告
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RESREC.md`
