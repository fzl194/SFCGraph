---
id: UNC@20.15.2@MMLCommand@ADD DNAREABINDN2TAI
type: MMLCommand
name: ADD DNAREABINDN2TAI（增加DNAI服务区名称绑定的5G TAI范围）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DNAREABINDN2TAI
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

# ADD DNAREABINDN2TAI（增加DNAI服务区名称绑定的5G TAI范围）

## 功能

**适用NF：SGW-C、SMF、GGSN、PGW-C**

该命令用于增加DNAI服务区名称绑定的5G TAI范围。

## 注意事项

- 该命令执行后立即生效。

- 同一个AREANAME下TAI区域不能有交叠，不同AREANAME下TAI区域不做限制。

- 最多可输入32000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | DNAI服务区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于标识DNAI服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与命令LST DNAREA查询结果中的AREANAME保持一致，且对应的AREATYPE取值应为N2TAI。 |
| N2BEGINTAI | DNAI服务区名称支持5G TAI范围的起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识DNAI服务区名称支持5G TAI范围的起始值，TAI = MCC+ MNC + TAC。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~12。后6位为16进制数，其余为10进制数。不区分大小写。<br>默认值：无<br>配置原则：<br>TAI范围的结束值需要不小于TAI范围的开始值，且结束值和开始值长度需相等。 |
| N2ENDTAI | DNAI服务区名称支持5G TAI范围的结束值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识DNAI服务区名称支持5G TAI范围的结束值，TAI = MCC+ MNC + TAC。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~12。后6位为16进制数，其余为10进制数。不区分大小写。<br>默认值：无<br>配置原则：<br>TAI范围的结束值需要不小于TAI范围的开始值，且结束值和开始值长度需相等。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DNAREABINDN2TAI]] · DNAI服务区名称绑定的5G TAI范围（DNAREABINDN2TAI）

## 使用实例

增加DNAI服务区名称为“DNAREA1”的TAI绑定范围46001000001~46001123456。

```
ADD DNAREABINDN2TAI: AREANAME="DNAREA1", N2BEGINTAI="46001000001", N2ENDTAI="46001123456";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DNAREABINDN2TAI.md`
