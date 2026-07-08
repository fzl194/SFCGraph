---
id: UDG@20.15.2@MMLCommand@SET SAAITRAINPARA
type: MMLCommand
name: SET SAAITRAINPARA（配置基于SA的Intelligence训练参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SAAITRAINPARA
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 1
category_path:
- SAPO服务管理
- SAPO训练参数
status: active
---

# SET SAAITRAINPARA（配置基于SA的Intelligence训练参数）

## 功能

**适用NF：UPF**

该命令用于配置基于SA的Intelligence训练参数。

## 注意事项

- 参数AITRAINSWITCH和AITRAINSAMPLE修改60秒后对新激活用户生效。参数AITRAINTHRES、AITRAINPERIOD和AIDBVALIDTIME修改后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | AITRAINTHRES | AITRAINSWITCH | AITRAINPERIOD | AITRAINSAMPLE | AIDBVALIDTIME |
| --- | --- | --- | --- | --- | --- |
| 初始值 | 9900 | DISABLE | 30 | 0 | 300 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AITRAINTHRES | Intelligence训练阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于配置intelligence训练任务中有效学习记录的流量阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围5000~10000，单位是万分比。<br>默认值：无<br>配置原则：无 |
| AITRAINSWITCH | Intelligence训练开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置intelligence训练功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：Intelligence训练功能关闭。<br>- ENABLE：Intelligence训练功能开启。<br>默认值：无<br>配置原则：使能intelligence能耗优化功能，需要打开AI训练功能开关。 |
| AITRAINPERIOD | Intelligence训练周期（分钟） | 可选必选说明：可选参数<br>参数含义：该参数用于配置intelligence训练任务的周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围10~180，单位是分钟。<br>默认值：无<br>配置原则：该参数修改后会影响SA性能优化库生效时长。生效时长=intelligence训练周期 *SA性能优化库有效时间。参数值改小后，SA性能优化库可能从生效状态变为失效状态；参数值改大后，SA性能优化库可能从失效状态变为生效状态。 |
| AITRAINSAMPLE | Intelligence训练抽样率 | 可选必选说明：可选参数<br>参数含义：该参数用于配置intelligence训练任务订阅流量的抽样率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0~10000，单位是万分比。<br>默认值：无<br>配置原则：该值如果配置过大会降低intelligence能耗优化流量比例，影响优化效果；如果配置过小，可能导致训练结果不准确。建议配置为100～500。 |
| AIDBVALIDTIME | SA性能优化库有效时间 | 可选必选说明：可选参数<br>参数含义：该参数用于配置训练生成的SA性能优化库有效时间相对于训练周期的倍数。<br>数据来源：本端规划<br>取值范围：数值类型，输入长度范围为2～65535。<br>默认值：无<br>配置原则：该参数修改后会影响SA性能优化库生效时长。生效时长=intelligence训练周期 * SA性能优化库有效时间。参数值改小后，SA性能优化库可能从生效状态变为失效状态；参数值改大后，SA性能优化库可能从失效状态变为生效状态。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SAAITRAINPARA]] · 基于SA的Intelligence训练参数（SAAITRAINPARA）

## 使用实例

如果希望配置intelligence训练开关等于ENABLE，intelligence训练阈值等于99%，intelligence训练周期等于15分钟，intelligence训练抽样率等于10%，则可以执行以下设置：

```
SET SAAITRAINPARA: AITRAINTHRES=9900, AITRAINSWITCH=ENABLE, AITRAINPERIOD=15, AITRAINSAMPLE=1000;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SAAITRAINPARA.md`
