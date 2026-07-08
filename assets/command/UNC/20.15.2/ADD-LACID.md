---
id: UNC@20.15.2@MMLCommand@ADD LACID
type: MMLCommand
name: ADD LACID（增加LAC组内绑定的LAC号段）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LACID
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 虚拟APN映射管理
- 基于LAC位置的虚拟APN映射管理
- LAC组的LAC段
status: active
---

# ADD LACID（增加LAC组内绑定的LAC号段）

## 功能

**适用NF：GGSN**

该命令用来在LAC组内绑定LAC号段。当需要在指定LAC组内绑定某个LAC号段时，使用该命令。SMF对来自某个LAC号段的用户进行虚拟APN的映射，将不同位置区域映射到不同的真实APN，真实APN下配置特定的IP地址池，以此建立用户IP地址与用户位置区域的对应关系，以便其它设备根据用户的IP地址做相应的策略控制。

## 注意事项

- 该命令执行后立即生效。

- 当一个LAC号段被绑定到某个LAC组内后，就不允许再绑定到其他的LAC组。LAC号段之间的LAC值不允许重叠。

- 最多可输入24000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LACSECNUM | LAC段编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~23999。<br>默认值：无<br>配置原则：无 |
| LACSTARTID | LAC起始ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC起始ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。字符串类型，长度为6位。 必须是0x/X开头的十六进制数，仅支持输入0x/X、0-9、a-f/A-F，字母不区分大小写，取值范围0x0001~0xFFFD，0xFFFF。<br>默认值：无<br>配置原则：<br>LACSTARTID的取值应小于或等于LACENDID。 |
| LACENDID | LAC截止ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC截止ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。字符串类型，长度为6位。 必须是0x/X开头的十六进制数，仅支持输入0x/X、0-9、a-f/A-F，字母不区分大小写，取值范围0x0001~0xFFFD，0xFFFF。<br>默认值：无<br>配置原则：<br>LACENDID的取值应大于或等于LACSTARTID。 |
| LACGROUPNAME | LAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该LACGROUPNAME必须已经由ADD LACGROUP配置过。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LACID]] · LAC组内绑定的LAC号段（LACID）

## 使用实例

假设运营商需要在一个本地已经配置的LAC组绑定一个LAC号段，“LAC组名”为“beijing”，“LAC段编号”为2，“LAC起始ID”为“0x000a”，“LAC截至ID”为“0x000b”：

```
ADD LACID:LACGROUPNAME="beijing",LACSECNUM=2,LACSTARTID="0x000a",LACENDID="0x000b";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加LAC组内绑定的LAC号段（ADD-LACID）_09651398.md`
