---
id: UNC@20.15.2@MMLCommand@DSP INSTANCESTATUS
type: MMLCommand
name: DSP INSTANCESTATUS（显示输入微服务名称下所有实例的具体信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: INSTANCESTATUS
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- GGSN
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- 状态查询
status: active
---

# DSP INSTANCESTATUS（显示输入微服务名称下所有实例的具体信息）

## 功能

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、GGSN、SMSF、NCG**

该命令用于显示输入微服务名称下所有进程实例的具体信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不输入的话显示所有服务的实例状况，可根据返回结果中的服务名称单独进行查询。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@INSTANCESTATUS]] · 输入微服务名称下所有实例的具体信息（INSTANCESTATUS）

## 使用实例

获取smcexec的所有实例ID，pod名称，token数目，稳态token数目和非稳态token数目。

```
%%DSP INSTANCESTATUS:;%%
RETCODE = 0  操作成功

结果如下
--------
服务名称           实例ID                Pod名称                    Token数目  稳态token  非稳态token  

GtpPathExecSvc     18393039437572502521  nsim-pod-55b9c78696-cfx8j  33         33         0            
GtpPathExecSvc     18393039437572498425  nsim-pod-55b9c78696-qqcmd  34         34         0            
StgExecSvc         18393936647650550765  sm2-pod-1                  784        784        0            
StgExecSvc         18393936647650563053  sm2-pod-0                  783        783        0            
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-INSTANCESTATUS.md`
