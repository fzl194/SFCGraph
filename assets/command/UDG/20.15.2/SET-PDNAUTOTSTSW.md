---
id: UDG@20.15.2@MMLCommand@SET PDNAUTOTSTSW
type: MMLCommand
name: SET PDNAUTOTSTSW（设置PDN自动探测功能开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PDNAUTOTSTSW
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- 网络侧连通性检测
- PDN侧路由探测
status: active
---

# SET PDNAUTOTSTSW（设置PDN自动探测功能开关）

## 功能

**适用NF：PGW-U、UPF**

设置PDN自动探测功能开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH | DNSKPIFTSW | FAULTTRACERTSW |
| --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | PDN侧路由自动探测开关 | 可选必选说明：必选参数<br>参数含义：PDN侧自动探测开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| DNSKPIFTSW | DNS KPI故障自动探测开关 | 可选必选说明：可选参数<br>参数含义：DNS KPI故障自动探测开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：无 |
| FAULTTRACERTSW | 路径故障Tracert开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DNSKPIFTSW”配置为“ENABLE”时为可选参数。<br>参数含义：路径故障Tracert开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PDNAUTOTSTSW]] · PDN自动探测开关状态（PDNAUTOTSTSW）

## 使用实例

- 打开PDN自动探测功能开关：
  ```
  SET PDNAUTOTSTSW:SWITCH="ENABLE";
  ```
- 打开KPI异常检测开关：
  ```
  SET PDNAUTOTSTSW:SWITCH="ENABLE", DNSKPIFTSW="ENABLE";
  ```
- 打开路径故障自动探测开关：
  ```
  SET PDNAUTOTSTSW:SWITCH="ENABLE", FAULTTRACERTSW="ENABLE";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置PDN自动探测功能开关（SET-PDNAUTOTSTSW）_12635692.md`
