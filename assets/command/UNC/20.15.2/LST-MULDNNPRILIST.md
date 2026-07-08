---
id: UNC@20.15.2@MMLCommand@LST MULDNNPRILIST
type: MMLCommand
name: LST MULDNNPRILIST（查询本地专网DNN就近接入优先级）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MULDNNPRILIST
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 智能分流专网DNN管理
status: active
---

# LST MULDNNPRILIST（查询本地专网DNN就近接入优先级）

## 功能

**适用NF：SMF、PGW-C**

该命令用于查询指定智能分流专网DNN接入省/市的优先级。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEDDNN | 智能分流专网DNN | 可选必选说明：可选参数<br>参数含义：该参数用于指定智能分流专网DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MULDNNPRILIST]] · 本地专网DNN就近接入优先级（MULDNNPRILIST）

## 使用实例

- 显示“智能分流专网DNN”为“special.dnn”的本地专网DNN就近接入优先级：
  ```
  %%LST MULDNNPRILIST: DEDDNN="special.dnn";%%
  RETCODE = 0  操作成功

  结果如下
  --------
         智能分流专网DNN  =  huawei.com
  就近接入省市第一级后缀  =  abc
  就近接入省市第二级后缀  =  def
  就近接入省市第三级后缀  =  ghi
  (结果个数 = 1)

  ---    END
  ```
- 显示全部智能分流专网DNN的本地专网DNN就近接入优先级：
  ```
  %%LST MULDNNPRILIST:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  智能分流专网DNN  就近接入省市第一级后缀  就近接入省市第二级后缀  就近接入省市第三级后缀  
  special.dnn      abc                     def                     ghi  
  special.dnn2     abcd                    defg                    ghij  
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MULDNNPRILIST.md`
