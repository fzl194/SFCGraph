---
id: UDG@20.15.2@MMLCommand@SET UPCHGCHKPARA
type: MMLCommand
name: SET UPCHGCHKPARA（设置计费检查参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UPCHGCHKPARA
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 用户面计费检查参数
status: active
---

# SET UPCHGCHKPARA（设置计费检查参数）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

用于设置用户面计费检查相关参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | USRRESALMSW | VOLCHKALMSW | VOLCHKALMTH | VOLCHKALMRSTTH |
| --- | --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | 500 | 300 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRRESALMSW | 用户资源告警开关 | 可选必选说明：可选参数<br>参数含义：控制单用户计费资源使用超规格是否上报告警。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| VOLCHKALMSW | 流量核查告警开关 | 可选必选说明：可选参数<br>参数含义：计费流量核查不一致时是否上报告警。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| VOLCHKALMTH | 流量核查告警上报阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“VOLCHKALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：配置流量不一致告警上报阈值，单位为1/10000。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1~10000，单位1/10000。<br>默认值：无<br>配置原则：无 |
| VOLCHKALMRSTTH | 流量核查告警恢复阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“VOLCHKALMSW”配置为“ENABLE”时为可选参数。<br>参数含义：配置流量不一致告警恢复阈值，单位为1/10000。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~10000，单位为万分比。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPCHGCHKPARA]] · 计费检查参数（UPCHGCHKPARA）

## 使用实例

- 使用SET UPCHGCHKPARA命令开启单用户资源超规格告警功能：
  ```
  SET UPCHGCHKPARA: USRRESALMSW=ENABLE;
  ```
- 使用SET UPCHGCHKPARA命令关闭单用户资源超规格告警功能：
  ```
  SET UPCHGCHKPARA: USRRESALMSW=DISABLE;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-UPCHGCHKPARA.md`
