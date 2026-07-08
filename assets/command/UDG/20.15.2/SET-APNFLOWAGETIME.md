---
id: UDG@20.15.2@MMLCommand@SET APNFLOWAGETIME
type: MMLCommand
name: SET APNFLOWAGETIME（设置APN五元组老化时间）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNFLOWAGETIME
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务五元组管理
- APN五元组节点老化时间
status: active
---

# SET APNFLOWAGETIME（设置APN五元组老化时间）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改指定APN下的五元组老化时间。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条。
- 对应的APN（使用ADD APN配置）必须存在才能配置成功。
- 修改FdAgeTime配置后对新接入的用户或更新用户生效。
- 每个APN五元组老化时间未配置或配置为0时不生效，此时继承全局配置的五元组老化时间。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| FDAGETIME | APN五元组老化时间（秒） | 可选必选说明：必选参数<br>参数含义：该参数用于设置APN五元组老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1275，单位是秒。0~1275的整数。<br>默认值：无<br>配置原则：<br>- 如果运营商希望限制某个APN下五元组的老化时间，则需要用该参数指定需要设置的五元组老化时间。<br>- 参数配置原则说明：配置过小，五元组快速老化，7层非关键报文无法获取正确的计费和策略信息，配置过大，五元组老化慢，五元组使用数升高，建议根据现网数据流报文的间隔和五元组使用情况配置。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@APNFLOWAGETIME]] · APN五元组老化时间（APNFLOWAGETIME）

## 使用实例

假如运营商需要设置APN五元组老化时间，APN为aa，FDAGETIME为100：

```
SET APNFLOWAGETIME:APN="aa",FDAGETIME=100;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-APNFLOWAGETIME.md`
