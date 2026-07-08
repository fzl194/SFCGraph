---
id: UNC@20.15.2@MMLCommand@LST NRFTAKEPARARULE
type: MMLCommand
name: LST NRFTAKEPARARULE（查询NF携带参数处理规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFTAKEPARARULE
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NF携带参数处理规则
status: active
---

# LST NRFTAKEPARARULE（查询NF携带参数处理规则）

## 功能

**适用NF：NRF**

该命令用于查询NF携带参数处理规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示配置携带参数处理规则的目标网元类型。<br>数据来源：本端规划<br>取值范围：<br>- UDM（UDM）<br>- AMF（AMF）<br>- SMF（SMF）<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDR（UDR）<br>- BSF（BSF）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- SMSF（SMSF）<br>- NWDAF（NWDAF）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFTAKEPARARULE]] · NF携带参数处理规则（NRFTAKEPARARULE）

## 使用实例

查询NF携带参数处理规则，执行如下命令。

```
LST NRFTAKEPARARULE:;
%%LST NRFTAKEPARARULE:;%%
RETCODE = 0  操作成功

结果如下
---------
网元类型    NF号段防呆开关                      NF无TAI处理开关              NF无IP处理开关            注册更新处理开关          全匹配开关      规则                   IP地址控制规则    

UDM         关闭                                 NULL                        关闭                      关闭                      关闭            IMSI&ROUTINGINDICATOR  NULL
AMF         关闭                                 关闭                        关闭                      关闭                      关闭            NULL                   NULL
SMF         关闭                                 关闭                        关闭                      关闭                      关闭            NULL                   NULL
AUSF        关闭                                 NULL                        关闭                      关闭                      关闭            NULL                   NULL
PCF         关闭                                 NULL                        关闭                      关闭                      关闭            NULL                   NULL
UDR         关闭                                 NULL                        关闭                      关闭                      关闭            NULL                   NULL
BSF         关闭                                 NULL                        关闭                      关闭                      关闭            NULL                   NULL
CHF         关闭                                 NULL                        关闭                      关闭                      关闭            NULL                   NULL
CUSTOM_OCS  关闭                                 NULL                        关闭                      关闭                      关闭            NULL                   NULL
SMSF        关闭                                 NULL                        关闭                      关闭                      关闭            NULL                   NULL
NWDAF       关闭                                 关闭                        关闭                      关闭                      关闭            NULL                   NULL
(结果个数 = 11)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF携带参数处理规则（LST-NRFTAKEPARARULE）_35519273.md`
