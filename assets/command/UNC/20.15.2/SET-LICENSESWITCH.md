---
id: UNC@20.15.2@MMLCommand@SET LICENSESWITCH
type: MMLCommand
name: SET LICENSESWITCH（设置License项的开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: LICENSESWITCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# SET LICENSESWITCH（设置License项的开关）

## 功能

该命令用于设置License项的配置开关。当License文件中含有某功能的许可时，通过此命令可以设置该功能是否开通。

## 注意事项

- 该命令执行后立即生效。

- 当license文件未激活时，无法设置任何license项，激活后只能设置已购买且支持配置开关的license项。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

> **说明**
> 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| LICITEM | SWITCH |
| --- | --- |
| LKV4W9BRCL01 | ENABLE |
| LKV2CHR03 | DISABLE |
| LKV2CHR04 | DISABLE |
| LKV2MUSP01 | DISABLE |
| LKV2PRA01 | DISABLE |
| LKV2VOLTE01 | DISABLE |
| LKV2MSCMG02 | DISABLE |
| LKV2BFD02 | DISABLE |
| LKV2PPTF01 | DISABLE |
| LKV2V6IF01 | DISABLE |
| LKV2DECOR00 | DISABLE |
| LKV2HD4M02 | DISABLE |
| LKV2HD8M02 | DISABLE |
| LKV2HD16M02 | DISABLE |
| LKV2HSPADL02 | DISABLE |
| LKV2HD32M01 | DISABLE |
| LKV2HD48M01 | DISABLE |
| LKV2HD84M01 | DISABLE |
| LKV2HU4M02 | DISABLE |
| LKV2HU8M02 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LICITEM | License项 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要开通的License项。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无。<br>配置原则：无 |
| SWITCH | 开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示License项的配置开关是否已经打开。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（开）”：开启License控制项<br>- “DISABLE（关）”：关闭License控制项<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LICENSESWITCH]] · License配置项开关（LICENSESWITCH）

## 使用实例

开通License项为“LKV2INLINR01”的功能的License开关：

```
%%SET LICENSESWITCH: LICITEM="LKV2INLINR01", SWITCH=ENABLE;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-LICENSESWITCH.md`
