# 查询BSF索引和DNN的关联关系（LST NRFBSFDNNREL）

- [命令功能](#ZH-CN_MMLREF_0245612431__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0245612431__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0245612431__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0245612431__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0245612431__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0245612431)

**适用NF：NRF**

该命令用于查询已配置的BSF索引和DNN的关联关系。

## [注意事项](#ZH-CN_MMLREF_0245612431)

无

#### [操作用户权限](#ZH-CN_MMLREF_0245612431)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0245612431)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINDEX | BSF索引 | 可选必选说明：可选参数<br>参数含义：该参数用于描述BSF路由实例信息的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFBSFINDEXRT配置，可通过LST NRFBSFINDEXRT命令查询获取。 |
| DNN | 数据网络名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示数据网络名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数不区分大小写。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0245612431)

- 查询所有已配置的BSF索引和DNN的关联关系：
  ```
  LST NRFBSFDNNREL:;
  %%LST NRFBSFDNNREL:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  BSF索引 数据网络名称
  1       huawei.com
  2       huawei.cn
  (结果个数 = 2)
  ```
- 查询BSF索引为1，数据网络名称为huawei.com的关联关系：
  ```
  LST NRFBSFDNNREL: BSFINDEX=1, DNN="huawei.com";
  %%LST NRFBSFDNNREL: BSFINDEX=1, DNN="huawei.com";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
       BSF索引 = 1
  数据网络名称 = huawei.com
  (结果个数 = 1)
  ```

## [输出结果说明](#ZH-CN_MMLREF_0245612431)

| 输出项名称 | 输出项解释 |
| --- | --- |
| BSF索引 | 该参数用于描述BSF路由实例信息的索引值。 |
| 数据网络名称 | 该参数用于表示数据网络名称。 |
