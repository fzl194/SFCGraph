---
id: UNC@20.15.2@MMLCommand@MOD CERTSCENE
type: MMLCommand
name: MOD CERTSCENE（修改证书场景描述）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CERTSCENE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 公钥基础设施
- PKI场景
status: active
---

# MOD CERTSCENE（修改证书场景描述）

## 功能

该命令用于修改证书场景描述。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCENENAME | 场景名称 | 可选必选说明：必选参数<br>参数含义：场景名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~192。不区分大小写，最多允许一个空格，不支持中文字符。<br>默认值：无<br>配置原则：无 |
| ENDESCRIPTION | 场景英文描述 | 可选必选说明：可选参数<br>参数含义：场景英文描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~192。不区分大小写。<br>默认值：无<br>配置原则：无 |
| CNDESCRIPTION | 场景中文描述 | 可选必选说明：可选参数<br>参数含义：场景中文描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~192。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CERTSCENE]] · 证书场景描述（CERTSCENE）

## 使用实例

修改场景名为“DeviceA”的证书场景：

```
MOD CERTSCENE: SCENENAME="DeviceA", ENDESCRIPTION="DeviceA", CNDESCRIPTION="DeviceA";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-CERTSCENE.md`
