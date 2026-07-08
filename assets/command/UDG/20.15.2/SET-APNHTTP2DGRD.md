---
id: UDG@20.15.2@MMLCommand@SET APNHTTP2DGRD
type: MMLCommand
name: SET APNHTTP2DGRD（设置APN HTTP2.0协议回落开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNHTTP2DGRD
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
- 业务公共参数管理
- APN HTTP2协议回落开关
status: active
---

# SET APNHTTP2DGRD（设置APN HTTP2.0协议回落开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用来设置指定APN下的HTTP2.0协议回落功能。当运营商部署的网关设备不具备HTTP2.0处理能力或者网关设备需要与不具备HTTP2.0处理能力的周边网元配合共同完成业务部署时，需要开启HTTP2.0协议回落。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条。
- 此命令的生效范围限于APN。
- 如果HTTP2.0协议回落开关设置为继承，则继承SET SRVCOMMONPARA命令的HTTP2DEGRADESW开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：APN实例名称是通过ADD APN命令配置的。 |
| HTTP2DEGRADESW | APN HTTP2协议回落开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP2回落是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能，不支持HTTP2协议回落。<br>- ENABLE：使能，支持HTTP2协议回落。<br>- INHERIT：继承，HTTP2协议回落开关需要继承上一级回落开关。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNHTTP2DGRD]] · APN HTTP2.0协议回落开关（APNHTTP2DGRD）

## 关联任务

- [[UDG@20.15.2@Task@0-00149]]

## 使用实例

假如运营商需使能名称为“huawei.com”的APN的HTTP2.0协议回落功能：

```
SET APNHTTP2DGRD:APN="huawei.com",HTTP2DEGRADESW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置APN-HTTP2.0协议回落开关（SET-APNHTTP2DGRD）_82837306.md`
