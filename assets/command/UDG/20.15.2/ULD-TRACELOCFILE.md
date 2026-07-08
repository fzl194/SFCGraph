---
id: UDG@20.15.2@MMLCommand@ULD TRACELOCFILE
type: MMLCommand
name: ULD TRACELOCFILE（上传跟踪本地文件）
nf: UDG
version: 20.15.2
verb: ULD
object_keyword: TRACELOCFILE
command_category: 调测类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务运维
- 业务跟踪管理
- 用户跟踪本地存盘文件管理
status: active
---

# ULD TRACELOCFILE（上传跟踪本地文件）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](上传跟踪本地文件（ULD TRACELOCFILE）_78310840.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，命令执行成功会将FileSver已经存在的文件删除

该命令用于上传指定pod下用户跟踪存盘文件到文件服务器上。

## 注意事项

- 该命令执行后立即生效。
- 使用ULD命令时需要去掉末尾分片标识与“.zip”等后缀。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAMEACT | POD名称 | 可选必选说明：必选参数<br>参数含义：POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：无 |
| FILENAMEACT | 文件名 | 可选必选说明：必选参数<br>参数含义：文件名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。不支持空格，区分大小写。<br>默认值：无<br>配置原则：无 |
| FILESTARTNO | 文件起始序号 | 可选必选说明：必选参数<br>参数含义：文件起始序号。<br>数据来源：本端规划<br>取值范围：1~4294967295。<br>默认值：无<br>配置原则：无 |
| FILEENDNO | 文件结束序号 | 可选必选说明：可选参数<br>参数含义：文件结束序号。<br>数据来源：本端规划<br>取值范围：1~4294967295。<br>默认值：无<br>配置原则：结束序号和开始序号之差不能大于或者等于50。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TRACELOCFILE]] · 上传跟踪本地文件（TRACELOCFILE）

## 使用实例

上传ssgpod-0的user_trace_20210918-163654_part2.zip文件和user_trace_20210918-163654_part3.zip文件到文件服务器上：

```
ULD TRACELOCFILE: PODNAMEACT="ssgpod-0", FILENAMEACT="user_trace_20210918-163654", FILESTARTNO=2, FILEENDNO=3;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ULD-TRACELOCFILE.md`
