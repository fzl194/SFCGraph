---
id: UNC@20.15.2@MMLCommand@SET HOSTGLBCONFIG
type: MMLCommand
name: SET HOSTGLBCONFIG（设置主机收发全局属性）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: HOSTGLBCONFIG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- IP协议全局配置
status: active
---

# SET HOSTGLBCONFIG（设置主机收发全局属性）

## 功能

该命令用于设置主机收发忽略管理平面接口上送的TCP或UDP协议报文的校验和。

如果网卡开启了GRO功能，分片的TCP或UDP报文被网卡聚合上送，聚合时校验和未刷新，在这种场景下使用该命令通知主机收发忽略校验和检查。

## 注意事项

- 当前版本不支持此命令。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| ISIGNORECHKSUM |
| --- |
| FALSE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ISIGNORECHKSUM | 忽略校验和 | 可选必选说明：必选参数<br>参数含义：该参数用于表示过滤校验和标记。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HOSTGLBCONFIG]] · 主机收发全局属性（HOSTGLBCONFIG）

## 使用实例

配置主机收发忽略校验和：

```
SET HOSTGLBCONFIG:ISIGNORECHKSUM=TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-HOSTGLBCONFIG.md`
