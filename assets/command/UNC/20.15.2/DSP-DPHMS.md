---
id: UNC@20.15.2@MMLCommand@DSP DPHMS
type: MMLCommand
name: DSP DPHMS（显示MS上下文信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DPHMS
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- MS上下文
status: active
---

# DSP DPHMS（显示MS上下文信息）

## 功能

**适用网元：SGSN**

用于查询DISP模块（Gb公共上下文管理模块）、LLC层和SNDCP层的MS上下文信息。

## 注意事项

- 支持IMSI查询和TLLI查询。TLLI查询时，需要同时给定GBP进程的RU名称、进程号。
- MS上下文通过IMSI或TLLI唯一确定，此命令可以查询该MS用户在DISP模块、LLC层和SNDCP层的一些基本信息。
- 此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INPUT | 输入类型 | 可选必选说明：必选参数<br>参数含义： 参数输入类型 。<br>取值范围：<br>- “IMSI(IMSI)”<br>- “TLLI(TLLI)”<br>默认值： 无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义： 国际移动用户标识 。<br>前提条件：此参数在<br>“输入类型”<br>设置为<br>“IMSI(IMSI)”<br>后生效。<br>取值范围： 1～15位十进制数字字符串<br>默认值： 无 |
| RUNAME | RU名称 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>前提条件：此参数在<br>“输入类型”<br>设置为<br>“TLLI(TLLI)”<br>后生效。<br>取值范围：0~63位字符串<br>默认值：无 |
| PRON | 进程号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定待查询NSE属性信息所在的GBP进程的进程号。<br>前提条件：此参数在<br>“输入类型”<br>设置为<br>“TLLI(TLLI)”<br>后生效。<br>取值范围：0～20<br>默认值：无 |
| TLLI | TLLI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定TLLI。<br>前提条件：此参数在<br>“输入类型”<br>设置为<br>“TLLI(TLLI)”<br>后生效。<br>取值范围：0x00000000 - 0xffffffff(十六进制)<br>默认值： 无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DPHMS]] · MS上下文信息（DPHMS）

## 使用实例

查询IMSI号为123034800000002用户的Gb用户上下文信息 ：

DSP DPHMS: INPUT=IMSI, IMSI="123034800000002";

```
%%DSP DPHMS: INPUT=IMSI, IMSI="123034800000002";%%
RETCODE = 0  执行成功。
操作结果如下
-------------------------
            IMSI对应的TLLI  =  0xC0A40000
                  TLLI标识  =  0xC0A40000
              旧的TLLI标识  =  0xFFFFFFFF
                      IMSI  =  NULL
                LLME主状态  =  Suspend
	         加密算法  =  255
                GMM RU名称  =  USN_SP_RU_0065
                 GMM进程号  =  0
               GMM控制表号  =  0
              SNDCP RU名称  =  USN_SP_RU_0065
               SNDCP进程号  =  3
	    SNDCP控制表号  =  0
              BSSGP RU名称  =  USN_SP_RU_0065
               BSSGP进程号  =  3
             BSSGP控制表号  =  0
                      R 位  =  0
(结果个数 = 1)
继续...
---    END

%%DSP DPHMS: INPUT=IMSI, IMSI="123034800000002";%%
RETCODE = 0  执行成功。
操作结果如下
-------------------------
 SAPI    UI 帧窗口       V(U)    V(UR)   上行方向非确认方式溢出计数器(加密)                    下行方向非确认方式溢出计数器(加密)     
                                                                                                                                                                     
 1       3                1       232     0                                                          0                                                               
 2       0                0       0       0                                                          0                                                               
 7       0                0       0       0                                                          0                                                               
 8       0                0       0       0                                                          0                                                               
查询Gb MS上下文续
Version    IOV-UI    T200 and T201    N200    N201-U 
                                                     
0          0         50               3       400    
0          0         50               3       270    
0          0         200              3       270    
0          0         200              3       270    
(结果个数 = 4)
继续...
---    END

%%DSP DPHMS: INPUT=IMSI, IMSI="123034800000002";%%
RETCODE = 0  执行成功。

操作结果如下
-------------------------
 SAPI    UI 帧窗口       V(U)    V(UR)   上行方向非确认方式溢出计数器(加密)                    下行方向非确认方式溢出计数器(加密)  

 3       0                0       0       0                                                          0                                                            
 5       0                0       0       0                                                          0                                                            
 9       0                0       0       0                                                          0                                                            
 11      0                0       0       0                                                          0                                                            

查询Gb MS上下文续
上行方向确认方式溢出计数器(加密)                    下行方向确认方式溢出计数器(加密)                                Version     IOV-UI  IOV-I       T200 and T201  
                                                                                                                                                                    
0                                                        0                                                          0            0       402653184   50             
0                                                        0                                                          0            0       671088640   100            
0                                                        0                                                          0            0       1207959552  200            
0                                                        0                                                          0            0       1476395008  400            

查询Gb MS上下文续
N200    N201-I    N201-U    MD      MU      KD    KU    V(S)    V(R)    V(A)    V(Q)    Buffer
                                                                                              
3       1503      500       1520    1520    16    16    0       0       0       0       0     
3       1503      500       760     760     8     8     0       0       0       0       0     
3       1503      500       380     380     4     4     0       0       0       0       0     
3       1503      500       190     190     2     2     0       0       0       0       0     
(结果个数 = 4)
继续...
---    END

%%DSP DPHMS: INPUT=IMSI, IMSI="123034800000002";%%
RETCODE = 0  执行成功。
操作结果如下
-------------------------
SAPI    SAPI的状态          标识每个SAPI上已有的NSAPI总数                   标识SAPI上已有的确认NSAPI总数                             N201-I    N201-U

3       WITHOUT_ACK_LINK    0                                               0                                                         1503      500   
5       WITHOUT_ACK_LINK    0                                               0                                                         1503      500   
9       WITHOUT_ACK_LINK    0                                               0                                                         1503      500   
11      WITHOUT_ACK_LINK    0                                               0                                                         1503      500   
(结果个数 = 4)
共4个报告
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DPHMS.md`
