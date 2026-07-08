---
id: UNC@20.15.2@MMLCommand@LST NRFDNNNIRT
type: MMLCommand
name: LST NRFDNNNIRT（查询DNN中网络标识最长后缀匹配转发路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFDNNNIRT
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
- DNN路由管理
status: active
---

# LST NRFDNNNIRT（查询DNN中网络标识最长后缀匹配转发路由）

## 功能

**适用NF：NRF**

该命令用于查询DNN中NI最长后缀匹配转发路由信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNNISUFFIX | DNN网络标识后缀 | 可选必选说明：可选参数<br>参数含义：该参数用于表示DNN网络标识后缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数不区分大小写。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于DNN的最长后缀匹配寻址NF时的下一跳NRF实例组名称，即被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示通过DNN中网络标识最长后缀匹配路由寻址的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL（适用于PCF、SMF、BSF类型）<br>- PCF（PCF）<br>- SMF（SMF）<br>- BSF（BSF）<br>默认值：无<br>配置原则：<br>ALL代表适用于PCF、SMF、BSF类型，当某个DNN的配置不区分NFType指向同一个下一跳NRF实例组时，可以配置ALL，节省配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFDNNNIRT]] · DNN中网络标识最长后缀匹配转发路由（NRFDNNNIRT）

## 使用实例

- 查询所有DNN中NI最长后缀匹配转发路由信息：
  ```
  LST NRFDNNNIRT:;
  %%LST NRFDNNNIRT:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  DNN网络标识后缀    归属NRF组名称    NF类型
  huawei.com         L-NRF1           适用于PCF、SMF、BSF类型
  huawei.com         H-NRF1           适用于PCF、SMF、BSF类型
  (结果个数 = 2)
  ```
- 查询DNN网络标识后缀为huawei.com，归属NRF组名称为L-NRF1的路由信息。
  ```
  LST NRFDNNNIRT: DNNNISUFFIX="huawei.com", NEXTNRFGRPNAME="L-NRF1", NFTYPE=ALL;
  %%LST NRFDNNNIRT: DNNNISUFFIX="huawei.com", NEXTNRFGRPNAME="L-NRF1", NFTYPE=ALL;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  DNN网络标识后缀  =  huawei.com
    归属NRF组名称  =  L-NRF1
           NF类型  =  适用于PCF、SMF、BSF类型
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNN中网络标识最长后缀匹配转发路由（LST-NRFDNNNIRT）_64343888.md`
