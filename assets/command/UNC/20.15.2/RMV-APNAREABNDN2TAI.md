---
id: UNC@20.15.2@MMLCommand@RMV APNAREABNDN2TAI
type: MMLCommand
name: RMV APNAREABNDN2TAI（删除APN相关服务区域绑定的5G TAI范围）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNAREABNDN2TAI
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN相关服务区域管理
status: active
---

# RMV APNAREABNDN2TAI（删除APN相关服务区域绑定的5G TAI范围）

## 功能

**适用NF：SMF**

该命令用于删除APN相关服务区域绑定的5G TAI范围。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | APN相关服务区域 | 可选必选说明：必选参数<br>参数含义：该参数用于配置APN相关服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。<br>默认值：无<br>配置原则：<br>与APNAREA配置中的AREANAME取值对应。 |
| N2BEGINTAI | 服务区域名称支持5GTAI范围的起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识APN相关服务区域支持5GTAI范围的起始值，TAI = MCC+ MNC + TAC。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~12。后6位为16进制数，其余为10进制数。<br>默认值：无<br>配置原则：<br>TAI范围的结束值需要不小于TAI范围的开始值，且结束值和开始值长度需相等。 |
| N2ENDTAI | 服务区域名称支持5GTAI范围的结束值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识APN相关服务区域支持5GTAI范围的结束值，TAI = MCC+ MNC + TAC。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~12。后6位为16进制数，其余为10进制数。<br>默认值：无<br>配置原则：<br>TAI范围的结束值需要不小于TAI范围的开始值，且结束值和开始值长度需相等。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNAREABNDN2TAI]] · APN相关服务区域绑定的5G TAI范围（APNAREABNDN2TAI）

## 使用实例

删除APN相关服务区域“dnnarea1”的TAI绑定范围46001000001~46001123456。

```
RMV APNAREABNDN2TAI: AREANAME="dnnarea1", N2BEGINTAI="46001000001", N2ENDTAI="46001123456";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN相关服务区域绑定的5G-TAI范围（RMV-APNAREABNDN2TAI）_00470288.md`
