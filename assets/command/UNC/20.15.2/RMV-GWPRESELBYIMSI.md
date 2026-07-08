---
id: UNC@20.15.2@MMLCommand@RMV GWPRESELBYIMSI
type: MMLCommand
name: RMV GWPRESELBYIMSI（删除指定用户优选网关）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GWPRESELBYIMSI
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- 网关优选
- 指定用户优选网关
status: active
---

# RMV GWPRESELBYIMSI（删除指定用户优选网关）

## 功能

**适用网元：MME**

该命令用于删除指定用户优选网关记录。

## 注意事项

无。

## 权限

manage-ug；system-ug；
G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户IMSI。<br>数据来源：整网规划<br>取值范围：14~15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GWPRESELBYIMSI]] · 指定用户优选网关（GWPRESELBYIMSI）

## 使用实例

删除用户IMSI为 "123030000100001" 的指定用户优选网关记录：

RMV GWPRESELBYIMSI: IMSI="123030000100001";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GWPRESELBYIMSI.md`
