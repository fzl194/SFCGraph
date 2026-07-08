---
id: UDG@20.15.2@MMLCommand@ADD OSPFNETWORK
type: MMLCommand
name: ADD OSPFNETWORK（指定OSPF运行的接口及所属区域）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: OSPFNETWORK
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 8016
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 指定OSPF运行的接口及所属区域
status: active
---

# ADD OSPFNETWORK（指定OSPF运行的接口及所属区域）

## 功能

该命令用于在OSPF进程下的区域增加一个网段。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8016。
- 只有执行ADD OSPF配置了OSPF进程和ADD OSPFAREA配置了OSPF区域后才能使用此命令。
- 可以把多个接口配置到一个区域中。
- ADD OSPFINTERFACE命令接口使能的优先级大于ADD OSPFNETWORK。
- OSPF网段规格默认为单进程500，实际以服务规格文件为准。
- OSPF不允许以从地址建立OSPF邻居关系，而只能以接口的主地址建立邻接关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程号必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| AREAID | 区域号 | 可选必选说明：必选参数<br>参数含义：OSPF区域号。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：OSPF区域号必须已经存在。请使用LST OSPFAREA命令查看可用的OSPF区域。 |
| IPADDRESS | IP地址 | 可选必选说明：必选参数<br>参数含义：接口所在的网段地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：该参数与IP地址通配符一起指定需要启用OSPF协议的接口，接口IP地址落在该网段内，则接口运行OSPF协议。 |
| WILDCARDMASK | 反掩码 | 可选必选说明：必选参数<br>参数含义：IP地址的反掩码。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：相当于将IP地址的掩码反转（0变1，1变0）。其中，“1”表示忽略IP地址中对应的位，“0”表示必须保留此位。 |
| DESCRIPTION | 描述 | 可选必选说明：可选参数<br>参数含义：对网段进行描述信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～80。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFNETWORK]] · OSPF运行的接口及所属区域（OSPFNETWORK）

## 关联任务

- [[UDG@20.15.2@Task@0-00076]]

## 使用实例

在OSPF进程下1区域0.0.0.0下新增网段192.168.0.0/24：

```
ADD OSPFNETWORK: PROCID=1, AREAID="0.0.0.0", IPADDRESS="192.168.0.0", WILDCARDMASK="0.0.0.255";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-OSPFNETWORK.md`
