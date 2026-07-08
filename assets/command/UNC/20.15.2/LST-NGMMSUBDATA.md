---
id: UNC@20.15.2@MMLCommand@LST NGMMSUBDATA
type: MMLCommand
name: LST NGMMSUBDATA（查询用户移动性管理参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGMMSUBDATA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 签约数据管理
status: active
---

# LST NGMMSUBDATA（查询用户移动性管理参数）

## 功能

**适用NF：AMF**

该命令用于查询系统中当前针对用户（群）配置的移动性管理相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用本地接入和移动性签约数据配置的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>- “IMSI（指定IMSI）”：IMSI<br>默认值：无<br>配置原则：<br>对于指定的用户（群），匹配优先级从高到低依次为：“IMSI(指定IMSI)”，“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。<br>当SUBRANGE取值为“IMSI(指定IMSI)”时，匹配用户的方式为全匹配。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定应用本地接入和移动性签约数据配置的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>当SUBRANGE取值为“IMSI(指定IMSI)”时，匹配用户的方式为全匹配。 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定应用本地接入和移动性签约数据配置的用户的IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用户移动性管理参数（NGMMSUBDATA）](configobject/UNC/20.15.2/NGMMSUBDATA.md)

## 使用实例

- 查询系统中配置的用户移动性管理参数，执行如下命令：
  ```
  %%LST NGMMSUBDATA:;%%
  RETCODE = 0  执行成功

  结果如下
  --------
               用户范围  =  指定IMSI前缀
               IMSI前缀  =  123031234567890
                   IMSI  =  NULL
                RAT限制  =  演进型通用陆地无线接入
         核心网类型限制  =  NULL
               RFSP索引  =  0
   网络切片包含模式策略  =  网络切片包含模式C
                寻呼DRX  =  0
             RFSP优先级  =  配置优先
     上行UE AMBR (kbps)  =  0
     下行UE AMBR (kbps)  =  0
            扩展RAT限制  =  仅支持本地配置
    主接入限制的RAT类型  =  NR
  辅助接入限制的RAT类型  =  NR		 
  (结果个数 = 1)

  --- END
  ```
- 查询IMSI为123031234567890的用户移动性管理参数，执行如下命令：
  ```
  %%LST NGMMSUBDATA: SUBRANGE=IMSI_PREFIX, IMSIPRE="123031234567890";%%
  RETCODE = 0  执行成功

  结果如下
  --------
               用户范围  =  指定IMSI前缀
               IMSI前缀  =  123031234567890
                   IMSI  =  NULL
                RAT限制  =  演进型通用陆地无线接入
         核心网类型限制  =  NULL
               RFSP索引  =  0
   网络切片包含模式策略  =  网络切片包含模式A
                寻呼DRX  =  0
             RFSP优先级  =  配置优先
     上行UE AMBR (kbps)  =  0
     下行UE AMBR (kbps)  =  0
            扩展RAT限制  =  仅支持本地配置
    主接入限制的RAT类型  =  NR
  辅助接入限制的RAT类型  =  NR		 
  (结果个数 = 1)

  --- END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户移动性管理参数（LST-NGMMSUBDATA）_09651400.md`
