---
id: UDG@20.15.2@MMLCommand@SET COSTOS
type: MMLCommand
name: SET COSTOS（设置COS TOS映射策略）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: COSTOS
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 传输层控制
- COSTOS映射策略
status: active
---

# SET COSTOS（设置COS TOS映射策略）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置Cos Tos映射策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：
- 使用该命令配置参数TOSPOLICY的值为ENABLE时，需要同时配置TunnelMarking功能，参考SET SRVCOMMONPARA命令。

| 参数标识 | TOSPOLICY |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TOSPOLICY | TOS策略 | 可选必选说明：必选参数<br>参数含义：该参数用于控制Cos Tos处理策略是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：表示在CoS to ToS映射功能中，接口untrust时的入口报文DSCP处理方式选择，继承报文中DSCP。<br>- ENABLE：表示在CoS to ToS映射功能中，接口untrust时的入口报文DSCP处理方式选择，将报文中的DSCP清为0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/COSTOS]] · COS TOS映射策略（COSTOS）

## 使用实例

- 当需要在CoS to ToS映射功能中，接口untrust时的入口报文DSCP处理方式选择，将报文中的DSCP清为0时，使能Cos Tos处理策略：
  ```
  SET COSTOS:TOSPOLICY=ENABLE;
  ```
- 当需要在CoS to ToS映射功能中，接口untrust时的入口报文DSCP处理方式选择，继承报文中DSCP时，不使能Cos Tos处理策略：
  ```
  SET COSTOS:TOSPOLICY=DISABLE;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-COSTOS.md`
