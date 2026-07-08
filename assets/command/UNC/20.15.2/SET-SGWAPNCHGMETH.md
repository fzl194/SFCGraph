---
id: UNC@20.15.2@MMLCommand@SET SGWAPNCHGMETH
type: MMLCommand
name: SET SGWAPNCHGMETH（设置SGW APN计费方式）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SGWAPNCHGMETH
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 对新用户生效
is_dangerous: true
max_records: 10000
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- SGW计费控制
- SGW APN计费方式
status: active
---

# SET SGWAPNCHGMETH（设置SGW APN计费方式）

## 功能

**适用NF：SGW-C**

![](设置SGW APN计费方式（SET SGWAPNCHGMETH）_09896992.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改配置会影响新激活的SGW用户是否产生S-GW话单，可能导致用户无法计费。

SET SGWAPNCHGMETH命令用来控制APN下的用户是否产生S-GW话单。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为10000。
- 参数APN在表APN中必须存在才能配置成功。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | Offline |
| --- | --- |
| 初始值 | INHERIT |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等。<br>默认值：无<br>配置原则：无 |
| OFFLINE | APN离线计费开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置APN下的用户是否产生S-GW离线话单。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：禁止。<br>- ENABLE：允许。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：<br>- ENABLE：用户执行离线计费功能，生成SGW离线话单。<br>- DISABLE：用户不执行离线计费功能。<br>- INHERIT：继承基于计费属性的配置。 |

## 操作的配置对象

- [SGW APN计费方式（SGWAPNCHGMETH）](configobject/UNC/20.15.2/SGWAPNCHGMETH.md)

## 使用实例

修改APN实例aa用户不产生S-GW话单：

```
SET SGWAPNCHGMETH: APN="aa",OFFLINE=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SGW-APN计费方式（SET-SGWAPNCHGMETH）_09896992.md`
