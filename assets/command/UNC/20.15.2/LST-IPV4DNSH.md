---
id: UNC@20.15.2@MMLCommand@LST IPV4DNSH
type: MMLCommand
name: LST IPV4DNSH（查询IPV4 DNS Hostfile记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPV4DNSH
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- DNS
- DNS Hostfile管理
status: active
---

# LST IPV4DNSH（查询IPV4 DNS Hostfile记录）

## 功能

**适用网元：SGSN、MME**

该命令用于显示网元接口所对应的IP地址信息。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入参数，则查询所有记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HSINDEX | 主机名索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定FQDN对应网元的索引。<br>前提条件：该参数必须先由<br>[**ADD IPV4DNSH**](增加IPV4 DNS Hostfile记录(ADD IPV4DNSH)_26145884.md)<br>命令定义，才能在此处引用。<br>数据来源：整网规划<br>取值范围：1~1024<br>默认值：无 |
| HOSTNAME | 主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询的主机名。<br>数据来源：整网规划<br>取值范围：0~255位字符串<br>默认值：无<br>说明：- 主机名不能以“.”开始，也不能以“.”结束。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPV4DNSH]] · IPV4 DNS Hostfile记录（IPV4DNSH）

## 使用实例

1. 查询主机名为 “RAC0002.LAC2301.MNC013.MCC308.3GPPNETWORK.ORG” 所对应的配置记录：
  LST IPV4DNSH: HOSTNAME="RAC0002.LAC2301.MNC013.MCC308.3GPPNETWORK.ORG";
  ```
  %%LST IPV4DNSH: HOSTNAME="RAC0002.LAC2301.MNC013.MCC308.3GPPNETWORK.ORG";%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------------------
    主机名索引  =  511
        主机名  =  RAC0002.LAC2301.MNC013.MCC308.3GPPNETWORK.ORG
    地址区间号  =  SECTION1
    IP地址类型  =  IPV4
       IP地址1  =  192.168.74.97
       优先级1  =  127
         权重1  =  127
       IP地址2  =  0.0.0.0
       优先级2  =  127
         权重2  =  127
       IP地址3  =  0.0.0.0
       优先级3  =  127
         权重3  =  127
       IP地址4  =  0.0.0.0
       优先级4  =  127
         权重4  =  127
       IP地址5  =  0.0.0.0
       优先级5  =  127
         权重5  =  127
       IP地址6  =  0.0.0.0
       优先级6  =  127
         权重6  =  127
       IP地址7  =  0.0.0.0
       优先级7  =  127
         权重7  =  127
       IP地址8  =  0.0.0.0
       优先级8  =  127
         权重8  =  127
  (结果个数 = 1)

  ---    END
  ```
2. 查询所有的HOSTFILE配置记录：
  LST IPV4DNSH:;
  ```
  %%LST IPV4DNSH:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
   主机名索引 主机名                                                  地址区间号  IP地址类型  IP地址1    优先级1  权重1   IP地址2    优先级2  权重2  IP地址3   优先级3  权重3  IP地址4   优先级4  权重4  IP地址5    优先级5  权重5 IP地址6   优先级6 权重6  IP地址7   优先级7  权重7  IP地址8    优先级8  权重8 

   900        HUAWEI1.COM.GTP.APN.EPC.MNC013.MCC308.3GPPNETWORK.ORG   SECTION1    IPV4        192.168.74.48  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127   
   901        HUAWEI2.COM.GTP.APN.EPC.MNC013.MCC308.3GPPNETWORK.ORG   SECTION1    IPV4        192.168.74.48  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127   
   902        HUAWEI3.COM.GTP.APN.EPC.MNC013.MCC308.3GPPNETWORK.ORG   SECTION1    IPV4        192.168.74.48  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127   
   903        HUAWEI1.COM.PMIP.APN.EPC.MNC013.MCC308.3GPPNETWORK.ORG  SECTION1    IPV4        192.168.74.48  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127   
   904        HUAWEI2.COM.PMIP.APN.EPC.MNC013.MCC308.3GPPNETWORK.ORG  SECTION1    IPV4        192.168.74.48  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127   
   905        HUAWEI3.COM.PMIP.APN.EPC.MNC013.MCC308.3GPPNETWORK.ORG  SECTION1    IPV4        192.168.74.48  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127   
   906        HUAWEI1.COM.GTP.APN.EPC.MNC033.MCC308.3GPPNETWORK.ORG   SECTION1    IPV4        192.168.74.48  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127   
   907        HUAWEI2.COM.GTP.APN.EPC.MNC033.MCC308.3GPPNETWORK.ORG   SECTION1    IPV4        192.168.74.48  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127   
   908        HUAWEI3.COM.GTP.APN.EPC.MNC033.MCC308.3GPPNETWORK.ORG   SECTION1    IPV4        192.168.74.48  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127   
   999        RAC0001.LAC2301.MNC013.MCC308.GPRS                      SECTION1    IPV4        192.168.74.80  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127     0.0.0.0  127      127   
  (结果个数 = 10)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IPV4DNSH.md`
