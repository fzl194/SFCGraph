---
id: UNC@20.15.2@MMLCommand@DSP CHGFILE
type: MMLCommand
name: DSP CHGFILE（显示硬盘话单文件信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CHGFILE
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 计费控制
status: active
---

# DSP CHGFILE（显示硬盘话单文件信息）

## 功能

**适用网元：SGSN**

该命令用于查询指定SPU硬盘上的话单文件信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅能查询CDP进程状态且硬盘状态正常的SPU上的话单文件，若CDP进程故障或SPU故障，请处理相关故障后再进行查询。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询的资源单元名称。该参数可以通过<br>[DSP RU](../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0～63位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGFILE]] · 硬盘话单文件信息（CHGFILE）

## 使用实例

查询SPU上硬盘的话单文件信息：

DSP CHGFILE: RUNAME="USN_SP_RU_0064";

```
%%DSP CHGFILE: RUNAME="USN_SP_RU_0064";%%
RETCODE = 0  操作成功。

输出结果如下
--------------
                         RU名称  =  USN_SP_RU_0064 
               硬盘剩余空间(MB)  =  55974
              硬盘剩余空间率(%)  =  93
       硬盘保存的正确话单文件数  =  0
     硬盘保存的正确R9话单文件数  =  0
     硬盘保存的正确R7话单文件数  =  0
     硬盘保存的正确R6话单文件数  =  0
     硬盘保存的正确R5话单文件数  =  0
     硬盘保存的正确R4话单文件数  =  0
    硬盘保存的正确R99话单文件数  =  0
    硬盘保存的正确R98话单文件数  =  0
       硬盘保存的损坏话单文件数  =  0
 硬盘保存的CG解码错误话单文件数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示硬盘话单文件信息(DSP-CHGFILE)_26305192.md`
