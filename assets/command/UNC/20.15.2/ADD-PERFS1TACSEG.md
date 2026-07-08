---
id: UNC@20.15.2@MMLCommand@ADD PERFS1TACSEG
type: MMLCommand
name: ADD PERFS1TACSEG（增加S1TAC段）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PERFS1TACSEG
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# ADD PERFS1TACSEG（增加S1TAC段）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用来增加一个S1TAC号段，主要用于指定区域或指定区域和APN的性能统计。

## 注意事项

- 该命令执行后立即生效。

- TAC号段之间的TAC值不允许重叠。

- 最多可输入1000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACSEGNAME | TAC段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| TACSTART | TAC段起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC段的起始值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是4~6。长度为4位或者6位的字符串。十六进制，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：<br>TAC段起始值一定要小于等于TAC段结束值。 |
| TACEND | TAC段结束值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC段的结束值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是4~6。长度为4位或者6位的字符串。十六进制，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：<br>TAC段起始值一定要小于等于TAC段结束值。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PERFS1TACSEG]] · S1TAC段（PERFS1TACSEG）

## 使用实例

当运营商需要配置一个TAC号段，执行如下命令：

```
ADD PERFS1TACSEG: TACSEGNAME="changping", TACSTART="0x0001", TACEND="0x0010";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PERFS1TACSEG.md`
