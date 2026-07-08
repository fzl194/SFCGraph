---
id: UNC@20.15.2@MMLCommand@LST CHGPLMNCFG
type: MMLCommand
name: LST CHGPLMNCFG（查询PLMN计费配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGPLMNCFG
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- PLMN计费配置
status: active
---

# LST CHGPLMNCFG（查询PLMN计费配置）

## 功能

**适用网元：SGSN**

该命令用于查询话单生成策略相关配置。

## 注意事项

如果有输入参数，则显示与输入参数匹配的话单生成策略配置记录；如果没有输入参数，则显示所有话单生成策略配置记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “CELL_PLMNID（指定CELL_PLMNID）”<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示PLMN的移动国家号码。<br>取值范围：位数为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示PLMN的移动网号码。<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN网络标识。<br>取值范围：1～62位字符串<br>默认值：无<br>说明：- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGPLMNCFG]] · PLMN计费配置（CHGPLMNCFG）

## 使用实例

查询SUBRANGE="指定CELL_PLMNID" ,MCC="123", MNC="001"的话单生成策略，配置格式为：

LST CHGPLMNCFG: SUBRANGE=CELL_PLMNID,MCC="123", MNC="001";

```
%%LST CHGPLMNCFG: SUBRANGE=CELL_PLMNID, MCC="123", MNC="001";%%
RETCODE = 0  操作成功。

输出结果如下
--------------
             用户范围  =  指定CELL_PLMNID
           移动国家码  =  123
             移动网号  =  001
                APNNI  =  *
            生成S-CDR  =  生成
        周期生成S-CDR  =  有流量时周期生成
   S-CDR生成周期(min)  =  60
        流量生成S-CDR  =  生成
生成S-CDR流量阈值(KB)  =  1000
计费条件变更生成S-CDR  =  生成
 最大计费条件变更次数  =  3
    位置更新生成S-CDR  =  不生成
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PLMN计费配置(LST-CHGPLMNCFG)_26145392.md`
