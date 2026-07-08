---
id: UDG@20.15.2@MMLCommand@RMV FILTERGROUP
type: MMLCommand
name: RMV FILTERGROUP（删除过滤器组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: FILTERGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 流过滤器管理
- 过滤器组
status: active
---

# RMV FILTERGROUP（删除过滤器组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除过滤器组，或者从组中删除一个过滤器。

## 注意事项

- 该命令执行后需要等待执行SET REFRESHSRV命令（REFRESHTYPE参数设置为USERPROFILE或ALL）刷新后生效。
- 如果FilterGroup被FlowFilter使用，不允许删除FilterGroup。
- 如果FilterGroup被FlowFilter使用，可以从FilterGroup中删除Filter。
- 如果不输入过滤器组名称，并且配置的过滤器组与过滤器的绑定关系总数不超过10000条，则可以一次删除成功。如果超过10000条，需要执行多次。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILTERGRPNAME | 过滤器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| FILTERNAME | 过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：如果指定FILTERNAME参数，必须先指定FILTERGRPNAME参数。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FILTERGROUP]] · 过滤器组（FILTERGROUP）

## 使用实例

- 删除所有过滤器组配置，执行如下命令：
  ```
  RMV FILTERGROUP:;
  ```
- 删除名称为group1的过滤器组，执行如下命令：
  ```
  RMV FILTERGROUP: FILTERGRPNAME="group1";
  ```
- 从过滤器组group1中删除过滤器filter1，执行如下命令：
  ```
  RMV FILTERGROUP: FILTERGRPNAME="group1", FILTERNAME="filter1";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除过滤器组（RMV-FILTERGROUP）_95089583.md`
