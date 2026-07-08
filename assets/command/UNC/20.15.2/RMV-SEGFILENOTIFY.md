---
id: UNC@20.15.2@MMLCommand@RMV SEGFILENOTIFY
type: MMLCommand
name: RMV SEGFILENOTIFY（删除号段文件通知记录）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SEGFILENOTIFY
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- 号段导入通知管理
status: active
---

# RMV SEGFILENOTIFY（删除号段文件通知记录）

## 功能

![](删除号段文件通知记录（RMV SEGFILENOTIFY）_50738961.assets/notice_3.0-zh-cn_2.png)

该操作会触发订阅通知，导致后续号段导入通知记录与预期不符。

**适用NF：NRF**

该命令用于在NRF上通过手动删除NF对应的IMSI/MSISDN号段信息达到NF号段更新，触发订阅通知。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活两个NRF上均需执行此命令，配置参数值参考实际规划。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示支持IMSI/MSISDN号段支持的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>默认值：无<br>配置原则：<br>支持IMSI号段配置的NF类型仅包含AUSF、PCF、UDM、 UDR、CHF、CUSTOM_OCS。支持MSISDN号段配置的NF类型仅包含PCF、UDM、 UDR、CHF、CUSTOM_OCS。 |
| SEGTYPE | 号段类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>默认值：无<br>配置原则：无 |
| NFGROUPID | NF组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示待配置IMSI/MSISDN号段的NF组标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [号段文件通知记录（SEGFILENOTIFY）](configobject/UNC/20.15.2/SEGFILENOTIFY.md)

## 使用实例

在NRF上手动触发删除CHF类型的NF组标识为nfgroup001的IMSI号段信息的订阅通知。

```
RMV SEGFILENOTIFY: SEGTYPE=IMSI, NFTYPE=CHF, NFGROUPID="nfgroup001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除号段文件通知记录（RMV-SEGFILENOTIFY）_50738961.md`
