---
id: UDG@20.15.2@MMLCommand@COL APPINFORMATION
type: MMLCommand
name: COL APPINFORMATION（第三方APP信息采集）
nf: UDG
version: 20.15.2
verb: COL
object_keyword: APPINFORMATION
command_category: 调测类
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- 第三方应用调测
- 第三方应用日志收集
status: active
---

# COL APPINFORMATION（第三方APP信息采集）

## 功能

该命令用于与网管信息采集功能配合使用，采集第三方应用的日志信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行时会消耗系统资源（CPU、内存和磁盘）。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INFOTYPE | 采集信息名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定收集信息名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。<br>默认值：无<br>配置原则：无 |
| APPNAME | APP实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定第三方应用名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。<br>默认值：无<br>配置原则：无 |
| VDUTYPE | VDU类型名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VDU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：无 |
| VMNAME | VM名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VM名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：无 |
| STARTTIME | 开始时间 | 可选必选说明：可选参数<br>参数含义：该参数用于指定收集开始时间。<br>数据来源：本端规划<br>取值范围：日期时间类型，输入格式是YYYY:MM:DD:HH:NN:SS。<br>默认值：无<br>配置原则：无 |
| ENDTIME | 结束时间 | 可选必选说明：可选参数<br>参数含义：该参数用于指定收集结束时间。<br>数据来源：本端规划<br>取值范围：日期时间类型，输入格式是YYYY:MM:DD:HH:NN:SS。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APPINFORMATION]] · 第三方APP信息采集（APPINFORMATION）

## 使用实例

收集第三方应用openwave的日志：

```
COL APPINFORMATION: INFOTYPE="LOG", APPNAME="openwave";
RETCODE = 0 操作成功

动作执行节点
------------
动作执行节点  =  sfmu-pod-1
    执行结果  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/COL-APPINFORMATION.md`
