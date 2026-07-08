---
id: UNC@20.15.2@MMLCommand@LST SCCPOPC
type: MMLCommand
name: LST SCCPOPC（查询SCCP本局信令点）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCCPOPC
command_category: 查询类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP本局信令点
status: active
---

# LST SCCPOPC（查询SCCP本局信令点）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用来查询SCCP本局信令点表中指定的记录。

## 注意事项

- 没有输入参数，表示查询所有记录。
- 输入本局信令点索引，查询对应记录。
- 输入本局信令点名，查询对应记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPX | 本局信令点索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本局信令点索引。<br>取值范围：1～64<br>默认值：无 |
| OPN | 本局信令点名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本局信令点名。<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCCPOPC]] · SCCP本局信令点（SCCPOPC）

## 使用实例

查询SCCP本局信令点表中所有记录：

LST SCCPOPC:;

```
%%LST SCCPOPC:;%%
RETCODE = 0  操作成功。

SCCP本局信令点表
----------------
 本局信令点索引  网络指示语  本局信令点编码  信令点用途  本局SGSN号    本局信令点名

 1               国内网      0x240012        CORE ONLY   861390211201  Peking      
 2               国内备用网  0x1419          IU ONLY     NULL          Peking      
（结果个数 = 2）

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SCCPOPC.md`
