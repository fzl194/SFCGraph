---
id: UNC@20.15.2@MMLCommand@MOD NGSGWPLMN
type: MMLCommand
name: MOD NGSGWPLMN（修改SGW-C Home PLMN）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGSGWPLMN
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- SGW计费控制
- SGW-C PLMN信息管理
status: active
---

# MOD NGSGWPLMN（修改SGW-C Home PLMN）

## 功能

**适用NF：SGW-C**

该命令用以修改指定SGW-C Home PLMN的描述信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于在UNC上唯一标识某个运营商。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成SGW-C上Home PLMN的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成SGW-C上Home PLMN的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数是对配置的SGW-C上Home PLMN的描述信息，在运维过程中起助记作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGSGWPLMN]] · SGW-C Home PLMN（NGSGWPLMN）

## 使用实例

将SGW-C Home PLMN 12303的DESC修改为12303，执行如下命令：

```
MOD NGSGWPLMN: NOID=0, MCC="123", MNC="03", DESC="12303";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NGSGWPLMN.md`
