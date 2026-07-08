---
id: UNC@20.15.2@MMLCommand@RMV CCPFOT
type: MMLCommand
name: RMV CCPFOT（删除融合计费Proxy Failover模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CCPFOT
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 融合计费Proxy Failover模板
status: active
---

# RMV CCPFOT（删除融合计费Proxy Failover模板）

## 功能

![](删除融合计费Proxy Failover模板（RMV CCPFOT）_45110929.assets/notice_3.0-zh-cn_2.png)

该命令用于删除融合计费模板标识。若删除可能导致NCG代应答时不携带默认流量或处理相应异常返回码时不按预期规则向OCS进行重新发现或不按预期向SMF代应答。

**适用NF：NCG**

该命令用于删除融合计费Proxy Failover模板。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FOTNM | Failover模板标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定融合计费Proxy Failover模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CCPFOT]] · 融合计费Proxy Failover模板（CCPFOT）

## 使用实例

删除Failover模板标识名称为“ccpfot1”的融合计费Proxy Failover模板：

```
RMV CCPFOT: FOTNM="ccpfot1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CCPFOT.md`
