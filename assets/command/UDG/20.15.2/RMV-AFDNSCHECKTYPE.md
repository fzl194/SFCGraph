---
id: UDG@20.15.2@MMLCommand@RMV AFDNSCHECKTYPE
type: MMLCommand
name: RMV AFDNSCHECKTYPE（删除需要进行防欺诈检查的DNS报文类型）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: AFDNSCHECKTYPE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新流生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务防欺诈
- 根据报文类型进行的DNS防欺诈检测
status: active
---

# RMV AFDNSCHECKTYPE（删除需要进行防欺诈检查的DNS报文类型）

## 功能

**适用NF：PGW-U、UPF**

![](删除需要进行防欺诈检查的DNS报文类型（RMV AFDNSCHECKTYPE）_82837804.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除AfDnsCheckType可能会影响用户的业务，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除进行DNS防欺诈检查的DNS报文类型值。

## 注意事项

该命令执行后对新数据流生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPEVALUE | DNS防欺诈检查类型值 | 可选必选说明：必选参数<br>参数含义：该参数用于配置需要进行防欺诈判断的DNS报文类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/AFDNSCHECKTYPE]] · 需要进行防欺诈检查的DNS报文类型（AFDNSCHECKTYPE）

## 使用实例

如果运营商要删除对类型值为10的DNS报文进行防欺诈检查，则配置命令如下：

```
RMV AFDNSCHECKTYPE: TYPEVALUE=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-AFDNSCHECKTYPE.md`
