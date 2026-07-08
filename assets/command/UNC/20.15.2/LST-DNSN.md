---
id: UNC@20.15.2@MMLCommand@LST DNSN
type: MMLCommand
name: LST DNSN（查询DNS NAPTR记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNSN
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
- DNS NAPTR管理
status: active
---

# LST DNSN（查询DNS NAPTR记录）

## 功能

**适用网元：SGSN、MME**

该命令用于查询 “FQDN” （全称标准规范域名）与网元接口的对应关系。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug；visit-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；G_4，来宾级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FQDN | FQDN | 可选必选说明：可选参数<br>参数含义：该参数用于标识由RAI、TAI、APN、MME等构建的域名，用来进行网元查询。详见命令<br>[**ADD DNSN**](增加DNS NAPTR记录(ADD DNSN)_72225569.md)<br>。<br>数据来源：整网规划<br>取值范围：0~255位字符串<br>默认值：无<br>说明：- FQDN不能以“.”开始，也不能以“.”结束。 |
| HSINDEX | 主机名索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定FQDN对应网元的索引。<br>数据来源：整网规划<br>取值范围：1~2048<br>默认值：无 |
| ENTITY | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口网元的类型。<br>数据来源：整网规划<br>取值范围：<br>- “Gn(Gn)”<br>- “SGSN(SGSN)”<br>- “GGSN(GGSN)”<br>- “MME(MME)”<br>- “SGW(SGW)”<br>- “PGW(PGW)”<br>- “MSC(MSC)”<br>- “IWS(IWS)”<br>- “AMF(AMF)”<br>默认值：无 |
| INTYPE | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用来指定接口对应的类型。<br>数据来源：整网规划<br>取值范围：<br>- “Gn(Gn)”<br>- “Gp(Gp)”<br>- “S3(S3)”<br>- “S4(S4)”<br>- “S5(S5)”<br>- “S8(S8)”<br>- “S10(S10)”<br>- “S11(S11)”<br>- “S16(S16)”<br>- “Sv(Sv)”<br>- “S102(S102)”<br>- “Sdup(Sdup)”<br>- “Sdup(Sdup)”<br>- “N26(N26)”<br>默认值：无<br>说明：- 当该配置数据用于链式备份网元寻址时，需要选Sdup枚举，Sdup接口华为私有接口，是MME和MME之间的接口，用于实现MME间的数据备份。 |
| UEUSGTYPEPLCY | UE USAGE TYPE策略 | 可选必选说明：可选参数<br>参数含义：该参数用来指定是否携带UE USAGE TYPE。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无 |
| DCNR | 支持DCNR | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否支持DCNR接入。<br>数据来源：全网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无 |
| SMF | 融合PGW-C/SMF | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否支持融合的PGW-C/SMF。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无 |

## 操作的配置对象

- [DNS NAPTR记录（DNSN）](configobject/UNC/20.15.2/DNSN.md)

## 使用实例

查询FQDN为“TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG”的记录结果：

LST DNSN: FQDN="TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG";

```
%%LST DNSN: FQDN="TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG";%%
RETCODE = 0  操作成功

操作结果如下
--------------
 FQDN                                                      主机名索引  网元类型  接口类型  S5接口协议类型  S8接口协议类型  UE USAGE TYPE策略  UE USAGE TYPE群组标识  支持DCNR  融合PGW-C/SMF  优先级  权重    描述  

 TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG   1           SGW       S11       GTP             GTP             是                 1                      否        否             0       100     To huawei SGW01  
 TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG   2           SGW       S11       GTP             GTP             是                 1                      否        否             0       100     To huawei SGW01  
 TAC-LB01.TAC-HB71.TAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG   3           SGW       S11       GTP             GTP             是                 1                      否        否             0       100     To huawei SGW01  
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNS-NAPTR记录(LST-DNSN)_26145892.md`
