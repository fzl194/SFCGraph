---
id: UDG@20.15.2@MMLCommand@DSP ETCDTTL
type: MMLCommand
name: DSP ETCDTTL（查询用于仲裁目的的key的租约信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ETCDTTL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP ETCDTTL（查询用于仲裁目的的key的租约信息）

## 功能

此命令用于查询用于仲裁目的的key租约的保活时长信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数表示查询用于仲裁目的的key的类型。<br>数据来源：本端规划<br>取值范围：<br>- MicroserviceSide（微服务侧）<br>- LargeGranularitySide（大颗粒侧）<br>- AllKeys（所有key值）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ETCDTTL]] · 用于仲裁目的的key的租约信息（ETCDTTL）

## 使用实例

- 查询微服务侧用于仲裁目的的key的租约信息。
  ```
  %%DSP ETCDTTL: TYPE=MicroserviceSide;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  Key值                              租约号               租约保活时长  Key值类型  

  haf/1000|999/                      4491342434916560914  4             Micoservice
  haf/1002|999/                      3164750869684858987  4             Micoservice
  (结果个数 = 2)

  ---    END
  ```
- 查询大颗粒侧用于仲裁目的的key的租约信息。
  ```
  %%DSP ETCDTTL: TYPE=LargeGranularitySide;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  Key值                              租约号               租约保活时长  Key值类型  

  ETCD_DSLE_KEY_ACS_VNFC_1           3164750869684858975  4             Large Granularity
  ha_leader_0                        5467523248242879628  4             Large Granularity
  (结果个数 = 2)

  ---    END
  ```
- 查询所有用于仲裁目的的key的租约信息。
  ```
  %%DSP ETCDTTL: TYPE=AllKeys;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  Key值                              租约号               租约保活时长  Key Type  

  haf/1000|999/                      4491342434916560914  4             Micoservice
  haf/1002|999/                      3164750869684858987  4             Micoservice
  ETCD_DSLE_KEY_ACS_VNFC_1           3164750869684858975  4             Large Granularity
  (结果个数 = 3)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询用于仲裁目的的key的租约信息（DSP-ETCDTTL）_94730406.md`
