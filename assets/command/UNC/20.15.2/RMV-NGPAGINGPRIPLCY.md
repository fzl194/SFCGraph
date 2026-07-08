---
id: UNC@20.15.2@MMLCommand@RMV NGPAGINGPRIPLCY
type: MMLCommand
name: RMV NGPAGINGPRIPLCY（删除5G寻呼优先级策略参数配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGPAGINGPRIPLCY
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
- 寻呼优先级策略参数配置
status: active
---

# RMV NGPAGINGPRIPLCY（删除5G寻呼优先级策略参数配置）

## 功能

**适用NF：AMF**

该命令用于删除5G寻呼优先级策略配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLCYIDX | 策略索引 | 可选必选说明：必选参数<br>参数含义：该参数用于在AMF内唯一标识一条寻呼优先级策略。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G寻呼优先级策略参数配置（NGPAGINGPRIPLCY）](configobject/UNC/20.15.2/NGPAGINGPRIPLCY.md)

## 使用实例

将策略索引为1的5G寻呼优先级配置删除，执行如下命令：

```
RMV NGPAGINGPRIPLCY: PLCYIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5G寻呼优先级策略参数配置（RMV-NGPAGINGPRIPLCY）_09652645.md`
