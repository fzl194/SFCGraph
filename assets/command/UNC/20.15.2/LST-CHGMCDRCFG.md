---
id: UNC@20.15.2@MMLCommand@LST CHGMCDRCFG
type: MMLCommand
name: LST CHGMCDRCFG（查询M-CDR计费配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGMCDRCFG
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 基于PLMN的M-CDR计费配置
status: active
---

# LST CHGMCDRCFG（查询M-CDR计费配置）

## 功能

**适用网元：SGSN**

本命令用于查询对特定PLMN用户生成M-CDR的配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “PLMNID（指定PLMNID）”<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示PLMN的移动国家号码。<br>前提条件：该参数在“用户范围”参数设置为“PLMNID（指定PLMNID）”时生效。<br>数据来源：整网规划<br>取值范围：位数为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示PLMN的移动网号码。<br>前提条件：该参数在“用户范围”参数设置为“PLMNID（指定PLMNID）”时生效。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGMCDRCFG]] · M-CDR计费配置（CHGMCDRCFG）

## 使用实例

查询对特定PLMN用户生成M-CDR的配置。

```
%%LST CHGMCDRCFG:;%% 
RETCODE = 0  操作成功 
操作结果如下 
------------------------ 
用户范围  移动国家码  移动网号    
PLMNID           460        03                    
PLMNID           460        04                   
(结果个数 = 2)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询M-CDR计费配置(LST-CHGMCDRCFG)_09617638.md`
