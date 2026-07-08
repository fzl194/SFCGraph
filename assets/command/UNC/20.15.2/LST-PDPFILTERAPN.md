---
id: UNC@20.15.2@MMLCommand@LST PDPFILTERAPN
type: MMLCommand
name: LST PDPFILTERAPN（查询APN优先级配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PDPFILTERAPN
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- PDP过滤功能
status: active
---

# LST PDPFILTERAPN（查询APN优先级配置）

## 功能

**适用网元：SGSN**

该命令用于查询APN优先级配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>该参数用于指定PDP过滤功能适用的用户范围。参考<br>[**SET PDPFILTERCTL**](设置PDP过滤功能参数(SET PDPFILTERCTL)_26145688.md)<br>命令。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “LOCAL_USER(本网用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件: 该参数在“用户范围”参数配置为“IMSI_PREFIX(指定IMSI前缀)”时生效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字字符串。<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定APNNI名称<br>数据来源：整网规划<br>取值范围：1～62位字符串。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PDPFILTERAPN]] · APN优先级配置（PDPFILTERAPN）

## 使用实例

1. 查询所有APN优先级记录：
  LST PDPFILTERAPN:;
  ```
  %%LST PDPFILTERAPN:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   用户范围      IMSI前缀  APNNI        优先级  描述  

   指定IMSI前缀  12302     HUAWEI4.COM  1       NULL  
   指定IMSI前缀  12302     HUAWEI5.COM  2       NULL  
   指定IMSI前缀  1230      HUAWEI3.COM  1       NULL  
   本网用户      NULL      HUAWEI2.COM  1       NULL  
   所有用户      NULL      HUAWEI1.COM  1       NULL  
  (结果个数 = 5)

  ---    END
  ```
2. 查询“用户范围”为“指定IMSI范围”，“IMSI前缀”为“12302”的APN优先级记录：
  LST PDPFILTERAPN: SUBRANGE=IMSI_PREFIX, IMSIPRE="12302";
  ```
  %%LST PDPFILTERAPN: SUBRANGE=IMSI_PREFIX, IMSIPRE="12302";%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   用户范围      IMSI前缀  APNNI        优先级  描述  

   指定IMSI前缀  12302     HUAWEI4.COM  1       NULL  
   指定IMSI前缀  12302     HUAWEI5.COM  2       NULL  
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PDPFILTERAPN.md`
