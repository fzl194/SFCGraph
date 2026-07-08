---
id: UDG@20.15.2@MMLCommand@RMV APNFLOWMAXNUM
type: MMLCommand
name: RMV APNFLOWMAXNUM（删除APN最大流数）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: APNFLOWMAXNUM
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- DN管理
- APN管理
- APN最大五元组数
status: active
---

# RMV APNFLOWMAXNUM（删除APN最大流数）

## 功能

**适用NF：PGW-U、UPF**

![](删除APN最大流数（RMV APNFLOWMAXNUM）_82837011.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当可能导致五元组资源耗尽，并且会影响用户业务访问，请谨慎使用并联系华为技术支持协助操作。

该命令用于将指定APN下的最大流数恢复默认，即全局配置的最大五元组个数，可以通过LST SRVCOMMONPARA命令行进行查看。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN最大流数（APNFLOWMAXNUM）](configobject/UDG/20.15.2/APNFLOWMAXNUM.md)

## 使用实例

APN最大流数恢复默认，APN名称为aa：

```
RMV APNFLOWMAXNUM:APN="aa";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除APN最大流数（RMV-APNFLOWMAXNUM）_82837011.md`
