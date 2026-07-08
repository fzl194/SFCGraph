---
id: UNC@20.15.2@MMLCommand@ADD ADDRLACID
type: MMLCommand
name: ADD ADDRLACID（增加LAC组内LAC号段）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ADDRLACID
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址分配位置区管理
- 地址分配LAC段
status: active
---

# ADD ADDRLACID（增加LAC组内LAC号段）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用来在LAC组内绑定LAC号段。当需要在指定LAC组内绑定某个LAC号段时，使用该命令。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 当一个LAC号段被绑定到某个LAC组内后，就不允许再绑定到其他的LAC组。LAC号段之间的LAC值不允许重叠。

- 最多可输入24000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LACGROUPNAME | LAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRLACGROUP命令配置生成。 |
| LACSECNUM | LAC段编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~23999。<br>默认值：无<br>配置原则：无 |
| LACSTARTID | LAC起始ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC起始ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~10。十六进制，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0001~0xFFFD，0xFFFF。<br>默认值：无<br>配置原则：<br>LACSTARTID的取值应小于或等于LACENDID。 |
| LACENDID | LAC终止ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定LAC终止ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~10。十六进制，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0001~0xFFFD，0xFFFF。<br>默认值：无<br>配置原则：<br>LACENDID的取值应大于或等于LACSTARTID。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ADDRLACID]] · LAC组内LAC号段（ADDRLACID）

## 使用实例

在一个本地已经配置的LAC组绑定一个LAC号段：

```
ADD ADDRLACID:LACGROUPNAME="beijing",LACSECNUM=2,LACSTARTID="0x0001",LACENDID="0x0010";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加LAC组内LAC号段（ADD-ADDRLACID）_49644907.md`
