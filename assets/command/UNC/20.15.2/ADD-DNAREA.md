---
id: UNC@20.15.2@MMLCommand@ADD DNAREA
type: MMLCommand
name: ADD DNAREA（增加DNAI服务区域）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD DNAREA（增加DNAI服务区域）

## 功能

**适用NF：SGW-C、SMF、GGSN、PGW-C**

该命令用于增加DNAI服务区域。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入16000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | DNAI服务区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置DNAI服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。不区分大小写。<br>默认值：无<br>配置原则：无 |
| AREATYPE | DNAI服务区域类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置DNAI服务区域类型。<br>数据来源：全网规划<br>取值范围：<br>- N2TAI（5G类型的TAI）<br>- N2CID（5G类型的Cell Id）<br>- S1TAI（4G类型的TAI）<br>- S1CID（4G类型的Cell Id）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DNAI服务区域（DNAREA）](configobject/UNC/20.15.2/DNAREA.md)

## 使用实例

增加5G类型的TAI服务区域

```
ADD DNAREA: AREANAME="DNAREA1", AREATYPE=N2TAI;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加DNAI服务区域（ADD-DNAREA）_24956616.md`
