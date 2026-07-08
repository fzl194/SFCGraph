---
id: UNC@20.15.2@MMLCommand@LST NRFBSFDNNREL
type: MMLCommand
name: LST NRFBSFDNNREL（查询BSF索引和DNN的关联关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFBSFDNNREL
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- BSF路由管理
status: active
---

# LST NRFBSFDNNREL（查询BSF索引和DNN的关联关系）

## 功能

**适用NF：NRF**

该命令用于查询已配置的BSF索引和DNN的关联关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINDEX | BSF索引 | 可选必选说明：可选参数<br>参数含义：该参数用于描述BSF路由实例信息的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFBSFINDEXRT配置，可通过LST NRFBSFINDEXRT命令查询获取。 |
| DNN | 数据网络名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示数据网络名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [BSF索引和DNN的关联关系（NRFBSFDNNREL）](configobject/UNC/20.15.2/NRFBSFDNNREL.md)

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BSF索引和DNN的关联关系（LST-NRFBSFDNNREL）_45612431.md`
