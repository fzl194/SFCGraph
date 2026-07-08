---
id: UNC@20.15.2@MMLCommand@DSP SDAPRSTCNT
type: MMLCommand
name: DSP SDAPRSTCNT（显示SDAP实体重启计数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SDAPRSTCNT
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- Sdup接口管理
- Sdup接口调测
status: active
---

# DSP SDAPRSTCNT（显示SDAP实体重启计数）

## 功能

**适用网元：MME**

本命令用于查询SDAP(Sdup Application Protocol)实体的重启计数。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug；visit-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；G_4，来宾级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SDAPRSTCNT]] · SDAP实体重启计数（SDAPRSTCNT）

## 使用实例

显示SDAP实体重启计数信息：

DSP SDAPRSTCNT:;

```
+++    mcr        2017-02-16 02:50:46
O&M    #HWHandle=37
%%DSP SDAPRSTCNT:;%%
RETCODE = 0  操作成功

操作结果如下:
-------------------------
RU名称           进程号       重启计数         文件状态

MCR_SP_RU_0064    0              55               正常   
MCR_SP_RU_0064    1              65               正常   
MCR_SP_RU_0064    2              229              正常   
MCR_SP_RU_0064    12             145              正常   
MCR_SP_RU_0064    11             65               正常   
MCR_SP_RU_0064    9              30               正常   
MCR_SP_RU_0064    10             225              正常   
MCR_SP_RU_0064    4              69               正常   
MCR_SP_RU_0064    3              68               正常   
MCR_SP_RU_0064    5              119              正常   
MCR_SP_RU_0064    8              214              正常   
MCR_SP_RU_0064    13             56               正常   
MCR_SP_RU_0064    6              33               正常   
MCR_SP_RU_0064    7              94               正常   
(结果个数 = 14)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示SDAP实体重启计数(DSP-SDAPRSTCNT)_26307106.md`
