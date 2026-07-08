---
id: UNC@20.15.2@MMLCommand@ADD UNCLOGCTRL
type: MMLCommand
name: ADD UNCLOGCTRL（增加UNC日志控制记录）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UNCLOGCTRL
command_category: 配置类
applicable_nf:
- SMF
- AMF
- NRF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# ADD UNCLOGCTRL（增加UNC日志控制记录）

## 功能

**适用NF：SMF、AMF、NRF、NSSF、SMSF、NCG**

该命令用于增加一条UNC日志的控制记录。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入255条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：记录索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| CSNAME | CS名称 | 可选必选说明：可选参数<br>参数含义：创建logger时的CS名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| FILE | 文件或路径名 | 可选必选说明：可选参数<br>参数含义：文件名或路径。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| LINE | 代码行号 | 可选必选说明：可选参数<br>参数含义：代码行号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |
| FUNC | 函数名 | 可选必选说明：可选参数<br>参数含义：函数名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| KEYWORD | 关键字 | 可选必选说明：可选参数<br>参数含义：日志关键字，可以有多个，以空格分隔。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| PRINTSTACK | 是否打印调用栈 | 可选必选说明：可选参数<br>参数含义：是否打印调用栈。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| LOGLEVEL | 设置匹配的日志的级别 | 可选必选说明：可选参数<br>参数含义：日志级别。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “DEBUG（DEBUG）”：打开调试级别及以上的日志输出<br>- “INFO（INFO）”：打开提示级别及以上的日志输出<br>- “WARN（WARN）”：打开告警级别及以上的日志输出<br>- “ERROR（ERROR）”：打开错误级别及以上的日志输出<br>- “CRITICAL（CRITICAL）”：打开致命级别的日志输出<br>- “CLOSE（CLOSE）”：关闭日志输出<br>默认值：INVALID<br>配置原则：无 |
| WHITEMODE | 白名单模式 | 可选必选说明：可选参数<br>参数含义：是否开启白名单模式。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：FALSE<br>配置原则：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：记录描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UNCLOGCTRL]] · UNC日志控制记录（UNCLOGCTRL）

## 使用实例

如下实例用于添加一条记录

```
ADD UNCLOGCTRL: INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-UNCLOGCTRL.md`
