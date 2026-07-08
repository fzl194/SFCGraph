---
id: UNC@20.15.2@MMLCommand@RMV ALLOWEDNFTYPES
type: MMLCommand
name: RMV ALLOWEDNFTYPES（删除允许访问的NF类型）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ALLOWEDNFTYPES
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- 访问授权控制
- NF类型访问授权控制
status: active
---

# RMV ALLOWEDNFTYPES（删除允许访问的NF类型）

## 功能

**适用NF：NRF**

该命令用于删除指定NF对象所允许访问的NF类型。

当某个NF不再通过NRF限制特定NF类型的NF访问，可以通过此命令删除允许访问的NF类型。

## 注意事项

- 该命令执行后并不会立即生效，需要执行CMT ALLOWPLCY命令生效。

- 当所有允许访问属性被删除后，表示针对此对象在NRF上的设置是可以被任何NF类型的NF实例访问。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJNAME | 授权对象名称 | 可选必选说明：必选参数<br>参数含义：该参数表示设置访问授权控制的NF对象名称。该参数通过LST ALLOWEDOBJNAME命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |
| ALLOWEDNFTYPE | 允许访问该对象的NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示指定NF对象允许访问的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NRF（NRF）<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- NEF（NEF）<br>- PCF（PCF）<br>- SMSF（SMSF）<br>- NSSF（NSSF）<br>- UDR（UDR）<br>- LMF（LMF）<br>- GMLC（GMLC）<br>- EIR_5G（EIR_5G）<br>- SEPP（SEPP）<br>- UPF（UPF）<br>- N3IWF（N3IWF）<br>- AF（AF）<br>- UDSF（UDSF）<br>- BSF（BSF）<br>- CHF（CHF）<br>- NWDAF（NWDAF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SCP（SCP）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [允许访问的NF类型（ALLOWEDNFTYPES）](configobject/UNC/20.15.2/ALLOWEDNFTYPES.md)

## 使用实例

授权对象objname001可以被多个NF类型访问，NF类型中包含NRF。运营商根据需要，不允许NRF继续访问objname001时，执行下面命令：

```
RMV ALLOWEDNFTYPES: OBJNAME="objname001", ALLOWEDNFTYPE=NRF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除允许访问的NF类型（RMV-ALLOWEDNFTYPES）_09653196.md`
