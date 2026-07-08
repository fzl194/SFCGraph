---
id: UDG@20.15.2@MMLCommand@SET GTSM
type: MMLCommand
name: SET GTSM（设置GTSM全局配置属性）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GTSM
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- GTSM
status: active
---

# SET GTSM（设置GTSM全局配置属性）

## 功能

该命令用于设置GTSM全局属性。

GTSM（Generalized TTL Security Mechanism），即通用TTL安全保护机制。GTSM通过检查IP报文头中的TTL值是否在一个预先定义好的范围内，对IP层以上业务进行保护。在实际应用中，用于保护建立在TCP/IP基础上的控制层面（路由协议等）免受CPU利用（CPU-utilization）类型的攻击，如CPU过载（CPU overload）。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| ACTION |
| --- |
| PASS |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACTION | 动作行为 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTSM动作行为。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DROP：丢弃。<br>- PASS：通过。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GTSM]] · GTSM全局配置属性（GTSM）

## 使用实例

设置GTSM全局属性：

```
SET GTSM:ACTION=DROP;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-GTSM.md`
