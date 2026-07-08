---
id: UNC@20.15.2@MMLCommand@LST SGWSELPLCY
type: MMLCommand
name: LST SGWSELPLCY（查询S-GW选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGWSELPLCY
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- S11接口管理
- S-GW选择策略
status: active
---

# LST SGWSELPLCY（查询S-GW选择策略）

## 功能

**适用网元：SGSN、MME**

该命令用于查询S-GW选择策略。

## 注意事项

- 无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “MSISDN_PREFIX(指定MSISDN前缀)”<br>- “SPECIFIC_IMSI(特定IMSI)”<br>- “SPECIFIC_MSISDN(特定MSISDN)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：只有<br>“SUBRANGE（用户范围）”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定MSISDN前缀。<br>前提条件：只有<br>“SUBRANGE（用户范围）”<br>为<br>“MSISDN_PREFIX(指定MSISDN前缀)”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件可选参数<br>参数说明：该参数用于指定国际移动用户标识。<br>前提条件：此参数在“用户范围”设置为“SPECIFIC_IMSI(特定IMSI)”后生效。<br>取值范围：15位十进制数字字符串<br>默认值：无 |
| MSISDN | MSISDN | 可选必选说明：条件可选参数<br>参数说明：该参数用于指定移动台国际ISDN号码。<br>前提条件：此参数在“用户范围”设置为“SPECIFIC_MSISDN (特定MSISDN)”后生效。<br>取值范围：13位十进制数字字符串<br>默认值：无 |
| SLCTM | 选择方法 | 可选必选说明：可选参数<br>参数含义：该参数用于指定选择方法。<br>数据来源：整网规划<br>取值范围：<br>- “S-GW_QNAME(指定S-GW的查询域名)”<br>- “S-GW_IP (指定S-GW的IP地址)”<br>默认值：无 |
| QNAME | 查询域名 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定查询域名。<br>前提条件：只有<br>“SLCTM（选择方法）”<br>为<br>“S-GW_QNAME(指定S-GW的查询域名)”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1~255位字符串<br>默认值：无<br>配置原则：<br>- 该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，字母不区分大小写。<br>- 按照协议RFC1035规定，Hostname最大有效字符数为253，并且每个Label最大长度为63个字节。 |
| IPV4 | S-GW的信令面IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定S-GW的信令面IPv4地址。<br>前提条件：该参数在“SLCTM（选择方法）”参数设置为“S-GW_IP（指定S-GW IP的地址）”值后生效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- IPV4地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- IPV4地址必须是A、B或者C类地址。 |
| IPV6 | S-GW的信令面IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定S-GW的信令面IPv6地址。<br>前提条件：该参数在“SLCTM（选择方法）”参数设置为“S-GW_IP（指定S-GW IP地址）”值后生效。<br>数据来源：整网规划<br>取值范围：::～FFFF：FFFF：FFFF：FFFF：FFFF：FFFF：FFFF：FFFF<br>默认值：无<br>配置原则：IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [S-GW选择策略（SGWSELPLCY）](configobject/UNC/20.15.2/SGWSELPLCY.md)

## 使用实例

1. 查询所有记录
  LST SGWSELPLCY:;
  ```
  %%LST SGWSELPLCY:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   用户范围        IMSI前缀  MSISDN前缀  IMSI  MSISDN  选择方法            查询域名                                                      S-GW的信令面IPv4地址  S-GW的信令面IPv6地址
   指定IMSI前缀    134       NULL        NULL  NULL    指定S-GW的查询域名                       TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG  NULL                  NULL
   指定MSISDN前缀  NULL      134         NULL  NULL    指定S-GW的查询域名  TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG  NULL                  NULL
  (结果个数 = 2)

  ---    END
  ```
2. 通过 “用户范围” 为 “MSISDN_PREFIX(指定MSISDN前缀)” 查询记录
  LST SGWSELPLCY: SUBRANGE=MSISDN_PREFIX, MSISDNPRE="134";
  ```
  %%LST SGWSELPLCY: SUBRANGE=MSISDN_PREFIX, MSISDNPRE="134";%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
              用户范围  =  指定MSISDN前缀
              IMSI前缀  =  NULL
            MSISDN前缀  =  134
                  IMSI  =  NULL
                MSISDN  =  NULL 
              选择方法  =  指定S-GW的查询域名
              查询域名  =  TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG
  S-GW的信令面IPv4地址  =  NULL
  S-GW的信令面IPv6地址  =  NULL
  (结果个数 = 1)

  ---    END
  ```
3. 通过 “用户范围” 为 “IMSI_PREFIX(指定IMSI前缀)” 查询记录
  LST SGWSELPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="134";
  ```
  %%LST SGWSELPLCY: SUBRANGE=
  IMSI
  _PREFIX, 
  IMSIPRE
  ="134";%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
  用户范围  =  指定MSISDN前缀
              IMSI前缀  =  134
            MSISDN前缀  =  NULL
                  IMSI  =  NULL
                MSISDN  =  NULL 
              选择方法  =  指定S-GW的查询域名
              查询域名  =  TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG
  S-GW的信令面IPv4地址  =  NULL
  S-GW的信令面IPv6地址  =  NULL
  (结果个数 = 1)

  ---    END
  ```
4. 通过 “选择方法” 为 “S-GW_QNAME(指定S-GW的查询域名)” 查询记录
  LST SGWSELPLCY: SLCTM=S-GW_QNAME;
  ```
  %%LST SGWSELPLCY: SLCTM=S-GW_QNAME;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   用户范围        IMSI前缀  MSISDN前缀  IMSI  MSISDN  选择方法            查询域名                                                      S-GW的信令面IPv4地址  S-GW的信令面IPv6地址
   指定IMSI前缀    134       NULL        NULL  NULL    指定S-GW的查询域名                       TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG  NULL                  NULL
   指定MSISDN前缀  NULL      134         NULL  NULL    指定S-GW的查询域名  TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG  NULL                  NULL
  (结果个数 = 2)

  ---    END
  ```
5. 通过 “选择方法” 为 “S-GW_QNAME(指定S-GW的查询域名)” ， “查询域名” 为指定域名方式查询记录
  LST SGWSELPLCY: SLCTM=S-GW_QNAME, QNAME="TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG";
  ```
  %%LST SGWSELPLCY: SLCTM=S-GW_QNAME, QNAME="TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG";%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   用户范围        IMSI前缀  MSISDN前缀  IMSI  MSISDN  选择方法            查询域名                                                      S-GW的信令面IPv4地址  S-GW的信令面IPv6地址
   指定IMSI前缀    134       NULL        NULL  NULL    指定S-GW的查询域名                       TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG  NULL                  NULL
   指定MSISDN前缀  NULL      134         NULL  NULL    指定S-GW的查询域名  TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG  NULL                  NULL
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S-GW选择策略(LST-SGWSELPLCY)_72345575.md`
