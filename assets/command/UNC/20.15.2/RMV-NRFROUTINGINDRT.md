---
id: UNC@20.15.2@MMLCommand@RMV NRFROUTINGINDRT
type: MMLCommand
name: RMV NRFROUTINGINDRT（删除选路指示器路由）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV NRFROUTINGINDRT（删除选路指示器路由）

## 功能

**适用NF：NRF**

该命令用于删除指定NF类型的选路指示器路由信息。

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

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFROUTINGINDRT]] · 选路指示器路由（NRFROUTINGINDRT）

## 使用实例

运营商网络为三层组网，最高层PLMN-NRF，中间层H-NRF，最低层L-NRF。L-NRF1归属于H-NRF1，H-HRF1归属于PLMN-NRF。在H-NRF1和PLMN-NRF上分别执行如下命令，删除NF类型为“UDM”，选路指示器为“1111”的路由信息。

```
RMV NRFROUTINGINDRT: NFTYPE=UDM, ROUTINGIND="1111";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRFROUTINGINDRT.md`
