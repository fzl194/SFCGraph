---
id: UNC@20.15.2@MMLCommand@RMV NRFBSFDNNREL
type: MMLCommand
name: RMV NRFBSFDNNREL（删除BSF索引和DNN的关联关系）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV NRFBSFDNNREL（删除BSF索引和DNN的关联关系）

## 功能

**适用NF：NRF**

该命令用于删除BSF索引和DNN的关联关系。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

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

运营商网络为三层网络，最高层PLMN-NRF，中间层H-NRF，最底层L-NRF。L-NRF1归属于H-NRF1，H-NRF1归属于PLMN-NRF。在H-NRF1和PLMN-NRF上分别执行如下命令，删除DNN为huawei.com对应的BSF路由的关联关系（对应DNN为huawei.com的BSF路由不再存在）：

```
RMV NRFBSFDNNREL: BSFINDEX=1, DNN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRFBSFDNNREL.md`
