# 查询用于仲裁目的的key的租约信息（DSP ETCDTTL）

- [命令功能](#ZH-CN_MMLREF_0294730406__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0294730406__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0294730406__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0294730406__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0294730406__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0294730406)

此命令用于查询用于仲裁目的的key租约的保活时长信息。

## [注意事项](#ZH-CN_MMLREF_0294730406)

无

#### [操作用户权限](#ZH-CN_MMLREF_0294730406)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0294730406)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数表示查询用于仲裁目的的key的类型。<br>数据来源：本端规划<br>取值范围：<br>- MicroserviceSide（微服务侧）<br>- LargeGranularitySide（大颗粒侧）<br>- AllKeys（所有key值）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0294730406)

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

## [输出结果说明](#ZH-CN_MMLREF_0294730406)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Key值 | 该参数表示用于仲裁目的的key的值。 |
| 租约号 | 该参数表示用于仲裁目的的key的租约号。 |
| 租约保活时长 | 该参数表示用于仲裁目的的key的租约保活时长。 |
| Key值类型 | 该参数表示用于仲裁目的的key的类型。 |
