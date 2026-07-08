---
id: UDG@20.15.2@MMLCommand@RTR FLOWAGETIME
type: MMLCommand
name: RTR FLOWAGETIME（恢复五元组老化时间）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: FLOWAGETIME
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务五元组管理
- 五元组节点老化时间
status: active
---

# RTR FLOWAGETIME（恢复五元组老化时间）

## 功能

**适用NF：PGW-U、UPF**

该命令用来恢复头增强五元组、三四层五元组、TCP信令五元组和任意协议五元组的老化时间初始设置值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RMVTYPE | 五元组老化时间删除类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定五元组老化时间删除类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ANY_PROTOCOL：恢复任意协议五元组老化时间的初始设置值。<br>- L34_PROTOCOL：恢复三四层五元组老化时间的初始设置值。<br>- TCP_SIGNALING：恢复TCP信令五元组老化时间的初始设置值。<br>- HEAD_ENRICH：恢复头增强五元组老化时间的初始设置值。<br>- TRAFF_CLASS：恢复流量分类五元组老化时间的初始设置值。<br>- LBO：恢复LBO业务五元组老化时间的初始设置值，此参数当前不支持。<br>默认值：无<br>配置原则：如果不设置五元组老化时间删除类型，则恢复所有类型的五元组老化时间的初始设置值。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FLOWAGETIME]] · 五元组老化时间（FLOWAGETIME）

## 使用实例

- 假如运营商需要恢复五元组老化时间的初始设置值：
  ```
  RTR FLOWAGETIME:;
  ```
- 假如运营商需要恢复三四层五元组老化时间的初始设置值：
  ```
  RTR FLOWAGETIME: RMVTYPE=L34_PROTOCOL;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复五元组老化时间（RTR-FLOWAGETIME）_82837292.md`
