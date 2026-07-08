---
id: UNC@20.15.2@MMLCommand@RMV NRFAMFREGIDRT
type: MMLCommand
name: RMV NRFAMFREGIDRT（删除AMF区域标识路由）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFAMFREGIDRT
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
- AMF区域标识路由管理
status: active
---

# RMV NRFAMFREGIDRT（删除AMF区域标识路由）

## 功能

**适用NF：NRF**

该命令用于删除目标AMF的区域标识路由信息。

## 注意事项

- 立即生效

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AMFREGID | AMF区域标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示AMF区域标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。按照十六进制输入，输入时不带0x，不足两位时从左边补0，取值范围0~ff。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFAMFREGIDRT]] · AMF区域标识路由（NRFAMFREGIDRT）

## 使用实例

运营商网络为三层网络，最高层PLMN-NRF，中间层H-NRF，最底层L-NRF。L-NRF1归属于H-NRF1，H-NRF1归属于PLMN-NRF。 在H-NRF1和PLMN-NRF上分别执行如下命令，删除AMF区域标识为09的路由信息。

```
RMV NRFAMFREGIDRT:AMFREGID="09";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除AMF区域标识路由（RMV-NRFAMFREGIDRT）_09651548.md`
