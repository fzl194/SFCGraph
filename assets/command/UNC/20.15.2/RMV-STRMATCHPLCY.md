---
id: UNC@20.15.2@MMLCommand@RMV STRMATCHPLCY
type: MMLCommand
name: RMV STRMATCHPLCY（删除字符串匹配策略）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV STRMATCHPLCY（删除字符串匹配策略）

## 功能

**适用NF：AMF**

该命令用于删除对指定文件名、行号配置字符串匹配策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILEPATH | 文件路径 | 可选必选说明：必选参数<br>参数含义：该参数表示调用匹配策略接口的函数所在文件的绝对路径。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| LINEPOS | 行号 | 可选必选说明：必选参数<br>参数含义：该参数表示调用匹配策略接口的函数所在行号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65534。<br>默认值：无<br>配置原则：无 |
| VERSION | 版本号 | 可选必选说明：必选参数<br>参数含义：该参数用于配置匹配策略支持的版本号（不包括补丁号）。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：<br>配置当前系统版本号（不含补丁号）。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/STRMATCHPLCY]] · 字符串匹配策略（STRMATCHPLCY）

## 使用实例

删除指定路径为b/test.go，行号为100的字符串匹配规则，执行如下命令：

```
RMV STRMATCHPLCY:FILEPATH="b/test.go",LINEPOS=100,VERSION="23.1.0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-STRMATCHPLCY.md`
