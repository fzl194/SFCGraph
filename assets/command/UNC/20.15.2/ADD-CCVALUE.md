---
id: UNC@20.15.2@MMLCommand@ADD CCVALUE
type: MMLCommand
name: ADD CCVALUE（增加计费特征值）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CCVALUE
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- 计费特征值
status: active
---

# ADD CCVALUE（增加计费特征值）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于增加计费属性组中的计费特征值配置。

## 注意事项

- 该命令执行后立即生效。

- 每个计费特征组下最多可以配置20个计费特征值。

- 最多可输入2560条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCGROUPNAME | 计费特征组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费特征组的名字，在系统内唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。由英文字母（大小写）、数字、下划线构成的字符串，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD CCGROUP命令配置生成。 |
| CCVALUE | 计费特征值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费特征值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~6。十六进制，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围为0x0000~0xFFFF，长度为4位或者6位的字符串。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CCVALUE]] · 计费特征值（CCVALUE）

## 使用实例

增加“计费特征组名称”为“c1”，“计费特征值”为“0x0000”的计费特征值配置：

```
ADD CCVALUE: CCGROUPNAME="c1", CCVALUE="0x0000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加计费特征值（ADD-CCVALUE）_88733215.md`
