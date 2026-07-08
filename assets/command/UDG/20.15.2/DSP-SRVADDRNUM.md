---
id: UDG@20.15.2@MMLCommand@DSP SRVADDRNUM
type: MMLCommand
name: DSP SRVADDRNUM（查询服务实例地址数）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SRVADDRNUM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 路由管理
- 服务实例地址统计
status: active
---

# DSP SRVADDRNUM（查询服务实例地址数）

## 功能

查询业务VNFC服务实例地址数量。用于核对业务VNFC的服务实例地址数量、CSLB的服务实例地址数量以及VNRS的路由数量是否一致。 CSLB查询到的一条服务实例地址对应VNRS上查询到的一条路由。

## 注意事项

- 如果业务VNFC和CSLB的服务实例地址数量不一致，需要业务VNFC确认是否存在服务实例地址丢失。如果存在丢失，执行如下命令，触发服务实例地址的重配置，恢复业务。
  **[ACT SRVRECFG](../../业务重配置/重配置业务数据（ACT SRVRECFG）_29627078.md)** : SRVTYPE=SRVADDR;
- 如果CSLB和VNRS的服务实例地址数量不一致，需要业务VNFC确认是否存在服务实例地址丢失。如果存在丢失，执行命令**[SYN LBSRVADDR](../服务实例地址同步/CSLB向VNRS同步服务实例地址（SYN LBSRVADDR）_29627071.md)**，触发服务实例地址的批量同步，恢复业务。
- 该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVVNFCID | 业务VNFCID | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在窗口下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_27372977.md)**<br>获得，所得NODE ID即为服务VNFC ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |
| SERVICEINDEX | 服务实例ID | 可选必选说明：可选参数<br>参数含义：业务VNFC定义的服务实例ID，通过<br>**[DSP LBSRVINST](../../服务实例管理/服务实例/查询LB服务实例（DSP LBSRVINST）_29627060.md)**<br>查询获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SRVADDRNUM]] · 服务实例地址数（SRVADDRNUM）

## 使用实例

- 查询所有业务VNFC的服务实例地址数。
  DSP SRVADDRNUM: ;

  ```
  %%DSP SRVADDRNUM: ;%%
  RETCODE = 0  操作成功。

  操作结果如下：
  -------------------------
  服务VNFC ID = 4
  服务实例ID = 0
  服务实例地址数 = 9
  (结果个数 = 1)
  --- END
  ```
- 查询指定业务VNFC的服务实例地址数。
  DSP SRVADDRNUM: SRVVNFCID=4;

  ```
  %%DSP SRVADDRNUM: SRVVNFCID=4;%%
  RETCODE = 0  操作成功。

  操作结果如下：
  -------------------------
  服务VNFC ID = 4
  服务实例ID = 0
  服务实例地址数 = 9
  (Number of results = 1)
  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SRVADDRNUM.md`
