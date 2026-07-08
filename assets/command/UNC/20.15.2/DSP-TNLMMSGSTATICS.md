---
id: UNC@20.15.2@MMLCommand@DSP TNLMMSGSTATICS
type: MMLCommand
name: DSP TNLMMSGSTATICS（显示隧道管理消息计数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TNLMMSGSTATICS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- VPN隧道管理
- 隧道管理消息计数
status: active
---

# DSP TNLMMSGSTATICS（显示隧道管理消息计数）

## 功能

该命令用于显示本设备上与隧道管理交互的消息计数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [隧道管理消息计数（TNLMMSGSTATICS）](configobject/UNC/20.15.2/TNLMMSGSTATICS.md)

## 使用实例

显示本设备上与隧道管理交互的消息计数：

```
DSP TNLMMSGSTATICS:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
组件ID       收到消息的总数    收到丢弃消息数    发送消息总数    失败消息数    重传消息数    收到序列号失序的消息数   流控消息数

7358039      1                 0                 1               0             0             0                        0
7996408      4                 0                 3               0             0             0                        0
6947836      9                 0                 47              0             0             0                        0
2149581906   5                 0                 11              0             0             0                        0
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示隧道管理消息计数（DSP-TNLMMSGSTATICS）_50120594.md`
