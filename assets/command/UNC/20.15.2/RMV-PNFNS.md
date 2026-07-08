---
id: UNC@20.15.2@MMLCommand@RMV PNFNS
type: MMLCommand
name: RMV PNFNS（删除对端NF的切片信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PNFNS
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
- PGW-C
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF实例切片信息管理
status: active
---

# RMV PNFNS（删除对端NF的切片信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG、PGW-C、SGW-C**

该命令用于删除本地配置的对端NF实例支持的切片信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定切片的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFNS]] · 对端NF的切片信息（PNFNS）

## 使用实例

删除对端NF实例的切片信息，NF实例标识为SMF_Instance_0，NF实例支持的SST为1，SD为000001。

```
RMV PNFNS: INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端NF的切片信息（RMV-PNFNS）_09652629.md`
