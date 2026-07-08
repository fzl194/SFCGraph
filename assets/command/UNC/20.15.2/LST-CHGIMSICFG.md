---
id: UNC@20.15.2@MMLCommand@LST CHGIMSICFG
type: MMLCommand
name: LST CHGIMSICFG（查询IMSI计费配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGIMSICFG
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- IMSI计费配置
status: active
---

# LST CHGIMSICFG（查询IMSI计费配置）

## 功能

**适用网元：SGSN**

该命令用于查询基于 [**ADD CHGIMSICFG**](增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md) 命令配置的计费相关配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无<br>说明：如果有输入参数，则显示与输入参数匹配的IMSI prefix计费配置记录； 如果没有输入参数，则显示所有IMSI prefix计费配置记录。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于系统根据指定用户的IMSI进行匹配，从而区分不同的用户群。<br>取值范围：5～15位十进制字符串<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN网络标识。<br>取值范围：1～62个字符<br>默认值：无<br>说明：- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

## 操作的配置对象

- [IMSI计费配置（CHGIMSICFG）](configobject/UNC/20.15.2/CHGIMSICFG.md)

## 使用实例

查询 “IMSI前缀” 为 “123036” 、 “APNNI” 值为 “1” 配置格式为：

LST CHGIMSICFG: SUBRANGE=IMSI_PREFIX, IMSIPRE="123036", APNNI="1";

```
%%LST CHGIMSICFG:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
             用户范围  =  指定IMSI前缀
             IMSI前缀  =  123036
             拜访类型  =  使用归属地GGSN的漫游用户
                APNNI  =  1
             计费属性  =  实时计费
            生成S-CDR  =  缺省策略
        周期生成S-CDR  =  缺省策略
   S-CDR生成周期(min)  =  0
        流量生成S-CDR  =  缺省策略
生成S-CDR流量阈值(KB)  =  0
计费条件变更生成S-CDR  =  缺省策略
 最大计费条件变更次数  =  0
    位置更新生成S-CDR  =  缺省策略
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IMSI计费配置(LST-CHGIMSICFG)_72344987.md`
