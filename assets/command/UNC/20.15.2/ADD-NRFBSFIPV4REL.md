---
id: UNC@20.15.2@MMLCommand@ADD NRFBSFIPV4REL
type: MMLCommand
name: ADD NRFBSFIPV4REL（增加BSF索引和IPv4的关联关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFBSFIPV4REL
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

# ADD NRFBSFIPV4REL（增加BSF索引和IPv4的关联关系）

## 功能

**适用NF：NRF**

该命令用于新增BSF索引和IPv4的关联关系。

该命令的使用场景为跨NRF对BSF进行寻址，基于特定IPv4选择BSF的路由信息，其中BSF的路由需要通过ADD NRFBSFINDEXRT提前配置。

如果针对同一个IPV4配置了多个不同的BSF索引，那么当前NRF会选取符合条件的所有BSF索引对应NRF组中优先级最高的NRF。

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
| START | IP起始地址 | 可选必选说明：必选参数<br>参数含义：该参数用于表示下一跳路由组支持的IPv4起始地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>IPv4地址不能为组播地址（224.x.y.z）和环回地址(127.x.y.z)。<br>IPv4地址必须是A、B或者C类地址。 |
| END | IP结束地址 | 可选必选说明：必选参数<br>参数含义：该参数用于表示下一跳路由组支持的IPv4结束地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>IPv4地址不能为组播地址（224.x.y.z）和环回地址(127.x.y.z)。<br>IPv4地址必须是A、B或者C类地址。 |

## 操作的配置对象

- [BSF索引和IPv4的关联关系（NRFBSFIPV4REL）](configobject/UNC/20.15.2/NRFBSFIPV4REL.md)

## 使用实例

- 运营商网络为三层组网，最高层PLMN-NRF，中间层H-NRF，最低层L-NRF。L-NRF1归属于H-NRF1，H-HRF1归属于PLMN-NRF。当跨NRF进行BSF服务发现时，基于IPv4地址范围为192.168.10.12~192.168.20.12，需要在H-NRF1和PLMN-NRF上分别配置到如下路由信息。 在H-NRF1上执行：
  ```
  ADD NRFBSFINDEXRT: BSFINDEX=1, NEXTNRFGRPNAME="L-NRF1";
  ADD NRFBSFIPV4REL: BSFINDEX=1, START="192.168.10.12", END="192.168.20.12";
  ```
- 在PLMN-NRF上执行：
  ```
  ADD NRFBSFINDEXRT: BSFINDEX=1, NEXTNRFGRPNAME="H-NRF1";
  ADD NRFBSFIPV4REL: BSFINDEX=1, START="192.168.10.12", END="192.168.20.12";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加BSF索引和IPv4的关联关系（ADD-NRFBSFIPV4REL）_45612408.md`
