---
id: UDG@20.15.2@MMLCommand@OPR INTERFACE
type: MMLCommand
name: OPR INTERFACE（设置接口维护状态）
nf: UDG
version: 20.15.2
verb: OPR
object_keyword: INTERFACE
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- IFM
status: active
---

# OPR INTERFACE（设置接口维护状态）

## 功能

![](设置接口维护状态（OPR INTERFACE）_50121206.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

该命令用于存储故障下，设置接口维护状态。

## 注意事项

- 该命令执行后立即生效。
- 该命令影响接口物理状态。
- 设备重启后，该操作失效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| IFACTSTATUS | 维护状态 | 可选必选说明：必选参数<br>参数含义：该参数用于设置该接口的维护状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- down：接口Down。<br>- up：接口Up。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/INTERFACE]] · 接口（INTERFACE）

## 使用实例

设置接口维护状态为up：

```
OPR INTERFACE:IFNAME="Ethernet66/0/3",IFACTSTATUS=up;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置接口维护状态（OPR-INTERFACE）_50121206.md`
