---
id: UNC@20.15.2@MMLCommand@RMV NGPAGINGTMRPLCY
type: MMLCommand
name: RMV NGPAGINGTMRPLCY（删除5G寻呼定时器策略配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGPAGINGTMRPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP接口寻呼管理
- NG寻呼定时器策略管理
status: active
---

# RMV NGPAGINGTMRPLCY（删除5G寻呼定时器策略配置）

## 功能

**适用NF：AMF**

该命令用于删除NG寻呼定时器策略配置数据。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLCYIDX | 策略索引 | 可选必选说明：必选参数<br>参数含义：该参数用于在AMF中唯一标识一条寻呼定时器策略。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPAGINGTMRPLCY]] · 5G寻呼定时器策略配置（NGPAGINGTMRPLCY）

## 使用实例

删除一条策略索引为1的NG寻呼定时器策略配置，执行如下命令：

```
RMV NGPAGINGTMRPLCY: PLCYIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGPAGINGTMRPLCY.md`
