---
id: UNC@20.15.2@MMLCommand@SET LINKMIGCTRL
type: MMLCommand
name: SET LINKMIGCTRL（设置链路迁移控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: LINKMIGCTRL
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- 链路管理
status: active
---

# SET LINKMIGCTRL（设置链路迁移控制参数）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置链路迁移控制参数，涉及的链路接口类型为Ga/Gx/Gy/S6b。

## 注意事项

- 该命令执行后立即生效。

- 对于Ga接口链路，仅在Ga集中点部署模式为SINGLE_CONNECT时生效。
- 容器CPU超过阈值至少持续50s时才会触发链路迁移，瞬时冲高不会触发。
- CPU阈值配置较小时可能反复触发链路迁移，每次链路迁移都会产生一定的消息损失，请谨慎配置。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CONTAINERCPUTS | AVRLINKTIMER |
| --- | --- |
| 65 | 2 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONTAINERCPUTS | 容器CPU阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置判定链路拥塞的容器CPU阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~100，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LINKMIGCTRL查询当前参数配置值。<br>配置原则：<br>该参数配置为100时关闭链路拥塞导致的链路迁移。 |
| AVRLINKTIMER | 均分链路时间间隔 | 可选必选说明：可选参数<br>参数含义：该参数用于设置整机复位场景均分链路时间间隔。整机复位场景，进程启动后，间隔该参数配置的时长后，如果所有链路分配在同一个POD上，则执行一次链路均分。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LINKMIGCTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [链路迁移控制参数（LINKMIGCTRL）](configobject/UNC/20.15.2/LINKMIGCTRL.md)

## 使用实例

设置链路迁移控制参数：

```
SET LINKMIGCTRL:CONTAINERCPUTS=65,AVRLINKTIMER=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置链路迁移控制参数（SET-LINKMIGCTRL）_81482582.md`
