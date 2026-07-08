---
id: UDG@20.15.2@MMLCommand@ADD SFELOADALARM
type: MMLCommand
name: ADD SFELOADALARM（设置转发过载告警参数）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SFELOADALARM
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP性能配置
- IP转发过载告警参数配置
status: active
---

# ADD SFELOADALARM（设置转发过载告警参数）

## 功能

该命令用于添加转发过载告警参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OVERLOADTYPE | 过载类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示转发过载告警的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- queue：队列告警。<br>默认值：无 |
| TRIGTHRESHOLD | 触发阈值（%） | 可选必选说明：必选参数<br>参数含义：该参数用于表示触发转发过载告警的阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2～99。<br>默认值：无 |
| RESUMTHRESHOLD | 恢复阈值（%） | 可选必选说明：必选参数<br>参数含义：该参数用于表示转发过载告警的恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～98。<br>默认值：无 |
| CHECKINTERVAL | 检测间隔（ms） | 可选必选说明：必选参数<br>参数含义：该参数用于表示转发过载告警的检测间隔，单位为ms。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1000～4294967295。<br>默认值：无 |
| CHECKTIMES | 检测次数 | 可选必选说明：必选参数<br>参数含义：该参数用于表示转发过载告警的检测次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFELOADALARM]] · 组件侧转发过载告警参数（SFELOADALARM）

## 使用实例

添加转发过载告警参数：

```
ADD SFELOADALARM:OVERLOADTYPE=queue,TRIGTHRESHOLD=92,RESUMTHRESHOLD=60,CHECKINTERVAL=2000,CHECKTIMES=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-SFELOADALARM.md`
