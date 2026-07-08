---
id: UDG@20.15.2@MMLCommand@ADD LACID
type: MMLCommand
name: ADD LACID（在LAC组内添加一个LAC）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: LACID
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 24000
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- LAC段
status: active
---

# ADD LACID（在LAC组内添加一个LAC）

## 功能

**适用NF：PGW-U、UPF**

该命令用来在LAC组内绑定LAC号段。当需要在指定LAC组内绑定某个LAC号段时，使用该命令。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为24000。
- 当一个LAC号段被绑定到某个LAC组内后，就不允许再绑定到其他的LAC组。LAC号段之间的LAC值不允许重叠。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LACGROUPNAME | 指定LAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该LACGROUPNAME必须已经配置过。 |
| LACSECNUM | Lac 段编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～23999。<br>默认值：无<br>配置原则：无 |
| LACSTARTID | LAC起始ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC起始ID。<br>数据来源：本端规划<br>取值范围：字符串类型，长度为4位或者6位表示十六进制的字符串。仅支持输入0x/X、a-f/A-F 、0-9。字母不区分大小写，如果输入6位字符串则取值范围0x0001~0xFFFD，0xFFFF，允许不输入0x前缀，4位字符串取值范围0001~FFFD，FFFF。<br>默认值：无<br>配置原则：LACSTARTID的取值应小于或等于LACENDID。 |
| LACENDID | LAC截止ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC截止ID。<br>数据来源：本端规划<br>取值范围：字符串类型，长度为4位或者6位表示十六进制的字符串。仅支持输入0x/X、a-f/A-F 、0-9。字母不区分大小写，如果输入6位字符串则取值范围0x0001~0xFFFD，0xFFFF，允许不输入0x前缀，4位字符串取值范围0001~FFFD，FFFF。<br>默认值：无<br>配置原则：LACENDID的取值应大于或等于LACSTARTID。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LACID]] · 从LAC组内删除一个LAC（LACID）

## 使用实例

假设运营商需要在一个本地已经配置的LAC组绑定一个LAC号段：

```
ADD LACID:LACGROUPNAME="beijing",LACSECNUM=2,LACSTARTID="0x000a",LACENDID="0x000b";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/在LAC组内添加一个LAC（ADD-LACID）_82837197.md`
