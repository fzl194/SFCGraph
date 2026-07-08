---
id: UNC@20.15.2@MMLCommand@ADD NRFGROUP
type: MMLCommand
name: ADD NRFGROUP（增加对端NRF实例组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFGROUP
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF拓扑配置
- NRF实例组管理
status: active
---

# ADD NRFGROUP（增加对端NRF实例组）

## 功能

**适用NF：NRF**

运营商希望新增对端NRF实例组时可使用此命令。需要多个NRF互通时，NRF之间要配置各自的对端NRF实例组信息，对端NRF实例组是一个或多个对端NRF实例的集合，用于容灾或负荷分担。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入10240条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | 实例组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示对端NRF实例组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |
| GROUPATTR | 实例组属性 | 可选必选说明：必选参数<br>参数含义：该参数用于表示对端NRF实例组属性。<br>数据来源：全网规划<br>取值范围：<br>- SNRF（东西向NRF组）<br>- HNRF（北向NRF组）<br>- LNRF（南向NRF组）<br>- SNRF_PLMN（跨PLMN NRF组）<br>- SELFNRF（本NRF组）<br>- INRF_PLMN（本PLMN国际漫游关口局NRF组）<br>默认值：无<br>配置原则：无 |
| FWDMODE | 转发模式 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NRF之间的消息转发模式，缺省为递归转发模式。<br>数据来源：全网规划<br>取值范围：<br>- “ITERATION（迭代转发）”：迭代转发模式。<br>- “RECURSION（递归转发）”：递归转发模式。<br>默认值：无<br>配置原则：<br>NRF组属性为北向NRF组/跨PLMN NRF组时，转发模式不允许设置为迭代模式。 |
| GROUPDESC | 实例组描述 | 可选必选说明：可选参数<br>参数含义：该参数用于表示对端NRF实例组描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFGROUP]] · 对端NRF实例组（NRFGROUP）

## 使用实例

当前NRF有南向对端NRF需要配置，且该南向对端NRF名称配置为nrfgroup001时，配置此命令。

```
ADD NRFGROUP: GROUPNAME="nrfgroup001", GROUPATTR=LNRF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加对端NRF实例组（ADD-NRFGROUP）_09653179.md`
