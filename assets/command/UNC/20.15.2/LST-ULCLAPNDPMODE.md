---
id: UNC@20.15.2@MMLCommand@LST ULCLAPNDPMODE
type: MMLCommand
name: LST ULCLAPNDPMODE（查询指定APN的ULCL部署模式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ULCLAPNDPMODE
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
- APN粒度的ULCL部署模式
status: active
---

# LST ULCLAPNDPMODE（查询指定APN的ULCL部署模式）

## 功能

**适用NF：SMF**

该命令用于查询指定APN的ULCL部署模式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数指定APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD APN命令中参数“APN”保持一致。 |
| ULCLDEPLOYMODE | ULCL部署模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ULCL部署模式。适用于5G通用分流场景。不影响4G ULCL分流、超级漫游分流场景。如果存在更细粒度的配置(ULCLDNAIDPMODE、ULCLAREADPMODE)，在细粒度上会被对应的配置覆盖。<br>数据来源：本端规划<br>取值范围：<br>- “AUXSHUNTPREFER（优先使用辅锚点分流）”：优先辅锚点分流。如果没有与辅锚点合设的ULCL，则使用分离的ULCL。在此基础上，如果依然没有分离的ULCL，则退出ULCL分流场景。<br>- “AUXSHUNTMUST（只使用辅锚点分流）”：只使用辅锚点分流。如果没有与辅锚点合设的ULCL，则退出ULCL分流场景。<br>- “PSASHUNTMUST（只使用主锚点分流）”：只使用主锚点分流。如果没有与主锚点合设的ULCL，则退出ULCL分流场景。<br>默认值：无<br>配置原则：<br>整机默认的ULCL部署策略为优先使用辅锚点分流。APN为通用DNN时，考虑继承性影响，建议不配置或设置ULCL部署模式为辅锚点优先分流。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ULCLAPNDPMODE]] · 指定APN的ULCL部署模式（ULCLAPNDPMODE）

## 使用实例

- 查询SMF在APN内的ULCL部署模式，APN为huawei1。
  ```
  %%LST ULCLAPNDPMODE: APN="huawei1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
           APN名称  =  huawei1
      ULCL部署模式  =  优先使用辅锚点分流	 
  (结果个数 = 1)

  ---    END
  ```
- 查询所有APN粒度的ULCL部署模式。
  ```
  %%LST ULCLAPNDPMODE:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  APN名称   ULCL部署模式

  huawei1   只使用辅锚点分流
  huawei3   只使用主锚点分流
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询指定APN的ULCL部署模式（LST-ULCLAPNDPMODE）_62084037.md`
