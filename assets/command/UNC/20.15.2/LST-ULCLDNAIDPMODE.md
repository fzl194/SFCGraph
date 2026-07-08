---
id: UNC@20.15.2@MMLCommand@LST ULCLDNAIDPMODE
type: MMLCommand
name: LST ULCLDNAIDPMODE（查询指定DNAI的ULCL部署模式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ULCLDNAIDPMODE
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- ULCL分流部署策略
- DNAI粒度的ULCL部署模式
status: active
---

# LST ULCLDNAIDPMODE（查询指定DNAI的ULCL部署模式）

## 功能

**适用NF：SMF**

该命令用于查询指定DNAI的ULCL部署模式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数指定APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD APN命令中参数“APN”保持一致。 |
| DNAI | 数据网络访问标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ULCLDNAIDPMODE]] · 指定DNAI的ULCL部署模式（ULCLDNAIDPMODE）

## 使用实例

- 查询SMF在DNAI内的ULCL部署模式，APN为huawei1，DNAI名称为huawei2。
  ```
  %%LST ULCLDNAIDPMODE: APN="huawei1",DNAI="huawei2";%%
  RETCODE = 0  操作成功

  结果如下
  --------
           APN名称  =  huawei1
  数据网络访问标识  =  huawei2
      ULCL部署模式  =  优先使用辅锚点分流	 
  (结果个数 = 1)

  ---    END
  ```
- 查询所有DNAI粒度的ULCL部署模式。
  ```
  %%LST ULCLDNAIDPMODE:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  APN名称   数据网络访问标识   ULCL部署模式

  huawei1   huawei2            只使用辅锚点分流
  huawei3   huawei4            只使用主锚点分流
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询指定DNAI的ULCL部署模式（LST-ULCLDNAIDPMODE）_09044576.md`
