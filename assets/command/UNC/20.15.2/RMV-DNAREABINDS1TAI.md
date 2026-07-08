---
id: UNC@20.15.2@MMLCommand@RMV DNAREABINDS1TAI
type: MMLCommand
name: RMV DNAREABINDS1TAI（删除DNAI服务区名称绑定的4G TAI范围）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DNAREABINDS1TAI
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
- DNAI位置绑定区域管理
status: active
---

# RMV DNAREABINDS1TAI（删除DNAI服务区名称绑定的4G TAI范围）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于删除DNAI服务区名称绑定的4G TAI范围。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | DNAI服务区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于标识DNAI服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与命令LST DNAREA查询结果中的AREANAME保持一致，且对应的AREATYPE取值应为S1TAI。 |
| S1BEGINTAI | DNAI服务区名称支持4G TAI范围的起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识DNAI服务区名称支持4G TAI范围的起始值，TAI = MCC+ MNC + TAC。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是9~10。后4位为16进制数，其余为10进制数。不区分大小写。<br>默认值：无<br>配置原则：<br>TAI范围的结束值需要不小于TAI范围的开始值，且结束值和开始值长度需相等。 |
| S1ENDTAI | DNAI服务区名称支持4G TAI范围的结束值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识DNAI服务区名称支持4G TAI范围的结束值，TAI = MCC+ MNC + TAC。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是9~10。后4位为16进制数，其余为10进制数。不区分大小写。<br>默认值：无<br>配置原则：<br>TAI范围的结束值需要不小于TAI范围的开始值，且结束值和开始值长度需相等。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DNAREABINDS1TAI]] · DNAI服务区名称绑定的4G TAI范围（DNAREABINDS1TAI）

## 使用实例

删除DNAI服务区名称为“DNAREA1”的TAI绑定范围460010001~460011234。

```
RMV DNAREABINDS1TAI: AREANAME="DNAREA1", S1BEGINTAI="460010001", S1ENDTAI="460011234";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DNAREABINDS1TAI.md`
