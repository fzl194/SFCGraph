---
id: UDG@20.15.2@MMLCommand@SET APNACCESSWAL
type: MMLCommand
name: SET APNACCESSWAL（设置Apn接入速率配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNACCESSWAL
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- APN的接入速率属性配置
status: active
---

# SET APNACCESSWAL（设置Apn接入速率配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](设置Apn接入速率配置（SET APNACCESSWAL）_06054797.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置合理的用户接入速率取值，否则无法保护自身及后端网元或用户激活失败。

该命令用来配置APN的接入速率。当需要限制APN的接入速率时使用此配置，比如可以用来防止APN相关的网元故障导致的激活信令突增造成对其他网元的冲击。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条ApnAccessWal。
- 流控失败将给用户返回无资源可用原因值。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| WALNUMBER | 用户的接入速率 | 可选必选说明：必选参数<br>参数含义：指定接入速率。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0，30～1000000，单位为 个/s。取值为0表示取消对APN的接入速率限制。<br>默认值：无<br>配置原则：阈值不合理可能导致用户激活失败或者设备过载。 |

## 操作的配置对象

- [Apn接入速率配置（APNACCESSWAL）](configobject/UDG/20.15.2/APNACCESSWAL.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00050]]

## 使用实例

根据网络规划，配置名称为“apn1.com”的APN整机的接入速率为300：

```
SET APNACCESSWAL:APN="huawei.com",WALNUMBER=300;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置Apn接入速率配置（SET-APNACCESSWAL）_06054797.md`
