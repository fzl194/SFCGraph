---
id: UNC@20.15.2@MMLCommand@RMV PNFPLMNRANGE
type: MMLCommand
name: RMV PNFPLMNRANGE（删除对端NF的PLMN范围）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PNFPLMNRANGE
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF实例PLMN范围管理
status: active
---

# RMV PNFPLMNRANGE（删除对端NF的PLMN范围）

## 功能

**适用NF：AMF、SMF、NSSF、NCG**

该命令用于删除本地配置的对端NF实例支持的PLMN范围信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~8191。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFPLMNRANGE]] · 对端NF的PLMN范围（PNFPLMNRANGE）

## 使用实例

删除对端NF的PLMN范围信息。

```
RMV PNFPLMNRANGE:INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端NF的PLMN范围（RMV-PNFPLMNRANGE）_09652099.md`
