---
id: UNC@20.15.2@MMLCommand@LST SMFRESEL
type: MMLCommand
name: LST SMFRESEL（查询本地SMF重选策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFRESEL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NAS传输管理
- 本地SMF的PDU会话重建功能管理
status: active
---

# LST SMFRESEL（查询本地SMF重选策略）

## 功能

**适用NF：AMF**

该命令用于查询本地SMF重选策略的配置记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | DNN | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMF重选目标DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| ISNSSAI | 是否匹配S-NSSAI | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMF重选时是否匹配S-NSSAI。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无<br>配置原则：<br>设置为“NO”，匹配所有S-NSSAI。 |
| SST | 切片业务类型 | 可选必选说明：该参数在"ISNSSAI"配置为"YES"时为条件可选参数。<br>参数含义：该参数用于表示组成SMF重选目标网络切片的业务类型信息。网络切片标识（S-NSSAI）由切片业务类型（SST）和切片细分标识（SD）两部分组成，其中切片细分标识是可选的。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：该参数在"ISNSSAI"配置为"YES"时为条件可选参数。<br>参数含义：该参数用于表示组成SMF重选目标网络切片的细分标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFRESEL]] · 本地SMF重选策略（SMFRESEL）

## 使用实例

- 查询所有本地SMF重选策略配置记录：
  ```
  LST SMFRESEL:;
  RETCODE = 0  操作成功

  结果如下
  --------
                      DNN  =  IMS
          是否匹配S-NSSAI  =  否
             切片业务类型  =  0
             切片细分标识  =  FFFFFF
                 重选条件  =  根据NFInstanceID判断
         区域标识起始位置  =  3
         区域标识终止位置  =  6
  CM-IDLE状态时间阈值(秒)  =  0
                 起始时间  =  16:08:55
                 结束时间  =  16:08:55
  (结果个数 = 1)

  ---    END
  ```
- 查询“DNN”为“IMS”且“是否匹配S-NSSAI”为“否”的本地SMF重选策略配置记录：
  ```
  %%LST SMFRESEL: DNN="IMS", ISNSSAI=NO;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                      DNN  =  IMS
          是否匹配S-NSSAI  =  否
             切片业务类型  =  0
             切片细分标识  =  FFFFFF
                 重选条件  =  根据NFInstanceID判断
         区域标识起始位置  =  5
         区域标识终止位置  =  6
  CM-IDLE状态时间阈值(秒)  =  0
                 起始时间  =  16:08:55
                 结束时间  =  16:08:55
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询本地SMF重选策略（LST-SMFRESEL）_45495624.md`
