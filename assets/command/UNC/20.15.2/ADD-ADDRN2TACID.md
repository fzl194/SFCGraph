---
id: UNC@20.15.2@MMLCommand@ADD ADDRN2TACID
type: MMLCommand
name: ADD ADDRN2TACID（增加N2TAC组内N2TAC号段）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ADDRN2TACID
command_category: 配置类
applicable_nf:
- GGSN
- SMF
- PGW-C
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址分配位置区管理
- 地址分配N2TAC段
status: active
---

# ADD ADDRN2TACID（增加N2TAC组内N2TAC号段）

## 功能

**适用NF：GGSN、SMF、PGW-C**

该命令用来在N2TAC组内绑定N2TAC号段。当需要在指定N2TAC组内绑定某个N2TAC号段时，使用该命令。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 当一个N2TAC号段被绑定到某个N2TAC组内后，就不允许再绑定到其他的N2TAC组。
- N2TAC号段之间的N2TAC值不允许重叠。

- 最多可输入16000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | N2TAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定N2TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRTACGROUP命令配置生成。 |
| TACSECNUM | N2TAC段编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定N2TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15999。<br>默认值：无<br>配置原则：无 |
| TACSTARTID | N2TAC起始ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定N2TAC起始ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~10。十六进制，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x000000~0xFFFFFF。<br>默认值：无<br>配置原则：<br>TACSTARTID的取值应小于或等于TACENDID。 |
| TACENDID | N2TAC终止ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定N2TAC终止ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~10。十六进制，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x000000~0xFFFFFF。<br>默认值：无<br>配置原则：<br>TACENDID的取值应大于或等于TACSTARTID。 |

## 操作的配置对象

- [N2TAC组内N2TAC号段（ADDRN2TACID）](configobject/UNC/20.15.2/ADDRN2TACID.md)

## 使用实例

在一个本地已经配置的N2TAC组绑定一个N2TAC号段：

```
ADD ADDRN2TACID:TACGROUPNAME="wz-sq",TACSECNUM=2,TACSTARTID="0x000001",TACENDID="0x00001F";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加N2TAC组内N2TAC号段（ADD-ADDRN2TACID）_49644908.md`
