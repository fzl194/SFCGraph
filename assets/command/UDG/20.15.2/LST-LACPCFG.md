---
id: UDG@20.15.2@MMLCommand@LST LACPCFG
type: MMLCommand
name: LST LACPCFG（查询LACP配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LACPCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- LACP管理
status: active
---

# LST LACPCFG（查询LACP配置）

## 功能

该命令用来查询LACP配置。

## 注意事项

- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRUNKINDEX | Trunk的索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Trunk的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967294<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LACPCFG]] · LACP配置（LACPCFG）

## 使用实例

- 查询LACP配置：
  ```
  LST LACPCFG:;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  --------
  Trunk的索引  接口名称    LACP探测速率  LACP优先级  工作模式  

  17           Eth-Trunk1  快            32768       开启      
  18           Eth-Trunk2  快            32768       关闭      
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询LACP配置（LST-LACPCFG）_51971891.md`
