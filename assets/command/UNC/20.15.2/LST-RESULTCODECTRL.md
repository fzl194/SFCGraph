---
id: UNC@20.15.2@MMLCommand@LST RESULTCODECTRL
type: MMLCommand
name: LST RESULTCODECTRL（查询返回码控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESULTCODECTRL
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 信令控制
- 返回码控制
status: active
---

# LST RESULTCODECTRL（查询返回码控制）

## 功能

**适用NF：PGW-C、SMF**

此命令用来查询指定返回码控制信息或所有返回码控制信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCTEMPLATE | PCC模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置该返回码所绑定的PCC模板。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| VENDORID | 设备提供商标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INTFTYPE”配置为“INTFTYPE_GX”时为可选参数。<br>参数含义：设备提供商标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |
| N7RESULTCODEVAL | N7返回码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INTFTYPE”配置为“INTFTYPE_N7”时为可选参数。<br>参数含义：N7返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～3。300-599或者3xx-5xx，不区分大小写。其中xx代表一个范围，例如3xx代表300~399。<br>默认值：无<br>配置原则：<br>- 超时返回码504不受该配置控制，而是执行一次failover操作，若failover失败则根据APN/DNN绑定的PCCTEMPLATE或全局用户PCCFAILACTION相关配置获取失败动作。其中，APN/DNN绑定的PCCTEMPLATE配置优先级高。<br>- 配置的单个的返回码落在一个范围内时，单个的优先级高。 |
| INTFTYPE | 接口类型 | 可选必选说明：可选参数<br>参数含义：接口类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- INTFTYPE_N7：N7接口类型。<br>- INTFTYPE_GX：Gx接口类型。<br>默认值：无<br>配置原则：无 |
| GXRESULTCODEVAL | Gx返回码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INTFTYPE”配置为“INTFTYPE_GX”时为可选参数。<br>参数含义：返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～4。1000-9999，1xxx-9xxx，不区分大小写。其中xxxx代表一个范围，例如1xxx代表1000~1999。配置的单个的返回码落在一个范围内时，单个的优先级高。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RESULTCODECTRL]] · 返回码控制（RESULTCODECTRL）

## 使用实例

- 查询VENDORID为0的返回码控制信息：
  ```
  LST RESULTCODECTRL: PCCTEMPLATE="global", INTFTYPE=INTFTYPE_GX, VENDORID=0;
  ```
  ```

  RETCODE = 0  操作成功

  PCC返回码控制
  -------------
                                PCC模板名称  =  global
                                   N7返回码  =  599
                             设备提供商标识  =  0
          Initial流程回滚后使能Holding-Time  =  不使能
           Update流程回滚后使能Holding-Time  =  不使能
  直连对端Initial流程回滚后使能Holding-Time  =  不使能
                         直连对端重激活请求  =  缺省取值
                               重新激活请求  =  缺省取值
              直连对端Terminate流程处理动作  =  无效值
                直连对端Initial流程处理动作  =  无效值
   直连对端Update流程回滚后使能Holding-Time  =  不使能
                 直连对端Update流程处理动作  =  无效值
                         Update流程处理动作  =  宕机备份
                        Initial流程处理动作  =  缺省动作
                      Terminate流程处理动作  =  缺省动作
                                   接口类型  =  Gx接口类型
                                   Gx返回码  =  5xxx
  (结果个数 = 1)

  ---    END
  ```
- 查询所有返回码控制信息：
  ```
  LST RESULTCODECTRL:;
  ```
  ```

  RETCODE = 0  操作成功

  PCC返回码控制
  -------------
  PCC模板名称  N7返回码  设备提供商标识  Initial流程回滚后使能Holding-Time  Update流程回滚后使能Holding-Time  直连对端Initial流程回滚后使能Holding-Time  直连对端重激活请求  重新激活请求  直连对端Terminate流程处理动作  直连对端Initial流程处理动作  直连对端Update流程回滚后使能Holding-Time  直连对端Update流程处理动作  Update流程处理动作  Initial流程处理动作            Terminate流程处理动作  接口类型    Gx返回码  

  global       599       0               不使能                             不使能                            不使能                                     缺省取值            缺省取值      无效值                         无效值                       不使能                                    无效值                      宕机备份            缺省动作                       缺省动作               Gx接口类型  5xxx      
  pcctemplate  599       10415           不使能                             不使能                            不使能                                     缺省取值            缺省取值      无效值                         无效值                       不使能                                    无效值                      宕机备份            回滚为本地PCC用户使用本地策略  继承                   Gx接口类型  5140      
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RESULTCODECTRL.md`
