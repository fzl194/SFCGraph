# 查询NRF管理的ProxySMF（LST NRFPROXYSMF）

- [命令功能](#ZH-CN_MMLREF_0000001870462553__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001870462553__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001870462553__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001870462553__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001870462553__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001870462553)

**适用NF：NRF**

该命令用于查询NRF管理的ProxySMF。

## [注意事项](#ZH-CN_MMLREF_0000001870462553)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001870462553)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001870462553)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示本NRF管理的ProxySMF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001870462553)

- 查询本NRF管理的所有ProxySMF信息：
  ```
  LST NRFPROXYSMF:;
  %%LST NRFPROXYSMF:;%%
  RETCODE = 0 执行成功

  结果如下
  -------------------------
  NF实例标识               NF名称 

  Nfinstanceid01   ProxySMF01                          
  Nfinstanceid02   ProxySMF01                             
  (结果个数 = 2)
  ```
- 查询NF实例标识为Nfinstanceid01的ProxySMF信息：
  ```
  LST NRFPROXYSMF: NFINSTANCEID="Nfinstanceid01";
  %%LST NRFPROXYSMF: NFINSTANCEID="Nfinstanceid01";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NF实例标识  =  Nfinstanceid01
      NF名称  =  ProxySMF01
  (结果个数 = 1)
  ```

## [输出结果说明](#ZH-CN_MMLREF_0000001870462553)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF实例标识 | 该参数用于表示本NRF管理的ProxySMF实例标识。 |
| NF名称 | 该参数用于表示本NRF管理的ProxySMF实例名称。 |
