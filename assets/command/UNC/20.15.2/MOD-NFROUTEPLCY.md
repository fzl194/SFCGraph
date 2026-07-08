---
id: UNC@20.15.2@MMLCommand@MOD NFROUTEPLCY
type: MMLCommand
name: MOD NFROUTEPLCY（修改NF路由策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NFROUTEPLCY
command_category: 配置类
applicable_nf:
- SMF
- AMF
- SMSF
- NCG
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- NF通信模式管理
- NF间接路由管理
status: active
---

# MOD NFROUTEPLCY（修改NF路由策略）

## 功能

**适用NF：SMF、AMF、SMSF、NCG、NSSF**

该命令用于修改对端NF路由策略。

## 注意事项

- 该命令执行后立即生效。

- 对于Model A、Model B和Model C模式，此命令优先级高于SET SCPFUNCSW。
- 此命令对于Model D模式不生效。
- 该命令不支持国际漫游场景跨PLMN的NF之间的路由配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| ROUTEPLCY | 路由策略 | 可选必选说明：必选参数<br>参数含义：该参数用于指定到对端NF的路由策略。<br>数据来源：全网规划<br>取值范围：<br>- “DIRECT（直连通信）”：通过直连通信<br>- “SCP（通过SCP通信）”：通过SCP Model C间接路由通信<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFROUTEPLCY]] · NF路由策略（NFROUTEPLCY）

## 使用实例

修改到对端NF的路由策略，索引为1，路由策略改为直连。

```
MOD NFROUTEPLCY: INDEX=1, ROUTEPLCY=DIRECT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NFROUTEPLCY.md`
