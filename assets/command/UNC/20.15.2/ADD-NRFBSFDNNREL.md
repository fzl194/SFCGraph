---
id: UNC@20.15.2@MMLCommand@ADD NRFBSFDNNREL
type: MMLCommand
name: ADD NRFBSFDNNREL（增加BSF索引和DNN的关联关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFBSFDNNREL
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- BSF路由管理
status: active
---

# ADD NRFBSFDNNREL（增加BSF索引和DNN的关联关系）

## 功能

**适用NF：NRF**

该命令用于新增BSF索引和DNN的关联关系。

该命令的使用场景为跨NRF对BSF进行寻址，基于特定DNN选择BSF的路由信息，其中BSF的路由需要通过ADD NRFBSFINDEXRT提前配置。

如果针对同一个BSFDNN配置了多个不同的BSF索引，那么当前NRF会选取符合条件的所有BSF索引对应NRF组中优先级最高的NRF。

此命令受到SET NRFFUNCSW命令中DNNNIMATCHSW开关控制。发现消息中DNN携带网络标识（NI）和操作标识符(OI)进行路由转发，当开关打开时，NRF优先精确匹配DNN的路由，如果未匹配到，再精确匹配DNN只包含NI的路由。当开关关闭时，NRF只能精确匹配DNN的路由。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINDEX | BSF索引 | 可选必选说明：必选参数<br>参数含义：该参数用于描述BSF路由实例信息的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFBSFINDEXRT配置，可通过LST NRFBSFINDEXRT命令查询获取。 |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示数据网络名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFBSFDNNREL]] · BSF索引和DNN的关联关系（NRFBSFDNNREL）

## 使用实例

- 运营商网络为三层组网，最高层PLMN-NRF，中间层H-NRF，最低层L-NRF。L-NRF1归属于H-NRF1，H-HRF1归属于PLMN-NRF。当跨NRF进行BSF服务发现时，基于DNN为huawei.com，则需要在H-NRF1和PLMN-NRF上分别配置如下路由信息。在H-NRF1上执行：
  ```
  ADD NRFBSFINDEXRT: BSFINDEX=1, NEXTNRFGRPNAME="L-NRF1";
  ADD NRFBSFDNNREL: BSFINDEX=1, DNN="huawei.com";
  ```
- 在PLMN-NRF上执行：
  ```
  ADD NRFBSFINDEXRT: BSFINDEX=1, NEXTNRFGRPNAME="H-NRF1";
  ADD NRFBSFDNNREL: BSFINDEX=1, DNN="huawei.com";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NRFBSFDNNREL.md`
