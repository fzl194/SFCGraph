---
id: UNC@20.15.2@MMLCommand@LST MULDNNBINDAREA
type: MMLCommand
name: LST MULDNNBINDAREA（查询智能分流专网DNN支持的服务区域）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MULDNNBINDAREA
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 智能分流专网DNN管理
status: active
---

# LST MULDNNBINDAREA（查询智能分流专网DNN支持的服务区域）

## 功能

**适用NF：SMF**

查询指定智能分流专网DNN支持的服务区域。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEDDNN | 智能分流专网DNN | 可选必选说明：可选参数<br>参数含义：该参数指定智能分流专网DNN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [智能分流专网DNN支持的服务区域（MULDNNBINDAREA）](configobject/UNC/20.15.2/MULDNNBINDAREA.md)

## 使用实例

- 查询指定智能分流专网DNN支持的服务区域，智能分流专网DNN为“special.dnn”，服务区域名称为“dnnarea1”和“dnnarea2”。
  ```
  %%LST MULDNNBINDAREA: DEDDNN="special.dnn";%%
  RETCODE = 0  操作成功

  结果如下
  ------------
  智能分流专网DNN      服务区域名称

  special.dnn              dnnarea1
  special.dnn              dnnarea2
  (结果个数 = 2)
  ```
- 查询全部智能分流专网DNN支持的服务区域。
  ```
  %%LST MULDNNBINDAREA:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------
  智能分流专网DNN      服务区域名称

  special.dnn1              dnnarea1
  special.dnn1              dnnarea2
  special.dnn2              dnnarea2
  (结果个数 = 3)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询智能分流专网DNN支持的服务区域（LST-MULDNNBINDAREA）_47699101.md`
