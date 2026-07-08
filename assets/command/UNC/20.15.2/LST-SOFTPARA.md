---
id: UNC@20.15.2@MMLCommand@LST SOFTPARA
type: MMLCommand
name: LST SOFTPARA（查询软件参数表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SOFTPARA
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 软件参数管理
- 软件参数
status: active
---

# LST SOFTPARA（查询软件参数表）

## 功能

**适用网元：SGSN、MME**

该命令用于查询软参配置记录。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DT | 参数类型 | 可选必选说明：必选参数<br>参数含义：待查询软件参数的数据类型。<br>取值范围：<br>- “BYTE(单字节类型)”<br>- “DWORD(无符号整数类型)”<br>- “STR(字符串类型)”<br>- “BYTE_EX(扩展单字节类型)”<br>- “DWORD_EX(扩展无符号整数类型)”<br>- “STR_EX(扩展字符串类型)”<br>- “BYTE_EX_B(扩展单字节类型B)”<br>- “DWORD_EX_B(扩展无符号整数类型B)”<br>- “STR_EX_B(扩展字符串类型B)”<br>默认值：无 |
| PARANUM | 参数索引 | 可选必选说明：可选参数<br>参数含义：待查询软件参数索引。<br>取值范围：1~512<br>默认值：无<br>配置原则：<br>- 当参数类型取值为“BYTE”时，参数索引的取值范围是“1~240”。<br>- 当参数类型取值为“DWORD”时，参数索引的取值范围是“1~60”。<br>- 当参数类型取值为“STR”时，参数索引的取值是“1”。<br>- 当参数类型取值为“BYTE_EX”时，参数索引的取值范围是“1~224”。<br>- 当参数类型取值为“DWORD_EX”时，参数索引的取值范围是“1~56”。<br>- 当参数类型取值为“STR_EX”时，参数索引的取值是“1”。<br>- 当参数类型取值为“BYTE_EX_B”时，参数索引的取值范围是“1~464”。<br>- 当参数类型取值为“DWORD_EX_B”时，参数索引的取值范围是“1~116”。<br>- 当参数类型取值为“STR_EX_B”时，参数索引的取值范围是“1”。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SOFTPARA]] · 软件参数表（SOFTPARA）

## 使用实例

查询当前参数索引为1的单字节类型软参的设置情况：

LST SOFTPARA: DT=BYTE, PARANUM=1;

```
%%LST SOFTPARA: DT=BYTE, PARANUM=1;%%
RETCODE = 0  操作成功。
查询软件参数表
--------------
参数类型  =  单字节类型
参数索引  =  1
  参数值  =  0x00(0)
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SOFTPARA.md`
