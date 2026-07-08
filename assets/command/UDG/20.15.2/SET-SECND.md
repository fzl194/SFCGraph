---
id: UDG@20.15.2@MMLCommand@SET SECND
type: MMLCommand
name: SET SECND（设置ND快回配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SECND
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略ND
status: active
---

# SET SECND（设置ND快回配置）

## 功能

该命令用来设置ND快回使能配置。

大量客户端发送ND请求报文会造成CPU负载过高。为了降低CPU负载，可通过配置此命令，使设备接收到ND请求报文后不上送CPU处理，直接转发ND响应报文给客户端。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| FASTRLYEN |
| --- |
| TRUE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FASTRLYEN | 使能标记 | 可选必选说明：必选参数<br>参数含义：使能标记。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SECND]] · ND快回（SECND）

## 使用实例

设置ND快回使能配置：

```
SET SECND:FASTRLYEN=TRUE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置ND快回配置（SET-SECND）_50281250.md`
