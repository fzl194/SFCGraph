---
id: UNC@20.15.2@MMLCommand@LST AMFSBICMPT
type: MMLCommand
name: LST AMFSBICMPT（查询AMF服务化接口兼容性参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFSBICMPT
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM协议参数管理
- AMF服务化接口兼容性参数管理
status: active
---

# LST AMFSBICMPT（查询AMF服务化接口兼容性参数）

## 功能

**适用NF：AMF**

该命令用于查询AMF服务化接口兼容性参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SBITYPE | 服务化接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务化接口类型，根据接口类型来确认是否需要配置相应的消息接口兼容性。<br>数据来源：全网规划<br>取值范围：<br>- N8（AMF与UDM之间的接口）<br>- N11（AMF与SMF之间的接口）<br>- N12（AMF与AUSF之间的接口）<br>- N14（AMF与AMF之间的接口）<br>- N15（AMF与PCF之间的接口）<br>- N17（AMF与5G-EIR之间的接口）<br>- N20（AMF与SMSF之间的接口）<br>- N22（AMF与NSSF之间的接口）<br>- N50（AMF与CBCF之间的接口）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFSBICMPT]] · AMF服务化接口兼容性参数（AMFSBICMPT）

## 使用实例

查询AMF服务化接口兼容性参数，执行如下命令：

```
%%LST AMFSBICMPT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                     时区变更是否通知SMF  =  否
                   是否给SMSF携带RATTYPE  =  否
                      是否携带RedCap指示  =  是
                    是否携带eDRX私有信元  =  否
                         是否携带PcfRfsp  =  否
                          是否携带动态NI  =  是
  是否携带UE Radio Capability for Paging  =  是
                   N15接口是否携带hpcfId  =  是
                    N14接口是否携带pcfId  =  是
                 N14接口是否携带pcfSetId  =  是
           N14接口是否携带pcfAmPolicyUri  =  是
   N14接口是否携带amPolicyReqTriggerList  =  是
                   N14接口是否携带hpcfId  =  是
               N14接口是否携带smfSelInfo  =  是
N14接口是否携带PEIPS信元以及寻呼分组标识  =  否
           N14接口是否携带pcfUePolicyUri  =  是
   N14接口是否携带uePolicyReqTriggerList  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF服务化接口兼容性参数（LST-AMFSBICMPT）_48331685.md`
