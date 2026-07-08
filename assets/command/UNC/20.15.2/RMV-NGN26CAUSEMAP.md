---
id: UNC@20.15.2@MMLCommand@RMV NGN26CAUSEMAP
type: MMLCommand
name: RMV NGN26CAUSEMAP（删除5G N26接口原因值映射配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGN26CAUSEMAP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM流程管理
- 5G N26接口原因值映射配置
status: active
---

# RMV NGN26CAUSEMAP（删除5G N26接口原因值映射配置）

## 功能

**适用NF：AMF**

该命令用于删除5G N26接口原因值映射配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROT | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程类型，根据场景来确认是否需要配置相应的流程。<br>数据来源：全网规划<br>取值范围：<br>- LTE_TO_NR_HO（EPC到5GC切换）<br>- NR_TO_LTE_ATTACH（5GS到LTE附着）<br>- NR_TO_LTE_TAU（5GS到LTE TAU）<br>- ALL（所有的失败流程）<br>- RESERV_PROC1（预留字段1）<br>- RESERV_PROC2（预留字段2）<br>默认值：无<br>配置原则：<br>指定流程和“ALL”类型同时配置时，指定流程配置的原因值映射优先级高于“ALL”类型配置的原因值映射。 |
| SCAUSE | 原始原因值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定下发到MME的原始原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGN26CAUSEMAP]] · 5G N26接口原因值映射配置（NGN26CAUSEMAP）

## 使用实例

删除流程类型为5GS到LTE附着，原始原因值为96的5G N26接口原因值映射配置，执行如下命令：

```
RMV NGN26CAUSEMAP:PROT=NR_TO_LTE_ATTACH,SCAUSE=96;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGN26CAUSEMAP.md`
