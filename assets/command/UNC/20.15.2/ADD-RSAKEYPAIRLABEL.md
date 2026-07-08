---
id: UNC@20.15.2@MMLCommand@ADD RSAKEYPAIRLABEL
type: MMLCommand
name: ADD RSAKEYPAIRLABEL（创建RSA密钥对标签）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: RSAKEYPAIRLABEL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 20
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 接入配置管理
- 密钥配置
- 标签密钥
status: active
---

# ADD RSAKEYPAIRLABEL（创建RSA密钥对标签）

## 功能

该命令用于创建RSA密钥对标签。为SSH服务器分配RSA服务器密钥，使用该命令生成密钥对标签。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为20。
- 密钥需定期修改否则会有安全风险。
- RSA算法如果密钥长度小于等于2048位将存在安全风险，建议使用3072位的密钥。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| KEYPAIRLABEL | RSA密钥对标签名 | 可选必选说明：必选参数<br>参数含义：RSA密钥对标签名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～35。名称只能使用数字、字母和下划线，不区分字母大小写。<br>默认值：无 |
| KEYSIZE | 公钥长度 | 可选必选说明：可选参数<br>参数含义：公钥的长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2048，3072。<br>默认值：3072 |

## 操作的配置对象

- [创建RSA密钥对标签（RSAKEYPAIRLABEL）](configobject/UNC/20.15.2/RSAKEYPAIRLABEL.md)

## 使用实例

创建名称为hw_key的RSA密钥对标签：

```
ADD RSAKEYPAIRLABEL:KEYPAIRLABEL="hw_key";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/创建RSA密钥对标签（ADD-RSAKEYPAIRLABEL）_00865881.md`
