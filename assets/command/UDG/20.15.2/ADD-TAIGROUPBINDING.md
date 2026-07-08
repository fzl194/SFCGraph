---
id: UDG@20.15.2@MMLCommand@ADD TAIGROUPBINDING
type: MMLCommand
name: ADD TAIGROUPBINDING（绑定TAC号段到TAI组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: TAIGROUPBINDING
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 3000
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- TAI组与TAI号段绑定关系
status: active
---

# ADD TAIGROUPBINDING（绑定TAC号段到TAI组）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来在TAI组内增加一个TAC号段。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为3000。
- 同一个TAI组内，TAC号段不允许重叠。不同TAI组，如果MCC、MNC和TacType相同，则TAC号段也不允许重叠。
- 同一个TAI组下的TAC长度需要保持一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAIGROUPNAME | 指定TAI组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAI组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD TAIGROUP命令配置生成。 |
| TACSECNUM | TAC 段编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～2999。<br>默认值：无<br>配置原则：无 |
| TACSTARTID | TAC起始ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC起始ID。<br>数据来源：本端规划<br>取值范围：取值范围：字符串类型，仅支持输入0x/X、a-f/A-F 、0-9。字母不区分大小写。 S1TAC：长度为4位或者6位表示十六进制的字符串。如果输入6位字符串则取值范围0x0000~0xFFFF，允许不输入0x前缀，4位字符串取值范围0000~FFFF。 N2TAC：长度为6位或者8位表示十六进制的字符串。如果输入8位字符串则取值范围0x000000~0xFFFFFF，允许不输入0x前缀，6位字符串取值范围000000~FFFFFF。<br>默认值：无<br>配置原则：TACSTARTID的取值应小于或等于TACENDID。 |
| TACENDID | TAC截止ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC截止ID。<br>数据来源：本端规划<br>取值范围：取值范围：字符串类型，仅支持输入0x/X、a-f/A-F 、0-9。字母不区分大小写。 S1TAC：长度为4位或者6位表示十六进制的字符串。如果输入6位字符串则取值范围0x0000~0xFFFF，允许不输入0x前缀，4位字符串取值范围0000~FFFF。 N2TAC：长度为6位或者8位表示十六进制的字符串。如果输入8位字符串则取值范围0x000000~0xFFFFFF，允许不输入0x前缀，6位字符串取值范围000000~FFFFFF。<br>默认值：无<br>配置原则：TACENDID的取值应大于或等于TACSTARTID。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TAIGROUPBINDING]] · TAC号段与TAI组的绑定关系（TAIGROUPBINDING）

## 使用实例

假设运营商需要在一个本地已经配置的TAI组绑定一个TAC号段：

```
ADD TAIGROUPBINDING: TAIGROUPNAME="beijing", TACSECNUM=2, TACSTARTID="0x000001", TACENDID="0x000010";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-TAIGROUPBINDING.md`
