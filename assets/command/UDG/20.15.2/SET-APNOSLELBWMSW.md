---
id: UDG@20.15.2@MMLCommand@SET APNOSLELBWMSW
type: MMLCommand
name: SET APNOSLELBWMSW（设置APN操作系统级带宽管理开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNOSLELBWMSW
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 10000
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- APN 操作系统级带宽管理
status: active
---

# SET APNOSLELBWMSW（设置APN操作系统级带宽管理开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用来设置APN下操作系统级带宽管理开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为10000。
- 此命令的生效范围限于APN。
- 如果开关设置为继承，则继承SET GLBOSLELBWMSW命令的IsEnable参数配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNAME | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD APN命令配置生成。<br>- 配置的APN必须是系统已经存在的APN对象名称。 |
| ISENABLE | APN操作系统级带宽管理开关 | 可选必选说明：必选参数<br>参数含义：APN操作系统级带宽管理开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）APN下操作系统级带宽管理开关。<br>- ENABLE：使能（开启）APN操作系统级带宽管理开关。<br>- INHERIT：继承SET GLBOSLELBWMSW命令的IsEnable参数配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNOSLELBWMSW]] · APN操作系统级带宽管理开关（APNOSLELBWMSW）

## 关联任务

- [[UDG@20.15.2@Task@0-00107]]

## 使用实例

假如运营商需使能名称为“huawei.com”的APN的操作系统BWM功能：

```
SET APNOSLELBWMSW:APNNAME="huawei.com",ISENABLE=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置APN操作系统级带宽管理开关（SET-APNOSLELBWMSW）_82837498.md`
