---
id: UNC@20.15.2@MMLCommand@DSP NFREGNRFSTATUS
type: MMLCommand
name: DSP NFREGNRFSTATUS（查询NF向NRF注册状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NFREGNRFSTATUS
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NCG
- NRF
- NSSF
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF 状态管理
status: active
---

# DSP NFREGNRFSTATUS（查询NF向NRF注册状态）

## 功能

**适用NF：AMF、SMF、NCG、NRF、NSSF、SMSF**

查询NF向NRF注册状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于显示NF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~36。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NF向NRF注册状态（NFREGNRFSTATUS）](configobject/UNC/20.15.2/NFREGNRFSTATUS.md)

## 使用实例

查询NF向NRF注册状态。

```
%%DSP NFREGNRFSTATUS:;%%
RETCODE = 0  操作成功

结果如下
--------
  NF实例名称  =  AMF_Instance_0
      NF类型  =  NfAMF
 NRF实例名称  =  NRF_Instance_0
  NF注册状态  =  Success/Registered
注册成功时间  =  2024-08-25T04:53:07+08:00
注册失败原因  =  Normal
    失败次数  =  0
  重注册时间  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF向NRF注册状态（DSP-NFREGNRFSTATUS）_12701649.md`
