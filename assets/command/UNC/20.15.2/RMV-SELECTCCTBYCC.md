---
id: UNC@20.15.2@MMLCommand@RMV SELECTCCTBYCC
type: MMLCommand
name: RMV SELECTCCTBYCC（删除基于CC配置融合计费模板处理）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SELECTCCTBYCC
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 融合计费模板绑定
status: active
---

# RMV SELECTCCTBYCC（删除基于CC配置融合计费模板处理）

## 功能

**适用NF：PGW-C、SMF、SGW-C**

该命令用于删除基于CC配置融合计费模板处理。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTYPE | CC类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费属性。<br>数据来源：全网规划<br>取值范围：<br>- DEFAULT（未指定Charge Characteristic的值）<br>- VALUE（指定Charge Characteristic的值）<br>默认值：无<br>配置原则：无 |
| CCVALUE | Charge Characteristic值 | 可选必选说明：该参数在"CCTYPE"配置为"VALUE"时为条件必选参数。<br>参数含义：该参数用于指定特殊的CC值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SELECTCCTBYCC]] · 基于CC配置融合计费模板处理（SELECTCCTBYCC）

## 使用实例

删除基于CC值为1234配置融合计费模板：

```
RMV SELECTCCTBYCC: CCTYPE=VALUE, CCVALUE="1234";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SELECTCCTBYCC.md`
