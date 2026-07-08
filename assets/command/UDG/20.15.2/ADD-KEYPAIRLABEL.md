---
id: UDG@20.15.2@MMLCommand@ADD KEYPAIRLABEL
type: MMLCommand
name: ADD KEYPAIRLABEL（创建DSA/ECC密钥对标签）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: KEYPAIRLABEL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 40
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 接入配置管理
- 密钥配置
- 标签密钥
status: active
---

# ADD KEYPAIRLABEL（创建DSA/ECC密钥对标签）

## 功能

该命令用创建DSA/ECC密钥对标签。为SSH服务器分配DSA服务器密钥和ECC服务器密钥，使用该命令生成密钥对标签。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为40。
- 公钥类型为DSA和ECC的命令最大记录数各为20。
- 密钥需定期修改否则会有安全风险。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYTYPE | 公钥类型 | 可选必选说明：必选参数<br>参数含义：公钥类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DSA：DSA公钥。<br>- ECC：ECC公钥。<br>默认值：无 |
| KEYPAIRLABEL | 密钥对标签名 | 可选必选说明：必选参数<br>参数含义：公钥的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～35。名称只能使用数字、字母和下划线，不区分字母大小写。<br>默认值：无 |
| DSAKEYSIZE | DSA公钥长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“KEYTYPE”配置为“DSA”时为可选参数。<br>参数含义：公钥的长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2048。<br>默认值：2048 |
| ECCKEYSIZE | ECC公钥长度 | 可选必选说明：条件可选参数<br>前提条件：该参数在“KEYTYPE”配置为“ECC”时为可选参数。<br>参数含义：公钥的长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为256，384，521。<br>默认值：521 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@KEYPAIRLABEL]] · 创建DSA/ECC密钥对标签（KEYPAIRLABEL）

## 使用实例

创建DSA/ECC密钥对标签，名称为hw_key，类型为DSA：

```
ADD KEYPAIRLABEL:KEYTYPE=DSA,KEYPAIRLABEL="hw_key";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-KEYPAIRLABEL.md`
