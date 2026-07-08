---
id: UNC@20.15.2@MMLCommand@ADD H2SRVPLMN
type: MMLCommand
name: ADD H2SRVPLMN（增加Home PLMN到Serving PLMN的对应关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: H2SRVPLMN
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
- GGSN
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- Home PLMN到Serving PLMN关联信息管理
status: active
---

# ADD H2SRVPLMN（增加Home PLMN到Serving PLMN的对应关系）

## 功能

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF、GGSN、SMSF**

该命令用于增加运营商的Home PLMN到Serving PLMN的对应关系。

## 注意事项

- 该命令执行后立即生效。

- 增加运营商的Home PLMN到Serving PLMN的对应关系，用于配置Home PLMN与切片的对应关系。
- 不配置该命令时，注册、更新时不会携带perPlmnSnssaiList信元。
- 使用该配置时，需要对所有的Home PLMN配置到Serving PLMN的对应关系。

- 最多可输入768条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HMCC | Home PLMN移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于配置Home PLMN的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：<br>- 只允许配置十进制数字（0-9）。<br>- 该参数通过ADD NGHPLMN的MCC进行配置。 |
| HMNC | Home PLMN移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于配置Home PLMN的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：<br>- 只允许配置十进制数字（0-9）。<br>- 该参数通过ADD NGHPLMN的MNC进行配置。 |
| SRVPLMNIDX | Serving PLMN索引 | 可选必选说明：必选参数<br>参数含义：该参数用于配置Home PLMN关联的Serving PLMN Index。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：<br>该参数通过ADD NGSRVPLMN的PLMNIDX进行配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/H2SRVPLMN]] · Home PLMN到Serving PLMN的对应关系（H2SRVPLMN）

## 使用实例

为Home PLMN (12368)增加到Serving PLMN(PLMNIDX为1)的对应关系：

```
ADD H2SRVPLMN: HMCC="123", HMNC="68", SRVPLMNIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Home-PLMN到Serving-PLMN的对应关系（ADD-H2SRVPLMN）_94923873.md`
