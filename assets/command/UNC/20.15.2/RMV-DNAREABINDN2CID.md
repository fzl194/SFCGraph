---
id: UNC@20.15.2@MMLCommand@RMV DNAREABINDN2CID
type: MMLCommand
name: RMV DNAREABINDN2CID（删除DNAI服务区名称绑定的5G Cell ID范围）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DNAREABINDN2CID
command_category: 配置类
applicable_nf:
- SGW-C
- GGSN
- SMF
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

# RMV DNAREABINDN2CID（删除DNAI服务区名称绑定的5G Cell ID范围）

## 功能

**适用NF：SGW-C、GGSN、SMF、PGW-C**

该命令用于删除DNAI服务区名称绑定的5G Cell ID范围。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | DNAI服务区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于标识DNAI服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与命令LST DNAREA查询结果中的AREANAME保持一致，且对应的AREATYPE取值应为N2CID。 |
| NGBEGINCID | DNAI服务区名称支持5G小区范围的起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识DNAI服务区名称支持5G小区范围的起始值，CID = MCC + MNC + NRCELLID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>小区范围的结束值需要不小于小区范围的开始值，且结束值和开始值长度需相等。 |
| NGENDCID | DNAI服务区名称支持5G小区范围的结束值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识DNAI服务区名称支持5G小区范围的结束值，CID = MCC + MNC + NRCELLID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>小区范围的结束值需要不小于小区范围的开始值，且结束值和开始值长度需相等。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNAREABINDN2CID]] · DNAI服务区名称绑定的5G Cell ID范围（DNAREABINDN2CID）

## 使用实例

删除UPF服务区名称为“DNAREA1”的CID绑定范围46001000001234~46001000005678。

```
RMV DNAREABINDN2CID: AREANAME="DNAREA1", NGBEGINCID="46001000001234", NGENDCID="46001000005678";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DNAI服务区名称绑定的5G-Cell-ID范围（RMV-DNAREABINDN2CID）_71436551.md`
