---
id: UNC@20.15.2@MMLCommand@LST AMFDNNPLCY
type: MMLCommand
name: LST AMFDNNPLCY（查询DNN接入选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFDNNPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- DNN接入选择策略管理
status: active
---

# LST AMFDNNPLCY（查询DNN接入选择策略）

## 功能

**适用NF：AMF**

该命令用于查询DNN接入选择策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNNI | DNN网络标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示DNN网络标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。输入指定的DNN NI，可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| SST | 切片业务类型 | 可选必选说明：可选参数<br>参数含义：该参数表示切片的业务类型，如eMBB（1）、URLLC（2）、MIoT（3）等协议定义的标准SST，或者运营商自定义的SST。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：可选参数<br>参数含义：该参数表示根据网络切片所提供的服务特点、所服务的对象差异，对某种网络切片的进一步细分。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFDNNPLCY]] · DNN接入选择策略（AMFDNNPLCY）

## 使用实例

- 查询一条DNN接入选择策略，“DNN网络标识”为“huawei.com”，“网络切片”为“eMBB”（SST=1），“切片细分标识”为“000001”，执行如下命令：
  ```
  +++    UNC/*MEID:0 MENAME:unc*/        2023-05-17 09:38:00+8:00
  O&M    #7422
  %%LST AMFDNNPLCY:DNNNI="huawei.com", SST=1, SD="000001";%%
  RETCODE = 0  操作成功

  输出结果如下
  ------------------------
                  DNN网络标识  =  HUAWEI.COM
                 切片业务类型  =  1
                 切片细分标识  =  000001
        是否携带Serving Scope  =  是
                     服务范围  =  pudong:puxi
                  是否使用TAI  =  否
  下一个Serving Scope映射类型  =  TAI
                  SMF重选次数  =  1
  (结果个数 = 1)

  ---    END
  ```
- 查询所有DNN接入选择策略，执行如下命令：
  ```
  +++    UNC/*MEID:0 MENAME:unc*/        2023-05-17 09:38:20+8:00
  O&M    #7423
  %%LST AMFDNNPLCY:;%%
  RETCODE = 0  操作成功

  输出结果如下
  ------------------------
  DNN网络标识                                                      切片业务类型  切片细分标识  是否携带Serving Scope  服务范围     是否使用TAI  下一个Serving Scope映射类型  SMF重选次数
                                                                                             
  012345678901234567890123456789012345678901234567890123456789012  0             AAAF09        是                     000          否           无效                         2   
  HUAWEI.COM                                                       1             000001        是                     pudong:puxi  否           TAI                          1  
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFDNNPLCY.md`
