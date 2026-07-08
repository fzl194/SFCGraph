---
id: UDG@20.15.2@MMLCommand@MOD ACLNODE
type: MMLCommand
name: MOD ACLNODE（修改ACL节点）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: ACLNODE
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
category_path:
- 用户面服务管理
- 业务安全防护
- 用户ACL管理
- ACL节点
status: active
---

# MOD ACLNODE（修改ACL节点）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](修改ACL节点（MOD ACLNODE）_86526702.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。

该命令用于修改ACL节点配置。当需要修改ACL节点下的filter过滤条件及对应的动作、或者filter过滤条件及对应的动作类型时，可以使用此命令。

## 注意事项

- ACL节点配置修改后，在执行SET REFRESHSRV命令30s后生效。建议该操作在对所有ACL节点的配置完成后执行。
- 不允许增加ACL节点名称不同、其他参数都相同的配置。
- 如果配置了redirect，则要求redirect和filter配置的IP版本一致。
- 操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。
- 执行该命令修改REDIRECTIPV4/REDIRECTIPV6参数时，需要确保对应路由存在，否则业务无法重定向到指定ip地址对应的设备，ACL重定向功能不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNODENAME | ACL节点名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置ACL节点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| FILTERNAME | 过滤器名字 | 可选必选说明：必选参数<br>参数含义：该参数用于配置filter名称，此filter必须预先配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD FILTER命令配置生成。<br>- 如果引用的filter下配置的server ip为host类型，则不允许配置与ACL节点绑定。 |
| ACTIONTYPE | 动作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置filter过滤条件对应的动作类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GATE：filter过滤条件对应的动作类型为门控。<br>- REDIRECT：filter过滤条件对应的动作类型为重定向。<br>默认值：无<br>配置原则：<br>- 该参数配置为GATE时，表示匹配到这个filter的报文做门控动作或者remark的业务。<br>- 该参数配置为REDIRECT时，表示匹配到这个filter的报文进行重定向的业务处理。 |
| GATEACTION | 门控动作 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ACTIONTYPE”配置为“GATE”时为可选参数。<br>参数含义：该参数用于设置门控制器动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISCARD：表示业务报文直接丢弃。<br>- PASS：表示业务报文直接通过。<br>默认值：无<br>配置原则：<br>- 当用户期望该filter下的报文允许被通过时则该参数配置为PASS。<br>- 当用户期望该filter下的报文拒绝被通过时则该参数配置为DISCARD。<br>- 如果配置门控动作为DISCARD，则remark动作不起作用，不可配置。 |
| REMARKT | 重标记类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“GATEACTION”配置为“PASS”时为可选参数。<br>参数含义：该参数用于设置重标记值的配置方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DSCPVALUE：表示使用数值型配置remark。<br>- DSCPCLASS：表示使用枚举型配置remark。<br>默认值：无<br>配置原则：无 |
| REMARKV | 重标记值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“REMARKT”配置为“DSCPVALUE”时为必选参数。<br>参数含义：该参数用于设置报文在转发过程中的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无<br>配置原则：无 |
| REMARKC | 重标记类 | 可选必选说明：条件必选参数<br>前提条件：该参数在“REMARKT”配置为“DSCPCLASS”时为必选参数。<br>参数含义：该参数用于设置重标记的类别名。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BE：表示remark值为0（0x00）。<br>- CS1：表示remark值为8（0x08）。<br>- AF11：表示remark值为10（0x0a）。<br>- AF12：表示remark值为12（0x0c）。<br>- AF13：表示remark值为14（0x0e）。<br>- CS2：表示remark值为16（0x10）。<br>- AF21：表示remark值为18（0x12）。<br>- AF22：表示remark值为20（0x14）。<br>- AF23：表示remark值为22（0x16）。<br>- CS3：表示remark值为24（0x18）。<br>- AF31：表示remark值为26（0x1a）。<br>- AF32：表示remark值为28（0x1c）。<br>- AF33：表示remark值为30（0x1e）。<br>- CS4：表示remark值为32（0x20）。<br>- AF41：表示remark值为34（0x22）。<br>- AF42：表示remark值为36（0x24）。<br>- AF43：表示remark值为38（0x26）。<br>- CS5：表示remark值为40（0x28）。<br>- EF：表示remark值为46（0x2e）。<br>- CS6：表示remark值为48（0x30）。<br>- CS7：表示remark值为56（0x38）。<br>默认值：无<br>配置原则：无 |
| REDIRECTIPVER | 重定向IP版本 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ACTIONTYPE”配置为“REDIRECT”时为必选参数。<br>参数含义：该参数用于设置重定向IP地址的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：表示地址类型为IPv4。<br>- IPv6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：<br>- 重定向IP地址的类型需与filter规则配置的IP版本一致。<br>- 当该参数配置为IPv4时，表示重定向的目的地址为IPv4的版本。<br>- 当该参数配置为IPv6时，表示重定向的目的地址为IPv6的版本。 |
| REDIRECTIPV4 | 重定向IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“REDIRECTIPVER”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于配置IPv4类型的重定向IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。有效的单播IPv4的地址。<br>默认值：无<br>配置原则：无 |
| REDIRECTIPV6 | 重定向IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“REDIRECTIPVER”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于配置IPv6类型的重定向IP地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。有效的单播IPv6的地址。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [ACL节点（ACLNODE）](configobject/UDG/20.15.2/ACLNODE.md)

## 使用实例

假如运营商需要修改ACL节点的配置，其门控动作为改为DISCARD：

```
MOD ACLNODE: ACLNODENAME="testaclnode1",FILTERNAME="testfilter1",ACTIONTYPE=GATE,GATEACTION=DISCARD;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改ACL节点（MOD-ACLNODE）_86526702.md`
