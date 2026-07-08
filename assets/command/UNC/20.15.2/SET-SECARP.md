---
id: UNC@20.15.2@MMLCommand@SET SECARP
type: MMLCommand
name: SET SECARP（设置ARP快回配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SECARP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略ARP
status: active
---

# SET SECARP（设置ARP快回配置）

## 功能

该命令用来设置ARP快回使能配置。

大量客户端发送ARP请求报文会造成CPU负载过高。为了降低CPU负载，可通过配置此命令，使设备接收到ARP请求报文后不上送CPU处理，直接转发ARP响应报文给客户端。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| FASTRLYEN |
| --- |
| TRUE |

- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：区分大小写，不支持空格，下发本MML命令前可使用<br>**DSP RU**<br>指定VNRS_VNFC（举例：VNRS_VNFC_999）查看转发板资源单元信息。 |
| FASTRLYEN | 使能标记 | 可选必选说明：必选参数<br>参数含义：使能标记。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECARP]] · ARP快回（SECARP）

## 使用实例

添加ARP快回使能配置：

```
SET SECARP:RUNAME="VNODE_VNRS_VNFC_IPU_0064",FASTRLYEN=TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SECARP.md`
