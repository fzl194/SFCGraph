---
id: UNC@20.15.2@MMLCommand@ADD NRFIMSDNN
type: MMLCommand
name: ADD NRFIMSDNN（增加IMS PCF的DNN）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFIMSDNN
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- IMS PCF的DNN信息管理
status: active
---

# ADD NRFIMSDNN（增加IMS PCF的DNN）

## 功能

**适用NF：NRF**

该命令用于配置IMS PCF支持的DNN信息。

独立部署的IMS PCF无号段信息（注册、配置和导入都无号段），即支持所有的号段。该PCF需使用此命令配置其支持的DNN，从而NRF认为PCF是独立部署的，可以正常处理业务。

如果不配置此命令，NRF可能会认为此PCF不是独立部署，没有支持的号段信息，从而屏蔽此PCF不被其他NF发现或检索以及在发生变更时通知已订阅的NF，并上报“ALM-100249 号段类NF无号段告警”，影响PCF的正常业务处理。NRF的上述判断通过SET NRFFUNCSW命令中NFNOSEGALARMSW开关控制。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入64条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DNN |
| --- |
| ims |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示IMS PCF的数据网络名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。字符串类型，输入长度范围是0~64。该参数不区分大小写。<br>默认值：无<br>配置原则：<br>PCF支持的DNN等于或包含了配置的DNN信息，即认为该DNN在配置中已生效。<br>NRF上认为PCF是独立部署的条件是，PCF携带的DNN信息全部在NRF上已配置。<br>例如：<br>PCF规划支持ims.xa和ims.gz两个DNN：<br>当只配置一条“ims”记录时，NRF认为其是独立部署的；<br>当配置两条“ims.xa”和“ims.gz”记录时，NRF认为其是独立部署的；<br>当只配置一条“ims.xa”记录时，NRF认为其是非独立部署的。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFIMSDNN]] · IMS PCF的DNN（NRFIMSDNN）

## 使用实例

运营商规划IMS PCF用来进行IMS业务，此PCF是支持所有号段信息，为了避免NRF误判此PCF未进行号段配置，从而屏蔽该PCF不被使用，需要执行此命令，保证PCF的正常业务。在NRF上执行：

```
ADD NRFIMSDNN: DNN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IMS-PCF的DNN（ADD-NRFIMSDNN）_96241770.md`
