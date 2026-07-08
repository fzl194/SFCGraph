---
id: UNC@20.15.2@MMLCommand@RMV NRFIMSDNN
type: MMLCommand
name: RMV NRFIMSDNN（删除IMS PCF的DNN）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV NRFIMSDNN（删除IMS PCF的DNN）

## 功能

![](删除IMS PCF的DNN（RMV NRFIMSDNN）_96242888.assets/notice_3.0-zh-cn_2.png)

执行该命令后，NRF的号段防呆规则会过滤独立部署的语音PCF（该类PCF无号段），导致独立部署的语音PCF无法被服务发现，引起语音业务失败。若要删除，则需要明确独立部署的语音PCF不支持该DNN。

**适用NF：NRF**

如果运营商希望在NRF上删除IMS PCF的DNN信息，执行此命令。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示IMS PCF的数据网络名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。字符串类型，输入长度范围是0~64。该参数不区分大小写。<br>默认值：无<br>配置原则：<br>PCF支持的DNN等于或包含了配置的DNN信息，即认为该DNN在配置中已生效。<br>NRF上认为PCF是独立部署的条件是，PCF携带的DNN信息全部在NRF上已配置。<br>例如：<br>PCF规划支持ims.xa和ims.gz两个DNN：<br>当只配置一条“ims”记录时，NRF认为其是独立部署的；<br>当配置两条“ims.xa”和“ims.gz”记录时，NRF认为其是独立部署的；<br>当只配置一条“ims.xa”记录时，NRF认为其是非独立部署的。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFIMSDNN]] · IMS PCF的DNN（NRFIMSDNN）

## 使用实例

删除DNN信息为“huawei.com”的记录，在NRF上执行：

```
RMV NRFIMSDNN: DNN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRFIMSDNN.md`
