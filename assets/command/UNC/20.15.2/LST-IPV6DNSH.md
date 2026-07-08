---
id: UNC@20.15.2@MMLCommand@LST IPV6DNSH
type: MMLCommand
name: LST IPV6DNSH（查询IPV6 DNS Hostfile记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPV6DNSH
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

# LST IPV6DNSH（查询IPV6 DNS Hostfile记录）

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
| HSINDEX | 主机名索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定FQDN对应网元的索引。<br>前提条件：该参数必须先由<br>[**ADD IPV6DNSH**](增加IPV6 DNS Hostfile记录(ADD IPV6DNSH)_26145886.md)<br>命令定义，才能在此处引用。<br>数据来源：整网规划<br>取值范围：1025～2048<br>默认值：无 |
| HOSTNAME | 主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询的主机名。<br>取值范围：1～255位字符串<br>默认值：无<br>配置原则：参见命令<br>[**ADD IPV6DNSH**](增加IPV6 DNS Hostfile记录(ADD IPV6DNSH)_26145886.md)<br>。 |

## 操作的配置对象

- [IPV6 DNS Hostfile记录（IPV6DNSH）](configobject/UNC/20.15.2/IPV6DNSH.md)

## 使用实例

查询 “主机名” 为 “TOPON.GW1.PGW.NODES.EPC.MNC01.MCC308.3GPPNETWORK.ORG” 所对应的配置记录：

LST IPV6DNSH: HOSTNAME="TOPON.GW1.PGW.NODES.EPC.MNC01.MCC308.3GPPNETWORK.ORG";

```
%%LST IPV6DNSH: HOSTNAME="TOPON.GW1.PGW.NODES.EPC.MNC01.MCC308.3GPPNETWORK.ORG";%%
RETCODE = 0  操作成功。

操作结果如下
--------------
主机名索引  =  1026
    主机名  =  TOPON.GW1.PGW.NODES.EPC.MNC01.MCC308.3GPPNETWORK.ORG
地址区间号  =  SECTION1
 IPv6地址1  =  2001:db8:10:19:44:55:10:12
   优先级1  =  127
     权重1  =  127
 IPv6地址2  =  2001:db8:10:19:44:55:10:13
   优先级2  =  127
     权重2  =  127
 IPv6地址3  =  2001:db8:10:19:44:55:10:14
   优先级3  =  127
     权重3  =  127
 IPv6地址4  =  2001:db8:10:19:44:55:10:15
   优先级4  =  127
     权重4  =  127
 IPv6地址5  =  2001:db8:10:19:44:55:10:16
   优先级5  =  127
     权重5  =  127
 IPv6地址6  =  2001:db8:10:19:44:55:10:17
   优先级6  =  127
     权重6  =  127
 IPv6地址7  =  2001:db8:10:19:44:55:10:18
   优先级7  =  127
     权重7  =  127
 IPv6地址8  =  2001:db8:10:19:44:55:10:19
   优先级8  =  127
     权重8  =  127
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IPV6-DNS-Hostfile记录(LST-IPV6DNSH)_72345487.md`
