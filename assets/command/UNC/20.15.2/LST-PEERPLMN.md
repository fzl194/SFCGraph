---
id: UNC@20.15.2@MMLCommand@LST PEERPLMN
type: MMLCommand
name: LST PEERPLMN（查询对等PLMN配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PEERPLMN
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
- 网络管理
- 对等PLMN管理
status: active
---

# LST PEERPLMN（查询对等PLMN配置）

## 功能

**适用网元：SGSN、MME**

此命令用于查询对等PLMN配置记录。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREA | 区域范围 | 可选必选说明：可选参数<br>参数含义：该参数用于显示指定区域的标识类型的信息。<br>取值范围：<br>- “ALL（所有区域）”：表示该区域标识类型为所有区域。<br>- “PLMN（指定PLMN区域）”：表示该区域标识类型为指定PLMN区域。<br>- “LA（指定位置区）”：表示该区域标识类型为指定位置区。<br>- “RA（指定路由区）”：表示该区域标识类型为指定路由区。<br>- “TA（指定跟踪区）”：表示该区域标识类型为指定跟踪区。<br>- “AREAGP（区域群）”：表示该区域标识类型为区域群。<br>默认值：无<br>说明：- 本表“区域范围”为“AREAGP（区域群）”的记录不能与“区域范围”为“PLMN（指定PLMN区域）”、“LA（指定位置区）”、“RA（指定路由区）”或“TA（指定跟踪区）”的记录共存。<br>- 区域范围按照粒度从粗到细分为以下几个级别： 所有区域，指定PLMN区域，区域群，指定位置区，指定路由区，指定跟踪区。<br>- 相同粒度区域范围的各记录的区域范围不能交迭。<br>- 使用时先按照用户IMSI查找记录是否存在，然后按照位置区域查找是否存在对应记录，查找不到再使用较粗的区域粒度进行查找。<br>- 未配置在该表区域范围中的用户缺省不下发等价PLMN。 |
| MCC | 移动国家码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于显示指定移动国家代码的信息。<br>前提条件：该参数在当<br>“AREA（区域范围）”<br>不为<br>“ALL（所有区域）”<br>和<br>“AREAGP（区域群）”<br>时生效。<br>取值范围：位数为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件可选参数<br>参数含义：该参数用于显示指定移动网号的信息。<br>前提条件：该参数在当<br>“AREA（区域范围）”<br>不为<br>“ALL（所有区域）”<br>和<br>“AREAGP（区域群）”<br>时生效。<br>取值范围：位数为2或3的十进制数字<br>默认值： 无 |
| LAC | 位置区域码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于显示指定位置区域码的信息。<br>前提条件：该参数在当<br>“AREA（区域范围）”<br>为<br>“LA（指定位置区）”<br>或<br>“RA（指定路由区）”<br>时生效。<br>取值范围：0x0000~0xFFFF<br>默认值：无 |
| RAC | 路由区域码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于显示指定路由区域码的信息。<br>前提条件：该参数在当<br>“AREA（区域范围）”<br>为<br>“RA（指定路由区）”<br>时生效。<br>取值范围：0x00~0xFF<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于显示指定跟踪区域码的信息。<br>前提条件：该参数在当<br>“AREA（区域范围）”<br>为<br>“TA（指定跟踪区）”<br>时生效。<br>取值范围：0x0000~0xFFFF<br>默认值：无 |
| AREAID | 区域群标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定区域群标识。<br>前提条件：该参数在当<br>“AREA（区域范围）”<br>为<br>“AREAGP（区域群）”<br>时生效。<br>取值范围：1~50<br>默认值：无 |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户范围。<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>- “IMSI_RANGE（指定IMSI范围）”<br>- “SUBGP（用户群）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀。使用时按照IMSI最长匹配进行查询。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>取值范围：1~15位十进制数字字符串<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>取值范围：1~15位十进制数字字符串<br>默认值：无 |
| SUBID | 用户群标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定用户群标识 。<br>前提条件：只有<br>“用户范围”<br>为<br>“SUBGP（用户群）”<br>时，该参数才有效。<br>取值范围：1~100<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PEERPLMN]] · 对等PLMN配置（PEERPLMN）

## 使用实例

查询表中全部对等PLMN配置记录：

LST PEERPLMN:;

```
%%LST PEERPLMN:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
      区域范围  =  指定位置区
    移动国家码  =  123
      移动网号  =  03
    位置区域码  =  NULL
位置区域码范围  =  NULL
    路由区域码  =  NULL
路由区域码范围  =  NULL
    跟踪区域码  =  NULL
跟踪区域码范围  =  NULL
    区域群标识  =  NULL
      用户范围  =  所有用户
     对等PLMN1  =  123031
     对等PLMN2  =  456789
     对等PLMN3  =  NULL
     对等PLMN4  =  NULL
     对等PLMN5  =  NULL
     对等PLMN6  =  NULL
     对等PLMN7  =  NULL
     对等PLMN8  =  NULL
     对等PLMN9  =  NULL
    对等PLMN10  =  NULL
    对等PLMN11  =  NULL
    对等PLMN12  =  NULL
    对等PLMN13  =  NULL
    对等PLMN14  =  NULL
    对等PLMN15  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PEERPLMN.md`
