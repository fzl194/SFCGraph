---
id: UDG@20.15.2@MMLCommand@LST APNTRFCDFDSWITCH
type: MMLCommand
name: LST APNTRFCDFDSWITCH（查询APN大流量攻击防护配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNTRFCDFDSWITCH
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- DDoS防护
- 大流量攻击防护APN开关
status: active
---

# LST APNTRFCDFDSWITCH（查询APN大流量攻击防护配置）

## 功能

**适用NF：UPF**

该命令用于查询APN下大流量攻击检测开关是否开启。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN大流量攻击防护配置（APNTRFCDFDSWITCH）](configobject/UDG/20.15.2/APNTRFCDFDSWITCH.md)

## 使用实例

查询APN为apn1.com的大流量检测开关是否开启：

```
LST APNTRFCDFDSWITCH: APN="apn1.com";
```

```

RETCODE = 0 操作成功。

大流量攻击防护配置信息
----------------------
                                          APN名称  =  apn1.com
                    上行大流量攻击防护APN功能开关  =  使能
                    下行大流量攻击防护APN功能开关  =  使能
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询APN大流量攻击防护配置（LST-APNTRFCDFDSWITCH）_86530452.md`
