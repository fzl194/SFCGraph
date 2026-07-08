---
id: UDG@20.15.2@MMLCommand@RMV CPASSOCIATION
type: MMLCommand
name: RMV CPASSOCIATION（删除CP）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CPASSOCIATION
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- CP节点管理
- CP
status: active
---

# RMV CPASSOCIATION（删除CP）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](删除CP（RMV CPASSOCIATION）_19141524.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除CP配置会触发UP发起系统停工流程，与此CP和UP相关的上下文会被删除。

此命令用于删除指定的CP。

## 注意事项

- 该命令执行后立即生效。
- CP的配置参数一般不需要修改。如需修改，例如组网变化使UP对接的CP发生变化，可以执行本命令删除CP后再重新配置。
- 修改CP的N4逻辑接口前，需要先执行本命令，否则会造成CP和UP对接失败，导致新用户无法正常接入。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPTYPE | CP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于根据HostName或者IP地址进行删除或查询SMF操作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- HOSTNAME：表示类型是SMF主机名。<br>- IPVERSION：表示为N4 IP地址版本。<br>默认值：无<br>配置原则：无 |
| CPDESCRIPTION | CP标识信息 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPTYPE”配置为“HOSTNAME”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“CPTYPE”配置为“IPVERSION”时为可选参数。<br>参数含义：该参数用于指定CP的标识信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址版本类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPTYPE”配置为“IPVERSION”时为必选参数。<br>参数含义：该参数用于设置CP N4 接口的IP地址版本类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| N4IPADDRESS | CP N4 接口IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于设定CP的N4接口的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：无 |
| N4IPV6ADDRESS | CP N4 接口IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于设定CP的N4接口的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CPASSOCIATION]] · CP（CPASSOCIATION）

## 使用实例

删除CP标识为cp1的CP：

```
RMV CPASSOCIATION: CPTYPE=HOSTNAME, CPDESCRIPTION="cp1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除CP（RMV-CPASSOCIATION）_19141524.md`
