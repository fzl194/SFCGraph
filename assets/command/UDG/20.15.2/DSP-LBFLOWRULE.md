---
id: UDG@20.15.2@MMLCommand@DSP LBFLOWRULE
type: MMLCommand
name: DSP LBFLOWRULE（查询业务引流规则）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LBFLOWRULE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 引流规则
status: active
---

# DSP LBFLOWRULE（查询业务引流规则）

## 功能

该命令用于查询业务引流规则。引流规则由业务VNFC下发，用来指示业务流和业务VNFC服务实例的关联关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULETYPE | 引流规则类型 | 可选必选说明：必选参数<br>参数含义：该参数表示引流规则类型。<br>数据来源：本端规划<br>默认值：无<br>取值范围：<br>- “TRIPLE(三元组引流规则)”：即使用目的IP，目的端口号和协议类型来确定一个服务VNFC实例。<br>- “QUINT(五元组引流规则)”：即使用目的IP，目的端口号，源IP，源端口号和协议类型来确定一个服务VNFC实例。 |
| DSTIPV4 | 目的IPv4 | 可选必选说明：条件必选参数<br>参数含义：本参数表示目的IPv4地址。<br>前提条件：该参数在"引流规则类型"参数配置为"三元组引流规则"或"五元组引流规则"后生效。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0.0.0.0~255.255.255.255 |
| SRCIPV4 | 源IPv4 | 可选必选说明：条件必选参数<br>参数含义：本参数表示源IPv4地址。<br>前提条件：该参数在"引流规则类型"参数配置为"五元组引流规则"后生效。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0.0.0.0~255.255.255.255 |
| VPNNAME | VPN名称 | 可选必选说明：必选参数<br>参数含义：本参数表示引流规则中的VPN名称。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0 ~ 31位字符串<br>说明：公网填“_public_”。 |
| DSTPORT | 目的端口号 | 可选必选说明：条件必选参数<br>参数含义：本参数表示引流规则中的目的端口。<br>前提条件：该参数在"引流规则类型"参数配置为"三元组引流规则"或"五元组引流规则"后生效。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~65535。 |
| SRCPORT | 源端口号 | 可选必选说明：条件必选参数<br>参数含义：本参数表示引流规则中的源端口。<br>前提条件：该参数在"引流规则类型"参数配置为"五元组引流规则"后生效。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~65535。 |
| PROTO | 协议类型 | 可选必选说明：条件必选参数<br>参数含义：本参数表示引流规则中的协议类型。<br>前提条件：该参数在"引流规则类型"参数配置为"三元组引流规则"或"五元组引流规则"后生效。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~255。常用的协议类型有6（TCP）和17（UDP）。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LBFLOWRULE]] · 业务引流规则（LBFLOWRULE）

## 使用实例

查询所有引流规则类型为三元组引流规则，目的IPv4为10.1.1.1，VPN名称为VPN1，目的端口为1，协议为17的业务VNFCID与业务VNFC服务实例ID的详细信息：

DSP LBFLOWRULE: RULETYPE=TRIPLE, DSTIPV4="10.1.1.1", VPNNAME="VPN1", DSTPORT=1, PROTO=17;

```
%%DSP LBFLOWRULE: RULETYPE=TRIPLE, DSTIPV4="10.1.1.1", VPNNAME="VPN1", DSTPORT=1, PROTO=17;%%
RETCODE = 0  操作成功。

操作结果如下：
--------------
业务VNFCID    业务VNFC服务实例ID

4             0                 
4             1                 
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-LBFLOWRULE.md`
