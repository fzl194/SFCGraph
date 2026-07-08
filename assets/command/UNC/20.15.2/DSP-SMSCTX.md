---
id: UNC@20.15.2@MMLCommand@DSP SMSCTX
type: MMLCommand
name: DSP SMSCTX（显示SMSF中注册的用户上下文）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMSCTX
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 用户上下文管理
- SMS上下文
status: active
---

# DSP SMSCTX（显示SMSF中注册的用户上下文）

## 功能

**适用NF：SMSF**

该命令用于查询5G SMSF注册用户的上下文信息，包括用户信息、用户短消息签约信息等。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于表示用户查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “SUPI（SUPI）”：填写用户的IMSI<br>- “GPSI（GPSI）”：填写用户的MSISDN<br>默认值：无<br>配置原则：无 |
| SUPI | SUPI | 可选必选说明：该参数在"QUERYOPT"配置为"SUPI"时为条件必选参数。<br>参数含义：该参数用于表示用户SUPI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| GPSI | GPSI | 可选必选说明：该参数在"QUERYOPT"配置为"GPSI"时为条件必选参数。<br>参数含义：该参数用于表示用户GPSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSCTX]] · 用户的SMS上下文（SMSCTX）

## 使用实例

当运营商希望查询IMSI为460023500100001用户的SMS上下文，执行如下命令：

```
DSP SMSCTX: QUERYOPT=SUPI, SUPI="460023500100001";
%%DSP SMSCTX: QUERYOPT=SUPI, SUPI="460023500100001";%%
RETCODE = 0  操作成功

结果如下：
------------------------
                          SUPI  =  460023500100001
                        AMF ID  =  AMF_Instance_0
             是否向UDM注册成功  =  是
     向UDM获取签约数据是否成功  =  是
                是否签约MT服务  =  是
                是否禁止MT服务  =  否
                是否签约MO服务  =  是
              MO服务是否被禁止  =  否
                          GPSI  =  8613535000001
                  用户注册时间  =  2020-12-22 09:30:03.361+08:00
            用户上下文更新时间  =  2020-12-22 09:31:20.185+08:00
SMSF向主注册中心注册成功的时间  =  2022-04-22 09:31:20.185+08:00
SMSF向主注册中心注册失败的时间  =  2022-04-20 09:30:20.185+08:00
SMSF向备注册中心注册成功的时间  =  2022-04-22 09:31:21.185+08:00
SMSF向备注册中心注册失败的时间  =  2022-04-20 09:30:45.185+08:00
        用户UDM Bypass状态标记  =  Normal
	          主注册中心响应码  =  200
	          备注册中心响应码  =  200
AMF Binding头域 = AMFBinding
UDM binding头域 = UDMBinding
备份AMF信息 = {amf2.cluster1.net2.amf.5gc.mnc003.mcc460.3gppnetwork.org,46001822700}
GUAMIS = 12303822700
		    用户业务有效性时间  =  2022-04-22 09:31:20.185+08:00

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SMSCTX.md`
