---
id: UNC@20.15.2@MMLCommand@LST GTPUINTFATTR
type: MMLCommand
name: LST GTPUINTFATTR（查询GTP-U IP地址接口属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPUINTFATTR
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-U接口管理
- GTP-U接口类型属性
status: active
---

# LST GTPUINTFATTR（查询GTP-U IP地址接口属性）

## 功能

**适用网元：SGSN、MME**

该命令用于查询GTPU IP地址在指定的接口使用，或者在指定的用户范围内使用的GTPU IP地址的组号。

## 注意事项

- 该命令执行后立即生效。
- 所有参数不输入，表示查询所有已存在的记录。
- 仅指定接口类型时，表示查询与之匹配的接口类型对应的记录。
- 仅指定用户范围类型，不指定运营商标识或者不指定IMSI前缀，表示查询与之匹配的用户范围类型对应的记录。
- 仅指定运营商标识时，表示查询与之匹配的运营商标识对应的记录。
- 仅指定IMSI前缀时，表示查询与之最长匹配的IMSI前缀对应的记录。
- 同时指定接口类型与用户范围类型，表示查询与之匹配的接口类型和用户范围类型对应的记录。
- 同时指定接口类型与运营商标识，表示查询与之匹配的接口类型和运营商标识对应的记录。
- 同时指定接口类型与IMSI前缀，表示查询与之匹配的接口类型和最长匹配的IMSI前缀对应的记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTPC IP地址适用的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”<br>- “SPECIAL_NOID(指定运营商)”<br>默认值：无<br>说明：- GTPU IP地址使用的优先级从高到低为：<br>- 指定接口类型+“SPECIAL_IMSIPRE（指定IMSI前缀）”。<br>- “ALL_INTERFACE（所有接口类型）”+“SPECIAL_IMSIPRE（指定IMSI前缀）”。<br>- 指定接口类型+“SPECIAL_NOID（指定运营商）”。<br>- “ALL_INTERFACE（所有接口类型）”+“SPECIAL_NOID（指定运营商）”。<br>- 指定接口类型+“ALL_USER（所有用户）”。<br>- “ALL_INTERFACE（所有接口类型）”+“ALL_USER（所有用户）”。 |
| NOID | 运营商标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定运营商标识<br>前提条件：该参数在"用户范围"参数配置为"SPECIAL_NOID(指定运营商)"后生效。<br>数据来源：本端规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：如果输入为空，表示查询所有“指定运营商标识”的记录。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定用户的IMSI前缀。使用时按照输入IMSI最长匹配进行查询，输出包含最长匹配IMSI前缀的记录。<br>前提条件：该参数在"用户范围"参数配置为"SPECIAL_IMSIPRE(指定IMSI前缀)"后生效。<br>数据来源：本端规划<br>取值范围：1~15位十进制数<br>默认值：无<br>配置原则：如果输入为空，表示查询所有“指定IMSI前缀”的记录。 |
| INTFTP1 | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTPU IP地址适用的接口类型。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “GN-SGSN/S16(Gn-SGSN/S16)”<br>- “Iu(IU)”<br>- “S11(S11)”<br>- “S4(S4)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPUINTFATTR]] · GTP-U IP地址接口属性（GTPUINTFATTR）

## 使用实例

查询GTPU IP地址接口属性：

LST GTPUINTFATTR:;

```
%%LST GTPUINTFATTR:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------

用户范围                        运营商标识                       IMSI前缀          接口类型                     组号          记录索引         描述信息 

所有用户                        NULL                             NULL              所有接口                     0             0                initial 
所有用户                        NULL                             NULL              IU                           32            1                IU interface group 
指定IMSI前缀                    NULL                             123456            所有接口                     1             2                huawei 
指定运营商                      128                              NULL              Gn-SGSN/S16                  1             3                huawei 

(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTP-U-IP地址接口属性(LST-GTPUINTFATTR)_72345585.md`
