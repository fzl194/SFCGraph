---
id: UNC@20.15.2@MMLCommand@LST NFNRFMGMTPARA
type: MMLCommand
name: LST NFNRFMGMTPARA（查询NF与NRF间的全局管理参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFNRFMGMTPARA
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- NCG
- SMSF
- CBCF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NRF管理
- NRF参数管理
- NF与NRF间全局管理参数管理
status: active
---

# LST NFNRFMGMTPARA（查询NF与NRF间的全局管理参数）

## 功能

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF、CBCF**

该命令用于查询NF与NRF间的全局管理参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFNRFMGMTPARA]] · NF与NRF间的全局管理参数（NFNRFMGMTPARA）

## 使用实例

查询NF与NRF间的全局管理参数。

```
%%LST NFNRFMGMTPARA:;%%
RETCODE = 0 操作成功

结果如下
--------
                  切换主用NRF开关  =  OFF
  订阅通知后触发缓存同步时延 (秒)  =  120
         NFService注册MAP格式开关  =  OFF
     NFService服务发现MAP格式开关  =  OFF
                   NF参数检查开关  =  AMF_TAI&SMF_SNSSAI&SMSF_GROUPID&SMSF_SUPI_OR_GPSI
            AMF向NRF注册的TAI策略  =  取本地配置和无线上报的TAI并集
       注册时BsfInfo的MAP格式开关  =  OFF
               数据校验周期(分钟)  =  0
           参数检查NF直接注册开关  =  OFF
        NF管理类流程NRF故障返回码  =  NULL
      NF服务发现流程NRF故障返回码  =  NULL
         SMSF注册携带SmsfInfo开关  =  OFF
             订阅通知更新缓存开关  =  OFF
           订阅通知中信元长度阈值  =  2
    注册携带PerPlmnSnssaiList开关  =  OFF
              NRF是否支持数据同步  =  支持
       数据校验不一致上报告警开关  =  OFF
      NRF服务发现流控告警上报开关  =  OFF
NRF服务发现流控告警检测周期(分钟)  =  5
(结果个数 = 1)

---- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFNRFMGMTPARA.md`
