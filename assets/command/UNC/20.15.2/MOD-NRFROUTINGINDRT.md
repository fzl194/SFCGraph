---
id: UNC@20.15.2@MMLCommand@MOD NRFROUTINGINDRT
type: MMLCommand
name: MOD NRFROUTINGINDRT（修改选路指示器路由）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NRFROUTINGINDRT
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
- 选路指示器路由管理
status: active
---

# MOD NRFROUTINGINDRT（修改选路指示器路由）

## 功能

**适用NF：NRF**

该命令用于修改指定选路指示器路由所归属的NRF实例组名称。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示在当前NRF上通过选路指示器路由寻址的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- UDM（UDM）<br>- AUSF（AUSF）<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为UDM、AUSF的路由转发功能，其他NF类型为预留功能。 |
| ROUTINGIND | 选路指示器 | 可选必选说明：必选参数<br>参数含义：该参数用于表示支持ROUTIINGIND号段信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~4。取值范围0~9999。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于NF实例组标识寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [选路指示器路由（NRFROUTINGINDRT）](configobject/UNC/20.15.2/NRFROUTINGINDRT.md)

## 使用实例

运营商网络规划变更，当前NRF上寻址选路指示器为“1111”的UDM下一跳路由发生变化，UDM所归属的NRF实例组名称由“L-NRF1”变为“L-NRF2”，需要执行：

```
MOD NRFROUTINGINDRT: NFTYPE=UDM, ROUTINGIND="1111", NEXTNRFGRPNAME="L-NRF2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改选路指示器路由（MOD-NRFROUTINGINDRT）_09652652.md`
