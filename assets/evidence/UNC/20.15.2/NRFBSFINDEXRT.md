# 查询BSFINDEX路由（LST NRFBSFINDEXRT）

- [命令功能](#ZH-CN_MMLREF_0244007034__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0244007034__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0244007034__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0244007034__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0244007034__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0244007034)

**适用NF：NRF**

该命令用于查询选择BSF时的路由实例信息。

## [注意事项](#ZH-CN_MMLREF_0244007034)

无

#### [操作用户权限](#ZH-CN_MMLREF_0244007034)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0244007034)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINDEX | BSF索引 | 可选必选说明：可选参数<br>参数含义：该参数用于表示BSF路由实例信息的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于BSF类型寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## [使用实例](#ZH-CN_MMLREF_0244007034)

- 查询所有的选择BSF时的路由实例信息：
  ```
  LST NRFBSFINDEXRT:;
  %%LST NRFBSFINDEXRT:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  BSF索引  归属NRF组名称
  1        L-NRF1
  1        H-NRF1
  (结果个数 = 2)
  ```
- 查询BSF索引为1，归属NRF组名称为H-NRF1的路由信息：
  ```
  LST NRFBSFINDEXRT: BSFINDEX=1, NEXTNRFGRPNAME="H-NRF1";
  %%LST NRFBSFINDEXRT: BSFINDEX=1, NEXTNRFGRPNAME="H-NRF1";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
        BSF索引  =  1
  归属NRF组名称  =  H-NRF1
  (结果个数 = 1)
  ```

## [输出结果说明](#ZH-CN_MMLREF_0244007034)

| 输出项名称 | 输出项解释 |
| --- | --- |
| BSF索引 | 该参数用于表示BSF路由实例信息的索引值。 |
| 归属NRF组名称 | 该参数用于表示当前NRF基于BSF类型寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。 |
