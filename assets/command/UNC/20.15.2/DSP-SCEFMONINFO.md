---
id: UNC@20.15.2@MMLCommand@DSP SCEFMONINFO
type: MMLCommand
name: DSP SCEFMONINFO（查询能力开放订阅任务信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SCEFMONINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Diameter应用协议
- 能力开放订阅管理
status: active
---

# DSP SCEFMONINFO（查询能力开放订阅任务信息）

## 功能

MME
该命令用于查询指定SCEF和指定SCEF参考号的能力开放订阅任务信息。

## 注意事项

- 无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询能力开放订阅任务信息的方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- “BYIMSI(指定IMSI)”：表示根据IMSI查询。<br>- “BYMSISDN(指定MSISDN)”：表示根据MSISDN查询。<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在<br>“查询方式”<br>配置为<br>“BYIMSI(指定IMSI)”<br>后生效。<br>参数含义：该参数用于指定国际移动用户标识。<br>数据来源：本端规划<br>取值范围：1～15位数字。<br>默认值：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在<br>“查询方式”<br>配置为<br>“BYMSISDN(指定MSISDN)”<br>后生效。<br>参数含义：该参数用于指定移动台国际ISDN号码。<br>数据来源：本端规划<br>取值范围：1～15位数字。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCEFMONINFO]] · 能力开放订阅任务信息（SCEFMONINFO）

## 使用实例

1. 根据IMSI查询订阅任务信息:
  DSP SCEFMONINFO: QUERYOPT=BYIMSI, IMSI="123031234567890";
  ```
  %%DSP SCEFMONINFO: QUERYOPT=BYIMSI, IMSI="
  123031234567890
  ";%%
  RETCODE = 0  操作成功。

  操作结果如下
  -------------------------
         SCEF主机名  =  scef1234.example03.com
   SCEF分配的参考号  =  1
       订阅能力类型  =  UE Loss of Connectivity
   报告最大上报次数  =  3
         已上报次数  =  0
       截止上报时间  =  NULL
     被订阅位置类型  =  NULL
     被订阅位置精度  =  NULL
  (结果个数 = 1)
  ---    END
  ```
2. 根据MSISDN查询订阅任务信息:
  DSP SCEFMONINFO: QUERYOPT=BYMSISDN, MSISDN="123456789012345";
  ```
  %%DSP SCEFMONINFO: QUERYOPT=BYMSISDN, MSISDN="123456789012345";%%
  RETCODE = 0  操作成功。

  操作结果如下
  -------------------------
         SCEF主机名  =  scef1234.example03.com
   SCEF分配的参考号  =  1
       订阅能力类型  =  UE连接丢失
   报告最大上报次数  =  3
         已上报次数  =  0
       截止上报时间  =  NULL
     被订阅位置类型  =  NULL
     被订阅位置精度  =  NULL
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SCEFMONINFO.md`
