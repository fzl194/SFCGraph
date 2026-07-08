---
id: UNC@20.15.2@MMLCommand@MOD NGSRVPLMN
type: MMLCommand
name: MOD NGSRVPLMN（修改5G Serving PLMN）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD NGSRVPLMN（修改5G Serving PLMN）

## 功能

![](修改5G Serving PLMN（MOD NGSRVPLMN）_09653241.assets/notice_3.0-zh-cn_2.png)

修改Serving PLMN可能影响AMF给无线侧广播的PLMN信息。

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF**

该命令用于修改指定的Serving PLMN。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMNIDX | PLMN索引 | 可选必选说明：必选参数<br>参数含义：该参数用于在系统内唯一标识一个PLMN。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本PLMN所归属的运营商。NOID通过ADD NGMNO进行配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数表示组成Serving PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数表示组成Serving PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数是对Serving PLMN的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGSRVPLMN]] · 5G Serving PLMN（NGSRVPLMN）

## 使用实例

将运营商A的Serving PLMN信息从12345修改为12346，执行如下命令：

```
MOD NGSRVPLMN: PLMNIDX=0, NOID=0, MCC="123", MNC="46";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改5G-Serving-PLMN（MOD-NGSRVPLMN）_09653241.md`
