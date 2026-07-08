---
id: UNC@20.15.2@MMLCommand@LST SCCPSSN
type: MMLCommand
name: LST SCCPSSN（查询SCCP子系统）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCCPSSN
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
- SCCP子系统
status: active
---

# LST SCCPSSN（查询SCCP子系统）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用来查询SCCP子系统表中指定的记录。

## 注意事项

未输入参数，表示查询所有记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SSNX | 子系统索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定子系统对应的索引值。<br>取值范围：0~2047<br>默认值：无 |
| SSNNAME | 子系统名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定子系统名。<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPSSN]] · SCCP子系统（SCCPSSN）

## 使用实例

查询所有子系统信息：

LST SCCPSSN:;

```
%%LST SCCPSSN:;%%
RETCODE = 0  操作成功。

SCCP子系统表
------------
 子系统索引  子系统号    网络指示语  目的信令点编码  本局信令点编码  子系统名     负荷分担类型  备用子系统索引

 0           SCMG(1)     国内备用网  0x2301          0x2301          IuC          不使用        NULL          
 1           RANAP(142)  国内备用网  0x2301          0x2301          IuC          不使用        NULL          
 375         SCMG(1)     国内备用网  0x3373          0x2301          IuC_BCMK     不使用        NULL          
 376         RANAP(142)  国内备用网  0x3373          0x2301          IuC_BCMK     不使用        NULL          
 2           SCMG(1)     国内网      0x102301        0x102301        Gr           不使用        NULL          
 3           SGSN(149)   国内网      0x102301        0x102301        Gr           不使用        NULL          
 377         SCMG(1)     国内网      0x103701        0x102301        Gr_BCMK      不使用        NULL    
(结果个数 = 7)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCCP子系统(LST-SCCPSSN)_72226013.md`
