---
id: UNC@20.15.2@MMLCommand@RMV NFROUTEPLCY
type: MMLCommand
name: RMV NFROUTEPLCY（删除NF路由策略）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV NFROUTEPLCY（删除NF路由策略）

## 功能

**适用NF：SMF、AMF、SMSF、NCG、NSSF**

该命令用于删除对端NF路由策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NF路由策略（NFROUTEPLCY）](configobject/UNC/20.15.2/NFROUTEPLCY.md)

## 使用实例

删除到对端NF的路由策略，索引为1。

```
RMV NFROUTEPLCY: INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF路由策略（RMV-NFROUTEPLCY）_47358580.md`
