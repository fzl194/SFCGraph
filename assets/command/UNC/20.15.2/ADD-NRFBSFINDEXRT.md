---
id: UNC@20.15.2@MMLCommand@ADD NRFBSFINDEXRT
type: MMLCommand
name: ADD NRFBSFINDEXRT（增加BSFINDEX路由）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFBSFINDEXRT
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

# ADD NRFBSFINDEXRT（增加BSFINDEX路由）

## 功能

**适用NF：NRF**

跨NRF的NF查询，当基于不同属性选择NF时，需要在NRF（多层NRF组网中的H-NRF或PLMN-NRF，单层NRF组网中存在东西向NRF的NRF）上配置下一跳路由，以便NRF能够寻址到其下一级NRF上所管理的NF。

该命令用于新增选择BSF时的路由实例信息。当跨NRF对BSF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标BSF所归属的NRF。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINDEX | BSF索引 | 可选必选说明：必选参数<br>参数含义：该参数用于表示BSF路由实例信息的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示当前NRF基于BSF类型寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFBSFINDEXRT]] · BSFINDEX路由（NRFBSFINDEXRT）

## 使用实例

在H-NRF1上新增BSF索引为1时对应的下一跳路由：

```
ADD NRFBSFINDEXRT: BSFINDEX=1, NEXTNRFGRPNAME="L-NRF1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NRFBSFINDEXRT.md`
