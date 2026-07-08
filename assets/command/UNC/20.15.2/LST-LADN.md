---
id: UNC@20.15.2@MMLCommand@LST LADN
type: MMLCommand
name: LST LADN（查询本地数据网络）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LADN
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- AMF
- 本地数据网络管理
status: active
---

# LST LADN（查询本地数据网络）

## 功能

**适用NF：AMF**

该命令用于查询本地数据网络的配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地数据网络。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| BGNTAI | 跟踪区标识起始值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地数据网络（LADN）的生效区域范围。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~12。TAI由MCC、MNC和TAC组成。MCC为3位数字，MNC为2个或者3位数字，填写时请遵循实际长度。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LADN]] · 本地数据网络（LADN）

## 使用实例

- 查询本地数据网络配置信息，执行如下命令：
  ```
  %%LST LADN:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
      数据网络名称  =  HUAWEI.COM
  跟踪区标识起始值  =  12300123888
  跟踪区标识结束值  =  12300123889
          描述信息  =  Shanghai
  (结果个数 = 1)

  ---    END
  ```
- 查询“数据网络名称”为“HUAWEI.COM”的本地数据网络配置信息，执行如下命令：
  ```
  %%LST LADN: DNN="HUAWEI.COM";%%
  RETCODE = 0  操作成功

  结果如下
  --------
      数据网络名称  =  HUAWEI.COM
  跟踪区标识起始值  =  12300123888
  跟踪区标识结束值  =  12300123889
          描述信息  =  for Pudong Jinqiao
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询本地数据网络（LST-LADN）_09651377.md`
