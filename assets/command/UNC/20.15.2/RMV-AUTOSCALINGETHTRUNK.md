---
id: UNC@20.15.2@MMLCommand@RMV AUTOSCALINGETHTRUNK
type: MMLCommand
name: RMV AUTOSCALINGETHTRUNK（删除以太网隧道自动化多虚拟网卡配置模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AUTOSCALINGETHTRUNK
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- 以太网隧道多虚拟网卡自动化配置
status: active
---

# RMV AUTOSCALINGETHTRUNK（删除以太网隧道自动化多虚拟网卡配置模板）

## 功能

该命令用于删除以太网隧道多虚拟网卡自动化配置模板。

## 注意事项

- 该命令执行后立即生效。
- 该命令在自动化配置开关为关闭的状态下才能执行，请先使用SET AUTOCONFIG命令关闭自动配置开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ETHTRUNKTMPID | 以太Trunk模板ID | 可选必选说明：必选参数<br>参数含义：该参数用来指定以太Trunk模板ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～99。<br>默认值：无 |

## 操作的配置对象

- [以太网隧道自动化多虚拟网卡配置模板（AUTOSCALINGETHTRUNK）](configobject/UNC/20.15.2/AUTOSCALINGETHTRUNK.md)

## 使用实例

删除以太网隧道多虚拟网卡自动化配置模板：

```
RMV AUTOSCALINGETHTRUNK: ETHTRUNKTMPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除以太网隧道自动化多虚拟网卡配置模板（RMV-AUTOSCALINGETHTRUNK）_49801826.md`
