---
id: UNC@20.15.2@MMLCommand@LST QOSACTRDRPOLICY
type: MMLCommand
name: LST QOSACTRDRPOLICY（查询流行为下级联流策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSACTRDRPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 级联流策略动作
status: active
---

# LST QOSACTRDRPOLICY（查询流行为下级联流策略）

## 功能

该命令用于查询级联流策略，可以输入过滤“行为名称”或“策略名称”，过滤结果。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 行为名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流行为的名称，不允许为系统预定义策略default。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| POLICYNAME | 策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流策略的名称，不允许为系统预定义策略default。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSACTRDRPOLICY]] · 流行为下级联流策略（QOSACTRDRPOLICY）

## 使用实例

查询流行为下级联流策略：

```
LST QOSACTRDRPOLICY:BEHAVIORNAME="a";
```

```
RETCODE = 0 操作成功

结果如下
-------------------------
行为名称 = a
策略名称 = a
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询流行为下级联流策略（LST-QOSACTRDRPOLICY）_00441345.md`
