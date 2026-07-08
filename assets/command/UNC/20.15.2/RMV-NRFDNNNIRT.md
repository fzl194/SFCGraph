---
id: UNC@20.15.2@MMLCommand@RMV NRFDNNNIRT
type: MMLCommand
name: RMV NRFDNNNIRT（删除DNN中网络标识最长后缀匹配转发路由）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFDNNNIRT
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

# RMV NRFDNNNIRT（删除DNN中网络标识最长后缀匹配转发路由）

## 功能

**适用NF：NRF**

该命令用于删除DNN中NI最长后缀匹配转发路由信息。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNNISUFFIX | DNN网络标识后缀 | 可选必选说明：必选参数<br>参数含义：该参数用于表示DNN网络标识后缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数不区分大小写。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示当前NRF基于DNN的最长后缀匹配寻址NF时的下一跳NRF实例组名称，即被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示通过DNN中网络标识最长后缀匹配路由寻址的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL（适用于PCF、SMF、BSF类型）<br>- PCF（PCF）<br>- SMF（SMF）<br>- BSF（BSF）<br>默认值：ALL<br>配置原则：<br>ALL代表适用于PCF、SMF、BSF类型，当某个DNN的配置不区分NFType指向同一个下一跳NRF实例组时，可以配置ALL，节省配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFDNNNIRT]] · DNN中网络标识最长后缀匹配转发路由（NRFDNNNIRT）

## 使用实例

运营商网络为三层网络，最高层PLMN-NRF，中间层H-NRF，最底层L-NRF。L-NRF1归属于H-NRF1，H-NRF1归属于PLMN-NRF。在H-NRF1和PLMN-NRF上分别执行如下命令，删除DNN网络标识后缀为huawei.com对应的路由信息：

```
RMV NRFDNNNIRT: DNNNISUFFIX="huawei.com", NEXTNRFGRPNAME="H-NRF1", NFTYPE=ALL;
RMV NRFDNNNIRT: DNNNISUFFIX="huawei.com", NEXTNRFGRPNAME="L-NRF1", NFTYPE=ALL;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRFDNNNIRT.md`
