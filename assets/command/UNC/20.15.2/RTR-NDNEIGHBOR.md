---
id: UNC@20.15.2@MMLCommand@RTR NDNEIGHBOR
type: MMLCommand
name: RTR NDNEIGHBOR（清除IPv6 ND邻居表项）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: NDNEIGHBOR
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 ND表项
status: active
---

# RTR NDNEIGHBOR（清除IPv6 ND邻居表项）

## 功能

![](清除IPv6 ND邻居表项（RTR NDNEIGHBOR）_00601313.assets/notice_3.0-zh-cn_2.png)

本命令为高危命令，操作不当会引起业务故障，请谨慎使用并联系华为技术支持协助操作。

该命令用于清除动态ND表项。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NDNEIGHBOR]] · 静态ND邻居表项（NDNEIGHBOR）

## 使用实例

清除动态ND表项：

```
RTR NDNEIGHBOR:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除IPv6-ND邻居表项（RTR-NDNEIGHBOR）_00601313.md`
