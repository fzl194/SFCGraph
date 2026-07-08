---
id: UDG@20.15.2@MMLCommand@ADD S1TACID
type: MMLCommand
name: ADD S1TACID（在S1TAC组内添加一个S1TAC）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: S1TACID
command_category: 配置类
applicable_nf:
- PGW-U
effect_mode: 对新用户生效
is_dangerous: false
max_records: 16000
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- S1TAC段
status: active
---

# ADD S1TACID（在S1TAC组内添加一个S1TAC）

## 功能

**适用NF：PGW-U**

该命令用来在S1TAC组内绑定S1TAC号段。当需要在指定S1TAC组内绑定某个S1TAC号段时，使用该命令。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为16000。
- 当一个S1TAC号段被绑定到某个S1TAC组内后，就不允许再绑定到其他的S1TAC组。S1TAC号段之间的S1TAC值不允许重叠。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | 指定S1TAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定S1TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该TACGROUPNAME必须已经配置过。 |
| TACSECNUM | S1Tac 段编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定S1TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～15999。<br>默认值：无<br>配置原则：无 |
| TACSTARTID | S1Tac 起始ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定S1TAC起始ID。<br>数据来源：本端规划<br>取值范围：字符串类型，长度为4位或者6位表示十六进制的字符串。仅支持输入0x/X、a-f/A-F 、0-9。字母不区分大小写，如果输入6位字符串则取值范围0x0000~0xFFFF，允许不输入0x前缀，4位字符串取值范围0000~FFFF。<br>默认值：无<br>配置原则：TACSTARTID的取值应小于或等于TACENDID。 |
| TACENDID | S1TAC截止ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定S1TAC截止ID。<br>数据来源：本端规划<br>取值范围：字符串类型，长度为4位或者6位表示十六进制的字符串。仅支持输入0x/X、a-f/A-F 、0-9。字母不区分大小写，如果输入6位字符串则取值范围0x0000~0xFFFF，允许不输入0x前缀，4位字符串取值范围0000~FFFF。<br>默认值：无<br>配置原则：TACENDID的取值应大于或等于TACSTARTID。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@S1TACID]] · 从S1TAC组内删除一个S1TAC（S1TACID）

## 使用实例

假设运营商需要在一个本地已经配置的S1TAC组绑定一个S1TAC号段：

```
ADD S1TACID:TACGROUPNAME="beijing",TACSECNUM=2,TACSTARTID="0x0001",TACENDID="0x0010";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-S1TACID.md`
