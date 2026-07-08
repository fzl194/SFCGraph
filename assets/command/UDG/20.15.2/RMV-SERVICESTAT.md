---
id: UDG@20.15.2@MMLCommand@RMV SERVICESTAT
type: MMLCommand
name: RMV SERVICESTAT（删除业务统计配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SERVICESTAT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新流生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 业务实例性能统计对象
status: active
---

# RMV SERVICESTAT（删除业务统计配置）

## 功能

**适用NF：PGW-U、UPF**

![](删除业务统计配置（RMV SERVICESTAT）_86528354.assets/notice_3.0-zh-cn.png)

本命令属于高危命令,执行本命令后将删除指定或所有业务统计对象，影响性能统计呈现，请谨慎使用。

该命令用于删除基于业务的性能统计对象组合，取消该记录下HTTP协议和DNS协议的统计开关设置，并删除该实例与协议和规则的绑定关系。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令支持批量删除。
- 执行该命令会删除对应的RuleBindSrvS和ProtBindSrvS设置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVSTATNAME | 业务统计名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务统计配置的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格及特殊字符“#”、“:”和“&”。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SERVICESTAT]] · 业务统计配置（SERVICESTAT）

## 使用实例

- 假如运营商希望删除基于业务的性能统计配置“stat1”，并取消该配置下的HTTP、DNS统计开关设置，清除该实例与协议和规则的绑定关系：
  ```
  RMV SERVICESTAT:SRVSTATNAME="stat1";
  ```
- 假如运营商希望删除所有基于业务的性能统计配置，取消所有HTTP、DNS统计开关设置，清除所有实例与协议和规则的绑定关系：
  ```
  RMV SERVICESTAT:;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除业务统计配置（RMV-SERVICESTAT）_86528354.md`
