# 查询选路指示器路由（LST NRFROUTINGINDRT）

- [命令功能](#ZH-CN_MMLREF_0209652642__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652642__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652642__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652642__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209652642__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209652642)

**适用NF：NRF**

该命令用于查询已配置的选路指示器路由信息。

## [注意事项](#ZH-CN_MMLREF_0209652642)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209652642)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652642)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示在当前NRF上通过选路指示器路由寻址的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- UDM（UDM）<br>- AUSF（AUSF）<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为UDM、AUSF的路由转发功能，其他NF类型为预留功能。 |
| ROUTINGIND | 选路指示器 | 可选必选说明：可选参数<br>参数含义：该参数用于表示支持ROUTIINGIND号段信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~4。取值范围0~9999。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于NF实例组标识寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## [使用实例](#ZH-CN_MMLREF_0209652642)

- 查询所有的选路指示器路由：
  ```
  LST NRFROUTINGINDRT:;
  %%LST NRFROUTINGINDRT:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NF类型  选路指示器  归属NRF组名称  

  UDM     1111        L-NRF1         
  AUSF    1111        L-NRF1         
  (结果个数 = 2)
  ```
- 查询指定NF类型的路由信息。例如，在H-NRF上，查询NF类型为UDM的选路指示器及该NF归属的L-NRF实例组名称。
  ```
  LST NRFROUTINGINDRT: NFTYPE=UDM;
  %%LST NRFROUTINGINDRT: NFTYPE=UDM;%%
  RETCODE = 0  操作成功

  结果如下
  --------
         NF类型 = UDM
     选路指示器 = 1111
  归属NRF组名称 = H-NRF1
  (结果个数 = 1)
  ```

## [输出结果说明](#ZH-CN_MMLREF_0209652642)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF类型 | 该参数用于表示在当前NRF上通过选路指示器路由寻址的NF类型。 |
| 选路指示器 | 该参数用于表示支持ROUTIINGIND号段信息。 |
| 归属NRF组名称 | 该参数用于表示当前NRF基于NF实例组标识寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。 |
