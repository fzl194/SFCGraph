---
id: UNC@20.15.2@MMLCommand@DSP NSE
type: MMLCommand
name: DSP NSE（显示NSE属性信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NSE
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- 信令实体管理
status: active
---

# DSP NSE（显示NSE属性信息）

## 功能

**适用网元：SGSN**

此命令用于查询自动上报的动态over IP的NSE的属性信息。通过 [**ADD NSE**](增加信令实体(ADD NSE)_26146028.md) 命令手动配置的NSE信息请使用 [**LST NSE**](查询信令实体（LST NSE）_72345629.md) 命令查询。

## 注意事项

- 此命令执行后立即生效。
- 系统最大支持8192个动态NSE，每个进程最大可配置1024个动态NSE。
- “NSE标识”与“RU名称”和“进程号”不能同时输入。
- 当输入“进程号”时，必须同时输入“RU名称”。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEIFLTP | “NSE标识”筛选方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定以<br>“NSE标识”<br>作为查询关键字的筛选方式。当<br>“NSE标识”<br>参数输入时，本参数将控制<br>“NSE标识”<br>输入值的查询方式。当<br>“NSE标识”<br>参数未输入时，本参数不起作用。<br>取值范围：<br>- “EQUAL（等于）”<br>- “NOT_EQ（不等于）”<br>- “NOT_LESS（不小于）”<br>- “NOT_LARGER（不大于）”<br>- “RANGE（范围）”<br>默认值：<br>“EQUAL（等于）”<br>说明：若要按上限数字和下限数字进行筛选，请选择<br>“RANGE（范围）”<br>。 |
| BNSEI | NSE标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询NSE属性信息的网络服务实体标识。<br>取值范围：0~65535<br>默认值：无<br>说明：当NSEIFLTP设置为<br>“RANGE（范围）”<br>时，本参数表示“起始NSE标识”。 |
| ENSEI | 结束NSE标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定网络服务实体标识。<br>前提条件：该参数在NSEIFLTP参数设置为<br>“RANGE（范围）”<br>时，才需要配置。<br>取值范围：0~65535<br>默认值：无<br>说明：当NSEIFLTP设置为<br>“RANGE（范围）”<br>时，本参数与<br>“NSE标识”<br>参数都必须输入，并且要求<br>“结束NSE标识”<br>的值必须大于或等于<br>“NSE标识”<br>的值。 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63位字符串<br>默认值：无 |
| PRON | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询NSE属性信息所在的GBP进程的进程号。<br>取值范围：0～20<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSE]] · 信令实体（NSE）

## 使用实例

查询系统所有NSE：

DSP NSE: NSEIFLTP=EQUAL;

```
 
%%DSP NSE: NSEIFLTP=EQUAL;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
                       NSE标识  =  14904
                        RU名称  =  GB_SP_RU_0066
                        进程号  =  1
                       BSS编号  =  14904
           FLUSH监控定时器(ms)  =  50
                   是否支持PFC  =  是
                   是否支持CBL  =  是
                   是否支持INR  =  是
                   是否支持LCS  =  否(BSS侧不支持,SGSN侧不支持)
                   是否支持RIM  =  否(BSS侧不支持,SGSN侧不支持)
               是否携带ARP信元  =  否
     是否携带RA Capability信元  =  否
               是否支持Gb-Flex  =  否
          是否支持特殊业务类型  =  否
              BSS支持的Qos版本  =  R99
                  是否支持MOCN  =  否(BSS侧不支持,SGSN侧不支持)
                  是否支持SPID  =  否
(结果个数 = 1)
---    END
```

查询 “NSE标识” 为 “14904” 的NSE属性信息：

DSP NSE: NSEIFLTP=EQUAL, BNSEI=14904;

```
%%DSP NSE: NSEIFLTP=EQUAL, BNSEI=14904;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
                       NSE标识  =  14904
                        RU名称  =  GB_SP_RU_0066
                        进程号  =  1
                       BSS编号  =  14904
           FLUSH监控定时器(ms)  =  50
                   是否支持PFC  =  是
                   是否支持CBL  =  是
                   是否支持INR  =  是
                   是否支持LCS  =  否(BSS侧不支持,SGSN侧不支持)
                   是否支持RIM  =  否(BSS侧不支持,SGSN侧不支持)
               是否携带ARP信元  =  否
     是否携带RA Capability信元  =  否
               是否支持Gb-Flex  =  否
          是否支持特殊业务类型  =  否
              BSS支持的Qos版本  =  R99
                  是否支持MOCN  =  否(BSS侧不支持,SGSN侧不支持)
                  是否支持SPID  =  否
(结果个数 = 1)
---    END
```

查询系统中RU名称为“GB_SP_RU_0066”的NSE：

DSP NSE: NSEIFLTP=EQUAL, RUNAME="GB_SP_RU_0066";

```
 
%%DSP NSE: NSEIFLTP=EQUAL, RUNAME="GB_SP_RU_0066"%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
NSE标识   RU名称            进程号         BSS编号    FLUSH监控定时器(ms)    是否支持PFC   是否支持CBL   是否支持INR      是否支持LCS                        是否支持RIM                    是否携带ARP信元     是否携带RA Capability信元    是否支持Gb-Flex     是否支持特殊业务类型            BSS支持的Qos版本         是否支持MOCN                    是否支持SPID 

14904     GB_SP_RU_0066    3              14904      50                     是            是            是               否(BSS侧不支持,SGSN侧不支持)       否(BSS侧不支持,SGSN侧不支持)    否                 否                           否                 否                               R99                      否(BSS侧不支持,SGSN侧不支持)    否           
14903     GB_SP_RU_0066    2              14903      50                     是            是            是               否(BSS侧不支持,SGSN侧不支持)       否(BSS侧不支持,SGSN侧不支持)    否                 否                           否                 否                               R99                      否(BSS侧不支持,SGSN侧不支持)    否           
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NSE属性信息（DSP-NSE）_26146030.md`
