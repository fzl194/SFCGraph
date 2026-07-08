---
id: UNC@20.15.2@MMLCommand@RMV NGAREATZ
type: MMLCommand
name: RMV NGAREATZ（删除5G区域时区参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGAREATZ
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 多时区管理
- 5G区域时区参数
status: active
---

# RMV NGAREATZ（删除5G区域时区参数）

## 功能

**适用NF：AMF**

此命令用于删除一条5G区域时区记录。即删除特定区域与时区标识的映射关系。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | MCC | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位的十进制数字。<br>默认值：无<br>配置原则：无 |
| MNC | MNC | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2～3位的十进制数字。<br>默认值：无<br>配置原则：无 |
| BGNTAC | 跟踪区编码起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于表示跟踪区编码的起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。字符串类型，输入长度是6。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGAREATZ]] · 5G区域时区参数（NGAREATZ）

## 使用实例

删除一条5G区域时区记录，“移动国家代码”为“460”，“移动网号”为“03”，“跟踪区编码起始值”为“000112”，执行如下命令：

```
RMV NGAREATZ: MCC="460", MNC="03", BGNTAC="000112";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGAREATZ.md`
