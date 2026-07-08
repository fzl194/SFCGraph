---
id: UNC@20.15.2@MMLCommand@ADD UPBINDS11
type: MMLCommand
name: ADD UPBINDS11（增加SGW-U与SGW-C侧S11接口的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UPBINDS11
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF绑定S11接口
status: active
---

# ADD UPBINDS11（增加SGW-U与SGW-C侧S11接口的绑定关系）

## 功能

**适用NF：SGW-C**

该命令用于增加SGW-U与SGW-C侧S11接口的绑定关系。

在切换场景下，如果SGW-C不能获取到用户的TAI信息，可以根据该绑定关系为用户选择满足条件的UPF。

该命令必须配置符合实际组网的UPF与S11的绑定关系，否则GW-U故障隔离功能不可用。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入2048条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | SGW-U实例名称 | 可选必选说明：必选参数<br>参数含义：该参数标识SGW-U实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要在ADD PNFPROFILE中事先配置，可执行LST PNFPROFILE进行查看。注意查询结果是NF类型为UPF的“NF实例标识”。 |
| S11IPTYPE | S11口地址类型 | 可选必选说明：必选参数<br>参数含义：该参数标识S11口IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPv4（IPv4类型地址）<br>- IPv6（IPv6类型地址）<br>- ALL（通配类型）<br>默认值：无<br>配置原则：<br>配置为ALL时，表示该NFINSTANCE支持所有的S11口IP地址。 |
| S11IPV4 | S11口IPv4地址 | 可选必选说明：该参数在"S11IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数标识S11口IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：<br>S11口IPv4地址不能为“0.0.0.0”、“255.255.255.255”和“0.x.y.z”；<br>S11口IPv4地址不能为组播地址(“224.x.y.z”)和环回地址(“127.x.y.z”)；S11口IPv4地址必须是A、B或者C类地址；<br>该参数需要在ADD GTPCLEGRPMEM中事先配置，可执行LST GTPCLEGRPMEM进行查看。注意查询结果是描述信息为S11接口的“IPv4地址”。 |
| S11IPV6 | S11口IPv6地址 | 可选必选说明：该参数在"S11IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数标识S11口IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：<br>必须是全球单播地址；<br>不能为“::”、“FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF”、环回地址(“::1”)、链路本地地址(“FE80::/10”)和组播地址(“FF00::/8”)；<br>该参数需要在ADD GTPCLEGRPMEM中事先配置，可执行LST GTPCLEGRPMEM进行查看。注意查询结果是描述信息为S11接口的“IPv6地址”。 |
| PRIORITY | S11口优先级 | 可选必选说明：可选参数<br>参数含义：该参数标识SGW-U的S11口优先级，该值越小，优先级越高。<br>在使用S11口选择SGW-U时，会优选S11口优先级高的UPF。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPBINDS11]] · SGW-U与SGW-C侧S11接口的绑定关系（UPBINDS11）

## 使用实例

使用前提：MME没有上报用户位置相关信息，需要使用该配置来查询SGW-U。 新增SGW-U与S11口的绑定关系，其中SGW-U唯一标识为"UPF1"，S11口地址类型为IPv4，IPv4地址为“192.168.1.2”，S11口优先级为3：

```
ADD UPBINDS11: NFINSTANCENAME="UPF1",S11IPTYPE=IPv4,S11IPV4="192.168.1.2",PRIORITY=3;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SGW-U与SGW-C侧S11接口的绑定关系（ADD-UPBINDS11）_09653045.md`
