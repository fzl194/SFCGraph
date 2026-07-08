---
id: UNC@20.15.2@MMLCommand@LST RSTRNSAREAMEM
type: MMLCommand
name: LST RSTRNSAREAMEM（查询TA级限制切片所属跟踪区成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RSTRNSAREAMEM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 网络切片选择管理
- TA级限制切片区域管理
status: active
---

# LST RSTRNSAREAMEM（查询TA级限制切片所属跟踪区成员）

## 功能

**适用NF：AMF**

该命令用于查询指定TA级限制切片所属区域或者系统中配置的所有TA级限制切片所属区域的跟踪区成员。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREACODE | 区域编码 | 可选必选说明：可选参数<br>参数含义：该参数用于标识TA级限制切片所属的某区域范围。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。该参数依赖于ADD RSTRNSAREACODE命令中的AREACODE参数。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成TA级限制切片所属区域的位置区成员的移动国家码，与无线接入网的MCC一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成TA级限制切片所属区域的位置区成员的移动网号，与无线接入网的MNC一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>两条记录间的MCC相同时，2位MNC与3位MNC的前两个数字不能相同。 |
| BGNTAC | 跟踪区编码起始值 | 可选必选说明：可选参数<br>参数含义：该参数用于表示跟踪区编码的起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RSTRNSAREAMEM]] · TA级限制切片所属跟踪区成员（RSTRNSAREAMEM）

## 使用实例

- 查询编码为“jq001.pd006.sh.mcc123.mnc45”的TA级限制切片所属区域成员信息，执行如下命令：
  ```
  %%LST RSTRNSAREAMEM: AREACODE="jq001.pd006.sh.mcc123.mnc45";%%
  RETCODE = 0  操作成功

  结果如下
  --------
          区域编码  =  jq001.pd006.sh.mcc123.mnc45
        移动国家码  =  123
          移动网号  =  45
  跟踪区编码起始值  =  111111
  跟踪区编码结束值  =  111111
          描述信息  =  NULL
  (结果个数  = 1)

  ---    END
  ```
- 查询所有的TA级限制切片所属区域成员信息，执行如下命令：
  ```
  %%LST RSTRNSAREAMEM:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
          区域编码  =  jq001.pd006.sh.mcc123.mnc45
        移动国家码  =  460
          移动网号  =  121
  跟踪区编码起始值  =  111111
  跟踪区编码结束值  =  111111
          描述信息  =  NULL
  (结果个数  = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RSTRNSAREAMEM.md`
