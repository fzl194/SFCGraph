---
id: UNC@20.15.2@MMLCommand@LST DMCMPT
type: MMLCommand
name: LST DMCMPT（查询Diameter兼容配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DMCMPT
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter协议接口兼容性配置
status: active
---

# LST DMCMPT（查询Diameter兼容配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询Diameter兼容配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMCMPT]] · Diameter兼容配置（DMCMPT）

## 使用实例

查询Diameter兼容配置，运行如下命令：

```
LST DMCMPT:;
```

```
%%LST DMCMPT:;%%
RETCODE = 0  操作成功。

输出结果如下
------------
    是否支持UE-SRVCC-Capability信元  =  支持
                           特性列表  =  UE可达通知
                          特性列表2  =  NULL
                        P-GW ID类型  =  MIP-Home-Agent-Host
              切换后P-GW ID更新策略  =  不更新
                    NOR消息更新参数  =  IMS VoPS参数
                  S6a/S6d-Indicator  =  融合SGSN/MME支持
Homogeneous Support of IMS VoPS信元  =  按照设备能力携带
                   用户能力匹配模式  =  快速匹配
           不允许IMS VoPS的用户处理  =  携带NOT SUPPORT
 T-ADS查询结果与IMS PDN连接状态相关  =  否
                  是否支持NBIoT RAT  =  不支持
                 支持上报的状态列表  =  NULL
                     T6接口特性列表  =  NULL
             未签约DCNR是否允许DCNR  =  否
        是否支持NOR消息上报RAT TYPE  =  不支持
        是否支持LTE-M类型的RAT TYPE  =  NULL
            EPS FB后P-GW ID更新策略  =  不更新
     是否支持UE-DCNR-Capability信元  =  不支持
        是否支持AMF Instance ID信元  =  不支持
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DMCMPT.md`
