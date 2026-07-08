---
id: UNC@20.15.2@MMLCommand@RMV PNFDNN
type: MMLCommand
name: RMV PNFDNN（删除对端NF的DNN信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PNFDNN
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
- SGW-C
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端DNN信息管理
status: active
---

# RMV PNFDNN（删除对端NF的DNN信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG、SGW-C、PGW-C、GGSN**

该命令用于删除本地配置的对端NF实例支持的DNN及其归属切片的信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNN的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>该参数取值不能重复，建议从0开始顺序取值。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFDNN]] · 对端NF的DNN信息（PNFDNN）

## 使用实例

删除对端NF的DNN信息，索引为1。

```
RMV PNFDNN: INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PNFDNN.md`
