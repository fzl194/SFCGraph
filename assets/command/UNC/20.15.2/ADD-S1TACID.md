---
id: UNC@20.15.2@MMLCommand@ADD S1TACID
type: MMLCommand
name: ADD S1TACID（增加TAC组内绑定的S1TAC号段）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: S1TACID
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 虚拟APN映射管理
- 基于TAC位置的虚拟APN映射管理
- TAC组的S1 TAC段
status: active
---

# ADD S1TACID（增加TAC组内绑定的S1TAC号段）

## 功能

**适用NF：PGW-C**

该命令用来在TAC组内绑定TAC号段。当需要在指定TAC组内绑定某个TAC号段时，使用该命令。

## 注意事项

- 该命令执行后立即生效。

- 当一个TAC号段被绑定到某个TAC组内后，就不允许再绑定到其他的TAC组。TAC号段之间的TAC值不允许重叠。

- 最多可输入9000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACSECNUM | TAC段编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15999。<br>默认值：无<br>配置原则：无 |
| TACSTARTID | TAC起始ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC起始ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是3~6。字符串类型，长度为3至6位。必须是0x/X开头的十六进制数，仅支持输入0x/X、0-9、a-f/A-F，字母不区分大小写，取值范围0x0~0xFFFF。<br>默认值：无<br>配置原则：<br>TACSTARTID一定要小于等于TACENDID。 |
| TACENDID | TAC截止ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC截止ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是3~6。字符串类型，长度为3至6位。必须是0x/X开头的十六进制数，仅支持输入0x/X、0-9、a-f/A-F，字母不区分大小写，取值范围0x0~0xFFFF。<br>默认值：无<br>配置原则：<br>TACSTARTID一定要小于等于TACENDID。 |
| TACGROUPNAME | TAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>本参数通过ADD TACGROUP命令进行配置，且TAC类型必须是S1TAC。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1TACID]] · TAC组内绑定的S1TAC号段（S1TACID）

## 使用实例

假设运营商需要在一个本地已经配置的TAC组绑定一个TAC号段：

```
ADD S1TACID:TACSECNUM=2,TACSTARTID="0x0001",TACENDID="0x0010",TACGROUPNAME="BEIJING";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-S1TACID.md`
