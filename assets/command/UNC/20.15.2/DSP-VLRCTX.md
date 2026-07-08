---
id: UNC@20.15.2@MMLCommand@DSP VLRCTX
type: MMLCommand
name: DSP VLRCTX（显示VLR注册用户的上下文信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: VLRCTX
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- 用户上下文管理
status: active
---

# DSP VLRCTX（显示VLR注册用户的上下文信息）

## 功能

**适用NF：SMSF**

该命令用以显示VLR注册用户的上下文信息，包含用户信息、用户短消息签约信息等。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | VLR用户的识别码类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示VLR用户的识别码类型。<br>数据来源：本端规划<br>取值范围：<br>- “IMSI（国际移动用户识别码）”：国际移动用户识别码<br>- “MSISDN（移动台国际ISDN号码）”：移动台国际ISDN号码<br>- “IMEI（国际移动设备标识）”：国际移动设备标识<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"QUERYOPT"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于表示VLR用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~15。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"QUERYOPT"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于表示VLR用户的MSISDN信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~15。<br>默认值：无<br>配置原则：无 |
| IMEI | IMEI | 可选必选说明：该参数在"QUERYOPT"配置为"IMEI"时为条件必选参数。<br>参数含义：该参数用于表示VLR用户的IMEI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~16。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VLRCTX]] · VLR用户的上下文（VLRCTX）

## 使用实例

当运营商希望查询IMSI为“460023500100001”的用户的VLR上下文，执行如下命令：

```
%%DSP VLRCTX: QUERYOPT=IMSI, IMSI="460023500100001";%%
RETCODE = 0  操作成功

结果如下：
------------------------
         MT签约标识  =  TRUE
         MO签约标识  =  TRUE
VLR用户位置更新时间  =  2023-04-06 20:05:54.963+00:00
 主注册中心响应时间  =  2023-04-06 20:05:54.731+00:00
   主注册中心响应码  =  200
 备注册中心响应时间  =  2023-04-06 20:05:54.731+00:00
   备注册中心响应码  =  200
            VLR名称  =  VLR1
         位置区标识  =  LAI1
         跟踪区标识  =  TAI1
E-UTRAN小区全球标识  =  ECGI1
             MME名称 =  mme1
               IMSI  =  imsi1
             MSISDN  =  msisdn1
               IMEI  =  imei1
 用户业务有效性时间  =  2023-04-06 20:05:54.731+00:00

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-VLRCTX.md`
