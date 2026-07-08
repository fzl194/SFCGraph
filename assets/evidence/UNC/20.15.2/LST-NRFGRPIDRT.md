# 查询NF组标识路由（LST NRFGRPIDRT）

- [命令功能](#ZH-CN_MMLREF_0209653153__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653153__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653153__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653153__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653153__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653153)

**适用NF：NRF**

该命令用于查询已配置的NF组标识路由信息。

## [注意事项](#ZH-CN_MMLREF_0209653153)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209653153)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653153)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示通过NF组标识路由寻址的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- AUSF（AUSF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- PCF（PCF）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SMSF（SMSF）<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为AUSF、UDM、PCF、CUSTOM_OCS、SMSF的路由转发功能，其他NF类型为预留功能。 |
| NFGROUPID | NF组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示被寻址NF所在的NF实例组标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于NF实例组标识寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数需通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## [使用实例](#ZH-CN_MMLREF_0209653153)

- 查看所有NF组实例标识：
  ```
  LST NRFGRPIDRT:
  %%LST NRFGRPIDRT:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NF类型  NF组标识         归属NRF组名称  

  PCF     nfgroupid01      L-NRF1         
  UDR     nfgroupid01      L-NRF1         
  (结果个数 = 2)
  ```
- 查询指定NF类型的路由信息。例如，在H-NRF上，查询NF类型为PCF的NF组标识及该NF归属的L-NRF实例组名称。执行：
  ```
  LST NRFGRPIDRT:NFTYPE=PCF:
  %%LST NRFGRPIDRT: NFTYPE=PCF;%%
  RETCODE = 0  操作成功

  结果如下
  --------
        NF类型  =  PCF
       NF组标识 =  nfgroupid01
  归属NRF组名称 =  L-NRF1
  (结果个数 = 1)
  ```

## [输出结果说明](#ZH-CN_MMLREF_0209653153)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NF类型 | 该参数用于表示通过NF组标识路由寻址的NF类型。 |
| NF组标识 | 该参数用于表示被寻址NF所在的NF实例组标识。 |
| 归属NRF组名称 | 该参数用于表示当前NRF基于NF实例组标识寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。 |
