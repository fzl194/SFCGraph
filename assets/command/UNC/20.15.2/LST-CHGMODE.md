---
id: UNC@20.15.2@MMLCommand@LST CHGMODE
type: MMLCommand
name: LST CHGMODE（查询计费接口选择方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGMODE
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 计费模式
status: active
---

# LST CHGMODE（查询计费接口选择方式）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用来查询不同终端和接入类型下所使用的计费接口。

## 注意事项

- 当非5G终端4G接入时，参数“非5G终端4G接入时按5GS互操作指示选择计费接口”的取值为“是”或参数“按5GC无限制接入标识选择计费接口”的取值为“是”时，参数“指定的计费接口”无实际意义。
- 当5G终端4G接入时，参数“按5GS互操作指示选择计费接口”的取值为“是”或参数“按5GC无限制接入标识选择计费接口”的取值为“是”时，参数“指定的计费接口”无实际意义。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGMODE]] · 计费接口选择方式（CHGMODE）

## 使用实例

查询不同终端和接入类型下所使用的计费接口。

```
%%LST CHGMODE:;%%
RETCODE = 0  操作成功

结果如下
--------
指定终端和接入类型  按5GS互操作指示选择计费接口  非5G终端4G接入时按5GS互操作指示选择计费接口  指定的计费接口  作为SGW计费模式  作为V-SMF计费模式  ISMF是否支持计费  按5GC无限制接入标识选择计费接口

5G终端4G接入        否                           否                                           Nchf模式        继承其他选项     Nchf模式           不使能            否
5G终端5G接入        否                           否                                           Nchf模式        继承其他选项     Nchf模式           不使能            否
非5G终端4G接入      否                           否                                           GaGy模式        继承其他选项     Nchf模式           不使能            否
2G接入              否                           否                                           GaGy模式        继承其他选项     Nchf模式           不使能            否
NB-IoT接入          否                           否                                           GaGy模式        继承其他选项     Nchf模式           不使能            否
非3GPP接入          否                           否                                           GaGy模式        继承其他选项     Nchf模式           不使能            否
LTE-M接入           否                           否                                           GaGy模式        继承其他选项     Nchf模式           不使能            否
3G接入              否                           否                                           GaGy模式        继承其他选项     Nchf模式           不使能            否
(结果个数 = 8)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询计费接口选择方式（LST-CHGMODE）_09652191.md`
