---
id: UNC@20.15.2@MMLCommand@RMV ARPRANGE
type: MMLCommand
name: RMV ARPRANGE（删除ARP策略范围配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ARPRANGE
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 差异化服务配置
status: active
---

# RMV ARPRANGE（删除ARP策略范围配置）

## 功能

**适用网元：SGSN**

该命令用于删除ARP策略范围配置。

## 注意事项

- 无

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定进行匹配的IMSI前缀。系统根据该参数值对用户的IMSI进行匹配，从而区分不同的用户群。<br>数据来源：整网规划<br>取值范围：1~15位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ARPRANGE]] · ARP策略范围配置（ARPRANGE）

## 使用实例

1. 删除IMSI前缀为123030000000001的用户的ARP策略组
  RMV ARPRANGE: IMSIPRE="123030000000001";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ARPRANGE.md`
