---
id: UNC@20.15.2@MMLCommand@SET GBACKOFFTIME
type: MMLCommand
name: SET GBACKOFFTIME（设置全局Back-off Time信息）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GBACKOFFTIME
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
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- 全局Back-off Time信息
status: active
---

# SET GBACKOFFTIME（设置全局Back-off Time信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置全局的Back-off Time信息。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| BACKOFFTIMER |
| --- |
| 600 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BACKOFFTIMER | 全局Back-off时长(秒) | 可选必选说明：必选参数<br>参数含义：该参数用于指定全局Back-off时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~3600，单位是秒。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [全局Back-off Time信息（GBACKOFFTIME）](configobject/UNC/20.15.2/GBACKOFFTIME.md)

## 使用实例

当运营商需要设置全局Back-off Time信息时，配置如下：

```
SET GBACKOFFTIME: BACKOFFTIMER = 600;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置全局Back-off-Time信息（SET-GBACKOFFTIME）_76686936.md`
