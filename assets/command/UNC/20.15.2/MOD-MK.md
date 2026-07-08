---
id: UNC@20.15.2@MMLCommand@MOD MK
type: MMLCommand
name: MOD MK（更新主密钥）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: MK
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 主密钥管理
status: active
---

# MOD MK（更新主密钥）

## 功能

![](更新主密钥（MOD MK）_59103979.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，执行该命令会更新主密钥，系统中所有的密文数据都会同步更新，操作不当会导致加密的数据无法恢复，请谨慎使用并联系华为技术支持协助操作。

该命令用于更新主密钥。当主密钥即将过期或者已经过期时，可使用该命令更新主密钥，系统中所有的密文数据都会使用新密钥加密。

## 注意事项

- 该命令执行后立即生效。
- 本命令属于高危命令，执行该命令会更新主密钥，系统中所有的密文数据都会同步更新。
- 更新后的主密钥，将会在7305天后过期。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MK]] · 更新主密钥（MK）

## 使用实例

更新主密钥：

```
MOD MK:
SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-MK.md`
