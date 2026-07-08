---
id: UNC@20.15.2@MMLCommand@LST VPLMNCHGMODE
type: MMLCommand
name: LST VPLMNCHGMODE（查询基于VPLMN配置的漫游用户归属地计费模式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VPLMNCHGMODE
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- QBC计费控制
status: active
---

# LST VPLMNCHGMODE（查询基于VPLMN配置的漫游用户归属地计费模式）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询基于VPLMN配置的漫游用户归属地计费模式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPLMN | VPLMN信息 | 可选必选说明：可选参数<br>参数含义：该参数用表示漫游场景拜访地的PLMN信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。PLMN字符串的格式为MCCMNC，MCC长度为3个字符，MNC长度为2或者3个字符。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VPLMNCHGMODE]] · 基于VPLMN配置的漫游用户归属地计费模式（VPLMNCHGMODE）

## 使用实例

查询VPLMN为“08600”的漫游用户归属地计费模式：

```
%%LST VPLMNCHGMODE: VPLMN="08600";%%
RETCODE = 0  操作成功

结果如下
--------
VPLMN信息  =  08600
 计费模式  =  FBC计费
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VPLMNCHGMODE.md`
