---
id: UNC@20.15.2@MMLCommand@LST S1SMARTRULE
type: MMLCommand
name: LST S1SMARTRULE（查询S1模式信令抑制规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1SMARTRULE
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- Smartphone管理
- 异常信令节省
- S1模式信令抑制规则管理
status: active
---

# LST S1SMARTRULE（查询S1模式信令抑制规则）

## 功能

**适用网元：MME**

该命令用于查询基于用户终端类型的S1模式信令抑制规则。

## 注意事项

无。

## 权限

manage-ug; system-ug; monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UETYPE | 终端类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的终端类型。<br>数据来源：本端规划<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>- “UNKNOWN_TYPE(未知类型)”<br>默认值：无<br>说明：“UNKNOWN_TYPE(未知类型)”：未获取到IMEI的终端类型或者没有匹配的<br>[**ADD IMEILIB**](../../终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md)<br>配置的终端类型。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1SMARTRULE]] · S1模式信令抑制规则（S1SMARTRULE）

## 使用实例

查询 “终端类型” 为“ANDROID”的S1模式异常信令抑制规则：

LST S1SMARTRULE: UETYPE=ANDROID;

```
%%LST S1SMARTRULE: UETYPE=ANDROID;%%
RETCODE = 0  操作成功。

输出结果如下
------------
                  终端类型  =  Android
              附着抑制措施  =  NULL
              附着拒绝原因  =  NO_SUITABLE_CELLS_IN_TA_15
          服务请求抑制措施  =  NULL
          服务请求拒绝原因  =  NO_SUITABLE_CELLS_IN_TA_15
    控制面服务请求抑制措施  =  NULL
    控制面服务请求拒绝原因  =  NO_SUITABLE_CELLS_IN_TA_15
           PDN连接抑制措施  =  NULL
           PDN连接拒绝原因  =  MULTI_PDN_FOR_APN_NOT_ALLOWED_55
     Backoff Timer分配开关  =  开启
Back off timer最小值（秒）  =  660
Back off timer最大值（秒）  =  3000
              抑制分离原因  =  NO_SUITABLE_CELLS_IN_TA_15
       Parking APN唤醒措施  =  网络侧去激活
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1模式信令抑制规则(LST-S1SMARTRULE)_72345347.md`
