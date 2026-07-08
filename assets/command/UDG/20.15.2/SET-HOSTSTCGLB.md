---
id: UDG@20.15.2@MMLCommand@SET HOSTSTCGLB
type: MMLCommand
name: SET HOSTSTCGLB（设置全局协议报文统计配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: HOSTSTCGLB
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- 主机报文统计
- 统计功能配置
status: active
---

# SET HOSTSTCGLB（设置全局协议报文统计配置）

## 功能

该命令用于设置全局协议报文统计配置。

该命令的优先级低于ADD HOSTSTCIF命令，如果接口上配置了接口协议报文统计配置，则对应接口的协议报文统计功能不受该命令的影响。

## 注意事项

- 该命令执行后立即生效。
- 该配置会影响设备性能。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| STCENABLE |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STCENABLE | 协议报文统计功能状态 | 可选必选说明：必选参数<br>参数含义：该参数用于表示协议报文统计功能状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：去使能协议报文统计功能。<br>- ENABLE：使能协议报文统计功能。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HOSTSTCGLB]] · 全局协议报文统计配置（HOSTSTCGLB）

## 使用实例

- 使能全局协议报文统计：
  ```
  SET HOSTSTCGLB: STCENABLE=ENABLE;
  ```
- 去使能全局协议报文统计：
  ```
  SET HOSTSTCGLB: STCENABLE=DISABLE;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置全局协议报文统计配置（SET-HOSTSTCGLB）_00441557.md`
