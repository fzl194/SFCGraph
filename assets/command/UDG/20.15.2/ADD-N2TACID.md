---
id: UDG@20.15.2@MMLCommand@ADD N2TACID
type: MMLCommand
name: ADD N2TACID（在N2TAC组内添加一个N2TAC）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: N2TACID
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 16000
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- N2TAC段
status: active
---

# ADD N2TACID（在N2TAC组内添加一个N2TAC）

## 功能

**适用NF：UPF**

该命令用来在N2TAC组内绑定N2TAC号段。当需要在指定N2TAC组内绑定某个N2TAC号段时，使用该命令。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为16000。
- 当一个N2TAC号段被绑定到某个N2TAC组内后，就不允许再绑定到其他的N2TAC组。N2TAC号段之间的N2TAC值不允许重叠。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | 指定N2TAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定N2TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD TACGROUP命令配置生成。 |
| TACSECNUM | N2Tac 段编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～15999。<br>默认值：无<br>配置原则：无 |
| TACSTARTID | N2Tac 起始ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定N2TAC起始ID。<br>数据来源：本端规划<br>取值范围：字符串类型，长度为6位或者8位表示十六进制的字符串。仅支持输入0x/X、a-f/A-F 、0-9。字母不区分大小写，如果输入8位字符串则取值范围0x000000~0xFFFFFF，允许不输入0x前缀，6位字符串取值范围000000~FFFFFF。<br>默认值：无<br>配置原则：TACSTARTID的取值应小于或等于TACENDID。 |
| TACENDID | N2TAC截止ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定N2TAC截止ID。<br>数据来源：本端规划<br>取值范围：字符串类型，长度为6位或者8位表示十六进制的字符串。仅支持输入0x/X、a-f/A-F 、0-9。字母不区分大小写，如果输入8位字符串则取值范围0x000000~0xFFFFFF，允许不输入0x前缀，6位字符串取值范围000000~FFFFFF。<br>默认值：无<br>配置原则：TACENDID的取值应大于或等于TACSTARTID。 |

## 操作的配置对象

- [从N2TAC组内删除一个TAC（N2TACID）](configobject/UDG/20.15.2/N2TACID.md)

## 使用实例

假设运营商需要在一个本地已经配置的N2TAC组绑定一个N2TAC号段：

```
ADD N2TACID: TACGROUPNAME="beijing", TACSECNUM=2, TACSTARTID="0x000001", TACENDID="0x000010";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/在N2TAC组内添加一个N2TAC（ADD-N2TACID）_97358681.md`
