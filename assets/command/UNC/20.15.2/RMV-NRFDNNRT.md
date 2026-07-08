---
id: UNC@20.15.2@MMLCommand@RMV NRFDNNRT
type: MMLCommand
name: RMV NRFDNNRT（删除DNN路由）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFDNNRT
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
- DNN路由管理
status: active
---

# RMV NRFDNNRT（删除DNN路由）

## 功能

**适用NF：NRF**

该命令用于删除目标DNN信息对应的某条路由或所有路由。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示数据网络名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数不区分大小写。<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为PCF的路由转发功能，其他NF类型为预留功能。 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于DNN寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [DNN路由（NRFDNNRT）](configobject/UNC/20.15.2/NRFDNNRT.md)

## 使用实例

运营商网络为三层组网，最高层PLMN-NRF，中间层H-NRF，最低层L-NRF。L-NRF1归属于H-NRF1，H-HRF1归属于PLMN-NRF。在H-NRF1和PLMN-NRF上分别执行如下命令，删除DNN为huawei.com的路由信息。

```
RMV NRFDNNRT: DNN="huawei.com", NEXTNRFGRPNAME="L-NRF1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DNN路由（RMV-NRFDNNRT）_09653721.md`
