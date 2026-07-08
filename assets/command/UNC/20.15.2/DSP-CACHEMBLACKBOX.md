---
id: UNC@20.15.2@MMLCommand@DSP CACHEMBLACKBOX
type: MMLCommand
name: DSP CACHEMBLACKBOX（查询CACHEM黑匣子诊断信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CACHEMBLACKBOX
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- CACHEM
status: active
---

# DSP CACHEMBLACKBOX（查询CACHEM黑匣子诊断信息）

## 功能

该命令用于查询CACHEM黑匣子诊断信息。不指定PID参数时，查询所有组件的黑匣子HA信息；当指定PID参数时，可以查询指定组件的黑匣子HA信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 诊断数据类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定诊断数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- HA：黑匣子HA信息。<br>- PATH：黑匣子Path信息。<br>- VERIFY：黑匣子Verify信息。<br>默认值：无 |
| PID | APP组件PID | 可选必选说明：条件可选参数<br>前提条件：该参数在“TYPE”配置为“HA”时为可选参数。<br>参数含义：该参数用来指定APP组件PID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |

## 操作的配置对象

- [CACHEM黑匣子诊断信息（CACHEMBLACKBOX）](configobject/UNC/20.15.2/CACHEMBLACKBOX.md)

## 使用实例

查询CACHEM黑匣子诊断信息：

```
DSP CACHEMBLACKBOX: TYPE=HA, PID="0x650009";
```

```

        RETCODE = 0  操作成功。

        结果如下
        --------
        查询结果数据  =  [Pid:0x650009]
        2017-3-28 19:29:19:40-00:00  [HA]Partner(6619145) state changed! 255 -> 0, event = 1
        2017-3-28 19:29:19:40-00:00  [HA]process smooth fsm :now SmoothFsm = 0,  rcv Event = 0
        2017-3-28 19:29:19:40-00:00  Notify smooth
        2017-3-28 19:29:19:47-00:00  [HA]Partner(0X650009) Snd SmoothTblBegin transNo(1), SmoothTblSeq(1)
        2017-3-28 19:29:19:47-00:00  [HA]process smooth fsm :now SmoothFsm = 1,  rcv Event = 2
        2017-3-28 19:29:19:47-00:00  [HA]process smooth fsm :Start Smooth
        2017-3-28 19:29:19:47-00:00  [HA]process smooth fsm :now SmoothFsm = 2,  rcv Event = 4
        2017-3-28 19:29:19:47-00:00  [HA]process smooth fsm :End Smooth
        2017-3-28 19:29:19:58-00:00  [HA]Partner SmoothTblBegin ack
        2017-3-28 19:29:19:59-00:00  [HA]Partner SmoothTblEnd ack
        2017-3-28 19:29:28:457-00:00  Notify Smooth End
        2017-3-28 19:29:28:457-00:00  Smooth End ACK

        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CACHEM黑匣子诊断信息（DSP-CACHEMBLACKBOX）_00440469.md`
