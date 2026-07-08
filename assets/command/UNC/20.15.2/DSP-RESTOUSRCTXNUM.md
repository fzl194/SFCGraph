---
id: UNC@20.15.2@MMLCommand@DSP RESTOUSRCTXNUM
type: MMLCommand
name: DSP RESTOUSRCTXNUM（显示容灾用户数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RESTOUSRCTXNUM
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME容灾管理
- 容灾功能调测
status: active
---

# DSP RESTOUSRCTXNUM（显示容灾用户数）

## 功能

**适用网元：MME**

本命令用于查询系统内备份用户的数量。查询输出结果为查询时刻的备份用户数量。

输出结果分为2个报告，1个报表显示对应RU名称、进程的备份用户数；1个报表显示系统内总的备份用户数。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：本参数显示备份用户处在的RU名称。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：本端规划<br>取值范围：1~63字符串<br>默认值：无 |
| PRON | 进程号 | 可选必选说明：可选参数<br>参数含义：本参数表示备份用户处在的进程序号。<br>数据来源：本端规划<br>取值范围：0~20<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESTOUSRCTXNUM]] · 容灾用户数（RESTOUSRCTXNUM）

## 使用实例

- 查询本网元备份到对端UNC的用户数：
  DSP RESTOUSRCTXNUM: ;
  ```
  %%DSP RESTOUSRCTXNUM:;%%
  RETCODE = 0  操作成功。

  备份用户数量信息
  -----------------------------
  RU名称           进程号        MM上下文数         PDN连接数                    承载上下文数                     MM签约上下文数              APN/PDP签约上下文数                在线备份用户的MM签约上下文数            在线备份用户的APN/PDP签约上下文数
  USN_SP_RU_0065    5              0                        0                            0                            0                                   0                                    0                                             0                    
  USN_SP_RU_0064    0              0                        0                            0                            1                                   3                                    0                                             0                    
  USN_SP_RU_0064    1              0                        0                            0                            0                                   0                                    0                                             0                    
  USN_SP_RU_0064    2              0                        0                            0                            0                                   0                                    0                                             0                    
  USN_SP_RU_0064    3              0                        0                            0                            0                                   0                                    0                                             0                    
  USN_SP_RU_0064    4              0                        0                            0                            0                                   0                                    0                                             0                    
  USN_SP_RU_0064    5              0                        0                            0                            0                                   0                                    0                                             0                    
  USN_SP_RU_0065    0              0                        0                            0                            0                                   0                                    0                                             0                    
  USN_SP_RU_0065    1              0                        0                            0                            0                                   0                                    0                                             0                    
  USN_SP_RU_0065    2              0                        0                            0                            0                                   0                                    0                                             0                    
  USN_SP_RU_0065    3              0                        0                            0                            0                                   0                                    0                                             0                    
  USN_SP_RU_0065    4              0                        0                            0                            0                                   0                                    0                                             0                    
  仍有后续报告输出
  ---    END

  +++    usn        2017-02-16 07:52:59
  O&M    #HWHandle=211
  %%DSP RESTOUSRCTXNUM:;%%
  RETCODE = 0  操作成功。

                         MM上下文数  =  0
                          PDN连接数  =  0
                       承载上下文数  =  0
                     MM签约上下文数  =  1
                APN/PDP签约上下文数  =  3
       在线备份用户的MM签约上下文数  =  0
  在线备份用户的APN/PDP签约上下文数  =  0
  (结果个数 = 13)
  共有2个报告
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示容灾用户数(DSP-RESTOUSRCTXNUM)_72345719.md`
