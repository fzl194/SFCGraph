---
id: UNC@20.15.2@MMLCommand@DSP CB
type: MMLCommand
name: DSP CB（显示CB表）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CB
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
- 扩展调测
- 公共信令调测
- CB表
status: active
---

# DSP CB（显示CB表）

## 功能

**适用网元：SGSN、MME**

该命令用于查询控制表的占用情况。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63 位字符串<br>默认值：无 |
| SPPNO | 进程号 | 可选必选说明：必选参数<br>参数含义：该参数用于设置需要查询的SPP进程的进程号。<br>取值范围：0~20<br>默认值：无 |
| PIDNO | PID号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定功能子模块号。<br>取值范围：<br>- “MM(MM)”<br>- “SM(SM)”<br>- “UDM(UDM)”<br>默认值：无<br>说明：参数取值“UDM(UDM)”为保留值。 |
| FR | 强制释放Cb | 可选必选说明：可选参数<br>参数含义：该参数用于强制释放指定的CB。<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>。<br>说明：强制释放可能会打断该CB关联用户的当前流程。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CB]] · CB表（CB）

## 使用实例

查询控制表的占用情况：

DSP CB: RUNAME="USN_SP_RU_0066", SPPNO=0, PIDNO=MM;

```
%%DSP CB: RUNAME="USN_SP_RU_0066", SPPNO=0, PIDNO=MM;%%
RETCODE = 0 执行成功。
 
查询结果如下
-----------
                RU名称  =  USN_SP_RU_0066
                进程号  =  0
                 PID号  =  MM
           使用中的CB数 =  0
         最大使用的CB数 =  6000
       MM_DEREGISTERED  =  0
         MM_REGISTIDLE  =  0
        MM_REGISTCONNT  =  0
             MM_ATTACH  =  0
          MM_UE_DETACH  =  0
          MM_CN_DETACH  =  0
         MM_S1_RELEASE  =  0
        MM_SERVICE_REQ  =  0
             MM_PAGING  =  0
      MM_INTRA_TAU_NEW  =  0
      MM_INTRA_TAU_OLD  =  0
      MM_INTER_TAU_NEW  =  0
      MM_INTER_TAU_OLD  =  0
              MM_GUARD  =  0
MM_PATHSWITCH_HANDOVER  =  0
 MM_INTRA_HANDOVER_NEW  =  0
 MM_INTRA_HANDOVER_OLD  =  0
 MM_INTER_HANDOVER_NEW  =  0
 MM_INTER_HANDOVER_OLD  =  0
       MM_GUTI_REALLOC  =  0
         MM_IU_RELEASE  =  0
          MM_INTRA_RAU  =  0
      MM_INTER_RAU_NEW  =  0
      MM_INTER_RAU_OLD  =  0
   MM_INTRA_SRNS_RELOC  =  0
    MM_INTER_RELOC_NEW  =  0
    MM_INTER_RELOC_OLD  =  0
          MM_UECTX_MOD  =  0
            MM_COM_SEC  =  0
        MM_PTMSI_RELOC  =  0
(结果个数 = 1)
 
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示CB表(DSP-CB)_72345479.md`
