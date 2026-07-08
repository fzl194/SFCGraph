---
id: UDG@20.15.2@MMLCommand@SET TOPLYPRIORITY
type: MMLCommand
name: SET TOPLYPRIORITY（设置TCP优化策略组合优先级）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TOPLYPRIORITY
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 7
category_path:
- TCP优化服务管理
- TCP优化策略优先级
status: active
---

# SET TOPLYPRIORITY（设置TCP优化策略组合优先级）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置TCP优化策略组合优先级。当运营商希望修改当前TCP优化策略组合优先级时，则配置该命令。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为7。
- 不同配置类型的优先级建议设置为不同值。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | COMBTYPE | PRIORITY |
| --- | --- | --- |
| 初始值 | TO_MATCH_IMSI | 10 |
| 初始值 | TO_MATCH_CELL | 20 |
| 初始值 | TO_MATCH_RAT | 30 |
| 初始值 | TO_MATCH_RAT_IMSI | 40 |
| 初始值 | TO_MATCH_CELL_IMSI | 50 |
| 初始值 | TO_MATCH_RAT_CELL | 60 |
| 初始值 | TO_MATCH_ALL | 70 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COMBTYPE | TCP优化策略组合类型 | 可选必选说明：可选参数<br>参数含义：用于指定TCP优化策略组合类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TO_MATCH_IMSI：仅匹配IMSIGroupName。<br>- TO_MATCH_CELL：仅匹配CellGroupName。<br>- TO_MATCH_RAT：仅匹配RATtype。<br>- TO_MATCH_RAT_IMSI：仅匹配RATtype和IMSIGroupName。<br>- TO_MATCH_CELL_IMSI：仅匹配CellGroupName和IMSIGroupName。<br>- TO_MATCH_RAT_CELL：仅匹配RATtype和CellGroupName。<br>- TO_MATCH_ALL：RATtype，CellGroupName和IMSIGroupName均需要匹配中。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：用于设置指定TCP优化策略组合优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1～255，数值越大优先级越高。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOPLYPRIORITY]] · TCP优化策略组合优先级（TOPLYPRIORITY）

## 使用实例

运营商需要设置TCP优化策略组合为RATtype和IMSIGroupName的优先级为100：

```
SET TOPLYPRIORITY: COMBTYPE=TO_MATCH_RAT_IMSI,PRIORITY =100;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置TCP优化策略组合优先级（SET-TOPLYPRIORITY）_87336172.md`
