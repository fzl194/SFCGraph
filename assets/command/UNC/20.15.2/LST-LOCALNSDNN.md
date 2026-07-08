---
id: UNC@20.15.2@MMLCommand@LST LOCALNSDNN
type: MMLCommand
name: LST LOCALNSDNN（查询网络切片或DNN纠正配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCALNSDNN
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- 网络切片和DNN纠正管理
status: active
---

# LST LOCALNSDNN（查询网络切片或DNN纠正配置）

## 功能

**适用NF：AMF**

该命令用于查询当前配置的网络切片和DNN的纠正信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于表示用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>- “IMSI（指定IMSI）”：IMSI<br>默认值：无<br>配置原则：<br>对于指定的用户（群），SMF选择策略的匹配优先级从高到低依次为：“IMSI(指定IMSI)”，“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。<br>当SUBRANGE取值为“IMSI(指定IMSI)”时，匹配用户的方式为全匹配。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI"时为条件可选参数。<br>参数含义：该参数用于指定IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| CORRECTTYPE | 纠正类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定纠正类型。<br>数据来源：全网规划<br>取值范围：<br>- “NS_CORRECTION（纠正网络切片）”：纠正网络切片<br>- “DNN_CORRECTION（纠正DNN）”：纠正DNN<br>默认值：无<br>配置原则：无 |
| SST | 切片业务类型 | 可选必选说明：该参数在"CORRECTTYPE"配置为"NS_CORRECTION"时为条件可选参数。<br>参数含义：该参数用于表示组成纠正目标网络切片的业务类型信息。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：该参数在"CORRECTTYPE"配置为"NS_CORRECTION"时为条件可选参数。<br>参数含义：该参数用于表示组成纠正目标网络切片的细分标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：该参数在"CORRECTTYPE"配置为"DNN_CORRECTION"时为条件可选参数。<br>参数含义：该参数用于表示纠正目标DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALNSDNN]] · 网络切片或DNN纠正配置（LOCALNSDNN）

## 使用实例

- 查询当前系统中配置的网络切片和DNN纠正信息，执行如下命令：
  ```
  %%LST LOCALNSDNN:;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
             用户范围  =  所有用户
             IMSI前缀  =  NULL
                 IMSI  =  NULL
             纠正类型  =  纠正网络切片
         切片业务类型  =  1
         切片细分标识  =  FFFFFF
                  DNN  =  NULL
          DNN纠正策略  =  仅本地配置DNN
  SMF发现失败处理策略  =  标准方式
             描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询当前系统中配置的“用户范围”为“IMSI前缀”且“IMSI前缀”为“1234567”的网络切片和DNN纠正信息，执行如下命令：
  ```
  %%LST LOCALNSDNN: SUBRANGE=IMSI_PREFIX, IMSIPRE="1234567";%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
             用户范围  =  IMSI前缀
             IMSI前缀  =  1234567
                 IMSI  =  NULL
             纠正类型  =  纠正DNN
         切片业务类型  =  1
         切片细分标识  =  FFFFFF
                  DNN  =  HUAWEI
          DNN纠正策略  =  仅本地配置DNN
  SMF发现失败处理策略  =  标准方式
             描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LOCALNSDNN.md`
