---
id: UNC@20.15.2@MMLCommand@DSP CACHEMCMDDATA
type: MMLCommand
name: DSP CACHEMCMDDATA（查询CACHEM命令信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CACHEMCMDDATA
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

# DSP CACHEMCMDDATA（查询CACHEM命令信息）

## 功能

该命令用于查询CACHEM命令信息。ISSLAVE是可选参数，ISSLAVE默认值是Master。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 诊断数据类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定诊断数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TABLESUB_INFO：表项订阅信息。<br>默认值：无 |
| ISSLAVE | 主备类型 | 可选必选说明：可选参数<br>参数含义：该参数用来指定主备类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Master：主资源单元。<br>- Slave：备资源单元。<br>默认值：Master |
| PID | APP组件PID | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“TABLESUB_INFO”时为必选参数。<br>参数含义：该参数用来指定APP组件PID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| PATHID | Path ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“TYPE”配置为“TABLESUB_INFO”时为必选参数。<br>参数含义：该参数用来指定Path ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CACHEMCMDDATA]] · CACHEM命令信息（CACHEMCMDDATA）

## 使用实例

查询CACHEM命令信息：

```
DSP CACHEMCMDDATA: TYPE=TABLESUB_INFO, PID="0x650018", PATHID="0x56";
```

```

        RETCODE = 0  操作成功。

        结果如下
        --------
        查询结果数据

        SegId:0x40002b2
          No Query Entry! QueryStatus[PATH REASON OK],Tbltype[31],keyType[30]
          Key Data:0 0 0 0 2f a0 30 d 71 0 0 0
          QueryStatus[PATH REASON OK],Tbltype[96],keyType[41],SubState[3],ItemStatus[2]
          Key Data:0 0 0 0 1 0 0 0 2 0 0 0
          QueryStatus[PATH REASON OK],Tbltype[1],keyType[1],SubState[3],ItemStatus[2]
          Key Data:0 0 0 0 1 0 0 0 f7 7 64 bd 20 0 0 0
          QueryStatus[PATH REASON OK],Tbltype[5],keyType[2],SubState[3],ItemStatus[2]
          Key Data:3 0 0 0

        SegId:0x100002b4

        SegId:0xc0002b3
          No Query Entry! QueryStatus[PATH REASON OK],Tbltype[86],keyType[42]
          Key Data:0 0 0 0 3 0 0 0
          QueryStatus[PATH REASON OK],Tbltype[5],keyType[2],SubState[3],ItemStatus[2]
          Key Data:3 0 0 0
          QueryStatus[PATH REASON OK],Tbltype[79],keyType[2],SubState[3],ItemStatus[2]
          Key Data:3 0 0 0
          QueryStatus[PATH REASON OK],Tbltype[2],keyType[2],SubState[3],ItemStatus[2]
          Key Data:3 0 0 0
          QueryStatus[PATH REASON OK],Tbltype[21],keyType[2],SubState[3],ItemStatus[2]
          Key Data:3 0 0 0
          No Query Entry! QueryStatus[NO],Tbltype[71],keyType[21]
          Key Data:0 0 0 0
          QueryStatus[PATH REASON OK],Tbltype[34],keyType[2],SubState[3],ItemStatus[2]
          Key Data:3 0 0 0
          QueryStatus[PATH REASON OK],Tbltype[3],keyType[3],SubState[3],ItemStatus[2]
          Key Data:3 0 0 0 f7 7 64 bd
          QueryStatus[PATH REASON OK],Tbltype[52],keyType[2],SubState[3],ItemStatus[2]
          Key Data:3 0 0 0
          QueryStatus[PATH REASON OK],Tbltype[5],keyType[2],SubState[3],ItemStatus[2]
          Key Data:6 0 0 0
          QueryStatus[PATH REASON OK],Tbltype[2],keyType[2],SubState[3],ItemStatus[2]
          Key Data:6 0 0 0
          QueryStatus[PATH REASON OK],Tbltype[21],keyType[2],SubState[3],ItemStatus[2]
          Key Data:6 0 0 0
          No Query Entry! QueryStatus[NO],Tbltype[31],keyType[30]
          Key Data:f0 3 0 0 30 a0 30 d 78 0 0 0
          QueryStatus[PATH REASON OK],Tbltype[50],keyType[26],SubState[0],ItemStatus[0]
          Key Data:1 0 0 0
          No Query Entry! QueryStatus[PATH REASON OK],Tbltype[31],keyType[30]
          Key Data:1 ff 1 0 b8 a6 30 d 78 0 0 0

        (结果个数 = 3)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CACHEM命令信息（DSP-CACHEMCMDDATA）_49802362.md`
