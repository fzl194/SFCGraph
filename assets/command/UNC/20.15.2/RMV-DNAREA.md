---
id: UNC@20.15.2@MMLCommand@RMV DNAREA
type: MMLCommand
name: RMV DNAREA（删除DNAI服务区域）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DNAREA
command_category: 配置类
applicable_nf:
- SGW-C
- SMF
- GGSN
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- DNAI位置绑定区域管理
status: active
---

# RMV DNAREA（删除DNAI服务区域）

## 功能

**适用NF：SGW-C、SMF、GGSN、PGW-C**

该命令用于删除DNAI服务区域。

## 注意事项

- 该命令执行后立即生效。

- 该命令用于删除DNAI服务区域，必须先使用命令RMV DNAREABINDN2TAI、RMV DNAREABINDN2CID、RMV DNAREABINDDNAI删除对应与该服务区名称相同的记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | DNAI服务区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置DNAI服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNAREA]] · DNAI服务区域（DNAREA）

## 使用实例

删除区域名称为"DNAREA1"的DNAI服务区域：

```
RMV DNAREA: AREANAME="DNAREA1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DNAREA.md`
