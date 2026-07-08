---
id: UNC@20.15.2@MMLCommand@RMV SMFPRESELBYIMSI
type: MMLCommand
name: RMV SMFPRESELBYIMSI（删除基于IMSI优选指定SMF配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMFPRESELBYIMSI
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- SMF优选策略管理
status: active
---

# RMV SMFPRESELBYIMSI（删除基于IMSI优选指定SMF配置）

## 功能

**适用NF：AMF**

该命令用于删除基于IMSI优选指定SMF配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定进行优选指定SMF的用户IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [基于IMSI优选指定SMF配置（SMFPRESELBYIMSI）](configobject/UNC/20.15.2/SMFPRESELBYIMSI.md)

## 使用实例

删除IMSI为“123456789012345”的用户优选指定SMF配置，执行如下命令：

```
RMV SMFPRESELBYIMSI:IMSI="123456789012345";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除基于IMSI优选指定SMF配置（RMV-SMFPRESELBYIMSI）_84694168.md`
