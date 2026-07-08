# 查询AMF区域标识路由（LST NRFAMFREGIDRT）

- [命令功能](#ZH-CN_MMLREF_0209653756__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653756__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653756__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653756__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653756__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653756)

**适用NF：NRF**

该命令用于查询已配置的AMF区域标识路由信息。

## [注意事项](#ZH-CN_MMLREF_0209653756)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209653756)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653756)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AMFREGID | AMF区域标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示AMF区域标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。按照十六进制输入，输入时不带0x，不足两位时从左边补0，取值范围0~ff。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于AMF区域标识寻址AMF时的下一跳NRF实例组名称，被寻址的AMF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |

## [使用实例](#ZH-CN_MMLREF_0209653756)

- 查询AMF区域标识为09，归属NRF组名称为L-NRF1的AMF区域标识路由信息：
  ```
  LST NRFAMFREGIDRT:AMFREGID="09", NEXTNRFGRPNAME="L-NRF1";
  %%LST NRFAMFREGIDRT: AMFREGID="09", NEXTNRFGRPNAME="L-NRF1";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
    AMF区域标识 =  09
  归属NRF组名称 =  L-NRF1
  (结果个数 = 1)
  ```
- 查询所有的AMF区域标识的路由信息：
  ```
  LST NRFAMFREGIDRT:;
  %%LST NRFAMFREGIDRT:;%%
  RETCODE = 0  操作成功

  结果如下
  AMF区域标识  归属NRF组名称 

  08           L-NRF3     
  09           L-NRF1      
  (结果个数 = 2)
  ```

## [输出结果说明](#ZH-CN_MMLREF_0209653756)

| 输出项名称 | 输出项解释 |
| --- | --- |
| AMF区域标识 | 该参数用于表示AMF区域标识。 |
| 归属NRF组名称 | 该参数用于表示当前NRF基于AMF区域标识寻址AMF时的下一跳NRF实例组名称，被寻址的AMF归属于该NRF实例组。 |
