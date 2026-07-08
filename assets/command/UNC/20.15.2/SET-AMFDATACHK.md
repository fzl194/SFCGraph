---
id: UNC@20.15.2@MMLCommand@SET AMFDATACHK
type: MMLCommand
name: SET AMFDATACHK（设置AMF数据核查相关参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AMFDATACHK
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF数据一致性核查
status: active
---

# SET AMFDATACHK（设置AMF数据核查相关参数）

## 功能

**适用NF：AMF**

该命令用于设置AMF数据核查相关参数。通过此命令AMF可以对存储的数据进行一致性校验。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DATATYPE | CHECKSW |
| --- | --- |
| UESR_INDEX_WITH_CTX | ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DATATYPE | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置AMF待核查的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- “UESR_INDEX_WITH_CTX（用户索引表与用户上下文表）”：核查用户索引表与用户上下文表数据的一致性<br>默认值：无。<br>配置原则：无 |
| CHECKSW | 核查开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示AMF数据一致性核查功能开关。当该开关打开时，AMF进行数据一致性核查，当该开关关闭时，AMF不进行数据一致性核查。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFDATACHK查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFDATACHK]] · AMF数据核查相关参数（AMFDATACHK）

## 使用实例

将AMF用户索引表与用户上下文表核查开关打开，执行如下命令：

```
SET AMFDATACHK:DATATYPE=UESR_INDEX_WITH_CTX,CHECKSW=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-AMFDATACHK.md`
