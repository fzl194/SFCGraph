---
id: UNC@20.15.2@MMLCommand@ADD STRMATCHPLCY
type: MMLCommand
name: ADD STRMATCHPLCY（增加字符串匹配策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: STRMATCHPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- 字符串匹配策略
status: active
---

# ADD STRMATCHPLCY（增加字符串匹配策略）

## 功能

![](增加字符串匹配策略（ADD STRMATCHPLCY）_29180525.assets/notice_3.0-zh-cn_2.png)

执行本命令将按照配置修改系统中字符串匹配策略，如果配置错误可能导致不可预期的故障。故建议在执行本命令前联系华为技术支持。

**适用NF：AMF**

该命令用于增加对指定文件名、行号配置字符串匹配策略。

## 注意事项

- 该命令执行后立即生效。

- 该命令配置的字符串匹配策略在版本升级后自动失效。
- 如果需要使用该命令请联系华为技术支持。

- 最多可输入256条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILEPATH | 文件路径 | 可选必选说明：必选参数<br>参数含义：该参数表示调用匹配策略接口的函数所在文件的绝对路径。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| LINEPOS | 行号 | 可选必选说明：必选参数<br>参数含义：该参数表示调用匹配策略接口的函数所在行号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65534。<br>默认值：无<br>配置原则：无 |
| POLICY | 字符串匹配策略 | 可选必选说明：必选参数<br>参数含义：该参数用于配置字符串匹配策略。<br>数据来源：本端规划<br>取值范围：<br>- SENSITIVITY（大小写敏感）<br>- INSENSITIVITY（大小写不敏感）<br>默认值：无<br>配置原则：无 |
| VERSION | 版本号 | 可选必选说明：必选参数<br>参数含义：该参数用于配置匹配策略支持的版本号（不包括补丁号）。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：<br>配置当前系统版本号（不含补丁号）。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/STRMATCHPLCY]] · 字符串匹配策略（STRMATCHPLCY）

## 使用实例

添加字符串匹配规则，修改系统中b/test.go文件中第100行的字符串匹配策略为大小写敏感，执行如下命令：

```
ADD STRMATCHPLCY:FILEPATH="b/test.go",LINEPOS=100,POLICY=SENSITIVITY,VERSION="23.1.0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-STRMATCHPLCY.md`
