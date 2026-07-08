# 查询指定消息类型固定速率流控信息（LST N4FIXEDFC）

- [命令功能](#ZH-CN_MMLREF_0000001088537096__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001088537096__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001088537096__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001088537096__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001088537096__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001088537096)

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询指定N4接口消息类型的固定速率流控信息。

## [注意事项](#ZH-CN_MMLREF_0000001088537096)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001088537096)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001088537096)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGTYPE | 流控消息类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置N4接口被流控的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- “ERRIND（错误指示）”：表示ERIR（Error Indication Report）类型的PFCP Session Report Request消息。<br>- “DLDATA（下行数据）”：表示DLDR（Downlink Data Report）类型的PFCP Session Report Request消息。<br>- “UPSDR（用户面发起的会话删除）”：表示UPDR（User Plane Session Delete Report）类型的PFCP Session Report Request消息。<br>- “MULTIDNN（基于多DNN的漫游分流）”：表示MultiDNN（基于多DNN的漫游分流）类型的PFCP Session Report Request消息<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001088537096)

- 查询所有流控消息类型流控信息，执行如下命令：
  ```
  %%LST N4FIXEDFC:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  流控消息类型                          固定速率流控开关     流控速率门
  Downlink Data                           开启                   1000
  Error Indication                        开启                   500
  User Plane Session Delete               开启                   500
  Multiple DNN                            开启                   2000
  (结果个数 = 4)

  ---    END
  ```
- 查询上报类型为DownlinkData的PFCP Session Report Request消息的流控信息，执行如下命令：
  ```
  %%LST N4FIXEDFC:MSGTYPE=DLDATA;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  流控消息类型          固定速率流控开关  流控速率门
  Downlink Data             开启             1000
  (结果个数 = 1)

  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0000001088537096)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 流控消息类型 | 该参数用于设置N4接口被流控的消息类型。 |
| 固定速率流控开关 | 该参数用于控制N4接口指定消息类型固定速率流控功能。 |
| 流控速率门限(个/秒) | 该参数用于设置N4接口指定消息的流控速率上限。该参数针对单POD指定消息类型进行流控。 |
