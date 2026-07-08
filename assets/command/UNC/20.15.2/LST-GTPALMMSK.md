---
id: UNC@20.15.2@MMLCommand@LST GTPALMMSK
type: MMLCommand
name: LST GTPALMMSK（查询GTP路径断告警屏蔽记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPALMMSK
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
- GTP-C协议管理
- 路径告警屏蔽
status: active
---

# LST GTPALMMSK（查询GTP路径断告警屏蔽记录）

## 功能

**适用网元：SGSN、MME**

该命令用于查看需要屏蔽的GTP路径断告警配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFGTP | 配置类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指示配置屏蔽GTP路径告警的类型。<br>取值范围：<br>- “IPMASK(IP+掩码)”<br>- “SENDIP(起始IP+终止IP)”<br>- “IPV6MASK(IPv6+前缀)”<br>- “SENDIPV6(起始IPv6+终止IPv6)”<br>默认值：无 |
| IPV4ADDR | 起始对端设备IP地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指示对端设备起始IPv4地址。<br>前提条件：在<br>“CFGTP”<br>配置为<br>“IPMASK(IP+掩码)”<br>和<br>“SENDIP(起始IP+终止IP)”<br>时，才需要配置本参数<br>数据来源：整网规划<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| EIPV4ADDR | 终止对端设备IP地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指示对端设备终止IPv4地址。<br>前提条件：只有在<br>“CFGTP”<br>配置为<br>“SENDIP(起始IP+终止IP)”<br>时，才需要配置该类型的IP地址。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>说明：- 本参数的取值应该大于等于“起始对端设备IP地址”的取值。 |
| MASKV4 | 掩码 | 可选必选说明：可选参数<br>参数含义：该参数用于指示对端设备的IPv4地址的掩码。<br>前提条件：只有在<br>“CFGTP”<br>配置为<br>“IPMASK(IP+掩码)”<br>时，才需要配置本参数。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| IPV6ADDR | 起始对端设备IPv6地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指示对端设备起始IPv6地址。<br>前提条件：在<br>“CFGTP”<br>配置为<br>“IPV6MASK(IPv6+前缀)”<br>和<br>“SENDIPV6(起始IPv6+终止IPv6)”<br>时，才需要配置本参数。<br>数据来源：整网规划<br>取值范围：::-FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| EIPV6ADDR | 终止对端设备IPv6地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指示对端设备终止IPv6地址。<br>前提条件：只有在<br>“CFGTP”<br>配置为<br>“SENDIPV6(起始IPv6+终止IPv6)”<br>时，才需要配置本参数。<br>数据来源：整网规划<br>取值范围：0:0:0:0:0:0:0:0 ~ FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>说明：- 本参数的取值应该大于等于“起始对端设备IPv6地址”的取值。 |
| PRELEN | 前缀长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指示对端设备的IPv6地址的前缀长度。<br>前提条件：只有在<br>“CFGTP”<br>配置为<br>“IPV6MASK(IPv6+前缀)”<br>时，才需要配置本参数。<br>数据来源：整网规划<br>取值范围：0~128<br>默认值：无 |
| SCRALM | 屏蔽GTP路径告警控制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定屏蔽GTP路径告警开关。<br>取值范围：<br>- “ON(启用)”：启用屏蔽GTP路径告警。<br>- “OFF(关闭)”：关闭屏蔽GTP路径告警。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTPALMMSK]] · GTP路径断告警屏蔽记录（GTPALMMSK）

## 使用实例

查询表项记录：

LST GTPALMMSK:;

```
%%LST GTPALMMSK:;%%
RETCODE = 0  执行成功。

输出结果如下
-------------------------
配置类型            起始对端设备IP地址    终止对端设备IP地址   掩码            屏蔽GTP路径告警控制开关

IP+掩码             192.168.5.5           192.168.5.255        255.255.255.0   启用          
起始IP+终止IP       192.168.5.5           192.168.0.0          0.0.0.0         关闭         
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GTPALMMSK.md`
