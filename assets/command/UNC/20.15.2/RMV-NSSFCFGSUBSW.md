---
id: UNC@20.15.2@MMLCommand@RMV NSSFCFGSUBSW
type: MMLCommand
name: RMV NSSFCFGSUBSW（删除按签约NSSAI分配Configed NSSAI的PLMN级别开关）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NSSFCFGSUBSW
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF功能开关配置
status: active
---

# RMV NSSFCFGSUBSW（删除按签约NSSAI分配Configed NSSAI的PLMN级别开关）

## 功能

**适用NF：NSSF**

该命令用于删除按签约NSSAI生成configuredNssai信元的PLMN级别开关。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于描述移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于描述移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NSSFCFGSUBSW]] · 按签约NSSAI分配Configed NSSAI的PLMN级别开关（NSSFCFGSUBSW）

## 使用实例

假如运营商希望删除一条移动国家码为235、移动网号为36的记录，执行以下命令。

```
RMV NSSFCFGSUBSW: MCC="235", MNC="36";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NSSFCFGSUBSW.md`
