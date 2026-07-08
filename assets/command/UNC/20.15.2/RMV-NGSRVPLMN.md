---
id: UNC@20.15.2@MMLCommand@RMV NGSRVPLMN
type: MMLCommand
name: RMV NGSRVPLMN（删除5G Serving PLMN）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGSRVPLMN
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- Serving PLMN信息管理
status: active
---

# RMV NGSRVPLMN（删除5G Serving PLMN）

## 功能

![](删除5G Serving PLMN（RMV NGSRVPLMN）_09653774.assets/notice_3.0-zh-cn_2.png)

删除Serving PLMN可能影响AMF给无线侧广播的PLMN信息。

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF**

该命令用于删除指定的Serving PLMN。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMNIDX | PLMN索引 | 可选必选说明：必选参数<br>参数含义：该参数用于在系统内唯一标识一个PLMN。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGSRVPLMN]] · 5G Serving PLMN（NGSRVPLMN）

## 使用实例

为运营商A删除Serving PLMN信息（索引为0），执行如下命令：

```
RMV NGSRVPLMN: PLMNIDX=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGSRVPLMN.md`
